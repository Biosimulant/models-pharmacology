# Qosa2014 - Mechanistic modeling that describes amyloid-Beta clearance across BBB

Cleaned Biosimulant pharmacology lab.

- Source ID: `MODEL1409240002`
- Scientific source of truth: bundled SBML XML in `models/core/data`
- Public question: Does the model clear amyloid-beta across the BBB?
- Visualisation focus: BBB clearance is interpreted from source-defined amyloid and transport states.

The wrapper executes the bundled source model through `TelluriumSBMLBioModule`.
Public ports are conservative, source-backed labels; raw SBML symbols are preserved in manifest `maps_to` fields and wrapper metadata.
