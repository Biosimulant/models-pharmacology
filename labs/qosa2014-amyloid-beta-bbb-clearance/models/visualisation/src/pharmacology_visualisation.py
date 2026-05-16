# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Dedicated visualisation model for pharmacology SBML labs."""
from __future__ import annotations

from typing import Any, Mapping, Optional

from biosim import BioModule
from biosim.signals import BioSignal, SignalSpec


GROUP_TITLES = {
    "pk": ("Pharmacokinetic exposure", "Drug exposure and compartment amounts over model time."),
    "pd": ("Pharmacodynamic response", "Response variables and tolerance/effect states over model time."),
    "pkpd": ("PK/PD response", "Exposure-response variables over model time."),
    "binding": ("Target engagement", "Free, bound, target, and complex states over model time."),
    "signaling": ("Signaling response", "Receptor and pathway signaling states over model time."),
    "metabolism": ("Metabolic state", "Metabolite and pathway states over model time."),
    "physiology": ("Physiological burden", "Tissue, recovery, and disease-state variables over model time."),
    "cell-biology": ("Cell-state balance", "Cell biological source states over model time."),
    "population": ("Population burden", "Population compartments over model time."),
}


def _value(signal: BioSignal | None) -> Any:
    if signal is None:
        return None
    raw = getattr(signal, "value", signal)
    if isinstance(raw, Mapping) and set(raw.keys()) == {"payload"}:
        return raw["payload"]
    return raw


def _number(raw: Any) -> float | None:
    try:
        value = float(raw)
    except (TypeError, ValueError):
        return None
    if value != value:
        return None
    return value


