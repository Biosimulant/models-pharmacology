# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule for Singh2006_TCA_Ecoli_acetate."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Singh2006TcaEcoliAcetateBiomd0000000221Model(TelluriumSBMLBioModule):
    """Faithfully executes the bundled SBML source for Singh2006_TCA_Ecoli_acetate."""

    _SBML_ID = 'BIOMD0000000221'
    _TITLE = 'Singh2006_TCA_Ecoli_acetate'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['aca', 'oaa', 'coa', 'cit', 'icit', 'akg', 'sca', 'suc']
    _SPECIES_LABELS = {'aca': 'Acetate Or Acetyl Coa Pool', 'oaa': 'Oxaloacetate Pool', 'coa': 'Coa Pool', 'cit': 'Citrate Pool', 'icit': 'Isocitrate Pool', 'akg': 'Alpha Ketoglutarate Pool', 'sca': 'Succinyl Coa Pool', 'suc': 'Succinate Pool'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_acetyl_coa_or_acetate_pool': ('aca', 0.5, 'native SBML amount', 'source `aca` TCA input pool. Maps to SBML symbol `aca`.'), 'initial_oxaloacetate_pool': ('oaa', 0.0014, 'native SBML amount', 'oxaloacetate pool. Maps to SBML symbol `oaa`.'), 'initial_coa_pool': ('coa', 0.0001, 'native SBML amount', 'CoA pool. Maps to SBML symbol `coa`.'), 'initial_citrate_pool': ('cit', 9.0, 'native SBML amount', 'citrate pool. Maps to SBML symbol `cit`.')}
    _HEADLINE_OUTPUTS = {'acetate_or_acetyl_coa_pool': ('aca', 'native SBML amount', 'Acetate Or Acetyl Coa Pool. Maps to SBML symbol `aca`.'), 'oxaloacetate_pool': ('oaa', 'native SBML amount', 'Oxaloacetate Pool. Maps to SBML symbol `oaa`.'), 'coa_pool': ('coa', 'native SBML amount', 'Coa Pool. Maps to SBML symbol `coa`.'), 'citrate_pool': ('cit', 'native SBML amount', 'Citrate Pool. Maps to SBML symbol `cit`.'), 'isocitrate_pool': ('icit', 'native SBML amount', 'Isocitrate Pool. Maps to SBML symbol `icit`.'), 'alpha_ketoglutarate_pool': ('akg', 'native SBML amount', 'Alpha Ketoglutarate Pool. Maps to SBML symbol `akg`.'), 'succinyl_coa_pool': ('sca', 'native SBML amount', 'Succinyl Coa Pool. Maps to SBML symbol `sca`.'), 'succinate_pool': ('suc', 'native SBML amount', 'Succinate Pool. Maps to SBML symbol `suc`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/BIOMD0000000221.xml", integration_step: float = 0.05) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
