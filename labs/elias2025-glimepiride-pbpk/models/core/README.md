# Elias2025 - Physiologically based pharmacokinetics (PBPK) model glimepiride

Cleaned Biosimulant pharmacology lab.

- Source ID: `MODEL2510140001`
- Scientific source of truth: bundled SBML XML in `models/core/data`
- Public question: Where does glimepiride exposure concentrate over time?
- Visualisation focus: PBPK exposure is interpreted from source-defined organ and plasma compartments.

The wrapper executes the bundled source model through `TelluriumSBMLBioModule`.
Public ports are conservative, source-backed labels; raw SBML symbols are preserved in manifest `maps_to` fields and wrapper metadata.
