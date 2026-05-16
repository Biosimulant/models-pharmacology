# Singh2006_TCA_Ecoli_acetate

This Biosimulant lab wraps `Singh2006_TCA_Ecoli_acetate` as a runnable pharmacology model with a companion visualization module.
This a model from the article: Kinetic modeling of tricarboxylic acid cycle and glyoxylate bypass in Mycobacterium tuberculosis, and its application to assessment of drug targets. It can be used to explore drug-exposure and pathway-response dynamics and compare scenario outcomes across configurations.

## What You'll See

The lab asks: How does acetate-supported TCA activity evolve across core intermediates? It runs for 5.0 time units with a communication step of 0.5. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on Acetate Or Acetyl Coa Pool, Oxaloacetate Pool, Coa Pool, Citrate Pool, Isocitrate Pool, and Alpha Ketoglutarate Pool, and related outputs, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

In this captured run, **cit** peaked at **9.000** and **cit** moved by **8.977** native units across 5.0 simulation windows.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

![Singh2006_TCA_Ecoli_acetate - run interpretation](assets/01-singh2006-tca-ecoli-acetate-run-interpretation.png)

*Summary table for Singh2006_TCA_Ecoli_acetate, reporting the scientific question, observed answer (largest change: **cit** at **8.977** native units), evidence (peak observable: **cit**), dominant module, and caveat.*

![Singh2006_TCA_Ecoli_acetate - timeseries visualization](assets/02-metabolic-state.png)

*Trajectories of cit, icit, suc, mal, gly, and fa across the 5.0 simulation. In this run **fa** climbed from 0.3000 to 0.4043 and **cit** fell from 9.000 to 0.0232 — the largest movements among the focused observables.*

![Singh2006_TCA_Ecoli_acetate - excursions bar](assets/03-largest-source-observable-excursions.png)

*Largest-excursion ranking of the focused observables — the absolute movement magnitude during the run. Top 3: **cit** = 8.977, **icit** = 7.755, **suc** = 5.935, with 5 more observables below.*

![Singh2006_TCA_Ecoli_acetate - endpoint snapshot bar](assets/04-final-source-state-snapshot.png)

*Endpoint snapshot of the focused observables — final values from the captured run. Top 3 by value: **aca** = 0.5000, **fa** = 0.4043, **gly** = 0.1593, with 7 more observables below.*

<!-- BIOSIMULANT_VISUALS_END -->

## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `sbml`
- Upstream source: `biomodels_ebi:BIOMD0000000221`
- License: `CC0`

## Inputs

| Input | Maps To | Default | Notes |
|---|---|---|---|
| Initial Acetyl Coa Or Acetate Pool | `pharmacology_sbml_singh2006_tca_ecoli_acetate_biomd0000000221_model.initial_acetyl_coa_or_acetate_pool` |  | Uses the model default unless overridden at run time. |
| Initial Oxaloacetate Pool | `pharmacology_sbml_singh2006_tca_ecoli_acetate_biomd0000000221_model.initial_oxaloacetate_pool` |  | Uses the model default unless overridden at run time. |
| Initial Coa Pool | `pharmacology_sbml_singh2006_tca_ecoli_acetate_biomd0000000221_model.initial_coa_pool` |  | Uses the model default unless overridden at run time. |
| Initial Citrate Pool | `pharmacology_sbml_singh2006_tca_ecoli_acetate_biomd0000000221_model.initial_citrate_pool` |  | Uses the model default unless overridden at run time. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| `state` | `pharmacology_sbml_singh2006_tca_ecoli_acetate_biomd0000000221_model.state` | Available to the visualization model and downstream workflows. |
| `summary` | `pharmacology_sbml_singh2006_tca_ecoli_acetate_biomd0000000221_model.summary` | Available to the visualization model and downstream workflows. |
| `species_labels` | `pharmacology_sbml_singh2006_tca_ecoli_acetate_biomd0000000221_model.species_labels` | Available to the visualization model and downstream workflows. |
| `acetate_or_acetyl_coa_pool` | `pharmacology_sbml_singh2006_tca_ecoli_acetate_biomd0000000221_model.acetate_or_acetyl_coa_pool` | Available to the visualization model and downstream workflows. |
| `oxaloacetate_pool` | `pharmacology_sbml_singh2006_tca_ecoli_acetate_biomd0000000221_model.oxaloacetate_pool` | Available to the visualization model and downstream workflows. |
| `coa_pool` | `pharmacology_sbml_singh2006_tca_ecoli_acetate_biomd0000000221_model.coa_pool` | Available to the visualization model and downstream workflows. |
| `citrate_pool` | `pharmacology_sbml_singh2006_tca_ecoli_acetate_biomd0000000221_model.citrate_pool` | Available to the visualization model and downstream workflows. |
| `isocitrate_pool` | `pharmacology_sbml_singh2006_tca_ecoli_acetate_biomd0000000221_model.isocitrate_pool` | Available to the visualization model and downstream workflows. |
| `alpha_ketoglutarate_pool` | `pharmacology_sbml_singh2006_tca_ecoli_acetate_biomd0000000221_model.alpha_ketoglutarate_pool` | Available to the visualization model and downstream workflows. |
| `succinyl_coa_pool` | `pharmacology_sbml_singh2006_tca_ecoli_acetate_biomd0000000221_model.succinyl_coa_pool` | Available to the visualization model and downstream workflows. |
| `succinate_pool` | `pharmacology_sbml_singh2006_tca_ecoli_acetate_biomd0000000221_model.succinate_pool` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `5.0`
- Communication step: `0.5`

## Running Locally

```bash
biosimulant labs serve .
```
