# Grange2001 - L Dopa PK model

This Biosimulant lab wraps `Grange2001 - L Dopa PK model` as a runnable pharmacology model with a companion visualization module.
Grange2001 - L-dopa PK model A pharmacokinetics of L-dopa in rats after administration of L-dopa alone (this model: BIOMD0000000321) or L-dopa combined with a peripheral AADC (amino-acid-decarboxylase. It can be used to explore drug-exposure and pathway-response dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: What L-DOPA exposure profile follows the selected dose and clearance? It runs for 24.0 time units with a communication step of 1.0. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on L Dopa Amount, L Dopa Concentration, and Three Omd Concentration, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **A dopa** peaked at **101.0** and **A dopa** moved by **101.0** native units across 24.0 simulation windows.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

![Grange2001 - L Dopa PK model - run interpretation](assets/01-grange2001-l-dopa-pk-model-run-interpretation.png)

*Summary table for Grange2001 - L Dopa PK model, reporting the scientific question, observed answer (largest change: **A dopa** at **101.0** native units), evidence (peak observable: **A dopa**), dominant module, and caveat.*

![Grange2001 - L Dopa PK model - timeseries visualization](assets/02-pharmacokinetic-exposure.png)

*Trajectories of A dopa, C dopa, and C 3 OMD across the 24.0 simulation. In this run **C 3 OMD** climbed from 0 to 0.5521 and **A dopa** fell from 101.0 to 8.47e-20 — the largest movements among the focused observables.*

![Grange2001 - L Dopa PK model - excursions bar](assets/03-largest-source-observable-excursions.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **A dopa** = 101.0, **C dopa** = 6.822, **C 3 OMD** = 1.822.*

![Grange2001 - L Dopa PK model - endpoint snapshot bar](assets/04-final-source-state-snapshot.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **C 3 OMD** = 0.5521, **C dopa** = 2.63e-15, **A dopa** = 8.47e-20.*

<!-- BIOSIMULANT_VISUALS_END -->

## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `sbml`
- Upstream source: `biomodels_ebi:BIOMD0000000321`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| L Dopa Dose Per Kg Rat | `pharmacology_sbml_grange2001_l_dopa_pk_model_biomd0000000321_model.l_dopa_dose_per_kg_rat` |  | Uses the model default unless overridden at run time. |
| L Dopa Clearance Rate | `pharmacology_sbml_grange2001_l_dopa_pk_model_biomd0000000321_model.l_dopa_clearance_rate` |  | Uses the model default unless overridden at run time. |
| Omd Clearance Rate | `pharmacology_sbml_grange2001_l_dopa_pk_model_biomd0000000321_model.omd_clearance_rate` |  | Uses the model default unless overridden at run time. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `pharmacology_sbml_grange2001_l_dopa_pk_model_biomd0000000321_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `pharmacology_sbml_grange2001_l_dopa_pk_model_biomd0000000321_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `pharmacology_sbml_grange2001_l_dopa_pk_model_biomd0000000321_model.species_labels` | Available to the visualization model and downstream workflows. |
| `l_dopa_amount` | `pharmacology_sbml_grange2001_l_dopa_pk_model_biomd0000000321_model.l_dopa_amount` | Available to the visualization model and downstream workflows. |
| `l_dopa_concentration` | `pharmacology_sbml_grange2001_l_dopa_pk_model_biomd0000000321_model.l_dopa_concentration` | Available to the visualization model and downstream workflows. |
| `three_omd_concentration` | `pharmacology_sbml_grange2001_l_dopa_pk_model_biomd0000000321_model.three_omd_concentration` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `24.0`
- Communication step: `1.0`

## Running Locally

```bash
biosimulant labs serve .
```
