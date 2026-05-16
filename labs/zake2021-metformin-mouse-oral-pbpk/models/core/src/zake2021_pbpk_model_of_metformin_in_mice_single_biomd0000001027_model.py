# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule for Zake2021 - PBPK model of metformin in mice: single dose peroral."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Zake2021PbpkModelOfMetforminInMiceSingleBiomd0000001027Model(TelluriumSBMLBioModule):
    """Faithfully executes the bundled SBML source for Zake2021 - PBPK model of metformin in mice: single dose peroral."""

    _SBML_ID = 'BIOMD0000001027'
    _TITLE = 'Zake2021 - PBPK model of metformin in mice: single dose peroral'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['mKidneyPlasma', 'mLiver', 'mPlasmaVenous', 'mPlasmaArterial', 'mKidneyTissue', 'mKidneyTubular']
    _SPECIES_LABELS = {'mKidneyPlasma': 'Kidney Plasma Metformin', 'mLiver': 'Liver Metformin', 'mPlasmaVenous': 'Venous Plasma Metformin', 'mPlasmaArterial': 'Arterial Plasma Metformin', 'mKidneyTissue': 'Kidney Tissue Metformin', 'mKidneyTubular': 'Kidney Tubular Metformin'}
    _PARAMETER_INPUTS = {'metformin_lumen_dose_mg': ('Metformin_Dose_in_Lumen_in_mg', 1.375, 'mg', 'oral/lumen metformin dose. Maps to SBML symbol `Metformin_Dose_in_Lumen_in_mg`.'), 'metformin_plasma_dose_mg': ('Metformin_Dose_in_Plasma_in_mg', 0.0, 'mg', 'plasma dose parameter, normally zero for oral scenario. Maps to SBML symbol `Metformin_Dose_in_Plasma_in_mg`.'), 'body_weight_g': ('ModelValue_1', 27.5, 'native SBML value', 'mouse body weight. Maps to SBML symbol `ModelValue_1`.'), 'cardiac_output_ml_per_min': ('ModelValue_3', 838.8, 'mg/min', 'cardiac output. Maps to SBML symbol `ModelValue_3`.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'kidney_plasma_metformin': ('mKidneyPlasma', 'native SBML value', 'Kidney Plasma Metformin. Maps to SBML symbol `mKidneyPlasma`.'), 'liver_metformin': ('mLiver', 'native SBML value', 'Liver Metformin. Maps to SBML symbol `mLiver`.'), 'venous_plasma_metformin': ('mPlasmaVenous', 'native SBML value', 'Venous Plasma Metformin. Maps to SBML symbol `mPlasmaVenous`.'), 'arterial_plasma_metformin': ('mPlasmaArterial', 'native SBML value', 'Arterial Plasma Metformin. Maps to SBML symbol `mPlasmaArterial`.'), 'kidney_tissue_metformin': ('mKidneyTissue', 'native SBML value', 'Kidney Tissue Metformin. Maps to SBML symbol `mKidneyTissue`.'), 'kidney_tubular_metformin': ('mKidneyTubular', 'native SBML value', 'Kidney Tubular Metformin. Maps to SBML symbol `mKidneyTubular`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/BIOMD0000001027.xml", integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
