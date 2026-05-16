# Tabak2007_dopamine

Cleaned Biosimulant pharmacology lab.

- Source ID: `BIOMD0000000138`
- Scientific source of truth: bundled SBML XML in `models/core/data`
- Public question: How does the modeled dopamine state respond over time?
- Visualisation focus: Dopamine response is interpreted from the source-defined dopamine state.

The wrapper executes the bundled source model through `TelluriumSBMLBioModule`.
Public ports are conservative, source-backed labels; raw SBML symbols are preserved in manifest `maps_to` fields and wrapper metadata.
