# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule for Grzegorzewski2022 - PBPK model of dextromethorphan."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Grzegorzewski2022PbpkModelOfDextromethorphanModel2301090002Model(TelluriumSBMLBioModule):
    """Faithfully executes the bundled SBML source for Grzegorzewski2022 - PBPK model of dextromethorphan."""

    _SBML_ID = 'MODEL2301090002'
    _TITLE = 'Grzegorzewski2022 - PBPK model of dextromethorphan'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Cli_plasma_dxm', 'Cgu_plasma_dxm', 'Cki_plasma_dxm', 'Clu_plasma_dxm', 'Cli_plasma_dxo', 'Cli_plasma_dxo_glu']
    _SPECIES_LABELS = {'Cli_plasma_dxm': 'Dextromethorphan Liver Plasma', 'Cgu_plasma_dxm': 'Dextromethorphan Gut Plasma', 'Cki_plasma_dxm': 'Dextromethorphan Kidney Plasma', 'Clu_plasma_dxm': 'Dextromethorphan Lung Plasma', 'Cli_plasma_dxo': 'Dextorphan Liver Plasma', 'Cli_plasma_dxo_glu': 'Dextorphan Glucuronide Liver Plasma'}
    _PARAMETER_INPUTS = {'oral_dextromethorphan_dose_mg': ('PODOSE_dxm', 0.0, 'mg', 'oral dextromethorphan dose. Maps to SBML symbol `PODOSE_dxm`.'), 'iv_dextromethorphan_bolus_mg': ('IVDOSE_dxm', 0.0, 'mg', 'IV dextromethorphan bolus dose. Maps to SBML symbol `IVDOSE_dxm`.'), 'dextromethorphan_infusion_rate_mg_per_min': ('Ri_dxm', 0.0, 'mg', 'infusion rate. Maps to SBML symbol `Ri_dxm`.'), 'cyp2d6_custom_activity': ('LI__cyp2d6_ac', 1.0, 'native SBML value', 'custom CYP2D6 activity. Maps to SBML symbol `LI__cyp2d6_ac`.'), 'cyp2d6_vmax': ('LI__DXMCYP2D6_Vmax', 0.003, 'native SBML rate', 'CYP2D6 Vmax for DXM metabolism. Maps to SBML symbol `LI__DXMCYP2D6_Vmax`.'), 'cyp3a4_vmax': ('LI__DXMCYP3A4_Vmax', 0.0004, 'native SBML rate', 'minor CYP3A4 pathway Vmax. Maps to SBML symbol `LI__DXMCYP3A4_Vmax`.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'dextromethorphan_liver_plasma': ('Cli_plasma_dxm', 'native SBML value', 'Dextromethorphan Liver Plasma. Maps to SBML symbol `Cli_plasma_dxm`.'), 'dextromethorphan_gut_plasma': ('Cgu_plasma_dxm', 'native SBML value', 'Dextromethorphan Gut Plasma. Maps to SBML symbol `Cgu_plasma_dxm`.'), 'dextromethorphan_kidney_plasma': ('Cki_plasma_dxm', 'native SBML value', 'Dextromethorphan Kidney Plasma. Maps to SBML symbol `Cki_plasma_dxm`.'), 'dextromethorphan_lung_plasma': ('Clu_plasma_dxm', 'native SBML value', 'Dextromethorphan Lung Plasma. Maps to SBML symbol `Clu_plasma_dxm`.'), 'dextorphan_liver_plasma': ('Cli_plasma_dxo', 'native SBML value', 'Dextorphan Liver Plasma. Maps to SBML symbol `Cli_plasma_dxo`.'), 'dextorphan_glucuronide_liver_plasma': ('Cli_plasma_dxo_glu', 'native SBML value', 'Dextorphan Glucuronide Liver Plasma. Maps to SBML symbol `Cli_plasma_dxo_glu`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/MODEL2301090002.xml", integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
