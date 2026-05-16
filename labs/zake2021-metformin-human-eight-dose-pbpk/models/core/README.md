# Zake2021 - PBPK model of metformin in humans, eight PO administrations with 12h interval

Cleaned Biosimulant pharmacology lab.

- Source ID: `BIOMD0000001029`
- Scientific source of truth: bundled SBML XML in `models/core/data`
- Public question: Does 12-hour repeated dosing accumulate in the human metformin model?
- Visualisation focus: Repeated-dose PBPK behavior is interpreted from source-defined metformin compartments.

The wrapper executes the bundled source model through `TelluriumSBMLBioModule`.
Public ports are conservative, source-backed labels; raw SBML symbols are preserved in manifest `maps_to` fields and wrapper metadata.
