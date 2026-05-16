# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule for Koeller2021 - PBPK model of ICG liver function tests."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Koeller2021PbpkModelOfIcgLiverFunctionTesModel2301090001Model(TelluriumSBMLBioModule):
    """Faithfully executes the bundled SBML source for Koeller2021 - PBPK model of ICG liver function tests."""

    _SBML_ID = 'MODEL2301090001'
    _TITLE = 'Koeller2021 - PBPK model of ICG liver function tests'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Cli_plasma_icg', 'Cve_icg', 'Car_icg', 'Cgi_plasma_icg', 'Clu_plasma_icg', 'Cpo_icg', 'LI__icg']
    _SPECIES_LABELS = {'Cli_plasma_icg': 'ICG Liver Plasma', 'Cve_icg': 'ICG Venous Plasma', 'Car_icg': 'ICG Arterial Plasma', 'Cgi_plasma_icg': 'ICG Gastrointestinal Plasma', 'Clu_plasma_icg': 'ICG Lung Plasma', 'Cpo_icg': 'ICG Portal Vein', 'LI__icg': 'ICG Liver Amount'}
    _PARAMETER_INPUTS = {'icg_infusion_rate_mg_per_min': ('Ri_icg', 0.0, 'mg', 'ICG infusion rate. Maps to SBML symbol `Ri_icg`.'), 'icg_injection_time_seconds': ('ti_icg', 5.0, 's', 'injection duration. Maps to SBML symbol `ti_icg`.'), 'liver_shunt_fraction': ('f_shunts', 0.0, 'fraction', 'portal venous blood shunted by liver. Maps to SBML symbol `f_shunts`.'), 'liver_tissue_loss_fraction': ('f_tissue_loss', 0.0, 'fraction', 'lost parenchymal liver volume fraction. Maps to SBML symbol `f_tissue_loss`.'), 'hepatic_blood_flow_scale': ('f_bloodflow', 1.0, 'native SBML value', 'hepatic blood-flow scaling factor. Maps to SBML symbol `f_bloodflow`.'), 'oatp1b3_activity_scale': ('LI__f_oatp1b3', 1.0, 'native SBML value', 'hepatic uptake transporter activity scale. Maps to SBML symbol `LI__f_oatp1b3`.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'icg_liver_plasma': ('Cli_plasma_icg', 'native SBML value', 'ICG Liver Plasma. Maps to SBML symbol `Cli_plasma_icg`.'), 'icg_venous_plasma': ('Cve_icg', 'native SBML value', 'ICG Venous Plasma. Maps to SBML symbol `Cve_icg`.'), 'icg_arterial_plasma': ('Car_icg', 'native SBML value', 'ICG Arterial Plasma. Maps to SBML symbol `Car_icg`.'), 'icg_gastrointestinal_plasma': ('Cgi_plasma_icg', 'native SBML value', 'ICG Gastrointestinal Plasma. Maps to SBML symbol `Cgi_plasma_icg`.'), 'icg_lung_plasma': ('Clu_plasma_icg', 'native SBML value', 'ICG Lung Plasma. Maps to SBML symbol `Clu_plasma_icg`.'), 'icg_portal_vein': ('Cpo_icg', 'native SBML value', 'ICG Portal Vein. Maps to SBML symbol `Cpo_icg`.'), 'icg_liver_amount': ('LI__icg', 'native SBML amount', 'ICG Liver Amount. Maps to SBML symbol `LI__icg`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/MODEL2301090001.xml", integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
