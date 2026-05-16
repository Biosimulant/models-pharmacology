# Telesco2011_HER3-ErbB3-RTK_SignalingNetwork

Cleaned Biosimulant pharmacology lab.

- Source ID: `MODEL1102210001`
- Scientific source of truth: bundled SBML XML in `models/core/data`
- Public question: Which RTK signaling module dominates?
- Visualisation focus: HER3/ErbB3 pathway behavior is interpreted from source-defined receptor and signaling species.

The wrapper executes the bundled source model through `TelluriumSBMLBioModule`.
Public ports are conservative, source-backed labels; raw SBML symbols are preserved in manifest `maps_to` fields and wrapper metadata.
