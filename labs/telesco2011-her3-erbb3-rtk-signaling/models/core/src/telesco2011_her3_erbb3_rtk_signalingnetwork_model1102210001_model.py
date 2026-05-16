# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule for Telesco2011_HER3-ErbB3-RTK_SignalingNetwork."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Telesco2011Her3Erbb3RtkSignalingnetworkModel1102210001Model(TelluriumSBMLBioModule):
    """Faithfully executes the bundled SBML source for Telesco2011_HER3-ErbB3-RTK_SignalingNetwork."""

    _SBML_ID = 'MODEL1102210001'
    _TITLE = 'Telesco2011_HER3-ErbB3-RTK_SignalingNetwork'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['pHer3_2_Nrg_Pi3k', 'pHer3_1_Nrg_Pi3k', 'pHer3_2_Nrg_Pi3k_Pip2', 'ipHer3_2_Nrg_Pi3k', 'ipHer3_2_Nrg_Pi3k_Pip2']
    _SPECIES_LABELS = {'pHer3_2_Nrg_Pi3k': 'Phosphorylated HER3 Neuregulin PI3K Complex', 'pHer3_1_Nrg_Pi3k': 'Phosphorylated HER3 1 Neuregulin PI3K Complex', 'pHer3_2_Nrg_Pi3k_Pip2': 'Phosphorylated HER3 Neuregulin PI3K PIP2 Complex', 'ipHer3_2_Nrg_Pi3k': 'Internalized Phosphorylated HER3 Neuregulin PI3K Complex', 'ipHer3_2_Nrg_Pi3k_Pip2': 'Internalized Phosphorylated HER3 Neuregulin PI3K PIP2 Complex'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_total_her3_receptor': ('Her3', 33000.0, 'native SBML value', 'initial HER3 receptor pool. Maps to SBML symbol `Her3`.'), 'initial_her3_neuregulin_complex': ('Her3_Nrg', 0.0, 'native SBML value', 'initial HER3-neuregulin complex. Maps to SBML symbol `Her3_Nrg`.'), 'initial_phosphorylated_her3_neuregulin_pi3k_complex': ('pHer3_2_Nrg_Pi3k', 0.0, 'native SBML value', 'initial phosphorylated HER3-neuregulin-PI3K complex. Maps to SBML symbol `pHer3_2_Nrg_Pi3k`.'), 'initial_internalized_phosphorylated_her3_pi3k_complex': ('ipHer3_2_Nrg_Pi3k', 0.0, 'native SBML value', 'initial internalized phosphorylated complex. Maps to SBML symbol `ipHer3_2_Nrg_Pi3k`.')}
    _HEADLINE_OUTPUTS = {'phosphorylated_her3_neuregulin_pi3k_complex': ('pHer3_2_Nrg_Pi3k', 'native SBML value', 'Phosphorylated HER3 Neuregulin PI3K Complex. Maps to SBML symbol `pHer3_2_Nrg_Pi3k`.'), 'phosphorylated_her3_1_neuregulin_pi3k_complex': ('pHer3_1_Nrg_Pi3k', 'native SBML value', 'Phosphorylated HER3 1 Neuregulin PI3K Complex. Maps to SBML symbol `pHer3_1_Nrg_Pi3k`.'), 'phosphorylated_her3_neuregulin_pi3k_pip2_complex': ('pHer3_2_Nrg_Pi3k_Pip2', 'native SBML value', 'Phosphorylated HER3 Neuregulin PI3K PIP2 Complex. Maps to SBML symbol `pHer3_2_Nrg_Pi3k_Pip2`.'), 'internalized_phosphorylated_her3_neuregulin_pi3k_complex': ('ipHer3_2_Nrg_Pi3k', 'native SBML value', 'Internalized Phosphorylated HER3 Neuregulin PI3K Complex. Maps to SBML symbol `ipHer3_2_Nrg_Pi3k`.'), 'internalized_phosphorylated_her3_neuregulin_pi3k_pip2_complex': ('ipHer3_2_Nrg_Pi3k_Pip2', 'native SBML value', 'Internalized Phosphorylated HER3 Neuregulin PI3K PIP2 Complex. Maps to SBML symbol `ipHer3_2_Nrg_Pi3k_Pip2`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/MODEL1102210001.xml", integration_step: float = 0.2) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
