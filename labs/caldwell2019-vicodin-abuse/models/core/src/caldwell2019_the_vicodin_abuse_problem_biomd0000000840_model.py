# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule for Caldwell2019 - The Vicodin abuse problem."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Caldwell2019TheVicodinAbuseProblemBiomd0000000840Model(TelluriumSBMLBioModule):
    """Faithfully executes the bundled SBML source for Caldwell2019 - The Vicodin abuse problem."""

    _SBML_ID = 'BIOMD0000000840'
    _TITLE = 'Caldwell2019 - The Vicodin abuse problem'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['M', 'C1', 'C2', 'A', 'T']
    _SPECIES_LABELS = {'M': 'Medical Vicodin Population', 'C1': 'Early Chronic Vicodin Population', 'C2': 'Late Chronic Vicodin Population', 'A': 'Vicodin Abuse Population', 'T': 'Vicodin Treatment Population'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_medical_vicodin_population': ('M', 37600000.0, 'people', 'initial medically prescribed Vicodin-use population. Maps to SBML symbol `M`.'), 'initial_early_chronic_vicodin_population': ('C1', 5640000.0, 'people', 'initial early chronic-use population. Maps to SBML symbol `C1`.'), 'initial_late_chronic_vicodin_population': ('C2', 3760000.0, 'people', 'initial late chronic-use population. Maps to SBML symbol `C2`.'), 'initial_vicodin_abuse_population': ('A', 2000000.0, 'people', 'initial abuse population. Maps to SBML symbol `A`.'), 'initial_vicodin_treatment_population': ('T', 700000.0, 'people', 'initial treatment population. Maps to SBML symbol `T`.')}
    _HEADLINE_OUTPUTS = {'medical_vicodin_population': ('M', 'people', 'Medical Vicodin Population. Maps to SBML symbol `M`.'), 'early_chronic_vicodin_population': ('C1', 'people', 'Early Chronic Vicodin Population. Maps to SBML symbol `C1`.'), 'late_chronic_vicodin_population': ('C2', 'people', 'Late Chronic Vicodin Population. Maps to SBML symbol `C2`.'), 'vicodin_abuse_population': ('A', 'people', 'Vicodin Abuse Population. Maps to SBML symbol `A`.'), 'vicodin_treatment_population': ('T', 'people', 'Vicodin Treatment Population. Maps to SBML symbol `T`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/BIOMD0000000840.xml", integration_step: float = 0.05) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
