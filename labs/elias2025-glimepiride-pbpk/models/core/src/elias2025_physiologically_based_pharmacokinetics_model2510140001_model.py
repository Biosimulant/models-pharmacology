# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule for Elias2025 - Physiologically based pharmacokinetics (PBPK) model glimepiride."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Elias2025PhysiologicallyBasedPharmacokineticsModel2510140001Model(TelluriumSBMLBioModule):
    """Faithfully executes the bundled SBML source for Elias2025 - Physiologically based pharmacokinetics (PBPK) model glimepiride."""

    _SBML_ID = 'MODEL2510140001'
    _TITLE = 'Elias2025 - Physiologically based pharmacokinetics (PBPK) model glimepiride'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Cli_plasma_gli', 'Car_gli', 'Cve_gli', 'Cki_plasma_gli', 'Cgu_plasma_gli', 'Cli_plasma_m1', 'Car_m1', 'Cve_m1']
    _SPECIES_LABELS = {'Cli_plasma_gli': 'Glimepiride Liver Plasma', 'Car_gli': 'Glimepiride Arterial Plasma', 'Cve_gli': 'Glimepiride Venous Plasma', 'Cki_plasma_gli': 'Glimepiride Kidney Plasma', 'Cgu_plasma_gli': 'Glimepiride Gut Plasma', 'Cli_plasma_m1': 'M1 Liver Plasma', 'Car_m1': 'M1 Arterial Plasma', 'Cve_m1': 'M1 Venous Plasma'}
    _PARAMETER_INPUTS = {'oral_glimepiride_dose_mg': ('PODOSE_gli', 0.0, 'mg', 'oral glimepiride dose. Maps to SBML symbol `PODOSE_gli`.'), 'iv_glimepiride_bolus_mg': ('IVDOSE_gli', 0.0, 'mg', 'IV glimepiride bolus dose. Maps to SBML symbol `IVDOSE_gli`.'), 'glimepiride_infusion_rate_mg_per_min': ('Ri_gli', 0.0, 'mg', 'glimepiride infusion rate. Maps to SBML symbol `Ri_gli`.'), 'cyp2c9_activity_scale': ('LI__f_cyp2c9', 1.0, 'native SBML value', 'CYP2C9 activity scaling factor. Maps to SBML symbol `LI__f_cyp2c9`.'), 'intestinal_absorption_scale': ('GU__f_absorption', 1.0, 'native SBML value', 'gut absorption-rate scaling factor. Maps to SBML symbol `GU__f_absorption`.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'glimepiride_liver_plasma': ('Cli_plasma_gli', 'native SBML value', 'Glimepiride Liver Plasma. Maps to SBML symbol `Cli_plasma_gli`.'), 'glimepiride_arterial_plasma': ('Car_gli', 'native SBML value', 'Glimepiride Arterial Plasma. Maps to SBML symbol `Car_gli`.'), 'glimepiride_venous_plasma': ('Cve_gli', 'native SBML value', 'Glimepiride Venous Plasma. Maps to SBML symbol `Cve_gli`.'), 'glimepiride_kidney_plasma': ('Cki_plasma_gli', 'native SBML value', 'Glimepiride Kidney Plasma. Maps to SBML symbol `Cki_plasma_gli`.'), 'glimepiride_gut_plasma': ('Cgu_plasma_gli', 'native SBML value', 'Glimepiride Gut Plasma. Maps to SBML symbol `Cgu_plasma_gli`.'), 'm1_liver_plasma': ('Cli_plasma_m1', 'native SBML value', 'M1 Liver Plasma. Maps to SBML symbol `Cli_plasma_m1`.'), 'm1_arterial_plasma': ('Car_m1', 'native SBML value', 'M1 Arterial Plasma. Maps to SBML symbol `Car_m1`.'), 'm1_venous_plasma': ('Cve_m1', 'native SBML value', 'M1 Venous Plasma. Maps to SBML symbol `Cve_m1`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/MODEL2510140001.xml", integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
