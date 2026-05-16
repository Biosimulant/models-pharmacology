# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule for Landberg2009 - Alkylresorcinol Dose Response."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Landberg2009AlkylresorcinolDoseResponseBiomd0000000948Model(TelluriumSBMLBioModule):
    """Faithfully executes the bundled SBML source for Landberg2009 - Alkylresorcinol Dose Response."""

    _SBML_ID = 'BIOMD0000000948'
    _TITLE = 'Landberg2009 - Alkylresorcinol Dose Response'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['AR_Dose', 'AR_A1', 'AR_A2', 'AR_Central', 'F1', 'F2']
    _SPECIES_LABELS = {'AR_Dose': 'Alkylresorcinol Dose Pool', 'AR_A1': 'Alkylresorcinol Absorption Pool 1', 'AR_A2': 'Alkylresorcinol Absorption Pool 2', 'AR_Central': 'Alkylresorcinol Central Concentration', 'F1': 'Bioavailability Fraction 1', 'F2': 'Bioavailability Fraction 2'}
    _PARAMETER_INPUTS = {'fast_absorption_rate': ('k_a_1', 0.3, 'native SBML rate', 'first absorption-rate constant. Maps to SBML symbol `k_a_1`.'), 'slow_absorption_rate': ('k_a_2', 1.8, 'native SBML rate', 'second absorption-rate constant. Maps to SBML symbol `k_a_2`.'), 'clearance_over_volume': ('CL_V', 20.0, 'native SBML rate', 'apparent clearance over volume. Maps to SBML symbol `CL_V`.'), 'baseline_concentration': ('base', 0.32, 'native SBML concentration', 'baseline concentration. Maps to SBML symbol `base`.')}
    _INITIAL_CONDITION_INPUTS = {'alkylresorcinol_dose': ('AR_Dose', 485.0, 'native SBML value', 'Initial setting for alkylresorcinol dose state. Maps to SBML symbol `AR_Dose`.')}
    _HEADLINE_OUTPUTS = {'alkylresorcinol_dose_pool': ('AR_Dose', 'native SBML amount', 'Alkylresorcinol Dose Pool. Maps to SBML symbol `AR_Dose`.'), 'alkylresorcinol_absorption_pool_1': ('AR_A1', 'native SBML amount', 'Alkylresorcinol Absorption Pool 1. Maps to SBML symbol `AR_A1`.'), 'alkylresorcinol_absorption_pool_2': ('AR_A2', 'native SBML amount', 'Alkylresorcinol Absorption Pool 2. Maps to SBML symbol `AR_A2`.'), 'alkylresorcinol_central_concentration': ('AR_Central', 'native SBML concentration', 'Alkylresorcinol Central Concentration. Maps to SBML symbol `AR_Central`.'), 'bioavailability_fraction_1': ('F1', 'fraction', 'Bioavailability Fraction 1. Maps to SBML symbol `F1`.'), 'bioavailability_fraction_2': ('F2', 'fraction', 'Bioavailability Fraction 2. Maps to SBML symbol `F2`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/BIOMD0000000948.xml", integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
