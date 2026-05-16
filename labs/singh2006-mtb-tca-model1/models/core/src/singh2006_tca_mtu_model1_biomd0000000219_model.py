# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule for Singh2006_TCA_mtu_model1."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Singh2006TcaMtuModel1Biomd0000000219Model(TelluriumSBMLBioModule):
    """Faithfully executes the bundled SBML source for Singh2006_TCA_mtu_model1."""

    _SBML_ID = 'BIOMD0000000219'
    _TITLE = 'Singh2006_TCA_mtu_model1'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['coa', 'aca', 'oaa', 'cit', 'icit', 'akg', 'ssa', 'suc']
    _SPECIES_LABELS = {'coa': 'Coa Pool', 'aca': 'Acetate Or Acetyl Pool', 'oaa': 'Oxaloacetate Pool', 'cit': 'Citrate Pool', 'icit': 'Isocitrate Pool', 'akg': 'Alpha Ketoglutarate Pool', 'ssa': 'Succinate Semialdehyde Pool', 'suc': 'Succinate Pool'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_coa_pool': ('coa', 0.0001, 'native SBML amount', 'CoA pool. Maps to SBML symbol `coa`.'), 'initial_acetate_or_acetyl_pool': ('aca', 0.5, 'native SBML amount', 'acetate/acetyl source pool. Maps to SBML symbol `aca`.'), 'initial_oxaloacetate_pool': ('oaa', 0.0003, 'native SBML amount', 'oxaloacetate pool. Maps to SBML symbol `oaa`.'), 'initial_citrate_pool': ('cit', 3.4, 'native SBML amount', 'citrate pool. Maps to SBML symbol `cit`.')}
    _HEADLINE_OUTPUTS = {'coa_pool': ('coa', 'native SBML amount', 'Coa Pool. Maps to SBML symbol `coa`.'), 'acetate_or_acetyl_pool': ('aca', 'native SBML amount', 'Acetate Or Acetyl Pool. Maps to SBML symbol `aca`.'), 'oxaloacetate_pool': ('oaa', 'native SBML amount', 'Oxaloacetate Pool. Maps to SBML symbol `oaa`.'), 'citrate_pool': ('cit', 'native SBML amount', 'Citrate Pool. Maps to SBML symbol `cit`.'), 'isocitrate_pool': ('icit', 'native SBML amount', 'Isocitrate Pool. Maps to SBML symbol `icit`.'), 'alpha_ketoglutarate_pool': ('akg', 'native SBML amount', 'Alpha Ketoglutarate Pool. Maps to SBML symbol `akg`.'), 'succinate_semialdehyde_pool': ('ssa', 'native SBML amount', 'Succinate Semialdehyde Pool. Maps to SBML symbol `ssa`.'), 'succinate_pool': ('suc', 'native SBML amount', 'Succinate Pool. Maps to SBML symbol `suc`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/BIOMD0000000219.xml", integration_step: float = 0.05) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
