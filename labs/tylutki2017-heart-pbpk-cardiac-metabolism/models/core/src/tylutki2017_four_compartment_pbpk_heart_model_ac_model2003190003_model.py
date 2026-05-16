# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule for Tylutki2017-four-compartment PBPK heart model accounting for cardiac metabolism."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Tylutki2017FourCompartmentPbpkHeartModelAcModel2003190003Model(TelluriumSBMLBioModule):
    """Faithfully executes the bundled SBML source for Tylutki2017-four-compartment PBPK heart model accounting for cardiac metabolism."""

    _SBML_ID = 'MODEL2003190003'
    _TITLE = 'Tylutki2017-four-compartment PBPK heart model accounting for cardiac metabolism'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['A_ad', 'A_bo', 'A_br', 'A_gu', 'A_epi', 'A_mid', 'A_endo', 'A_pf']
    _SPECIES_LABELS = {'A_ad': 'Adipose Drug Amount', 'A_bo': 'Bone Drug Amount', 'A_br': 'Brain Drug Amount', 'A_gu': 'Gut Drug Amount', 'A_epi': 'Epicardium Drug Amount', 'A_mid': 'Myocardium Drug Amount', 'A_endo': 'Endocardium Drug Amount', 'A_pf': 'Perfusate Drug Amount'}
    _PARAMETER_INPUTS = {'fraction_absorbed': ('F_abs', 0.5, 'fraction', 'absorption fraction. Maps to SBML symbol `F_abs`.'), 'absorption_rate': ('k_a', 0.80075, 'native SBML rate', 'absorption rate. Maps to SBML symbol `k_a`.'), 'renal_clearance': ('CL_renal', 0.504, 'native SBML rate', 'renal clearance. Maps to SBML symbol `CL_renal`.'), 'cyp2c9_expression': ('CYP2C9', 5.5, 'native SBML value', 'CYP2C9 expression/activity amount. Maps to SBML symbol `CYP2C9`.'), 'cyp2c8_expression': ('CYP2C8', 0.2, 'native SBML value', 'CYP2C8 expression/activity amount. Maps to SBML symbol `CYP2C8`.')}
    _INITIAL_CONDITION_INPUTS = {'drug_dose': ('D', 2.5, 'native SBML value', 'Initial setting for source dose state. Maps to SBML symbol `D`.')}
    _HEADLINE_OUTPUTS = {'adipose_drug_amount': ('A_ad', 'native SBML amount', 'Adipose Drug Amount. Maps to SBML symbol `A_ad`.'), 'bone_drug_amount': ('A_bo', 'native SBML amount', 'Bone Drug Amount. Maps to SBML symbol `A_bo`.'), 'brain_drug_amount': ('A_br', 'native SBML amount', 'Brain Drug Amount. Maps to SBML symbol `A_br`.'), 'gut_drug_amount': ('A_gu', 'native SBML amount', 'Gut Drug Amount. Maps to SBML symbol `A_gu`.'), 'epicardium_drug_amount': ('A_epi', 'native SBML amount', 'Epicardium Drug Amount. Maps to SBML symbol `A_epi`.'), 'myocardium_drug_amount': ('A_mid', 'native SBML amount', 'Myocardium Drug Amount. Maps to SBML symbol `A_mid`.'), 'endocardium_drug_amount': ('A_endo', 'native SBML amount', 'Endocardium Drug Amount. Maps to SBML symbol `A_endo`.'), 'perfusate_drug_amount': ('A_pf', 'native SBML amount', 'Perfusate Drug Amount. Maps to SBML symbol `A_pf`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/MODEL2003190003.xml", integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
