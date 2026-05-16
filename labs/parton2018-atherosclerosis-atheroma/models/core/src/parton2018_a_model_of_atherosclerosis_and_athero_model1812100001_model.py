# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule for Parton2018 - A model of Atherosclerosis and atheroma formation.."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Parton2018AModelOfAtherosclerosisAndAtheroModel1812100001Model(TelluriumSBMLBioModule):
    """Faithfully executes the bundled SBML source for Parton2018 - A model of Atherosclerosis and atheroma formation.."""

    _SBML_ID = 'MODEL1812100001'
    _TITLE = 'Parton2018 - A model of Atherosclerosis and atheroma formation.'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['s1', 's2', 's5', 's6', 's14', 's15', 's16', 's19', 's21']
    _SPECIES_LABELS = {'s1': 'HDL', 's2': 'LDL', 's5': 'Blood LDL', 's6': 'Blood HDL', 's14': 'Oxidized LDL', 's15': 'Oxidized HDL', 's16': 'Monocytes', 's19': 'Macrophages', 's21': 'Foam Cells'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_ldl': ('s5', 190000.0, 'native SBML value', 'initial LDL pool. Maps to SBML symbol `s5`.'), 'initial_hdl': ('s6', 40000.0, 'native SBML value', 'initial HDL pool. Maps to SBML symbol `s6`.'), 'initial_free_oxygen_radicals': ('s10', 500.0, 'native SBML value', 'oxidative burden pool. Maps to SBML symbol `s10`.'), 'initial_monocytes': ('s16', 20000.0, 'native SBML value', 'monocyte pool. Maps to SBML symbol `s16`.'), 'initial_t_cells': ('s39', 500000.0, 'native SBML value', 'T-cell pool. Maps to SBML symbol `s39`.')}
    _HEADLINE_OUTPUTS = {'hdl': ('s1', 'native SBML value', 'HDL. Maps to SBML symbol `s1`.'), 'ldl': ('s2', 'native SBML value', 'LDL. Maps to SBML symbol `s2`.'), 'blood_ldl': ('s5', 'native SBML value', 'Blood LDL. Maps to SBML symbol `s5`.'), 'blood_hdl': ('s6', 'native SBML value', 'Blood HDL. Maps to SBML symbol `s6`.'), 'oxidized_ldl': ('s14', 'native SBML value', 'Oxidized LDL. Maps to SBML symbol `s14`.'), 'oxidized_hdl': ('s15', 'native SBML value', 'Oxidized HDL. Maps to SBML symbol `s15`.'), 'monocytes': ('s16', 'native SBML value', 'Monocytes. Maps to SBML symbol `s16`.'), 'macrophages': ('s19', 'native SBML value', 'Macrophages. Maps to SBML symbol `s19`.'), 'foam_cells': ('s21', 'native SBML value', 'Foam Cells. Maps to SBML symbol `s21`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/MODEL1812100001.xml", integration_step: float = 0.05) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
