# Landberg2009 - Alkylresorcinol Dose Response

Cleaned Biosimulant pharmacology lab.

- Source ID: `BIOMD0000000948`
- Scientific source of truth: bundled SBML XML in `models/core/data`
- Public question: Does exposure scale with alkylresorcinol dose?
- Visualisation focus: Dose-response behavior is interpreted from source-defined alkylresorcinol exposure states.

The wrapper executes the bundled source model through `TelluriumSBMLBioModule`.
Public ports are conservative, source-backed labels; raw SBML symbols are preserved in manifest `maps_to` fields and wrapper metadata.
