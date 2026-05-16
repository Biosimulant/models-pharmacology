# Singh2006_TCA_mtu_model2

Cleaned Biosimulant pharmacology lab.

- Source ID: `BIOMD0000000218`
- Scientific source of truth: bundled SBML XML in `models/core/data`
- Public question: Which TCA states dominate the second MTB model?
- Visualisation focus: MTB TCA behavior is interpreted from source-defined metabolite states.

The wrapper executes the bundled source model through `TelluriumSBMLBioModule`.
Public ports are conservative, source-backed labels; raw SBML symbols are preserved in manifest `maps_to` fields and wrapper metadata.
