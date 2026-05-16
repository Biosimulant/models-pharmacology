# KaratzaKaralis2020 - CYP mediated losartan metabolism

Cleaned Biosimulant pharmacology lab.

- Source ID: `MODEL2412180001`
- Scientific source of truth: bundled SBML XML in `models/core/data`
- Public question: How does CYP-mediated metabolism transform losartan?
- Visualisation focus: Losartan and metabolite pools are tracked from the source model.

The wrapper executes the bundled source model through `TelluriumSBMLBioModule`.
Public ports are conservative, source-backed labels; raw SBML symbols are preserved in manifest `maps_to` fields and wrapper metadata.
