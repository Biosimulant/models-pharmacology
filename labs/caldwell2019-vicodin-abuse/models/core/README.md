# Caldwell2019 - The Vicodin abuse problem

Cleaned Biosimulant pharmacology lab.

- Source ID: `BIOMD0000000840`
- Scientific source of truth: bundled SBML XML in `models/core/data`
- Public question: Does modeled Vicodin misuse rise, peak, or settle under the baseline scenario?
- Visualisation focus: Population burden is interpreted from source-defined use, abuse, and recovery compartments.

The wrapper executes the bundled source model through `TelluriumSBMLBioModule`.
Public ports are conservative, source-backed labels; raw SBML symbols are preserved in manifest `maps_to` fields and wrapper metadata.
