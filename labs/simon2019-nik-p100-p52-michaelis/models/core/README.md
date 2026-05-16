# Simon2019 - NIK-dependent p100 processing into p52, Michaelis-Menten, SBML 2v4

Cleaned Biosimulant pharmacology lab.

- Source ID: `BIOMD0000000866`
- Scientific source of truth: bundled SBML XML in `models/core/data`
- Public question: Does NIK drive p100-to-p52 processing in the Michaelis-Menten model?
- Visualisation focus: NIK-dependent NF-kB processing is interpreted from source-defined p100/p52 states.

The wrapper executes the bundled source model through `TelluriumSBMLBioModule`.
Public ports are conservative, source-backed labels; raw SBML symbols are preserved in manifest `maps_to` fields and wrapper metadata.
