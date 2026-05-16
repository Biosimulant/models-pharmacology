# Singh2006_TCA_Ecoli_acetate

Cleaned Biosimulant pharmacology lab.

- Source ID: `BIOMD0000000221`
- Scientific source of truth: bundled SBML XML in `models/core/data`
- Public question: How does acetate-supported TCA activity evolve?
- Visualisation focus: TCA behavior is interpreted from source-defined E. coli metabolite states.

The wrapper executes the bundled source model through `TelluriumSBMLBioModule`.
Public ports are conservative, source-backed labels; raw SBML symbols are preserved in manifest `maps_to` fields and wrapper metadata.
