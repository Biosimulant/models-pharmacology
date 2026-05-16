# Zake2021 - PBPK model of metformin in humans, single PO dose

Cleaned Biosimulant pharmacology lab.

- Source ID: `BIOMD0000001028`
- Scientific source of truth: bundled SBML XML in `models/core/data`
- Public question: Where does metformin exposure peak after a human single dose?
- Visualisation focus: Single-dose PBPK behavior is interpreted from source-defined metformin compartments.

The wrapper executes the bundled source model through `TelluriumSBMLBioModule`.
Public ports are conservative, source-backed labels; raw SBML symbols are preserved in manifest `maps_to` fields and wrapper metadata.
