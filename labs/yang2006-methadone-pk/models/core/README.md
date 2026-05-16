# Yang2006_Methadone_PKmodel

Cleaned Biosimulant pharmacology lab.

- Source ID: `MODEL1006230040`
- Scientific source of truth: bundled SBML XML in `models/core/data`
- Public question: What methadone exposure trajectory is produced?
- Visualisation focus: Methadone PK is interpreted from source-defined state variables after applying the generic time-parameter repair.

The wrapper executes the bundled source model through `TelluriumSBMLBioModule`.
Public ports are conservative, source-backed labels; raw SBML symbols are preserved in manifest `maps_to` fields and wrapper metadata.
