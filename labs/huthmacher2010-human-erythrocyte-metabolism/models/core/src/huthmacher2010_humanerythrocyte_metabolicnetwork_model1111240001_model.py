# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule for Huthmacher2010_HumanErythrocyte_MetabolicNetwork."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Huthmacher2010HumanerythrocyteMetabolicnetworkModel1111240001Model(TelluriumSBMLBioModule):
    """Faithfully executes the bundled SBML source for Huthmacher2010_HumanErythrocyte_MetabolicNetwork."""

    _SBML_ID = 'MODEL1111240001'
    _TITLE = 'Huthmacher2010_HumanErythrocyte_MetabolicNetwork'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['C00002_c_host', 'C00003_c_host', 'C00004_c_host', 'C00022_c_host', 'C00103_c_host', 'C00131_c_host']
    _SPECIES_LABELS = {'C00002_c_host': 'Erythrocyte ATP', 'C00003_c_host': 'Erythrocyte NAD', 'C00004_c_host': 'Erythrocyte NADH', 'C00022_c_host': 'Pyruvate', 'C00103_c_host': 'Glucose 1 Phosphate', 'C00131_c_host': 'Datp'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_erythrocyte_atp': ('C00002_c_host', 0.0, 'native SBML value', 'ATP pool. Maps to SBML symbol `C00002_c_host`.'), 'initial_erythrocyte_nad': ('C00003_c_host', 0.0, 'native SBML value', 'NAD pool. Maps to SBML symbol `C00003_c_host`.'), 'initial_erythrocyte_nadh': ('C00004_c_host', 0.0, 'native SBML value', 'NADH pool. Maps to SBML symbol `C00004_c_host`.'), 'initial_pyruvate': ('C00022_c_host', 0.0, 'native SBML value', 'pyruvate pool. Maps to SBML symbol `C00022_c_host`.'), 'initial_glucose_1_phosphate': ('C00103_c_host', 0.0, 'native SBML value', 'glucose-1-phosphate pool. Maps to SBML symbol `C00103_c_host`.')}
    _HEADLINE_OUTPUTS = {'erythrocyte_atp': ('C00002_c_host', 'native SBML value', 'Erythrocyte ATP. Maps to SBML symbol `C00002_c_host`.'), 'erythrocyte_nad': ('C00003_c_host', 'native SBML value', 'Erythrocyte NAD. Maps to SBML symbol `C00003_c_host`.'), 'erythrocyte_nadh': ('C00004_c_host', 'native SBML value', 'Erythrocyte NADH. Maps to SBML symbol `C00004_c_host`.'), 'pyruvate': ('C00022_c_host', 'native SBML value', 'Pyruvate. Maps to SBML symbol `C00022_c_host`.'), 'glucose_1_phosphate': ('C00103_c_host', 'native SBML value', 'Glucose 1 Phosphate. Maps to SBML symbol `C00103_c_host`.'), 'datp': ('C00131_c_host', 'native SBML value', 'Datp. Maps to SBML symbol `C00131_c_host`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/MODEL1111240001.xml", integration_step: float = 0.05) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
