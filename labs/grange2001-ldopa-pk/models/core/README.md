# Grange2001 - L Dopa PK model

Cleaned Biosimulant pharmacology lab.

- Source ID: `BIOMD0000000321`
- Scientific source of truth: bundled SBML XML in `models/core/data`
- Public question: What exposure profile follows L-DOPA administration?
- Visualisation focus: L-DOPA pharmacokinetics are tracked from source-defined drug amount and compartment states.

The wrapper executes the bundled source model through `TelluriumSBMLBioModule`.
Public ports are conservative, source-backed labels; raw SBML symbols are preserved in manifest `maps_to` fields and wrapper metadata.
