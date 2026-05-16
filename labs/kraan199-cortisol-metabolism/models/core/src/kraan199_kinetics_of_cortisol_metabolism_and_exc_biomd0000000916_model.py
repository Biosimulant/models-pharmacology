# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule for Kraan199_Kinetics of Cortisol Metabolism and Excretion.."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kraan199KineticsOfCortisolMetabolismAndExcBiomd0000000916Model(TelluriumSBMLBioModule):
    """Faithfully executes the bundled SBML source for Kraan199_Kinetics of Cortisol Metabolism and Excretion.."""

    _SBML_ID = 'BIOMD0000000916'
    _TITLE = 'Kraan199_Kinetics of Cortisol Metabolism and Excretion.'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['The_FOD_in_the_circulation__X1', 'The_FOD_in_the_metabolizing_tissues__X4', 'The_cumulative_FOD_excreted_in_the_urine__X2', 'The_cumulative_FOD_excreted_in_the_non_urinary_pool__X3', 'The_FOD_in_the_gallbladder___intestinal_lumen__X5']
    _SPECIES_LABELS = {'The_FOD_in_the_circulation__X1': 'Circulating Cortisol', 'The_FOD_in_the_metabolizing_tissues__X4': 'Metabolizing Tissue Cortisol', 'The_cumulative_FOD_excreted_in_the_urine__X2': 'Urinary Excreted Cortisol', 'The_cumulative_FOD_excreted_in_the_non_urinary_pool__X3': 'Non Urinary Excreted Cortisol', 'The_FOD_in_the_gallbladder___intestinal_lumen__X5': 'Gallbladder Intestinal Cortisol'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_circulating_cortisol': ('The_FOD_in_the_circulation__X1', 1.0, 'native SBML value', 'initial circulating cortisol/FOD state. Maps to SBML symbol `The_FOD_in_the_circulation__X1`.'), 'initial_urinary_excreted_cortisol': ('The_cumulative_FOD_excreted_in_the_urine__X2', 0.0, 'native SBML value', 'initial urinary excreted pool. Maps to SBML symbol `The_cumulative_FOD_excreted_in_the_urine__X2`.'), 'initial_non_urinary_excreted_cortisol': ('The_cumulative_FOD_excreted_in_the_non_urinary_pool__X3', 0.0, 'native SBML value', 'initial non-urinary excreted pool. Maps to SBML symbol `The_cumulative_FOD_excreted_in_the_non_urinary_pool__X3`.'), 'initial_metabolizing_tissue_cortisol': ('The_FOD_in_the_metabolizing_tissues__X4', 0.0, 'native SBML value', 'initial metabolizing tissue pool. Maps to SBML symbol `The_FOD_in_the_metabolizing_tissues__X4`.')}
    _HEADLINE_OUTPUTS = {'circulating_cortisol': ('The_FOD_in_the_circulation__X1', 'native SBML value', 'Circulating Cortisol. Maps to SBML symbol `The_FOD_in_the_circulation__X1`.'), 'metabolizing_tissue_cortisol': ('The_FOD_in_the_metabolizing_tissues__X4', 'native SBML value', 'Metabolizing Tissue Cortisol. Maps to SBML symbol `The_FOD_in_the_metabolizing_tissues__X4`.'), 'urinary_excreted_cortisol': ('The_cumulative_FOD_excreted_in_the_urine__X2', 'native SBML value', 'Urinary Excreted Cortisol. Maps to SBML symbol `The_cumulative_FOD_excreted_in_the_urine__X2`.'), 'non_urinary_excreted_cortisol': ('The_cumulative_FOD_excreted_in_the_non_urinary_pool__X3', 'native SBML value', 'Non Urinary Excreted Cortisol. Maps to SBML symbol `The_cumulative_FOD_excreted_in_the_non_urinary_pool__X3`.'), 'gallbladder_intestinal_cortisol': ('The_FOD_in_the_gallbladder___intestinal_lumen__X5', 'native SBML value', 'Gallbladder Intestinal Cortisol. Maps to SBML symbol `The_FOD_in_the_gallbladder___intestinal_lumen__X5`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/BIOMD0000000916.xml", integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
