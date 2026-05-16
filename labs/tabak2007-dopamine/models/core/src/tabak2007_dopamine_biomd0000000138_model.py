# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule for Tabak2007_dopamine."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Tabak2007DopamineBiomd0000000138Model(TelluriumSBMLBioModule):
    """Faithfully executes the bundled SBML source for Tabak2007_dopamine."""

    _SBML_ID = 'BIOMD0000000138'
    _TITLE = 'Tabak2007_dopamine'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['c']
    _SPECIES_LABELS = {'c': 'Calcium Concentration'}
    _PARAMETER_INPUTS = {'calcium_conductance': ('gcal', 2.0, 'native SBML value', 'calcium conductance. Maps to SBML symbol `gcal`.'), 'potassium_conductance': ('gk', 4.0, 'native SBML value', 'potassium conductance. Maps to SBML symbol `gk`.'), 'sk_conductance': ('gsk', 1.7, 'native SBML value', 'SK conductance. Maps to SBML symbol `gsk`.'), 'membrane_capacitance': ('Cm', 10.0, 'native SBML value', 'membrane capacitance. Maps to SBML symbol `Cm`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_calcium_concentration': ('c', 0.3, 'native SBML concentration', 'initial calcium concentration. Maps to SBML symbol `c`.')}
    _HEADLINE_OUTPUTS = {'calcium_concentration': ('c', 'native SBML concentration', 'Calcium Concentration. Maps to SBML symbol `c`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/BIOMD0000000138.xml", integration_step: float = 0.2) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
