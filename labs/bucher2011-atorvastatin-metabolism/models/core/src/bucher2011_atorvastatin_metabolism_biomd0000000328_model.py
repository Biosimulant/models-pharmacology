# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule for Bucher2011_Atorvastatin_Metabolism."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bucher2011AtorvastatinMetabolismBiomd0000000328Model(TelluriumSBMLBioModule):
    """Faithfully executes the bundled SBML source for Bucher2011_Atorvastatin_Metabolism."""

    _SBML_ID = 'BIOMD0000000328'
    _TITLE = 'Bucher2011_Atorvastatin_Metabolism'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['AS_m', 'ASL_m', 'ASpOH_m', 'ASoOH_m', 'AS_c', 'ASL_c']
    _SPECIES_LABELS = {'AS_m': 'Mitochondrial Atorvastatin Acid', 'ASL_m': 'Mitochondrial Atorvastatin Lactone', 'ASpOH_m': 'Mitochondrial Para Hydroxy Atorvastatin', 'ASoOH_m': 'Mitochondrial Ortho Hydroxy Atorvastatin', 'AS_c': 'Cytosolic Atorvastatin Acid', 'ASL_c': 'Cytosolic Atorvastatin Lactone'}
    _PARAMETER_INPUTS = {'cyp3a4_para_hydroxylation_capacity': ('CYP3A4_ASpOH_Vmax', 15.7336, 'native SBML rate', 'CYP3A4 capacity for para-hydroxy atorvastatin formation. Maps to SBML symbol `CYP3A4_ASpOH_Vmax`.'), 'cyp3a4_ortho_hydroxylation_capacity': ('CYP3A4_ASoOH_Vmax', 47.4985, 'native SBML rate', 'CYP3A4 capacity for ortho-hydroxy atorvastatin formation. Maps to SBML symbol `CYP3A4_ASoOH_Vmax`.'), 'ugt1a3_lactonization_capacity': ('UGT1A3_AS_Vmax', 13.5862, 'native SBML rate', 'UGT1A3 capacity for atorvastatin lactonization. Maps to SBML symbol `UGT1A3_AS_Vmax`.'), 'pon_lactone_hydrolysis_rate': ('k_PON_ASL_c', 0.0043734, 'native SBML rate', 'cytosolic PON-mediated atorvastatin lactone hydrolysis rate. Maps to SBML symbol `k_PON_ASL_c`.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'mitochondrial_atorvastatin_acid': ('AS_m', 'native SBML value', 'Mitochondrial Atorvastatin Acid. Maps to SBML symbol `AS_m`.'), 'mitochondrial_atorvastatin_lactone': ('ASL_m', 'native SBML value', 'Mitochondrial Atorvastatin Lactone. Maps to SBML symbol `ASL_m`.'), 'mitochondrial_para_hydroxy_atorvastatin': ('ASpOH_m', 'native SBML value', 'Mitochondrial Para Hydroxy Atorvastatin. Maps to SBML symbol `ASpOH_m`.'), 'mitochondrial_ortho_hydroxy_atorvastatin': ('ASoOH_m', 'native SBML value', 'Mitochondrial Ortho Hydroxy Atorvastatin. Maps to SBML symbol `ASoOH_m`.'), 'cytosolic_atorvastatin_acid': ('AS_c', 'native SBML value', 'Cytosolic Atorvastatin Acid. Maps to SBML symbol `AS_c`.'), 'cytosolic_atorvastatin_lactone': ('ASL_c', 'native SBML value', 'Cytosolic Atorvastatin Lactone. Maps to SBML symbol `ASL_c`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/BIOMD0000000328.xml", integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
