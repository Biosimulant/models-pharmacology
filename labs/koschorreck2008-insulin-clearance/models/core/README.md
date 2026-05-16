# Koschorreck2008_InsulinClearance

Cleaned Biosimulant pharmacology lab.

- Source ID: `BIOMD0000000345`
- Scientific source of truth: bundled SBML XML in `models/core/data`
- Public question: How quickly does modeled insulin clear?
- Visualisation focus: Insulin clearance is interpreted from source-defined insulin and clearance states.

The wrapper executes the bundled source model through `TelluriumSBMLBioModule`.
Public ports are conservative, source-backed labels; raw SBML symbols are preserved in manifest `maps_to` fields and wrapper metadata.
