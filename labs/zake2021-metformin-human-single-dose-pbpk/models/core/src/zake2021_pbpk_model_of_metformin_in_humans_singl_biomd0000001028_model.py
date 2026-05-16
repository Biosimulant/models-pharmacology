# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule for Zake2021 - PBPK model of metformin in humans, single PO dose."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Zake2021PbpkModelOfMetforminInHumansSinglBiomd0000001028Model(TelluriumSBMLBioModule):
    """Faithfully executes the bundled SBML source for Zake2021 - PBPK model of metformin in humans, single PO dose."""

    _SBML_ID = 'BIOMD0000001028'
    _TITLE = 'Zake2021 - PBPK model of metformin in humans, single PO dose'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['mKidneyPlasma', 'mLiver', 'mPlasmaVenous', 'mPlasmaArterial', 'mKidneyTissue', 'mKidneyTubular']
    _SPECIES_LABELS = {'mKidneyPlasma': 'Kidney Plasma Metformin', 'mLiver': 'Liver Metformin', 'mPlasmaVenous': 'Venous Plasma Metformin', 'mPlasmaArterial': 'Arterial Plasma Metformin', 'mKidneyTissue': 'Kidney Tissue Metformin', 'mKidneyTubular': 'Kidney Tubular Metformin'}
    _PARAMETER_INPUTS = {'metformin_lumen_dose_mg': ('Metformin_Dose_in_Lumen_in_mg', 389.92, 'mg', 'oral/lumen metformin dose. Maps to SBML symbol `Metformin_Dose_in_Lumen_in_mg`.'), 'body_weight_g': ('ModelValue_1', 70000.0, 'native SBML value', 'body weight initial value. Maps to SBML symbol `ModelValue_1`.'), 'cardiac_output_ml_per_min': ('ModelValue_2', 312000.0, 'mg/min', 'cardiac output initial value. Maps to SBML symbol `ModelValue_2`.'), 'kidney_partition_coefficient': ('ModelValue_56', 320.0, 'native SBML value', 'kidney coefficient. Maps to SBML symbol `ModelValue_56`.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'kidney_plasma_metformin': ('mKidneyPlasma', 'native SBML value', 'Kidney Plasma Metformin. Maps to SBML symbol `mKidneyPlasma`.'), 'liver_metformin': ('mLiver', 'native SBML value', 'Liver Metformin. Maps to SBML symbol `mLiver`.'), 'venous_plasma_metformin': ('mPlasmaVenous', 'native SBML value', 'Venous Plasma Metformin. Maps to SBML symbol `mPlasmaVenous`.'), 'arterial_plasma_metformin': ('mPlasmaArterial', 'native SBML value', 'Arterial Plasma Metformin. Maps to SBML symbol `mPlasmaArterial`.'), 'kidney_tissue_metformin': ('mKidneyTissue', 'native SBML value', 'Kidney Tissue Metformin. Maps to SBML symbol `mKidneyTissue`.'), 'kidney_tubular_metformin': ('mKidneyTubular', 'native SBML value', 'Kidney Tubular Metformin. Maps to SBML symbol `mKidneyTubular`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/BIOMD0000001028.xml", integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
