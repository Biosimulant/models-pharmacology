# Koeller2021 - PBPK model of ICG liver function tests

Cleaned Biosimulant pharmacology lab.

- Source ID: `MODEL2301090001`
- Scientific source of truth: bundled SBML XML in `models/core/data`
- Public question: Does ICG clearance indicate hepatic function in the model?
- Visualisation focus: ICG liver-function behavior is interpreted from source-defined plasma and liver compartments.

The wrapper executes the bundled source model through `TelluriumSBMLBioModule`.
Public ports are conservative, source-backed labels; raw SBML symbols are preserved in manifest `maps_to` fields and wrapper metadata.
