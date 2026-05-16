# Bucher2011_Atorvastatin_Metabolism

Cleaned Biosimulant pharmacology lab.

- Source ID: `BIOMD0000000328`
- Scientific source of truth: bundled SBML XML in `models/core/data`
- Public question: How does atorvastatin move through modeled metabolic pools?
- Visualisation focus: Atorvastatin metabolism is tracked using the source-defined parent and metabolite states.

The wrapper executes the bundled source model through `TelluriumSBMLBioModule`.
Public ports are conservative, source-backed labels; raw SBML symbols are preserved in manifest `maps_to` fields and wrapper metadata.
