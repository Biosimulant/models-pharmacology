# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule for Simon2019 - NIK-dependent p100 processing into p52, Mass Action, SBML 2v4."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Simon2019NikDependentP100ProcessingIntoP52Biomd0000000868Model(TelluriumSBMLBioModule):
    """Faithfully executes the bundled SBML source for Simon2019 - NIK-dependent p100 processing into p52, Mass Action, SBML 2v4."""

    _SBML_ID = 'BIOMD0000000868'
    _TITLE = 'Simon2019 - NIK-dependent p100 processing into p52, Mass Action, SBML 2v4'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['p100_NIK', 'p100', 'p52', 'NIK']
    _SPECIES_LABELS = {'p100_NIK': 'P100 NIK Complex', 'p100': 'P100 Pool', 'p52': 'P52 Pool', 'NIK': 'NIK Pool'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_p100_pool': ('p100', 0.0, 'native SBML amount', 'initial p100 pool. Maps to SBML symbol `p100`.'), 'initial_nik_pool': ('NIK', 10.0, 'native SBML amount', 'initial NIK pool. Maps to SBML symbol `NIK`.'), 'initial_p100_nik_complex': ('p100_NIK', 0.0, 'native SBML value', 'initial p100:NIK complex. Maps to SBML symbol `p100_NIK`.'), 'total_p100_boundary_pool': ('p100t', 2.5, 'native SBML amount', 'Initial setting for total/boundary p100 pool. Maps to SBML symbol `p100t`.')}
    _HEADLINE_OUTPUTS = {'p100_nik_complex': ('p100_NIK', 'native SBML value', 'P100 NIK Complex. Maps to SBML symbol `p100_NIK`.'), 'p100_pool': ('p100', 'native SBML amount', 'P100 Pool. Maps to SBML symbol `p100`.'), 'p52_pool': ('p52', 'native SBML amount', 'P52 Pool. Maps to SBML symbol `p52`.'), 'nik_pool': ('NIK', 'native SBML amount', 'NIK Pool. Maps to SBML symbol `NIK`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/BIOMD0000000868.xml", integration_step: float = 0.2) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