class PharmacologyVisualisationModel(BioModule):
    def __init__(
        self,
        *,
        lab_title: str,
        question: str,
        answer_focus: str,
        sources: list[dict[str, Any]],
        integration_step: float = 1.0,
    ) -> None:
        self.lab_title = str(lab_title)
        self.question = str(question)
        self.answer_focus = str(answer_focus)
        self.sources = list(sources)
        self.integration_step = float(integration_step)
        self._inputs: dict[str, BioSignal] = {}
        self._history: dict[str, list[dict[str, float]]] = {}
        self._summary: dict[str, Mapping[str, Any]] = {}
        self._labels: dict[str, dict[str, str]] = {}

    def inputs(self) -> dict[str, SignalSpec]:
        specs: dict[str, SignalSpec] = {}
        summary_schema = {
            "duration_simulated": "float",
            "observable_count": "int",
            "largest_change_observable": "str",
            "largest_change_magnitude": "float",
            "peak_observable": "str",
            "peak_value": "float",
        }
        for source in self.sources:
            alias = str(source["alias"])
            ids = [str(item["id"]) for item in source.get("observables", []) if item.get("id")]
            specs[f"{alias}_state"] = SignalSpec.record(schema={name: "float" for name in ids} or {"payload": "json"})
            specs[f"{alias}_summary"] = SignalSpec.record(schema=summary_schema)
            specs[f"{alias}_species_labels"] = SignalSpec.record(schema={name: "str" for name in ids} or {"payload": "json"})
        return specs

    def outputs(self) -> dict[str, SignalSpec]:
        return {}

    def setup(self, config: Optional[dict[str, Any]] = None) -> None:
        self.reset()

    def reset(self) -> None:
        self._inputs = {}
        self._history = {str(source["alias"]): [] for source in self.sources}
        self._summary = {}
        self._labels = {}

    def set_inputs(self, inputs: dict[str, BioSignal]) -> None:
        self._inputs = dict(inputs or {})

    def advance_window(self, start: float, end: float) -> None:
        for source in self.sources:
            alias = str(source["alias"])
            state = _value(self._inputs.get(f"{alias}_state"))
            if isinstance(state, Mapping):
                row = {"t": float(getattr(self._inputs.get(f"{alias}_state"), "emitted_at", end))}
                for key, raw in state.items():
                    value = _number(raw)
                    if value is not None:
                        row[str(key)] = value
                if len(row) > 1:
                    history = self._history.setdefault(alias, [])
                    if not history or abs(row["t"] - history[-1]["t"]) > 1e-12:
                        history.append(row)
            summary = _value(self._inputs.get(f"{alias}_summary"))
            if isinstance(summary, Mapping):
                self._summary[alias] = dict(summary)
            labels = _value(self._inputs.get(f"{alias}_species_labels"))
            if isinstance(labels, Mapping):
                self._labels[alias] = {str(k): str(v) for k, v in labels.items()}

    def get_outputs(self) -> dict[str, BioSignal]:
        return {}

    def visualize(self) -> Optional[list[dict[str, Any]]]:
        visuals: list[dict[str, Any]] = []
        for source in self.sources:
            alias = str(source["alias"])
            history = self._history.get(alias) or []
            if not history:
                continue
            observables = self._observables(alias, source, history)
            if not observables:
                continue
            visuals.append(self._qa(alias, source, history, observables))
            ts = self._timeseries(source, history, observables)
            if ts:
                visuals.append(ts)
            ranges = self._ranges(source, history, observables)
            if ranges:
                visuals.append(ranges)
            snapshot = self._snapshot(source, history, observables)
            if snapshot:
                visuals.append(snapshot)
        return visuals or None

    def _observables(self, alias: str, source: Mapping[str, Any], history: list[dict[str, float]]) -> list[dict[str, str]]:
        latest = history[-1]
        labels = self._labels.get(alias, {})
        items = []
        for item in source.get("observables", []):
            obs_id = str(item.get("id") or "")
            if obs_id in latest:
                items.append({
                    "id": obs_id,
                    "label": str(item.get("label") or labels.get(obs_id) or obs_id),
                    "group": str(item.get("group") or source.get("visual_group") or "pk"),
                })
        return items

    def _qa(self, alias: str, source: Mapping[str, Any], history: list[dict[str, float]], observables: list[dict[str, str]]) -> dict[str, Any]:
        summary = self._summary.get(alias, {})
        label_by_id = {item["id"]: item["label"] for item in observables}
        largest = str(summary.get("largest_change_observable") or "")
        peak = str(summary.get("peak_observable") or "")
        change = _number(summary.get("largest_change_magnitude")) or 0.0
        largest_label = label_by_id.get(largest, largest or "No dominant mover detected")
        peak_label = label_by_id.get(peak, peak or "No peak detected")
        if abs(change) < 1e-12:
            answer = "The baseline run is near steady over the sampled window."
            evidence = "Tracked source observables changed minimally; the evidence is shown as final-state and steady-state summaries."
        else:
            answer = f"The run shows measurable activity led by {largest_label}."
            evidence = f"{largest_label} had the largest excursion ({change:.4g}); the largest peak was {peak_label}."
        rows = [
            ["Scientific question", self.question],
            ["Observed answer", answer],
            ["Evidence", evidence],
            ["Dominant module", GROUP_TITLES.get(str(source.get("visual_group")), GROUP_TITLES["pk"])[0]],
            ["Caveat", "Values are native SBML quantities; the visualisation preserves the bundled source model and does not rewrite equations."],
        ]
        return {"render": "table", "description": "Direct scientific answer for this lab run.", "data": {"title": f"{self.lab_title} - run interpretation", "columns": ["Prompt", "Answer"], "rows": rows}}

    def _timeseries(self, source: Mapping[str, Any], history: list[dict[str, float]], observables: list[dict[str, str]]) -> dict[str, Any] | None:
        ranked = sorted(observables, key=lambda item: self._range(history, item["id"]), reverse=True)[:8]
        series = [{"name": item["label"], "points": [[row["t"], row[item["id"]]] for row in history if item["id"] in row]} for item in ranked]
        series = [item for item in series if item["points"]]
        if not series:
            return None
        title, description = GROUP_TITLES.get(str(source.get("visual_group")), GROUP_TITLES["pk"])
        return {"render": "timeseries", "description": description, "data": {"title": title, "x_label": "Model time", "y_label": "Native SBML value", "series": series}}

    def _ranges(self, source: Mapping[str, Any], history: list[dict[str, float]], observables: list[dict[str, str]]) -> dict[str, Any] | None:
        items = [{"label": item["label"], "value": self._range(history, item["id"])} for item in observables]
        items = [item for item in sorted(items, key=lambda x: x["value"], reverse=True) if item["value"] > 0][:10]
        if not items:
            return None
        return {"render": "bar", "description": "Tracked variables ranked by within-run excursion.", "data": {"title": "Largest source-observable excursions", "items": items, "x_label": "Observable", "y_label": "Max-min range"}}

    def _snapshot(self, source: Mapping[str, Any], history: list[dict[str, float]], observables: list[dict[str, str]]) -> dict[str, Any] | None:
        latest = history[-1]
        items = [{"label": item["label"], "value": abs(float(latest.get(item["id"], 0.0)))} for item in observables if item["id"] in latest]
        items = [item for item in sorted(items, key=lambda x: x["value"], reverse=True) if item["value"] > 0][:10]
        if not items:
            return None
        return {"render": "bar", "description": "Final-state magnitude of tracked source observables.", "data": {"title": "Final source-state snapshot", "items": items, "x_label": "Observable", "y_label": "Absolute final value"}}

    @staticmethod
    def _range(history: list[dict[str, float]], key: str) -> float:
        values = [float(row[key]) for row in history if key in row]
        return max(values) - min(values) if values else 0.0
