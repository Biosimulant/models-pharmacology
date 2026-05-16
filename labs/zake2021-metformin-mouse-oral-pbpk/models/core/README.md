# Zake2021 - PBPK model of metformin in mice: single dose peroral

Cleaned Biosimulant pharmacology lab.

- Source ID: `BIOMD0000001027`
- Scientific source of truth: bundled SBML XML in `models/core/data`
- Public question: How does oral dosing distribute in mouse compartments?
- Visualisation focus: Mouse oral PBPK behavior is interpreted from source-defined metformin compartments.

The wrapper executes the bundled source model through `TelluriumSBMLBioModule`.
Public ports are conservative, source-backed labels; raw SBML symbols are preserved in manifest `maps_to` fields and wrapper metadata.
