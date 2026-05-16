# Schropp2019 - Target-Mediated Drug Disposition Model for Bispecific Antibodies

Cleaned Biosimulant pharmacology lab.

- Source ID: `BIOMD0000000788`
- Scientific source of truth: bundled SBML XML in `models/core/data`
- Public question: Does bispecific target binding shape disposition?
- Visualisation focus: TMDD behavior is interpreted from source-defined antibody, target, and complex states.

The wrapper executes the bundled source model through `TelluriumSBMLBioModule`.
Public ports are conservative, source-backed labels; raw SBML symbols are preserved in manifest `maps_to` fields and wrapper metadata.
