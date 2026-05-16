# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule for Yang2006_Methadone_PKmodel."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Yang2006MethadonePkmodelModel1006230040Model(TelluriumSBMLBioModule):
    """Faithfully executes the bundled SBML source for Yang2006_Methadone_PKmodel."""

    _SBML_ID = 'MODEL1006230040'
    _TITLE = 'Yang2006_Methadone_PKmodel'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = ['Ca', 'C']
    _SPECIES_LABELS = {'Ca': 'Methadone Absorption State', 'C': 'Methadone Concentration'}
    _PARAMETER_INPUTS = {'initial_methadone_absorption_state': ('Ca', 6.6685, 'native SBML value', 'initial absorption/central source state Ca. Maps to SBML symbol `Ca`.'), 'initial_methadone_concentration': ('C', 0.0, 'native SBML concentration', 'initial methadone concentration/state C. Maps to SBML symbol `C`.'), 'metabolism_vmax': ('Vmax', 0.009433, 'native SBML rate', 'saturable metabolism Vmax. Maps to SBML symbol `Vmax`.'), 'metabolism_km': ('Km', 198.0, 'native SBML value', 'saturable metabolism Km. Maps to SBML symbol `Km`.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'methadone_absorption_state': ('Ca', 'native SBML value', 'Methadone Absorption State. Maps to SBML symbol `Ca`.'), 'methadone_concentration': ('C', 'native SBML concentration', 'Methadone Concentration. Maps to SBML symbol `C`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/MODEL1006230040.xml", integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
