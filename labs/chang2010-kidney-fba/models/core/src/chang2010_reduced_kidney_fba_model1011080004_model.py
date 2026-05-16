# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule for Chang2010_Reduced_Kidney_FBA."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Chang2010ReducedKidneyFbaModel1011080004Model(TelluriumSBMLBioModule):
    """Faithfully executes the bundled SBML source for Chang2010_Reduced_Kidney_FBA."""

    _SBML_ID = 'MODEL1011080004'
    _TITLE = 'Chang2010_Reduced_Kidney_FBA'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['M_atp_c', 'M_atp_m', 'M_glc_DASH_D_c', 'M_glc_DASH_D_e', 'M_lac_DASH_L_c', 'M_lac_DASH_L_e', 'M_urea_c']
    _SPECIES_LABELS = {'M_atp_c': 'Cytosolic ATP', 'M_atp_m': 'Mitochondrial ATP', 'M_glc_DASH_D_c': 'Cytosolic Glucose', 'M_glc_DASH_D_e': 'Extracellular Glucose', 'M_lac_DASH_L_c': 'Cytosolic Lactate', 'M_lac_DASH_L_e': 'Extracellular Lactate', 'M_urea_c': 'Cytosolic Urea'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_cytosolic_atp': ('M_atp_c', 0.0, 'native SBML value', 'initial cytosolic ATP pool. Maps to SBML symbol `M_atp_c`.'), 'initial_mitochondrial_atp': ('M_atp_m', 0.0, 'native SBML value', 'initial mitochondrial ATP pool. Maps to SBML symbol `M_atp_m`.'), 'initial_extracellular_glucose': ('M_glc_DASH_D_e', 0.0, 'native SBML value', 'initial extracellular D-glucose pool. Maps to SBML symbol `M_glc_DASH_D_e`.'), 'initial_cytosolic_lactate': ('M_lac_DASH_L_c', 0.0, 'native SBML value', 'initial cytosolic L-lactate pool. Maps to SBML symbol `M_lac_DASH_L_c`.')}
    _HEADLINE_OUTPUTS = {'cytosolic_atp': ('M_atp_c', 'native SBML value', 'Cytosolic ATP. Maps to SBML symbol `M_atp_c`.'), 'mitochondrial_atp': ('M_atp_m', 'native SBML value', 'Mitochondrial ATP. Maps to SBML symbol `M_atp_m`.'), 'cytosolic_glucose': ('M_glc_DASH_D_c', 'native SBML value', 'Cytosolic Glucose. Maps to SBML symbol `M_glc_DASH_D_c`.'), 'extracellular_glucose': ('M_glc_DASH_D_e', 'native SBML value', 'Extracellular Glucose. Maps to SBML symbol `M_glc_DASH_D_e`.'), 'cytosolic_lactate': ('M_lac_DASH_L_c', 'native SBML value', 'Cytosolic Lactate. Maps to SBML symbol `M_lac_DASH_L_c`.'), 'extracellular_lactate': ('M_lac_DASH_L_e', 'native SBML value', 'Extracellular Lactate. Maps to SBML symbol `M_lac_DASH_L_e`.'), 'cytosolic_urea': ('M_urea_c', 'native SBML value', 'Cytosolic Urea. Maps to SBML symbol `M_urea_c`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/MODEL1011080004.xml", integration_step: float = 0.05) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
