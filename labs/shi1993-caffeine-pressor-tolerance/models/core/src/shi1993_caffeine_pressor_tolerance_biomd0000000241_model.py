# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule for Shi1993_Caffeine_pressor_tolerance."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Shi1993CaffeinePressorToleranceBiomd0000000241Model(TelluriumSBMLBioModule):
    """Faithfully executes the bundled SBML source for Shi1993_Caffeine_pressor_tolerance."""

    _SBML_ID = 'BIOMD0000000241'
    _TITLE = 'Shi1993_Caffeine_pressor_tolerance'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['X_gut', 'C_p', 'C_per', 'C_e', 'C_t']
    _SPECIES_LABELS = {'X_gut': 'Gut Caffeine Amount', 'C_p': 'Plasma Caffeine Concentration', 'C_per': 'Peripheral Caffeine Concentration', 'C_e': 'Effect Site Caffeine Concentration', 'C_t': 'Tolerance State'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_gut_caffeine_amount': ('X_gut', 0.0, 'native SBML amount', 'initial gut caffeine amount. Maps to SBML symbol `X_gut`.'), 'initial_plasma_caffeine_concentration': ('C_p', 0.0, 'native SBML concentration', 'initial plasma caffeine concentration. Maps to SBML symbol `C_p`.'), 'initial_effect_site_caffeine': ('C_e', 0.0, 'native SBML value', 'initial effect-site caffeine concentration. Maps to SBML symbol `C_e`.'), 'initial_tolerance_state': ('C_t', 0.0, 'native SBML value', 'initial tolerance-state variable. Maps to SBML symbol `C_t`.')}
    _HEADLINE_OUTPUTS = {'gut_caffeine_amount': ('X_gut', 'native SBML amount', 'Gut Caffeine Amount. Maps to SBML symbol `X_gut`.'), 'plasma_caffeine_concentration': ('C_p', 'native SBML concentration', 'Plasma Caffeine Concentration. Maps to SBML symbol `C_p`.'), 'peripheral_caffeine_concentration': ('C_per', 'native SBML concentration', 'Peripheral Caffeine Concentration. Maps to SBML symbol `C_per`.'), 'effect_site_caffeine_concentration': ('C_e', 'native SBML concentration', 'Effect Site Caffeine Concentration. Maps to SBML symbol `C_e`.'), 'tolerance_state': ('C_t', 'native SBML value', 'Tolerance State. Maps to SBML symbol `C_t`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/BIOMD0000000241.xml", integration_step: float = 0.2) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
