# Tylutki2017-four-compartment PBPK heart model accounting for cardiac metabolism

Cleaned Biosimulant pharmacology lab.

- Source ID: `MODEL2003190003`
- Scientific source of truth: bundled SBML XML in `models/core/data`
- Public question: How does cardiac metabolism change drug disposition?
- Visualisation focus: Cardiac PBPK behavior is interpreted from source-defined heart and drug states.

The wrapper executes the bundled source model through `TelluriumSBMLBioModule`.
Public ports are conservative, source-backed labels; raw SBML symbols are preserved in manifest `maps_to` fields and wrapper metadata.
