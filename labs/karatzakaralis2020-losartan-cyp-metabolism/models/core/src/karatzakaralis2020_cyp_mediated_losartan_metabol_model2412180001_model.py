# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule for KaratzaKaralis2020 - CYP mediated losartan metabolism."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Karatzakaralis2020CypMediatedLosartanMetabolModel2412180001Model(TelluriumSBMLBioModule):
    """Faithfully executes the bundled SBML source for KaratzaKaralis2020 - CYP mediated losartan metabolism."""

    _SBML_ID = 'MODEL2412180001'
    _TITLE = 'KaratzaKaralis2020 - CYP mediated losartan metabolism'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['losartan_cc', 'losartan_int', 'losartan_out', 'losartan_pc', 'losartan_stm', 'E3174_out', 'E3174_cc']
    _SPECIES_LABELS = {'losartan_cc': 'Losartan Cellular Compartment', 'losartan_int': 'Losartan Intracellular', 'losartan_out': 'Losartan Outflow', 'losartan_pc': 'Losartan Portal Compartment', 'losartan_stm': 'Losartan Stomach', 'E3174_out': 'E3174 Outflow', 'E3174_cc': 'E3174 Cellular Compartment'}
    _PARAMETER_INPUTS = {'losartan_oral_dose': ('oral_dose', 100.0, 'native SBML value', 'losartan oral dose parameter. Maps to SBML symbol `oral_dose`.'), 'cyp2c9_metabolism_start_time': ('start_CYP2C9', 0.0, 'native SBML value', 'start time for CYP2C9-mediated metabolism. Maps to SBML symbol `start_CYP2C9`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_losartan_stomach': ('losartan_stm', 0.0, 'native SBML value', 'initial stomach losartan state, if dose parameter alone does not drive the simulator. Maps to SBML symbol `losartan_stm`.')}
    _HEADLINE_OUTPUTS = {'losartan_cellular_compartment': ('losartan_cc', 'native SBML value', 'Losartan Cellular Compartment. Maps to SBML symbol `losartan_cc`.'), 'losartan_intracellular': ('losartan_int', 'native SBML value', 'Losartan Intracellular. Maps to SBML symbol `losartan_int`.'), 'losartan_outflow': ('losartan_out', 'native SBML value', 'Losartan Outflow. Maps to SBML symbol `losartan_out`.'), 'losartan_portal_compartment': ('losartan_pc', 'native SBML value', 'Losartan Portal Compartment. Maps to SBML symbol `losartan_pc`.'), 'losartan_stomach': ('losartan_stm', 'native SBML value', 'Losartan Stomach. Maps to SBML symbol `losartan_stm`.'), 'e3174_outflow': ('E3174_out', 'native SBML value', 'E3174 Outflow. Maps to SBML symbol `E3174_out`.'), 'e3174_cellular_compartment': ('E3174_cc', 'native SBML value', 'E3174 Cellular Compartment. Maps to SBML symbol `E3174_cc`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/MODEL2412180001.xml", integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
