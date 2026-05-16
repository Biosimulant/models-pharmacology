# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule for Sluka2016 - Acetaminophen PBPK."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Sluka2016AcetaminophenPbpkBiomd0000000619Model(TelluriumSBMLBioModule):
    """Faithfully executes the bundled SBML source for Sluka2016 - Acetaminophen PBPK."""

    _SBML_ID = 'BIOMD0000000619'
    _TITLE = 'Sluka2016 - Acetaminophen PBPK'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['CLiver', 'CArt', 'CGut', 'AGutlumen', 'CLung', 'CVen', 'CRest', 'CMetabolized']
    _SPECIES_LABELS = {'CLiver': 'Liver Acetaminophen Concentration', 'CArt': 'Arterial Acetaminophen Concentration', 'CGut': 'Gut Acetaminophen Concentration', 'AGutlumen': 'Gut Lumen Acetaminophen Amount', 'CLung': 'Lung Acetaminophen Concentration', 'CVen': 'Venous Acetaminophen Concentration', 'CRest': 'Rest Body Acetaminophen Concentration', 'CMetabolized': 'Metabolized Acetaminophen Concentration'}
    _PARAMETER_INPUTS = {'acetaminophen_dose_grams': ('APAP_Dose_grams', 1.4, 'g', 'acetaminophen dose in grams. Maps to SBML symbol `APAP_Dose_grams`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_gut_lumen_acetaminophen': ('AGutlumen', 0.0093, 'native SBML value', 'initial gut-lumen amount. Maps to SBML symbol `AGutlumen`.'), 'initial_liver_acetaminophen_concentration': ('CLiver', 0.0, 'native SBML concentration', 'initial liver concentration. Maps to SBML symbol `CLiver`.'), 'initial_metabolized_acetaminophen': ('CMetabolized', 0.0, 'native SBML value', 'initial metabolized pool. Maps to SBML symbol `CMetabolized`.')}
    _HEADLINE_OUTPUTS = {'liver_acetaminophen_concentration': ('CLiver', 'native SBML concentration', 'Liver Acetaminophen Concentration. Maps to SBML symbol `CLiver`.'), 'arterial_acetaminophen_concentration': ('CArt', 'native SBML concentration', 'Arterial Acetaminophen Concentration. Maps to SBML symbol `CArt`.'), 'gut_acetaminophen_concentration': ('CGut', 'native SBML concentration', 'Gut Acetaminophen Concentration. Maps to SBML symbol `CGut`.'), 'gut_lumen_acetaminophen_amount': ('AGutlumen', 'native SBML amount', 'Gut Lumen Acetaminophen Amount. Maps to SBML symbol `AGutlumen`.'), 'lung_acetaminophen_concentration': ('CLung', 'native SBML concentration', 'Lung Acetaminophen Concentration. Maps to SBML symbol `CLung`.'), 'venous_acetaminophen_concentration': ('CVen', 'native SBML concentration', 'Venous Acetaminophen Concentration. Maps to SBML symbol `CVen`.'), 'rest_body_acetaminophen_concentration': ('CRest', 'native SBML concentration', 'Rest Body Acetaminophen Concentration. Maps to SBML symbol `CRest`.'), 'metabolized_acetaminophen_concentration': ('CMetabolized', 'native SBML concentration', 'Metabolized Acetaminophen Concentration. Maps to SBML symbol `CMetabolized`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/BIOMD0000000619.xml", integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
