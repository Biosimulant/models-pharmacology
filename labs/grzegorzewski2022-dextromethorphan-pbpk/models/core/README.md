# Grzegorzewski2022 - PBPK model of dextromethorphan

Cleaned Biosimulant pharmacology lab.

- Source ID: `MODEL2301090002`
- Scientific source of truth: bundled SBML XML in `models/core/data`
- Public question: Which compartments drive dextromethorphan exposure?
- Visualisation focus: PBPK exposure and metabolism are interpreted from source-defined organ and plasma states.

The wrapper executes the bundled source model through `TelluriumSBMLBioModule`.
Public ports are conservative, source-backed labels; raw SBML symbols are preserved in manifest `maps_to` fields and wrapper metadata.
