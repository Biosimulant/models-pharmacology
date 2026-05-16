# Shi1993_Caffeine_pressor_tolerance

Cleaned Biosimulant pharmacology lab.

- Source ID: `BIOMD0000000241`
- Scientific source of truth: bundled SBML XML in `models/core/data`
- Public question: Does pressor tolerance attenuate caffeine response?
- Visualisation focus: Caffeine pharmacodynamics are interpreted from source-defined pressure and tolerance states.

The wrapper executes the bundled source model through `TelluriumSBMLBioModule`.
Public ports are conservative, source-backed labels; raw SBML symbols are preserved in manifest `maps_to` fields and wrapper metadata.
