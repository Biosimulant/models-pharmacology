# Kraan199_Kinetics of Cortisol Metabolism and Excretion.

Cleaned Biosimulant pharmacology lab.

- Source ID: `BIOMD0000000916`
- Scientific source of truth: bundled SBML XML in `models/core/data`
- Public question: How does cortisol move through modeled metabolism and excretion?
- Visualisation focus: Cortisol and metabolite states are interpreted from the bundled source.

The wrapper executes the bundled source model through `TelluriumSBMLBioModule`.
Public ports are conservative, source-backed labels; raw SBML symbols are preserved in manifest `maps_to` fields and wrapper metadata.
