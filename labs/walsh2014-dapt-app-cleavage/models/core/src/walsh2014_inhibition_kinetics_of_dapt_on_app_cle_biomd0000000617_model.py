# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule for Walsh2014 - Inhibition kinetics of DAPT on APP Cleavage."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Walsh2014InhibitionKineticsOfDaptOnAppCleBiomd0000000617Model(TelluriumSBMLBioModule):
    """Faithfully executes the bundled SBML source for Walsh2014 - Inhibition kinetics of DAPT on APP Cleavage."""

    _SBML_ID = 'BIOMD0000000617'
    _TITLE = 'Walsh2014 - Inhibition kinetics of DAPT on APP Cleavage'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['v']
    _SPECIES_LABELS = {'v': 'APP Cleavage State'}
    _PARAMETER_INPUTS = {'dapt_inhibitor_concentration': ('Ii', 1000.0, 'native SBML concentration', 'inhibitor concentration. Maps to SBML symbol `Ii`.'), 'substrate_concentration': ('S', 61.0, 'native SBML concentration', 'APP substrate concentration. Maps to SBML symbol `S`.'), 'cleavage_vmax_1': ('V1', 20.06, 'native SBML rate', 'first cleavage Vmax. Maps to SBML symbol `V1`.'), 'cleavage_vmax_2': ('V2', 443.68, 'native SBML rate', 'second cleavage Vmax. Maps to SBML symbol `V2`.')}
    _INITIAL_CONDITION_INPUTS = {'cleavage_state': ('v', 1.0, 'native SBML value', 'Initial setting for model cleavage state. Maps to SBML symbol `v`.')}
    _HEADLINE_OUTPUTS = {'app_cleavage_state': ('v', 'native SBML value', 'APP Cleavage State. Maps to SBML symbol `v`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/BIOMD0000000617.xml", integration_step: float = 0.2) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
