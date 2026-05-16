# models-pharmacology

> Clean lab repo: kept runnable pharmacology simulators live under
> `labs/<slug>/models/core/` with companion desktop visualisations in
> `labs/<slug>/models/visualisation/`. Non-runnable source-data and scope
> mismatches have been moved to the shared orphan area with evidence READMEs.

Curated collection of **pharmacology** and **pharmacokinetics** simulation models for the **biosim** platform. The kept labs expose runnable SBML-backed models of drug absorption, distribution, metabolism, excretion (ADME), pharmacodynamics, and drug-target interactions.

## What's Inside

### Models

**Pharmacology** — drug kinetics, pharmacodynamics, and therapeutic modeling:

**Key Areas:** PBPK (physiologically-based pharmacokinetic) models, dose-response relationships, drug metabolism and clearance, receptor binding dynamics, drug-drug interactions, and therapeutic dosing optimization.

All models use SBML format with tellurium runtime.

## Prerequisites
```bash
pip install "biosim @ git+https://github.com/BioSimulant/biosim.git@main"
```

## License
Dual-licensed: Apache-2.0 (code), CC BY 4.0 (content)
