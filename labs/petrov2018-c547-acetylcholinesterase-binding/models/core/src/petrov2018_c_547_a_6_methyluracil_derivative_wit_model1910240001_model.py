# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule for Petrov2018 - C-547 a 6-methyluracil derivative with long-lasting binding and rebinding on acetylcholinesterase."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Petrov2018C547A6MethyluracilDerivativeWitModel1910240001Model(TelluriumSBMLBioModule):
    """Faithfully executes the bundled SBML source for Petrov2018 - C-547 a 6-methyluracil derivative with long-lasting binding and rebinding on acetylcholinesterase."""

    _SBML_ID = 'MODEL1910240001'
    _TITLE = 'Petrov2018 - C-547 a 6-methyluracil derivative with long-lasting binding and rebinding on acetylcholinesterase'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['y1', 'y2', 'y3', 'y4', 'y5']
    _SPECIES_LABELS = {'y1': 'C547 Binding State Y1', 'y2': 'C547 Binding State Y2', 'y3': 'C547 Binding State Y3', 'y4': 'C547 Binding State Y4', 'y5': 'C547 Binding State Y5'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_c547_binding_state_y1': ('y1', 0.0, 'native SBML value', 'initial binding state y1. Maps to SBML symbol `y1`.'), 'initial_c547_binding_state_y2': ('y2', 0.0, 'native SBML value', 'initial binding state y2. Maps to SBML symbol `y2`.'), 'initial_c547_binding_state_y3': ('y3', 75.0, 'native SBML value', 'initial binding state y3. Maps to SBML symbol `y3`.'), 'initial_c547_binding_state_y4': ('y4', 0.0, 'native SBML value', 'initial binding state y4. Maps to SBML symbol `y4`.'), 'initial_c547_binding_state_y5': ('y5', 75.0, 'native SBML value', 'initial binding state y5. Maps to SBML symbol `y5`.')}
    _HEADLINE_OUTPUTS = {'c547_binding_state_y1': ('y1', 'native SBML value', 'C547 Binding State Y1. Maps to SBML symbol `y1`.'), 'c547_binding_state_y2': ('y2', 'native SBML value', 'C547 Binding State Y2. Maps to SBML symbol `y2`.'), 'c547_binding_state_y3': ('y3', 'native SBML value', 'C547 Binding State Y3. Maps to SBML symbol `y3`.'), 'c547_binding_state_y4': ('y4', 'native SBML value', 'C547 Binding State Y4. Maps to SBML symbol `y4`.'), 'c547_binding_state_y5': ('y5', 'native SBML value', 'C547 Binding State Y5. Maps to SBML symbol `y5`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/MODEL1910240001.xml", integration_step: float = 0.2) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
