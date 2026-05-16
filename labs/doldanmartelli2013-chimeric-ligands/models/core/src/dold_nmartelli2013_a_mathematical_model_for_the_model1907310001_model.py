# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule for DoldánMartelli2013 - A Mathematical Model for the Rational Design of Chimeric Ligands in Selective Drug Therapies."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class DoldNmartelli2013AMathematicalModelForTheModel1907310001Model(TelluriumSBMLBioModule):
    """Faithfully executes the bundled SBML source for DoldánMartelli2013 - A Mathematical Model for the Rational Design of Chimeric Ligands in Selective Drug Therapies."""

    _SBML_ID = 'MODEL1907310001'
    _TITLE = 'DoldánMartelli2013 - A Mathematical Model for the Rational Design of Chimeric Ligands in Selective Drug Therapies'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['R_1_D', 'R_2_D', 'R_1_DE', 'R_2_DE', 'C_1', 'C_2', 'C_3']
    _SPECIES_LABELS = {'R_1_D': 'Target 1 Drug Complex', 'R_2_D': 'Target 2 Drug Complex', 'R_1_DE': 'Target 1 Drug Effector Complex', 'R_2_DE': 'Target 2 Drug Effector Complex', 'C_1': 'Selectivity Complex 1', 'C_2': 'Selectivity Complex 2', 'C_3': 'Selectivity Complex 3'}
    _PARAMETER_INPUTS = {'target_1_association_rate': ('k_on_1', 0.09, 'native SBML rate', 'target-1 association rate. Maps to SBML symbol `k_on_1`.'), 'target_1_dissociation_rate': ('k_off_1', 0.24, 'native SBML rate', 'target-1 dissociation rate. Maps to SBML symbol `k_off_1`.'), 'target_2_association_rate': ('k_wt_on_2', 0.22, 'native SBML rate', 'wild-type target-2 association rate. Maps to SBML symbol `k_wt_on_2`.'), 'target_2_dissociation_rate': ('k_wt_off_2', 0.66, 'native SBML rate', 'wild-type target-2 dissociation rate. Maps to SBML symbol `k_wt_off_2`.')}
    _INITIAL_CONDITION_INPUTS = {'ligand_concentration': ('L', 1.0, 'native SBML concentration', 'Initial setting for source boundary ligand concentration. Maps to SBML symbol `L`.')}
    _HEADLINE_OUTPUTS = {'target_1_drug_complex': ('R_1_D', 'native SBML value', 'Target 1 Drug Complex. Maps to SBML symbol `R_1_D`.'), 'target_2_drug_complex': ('R_2_D', 'native SBML value', 'Target 2 Drug Complex. Maps to SBML symbol `R_2_D`.'), 'target_1_drug_effector_complex': ('R_1_DE', 'native SBML value', 'Target 1 Drug Effector Complex. Maps to SBML symbol `R_1_DE`.'), 'target_2_drug_effector_complex': ('R_2_DE', 'native SBML value', 'Target 2 Drug Effector Complex. Maps to SBML symbol `R_2_DE`.'), 'selectivity_complex_1': ('C_1', 'native SBML value', 'Selectivity Complex 1. Maps to SBML symbol `C_1`.'), 'selectivity_complex_2': ('C_2', 'native SBML value', 'Selectivity Complex 2. Maps to SBML symbol `C_2`.'), 'selectivity_complex_3': ('C_3', 'native SBML value', 'Selectivity Complex 3. Maps to SBML symbol `C_3`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/MODEL1907310001.xml", integration_step: float = 0.2) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
