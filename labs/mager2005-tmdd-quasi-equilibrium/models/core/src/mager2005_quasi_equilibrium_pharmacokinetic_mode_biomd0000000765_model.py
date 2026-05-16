# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule for Mager2005 - Quasi-equilibrium pharmacokinetic model for drugs exhibiting target-mediated drug disposition."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Mager2005QuasiEquilibriumPharmacokineticModeBiomd0000000765Model(TelluriumSBMLBioModule):
    """Faithfully executes the bundled SBML source for Mager2005 - Quasi-equilibrium pharmacokinetic model for drugs exhibiting target-mediated drug disposition."""

    _SBML_ID = 'BIOMD0000000765'
    _TITLE = 'Mager2005 - Quasi-equilibrium pharmacokinetic model for drugs exhibiting target-mediated drug disposition'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['C', 'A_T', 'R', 'RC']
    _SPECIES_LABELS = {'C': 'Free Drug Concentration', 'A_T': 'Total Target Amount', 'R': 'Free Target Concentration', 'RC': 'Drug Target Complex'}
    _PARAMETER_INPUTS = {'target_binding_affinity_kd': ('K_D', 1.0, 'native SBML value', 'binding dissociation constant. Maps to SBML symbol `K_D`.'), 'drug_elimination_rate': ('k_el', 1.0, 'native SBML rate', 'drug elimination rate. Maps to SBML symbol `k_el`.'), 'complex_internalization_rate': ('k_int', 0.0, 'native SBML rate', 'drug-target complex internalization rate. Maps to SBML symbol `k_int`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_free_drug_concentration': ('C', 4000.0, 'native SBML concentration', 'initial free drug concentration. Maps to SBML symbol `C`.'), 'initial_free_target_concentration': ('R', 53.0, 'native SBML concentration', 'initial free target concentration. Maps to SBML symbol `R`.')}
    _HEADLINE_OUTPUTS = {'free_drug_concentration': ('C', 'native SBML concentration', 'Free Drug Concentration. Maps to SBML symbol `C`.'), 'total_target_amount': ('A_T', 'native SBML amount', 'Total Target Amount. Maps to SBML symbol `A_T`.'), 'free_target_concentration': ('R', 'native SBML concentration', 'Free Target Concentration. Maps to SBML symbol `R`.'), 'drug_target_complex': ('RC', 'native SBML value', 'Drug Target Complex. Maps to SBML symbol `RC`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/BIOMD0000000765.xml", integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
