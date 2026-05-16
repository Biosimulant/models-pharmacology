# Chang2010_Reduced_Kidney_FBA

Cleaned Biosimulant pharmacology lab.

- Source ID: `MODEL1011080004`
- Scientific source of truth: bundled SBML XML in `models/core/data`
- Public question: Which kidney metabolic modules are active in the runnable source model?
- Visualisation focus: The visualisation emphasizes steady metabolic evidence rather than inventing a pharmacological endpoint.

The wrapper executes the bundled source model through `TelluriumSBMLBioModule`.
Public ports are conservative, source-backed labels; raw SBML symbols are preserved in manifest `maps_to` fields and wrapper metadata.
