# Sluka2016 - Acetaminophen PBPK

Cleaned Biosimulant pharmacology lab.

- Source ID: `BIOMD0000000619`
- Scientific source of truth: bundled SBML XML in `models/core/data`
- Public question: Which compartments carry acetaminophen burden?
- Visualisation focus: PBPK burden is interpreted from source-defined acetaminophen and tissue states.

The wrapper executes the bundled source model through `TelluriumSBMLBioModule`.
Public ports are conservative, source-backed labels; raw SBML symbols are preserved in manifest `maps_to` fields and wrapper metadata.
