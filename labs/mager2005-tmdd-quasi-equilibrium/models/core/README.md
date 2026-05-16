# Mager2005 - Quasi-equilibrium pharmacokinetic model for drugs exhibiting target-mediated drug disposition

Cleaned Biosimulant pharmacology lab.

- Source ID: `BIOMD0000000765`
- Scientific source of truth: bundled SBML XML in `models/core/data`
- Public question: Does target binding dominate drug disposition?
- Visualisation focus: TMDD behavior is interpreted from free drug, target, and complex states.

The wrapper executes the bundled source model through `TelluriumSBMLBioModule`.
Public ports are conservative, source-backed labels; raw SBML symbols are preserved in manifest `maps_to` fields and wrapper metadata.
