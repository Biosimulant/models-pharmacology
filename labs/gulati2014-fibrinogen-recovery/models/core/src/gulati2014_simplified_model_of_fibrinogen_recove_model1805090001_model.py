# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule for Gulati2014 - Simplified model of fibrinogen recovery following brown snake bite_1."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Gulati2014SimplifiedModelOfFibrinogenRecoveModel1805090001Model(TelluriumSBMLBioModule):
    """Faithfully executes the bundled SBML source for Gulati2014 - Simplified model of fibrinogen recovery following brown snake bite_1."""

    _SBML_ID = 'MODEL1805090001'
    _TITLE = 'Gulati2014 - Simplified model of fibrinogen recovery following brown snake bite_1'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Venom_plasma1', 'Fibrinogen_g_l', 'Fibrinogen1', 'Venom_Absorption1', 'IIa1']
    _SPECIES_LABELS = {'Venom_plasma1': 'Plasma Venom', 'Fibrinogen_g_l': 'Fibrinogen G Per L', 'Fibrinogen1': 'Fibrinogen Pool', 'Venom_Absorption1': 'Venom Absorption', 'IIa1': 'Thrombin Activity'}
    _PARAMETER_INPUTS = {'brown_snake_venom_fraction': ('BSV_F_venom', 1.4, 'fraction', 'venom fraction parameter. Maps to SBML symbol `BSV_F_venom`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_plasma_venom': ('Venom_plasma1', 0.0, 'native SBML value', 'initial plasma venom state. Maps to SBML symbol `Venom_plasma1`.'), 'initial_thrombin_activity': ('IIa1', 0.0, 'native SBML value', 'initial thrombin activity state. Maps to SBML symbol `IIa1`.')}
    _HEADLINE_OUTPUTS = {'plasma_venom': ('Venom_plasma1', 'native SBML value', 'Plasma Venom. Maps to SBML symbol `Venom_plasma1`.'), 'fibrinogen_g_per_l': ('Fibrinogen_g_l', 'native SBML value', 'Fibrinogen G Per L. Maps to SBML symbol `Fibrinogen_g_l`.'), 'fibrinogen_pool': ('Fibrinogen1', 'native SBML amount', 'Fibrinogen Pool. Maps to SBML symbol `Fibrinogen1`.'), 'venom_absorption': ('Venom_Absorption1', 'native SBML value', 'Venom Absorption. Maps to SBML symbol `Venom_Absorption1`.'), 'thrombin_activity': ('IIa1', 'native SBML value', 'Thrombin Activity. Maps to SBML symbol `IIa1`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/MODEL1805090001.xml", integration_step: float = 0.05) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
