# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule for Strasen2018 - TGFb SMAD Signalling - Dose dependent dynamics upon TGFb stimulation."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Strasen2018TgfbSmadSignallingDoseDependentBiomd0000000989Model(TelluriumSBMLBioModule):
    """Faithfully executes the bundled SBML source for Strasen2018 - TGFb SMAD Signalling - Dose dependent dynamics upon TGFb stimulation."""

    _SBML_ID = 'BIOMD0000000989'
    _TITLE = 'Strasen2018 - TGFb SMAD Signalling - Dose dependent dynamics upon TGFb stimulation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['TGFb_R1_surface', 'TGFb_R2_surface', 'TGFb_R1_endo', 'TGFb_R2_endo', 'TGFb', 'TGFb_In', 'Active_R2', 'Active_Rec']
    _SPECIES_LABELS = {'TGFb_R1_surface': 'Surface TGF Beta Receptor 1', 'TGFb_R2_surface': 'Surface TGF Beta Receptor 2', 'TGFb_R1_endo': 'Endosomal TGF Beta Receptor 1', 'TGFb_R2_endo': 'Endosomal TGF Beta Receptor 2', 'TGFb': 'TGF Beta Ligand', 'TGFb_In': 'Internalized TGF Beta', 'Active_R2': 'Active Receptor 2', 'Active_Rec': 'Active TGF Beta Receptor Complex'}
    _PARAMETER_INPUTS = {'tgfb_ligand_dose': ('TGFb_LIGAND_Dose', 25.0, 'native SBML value', 'TGF-beta ligand dose. Maps to SBML symbol `TGFb_LIGAND_Dose`.'), 'receptor_phosphorylation_rate': ('k_phosphorylation', 0.0701273900652988, 'native SBML rate', 'receptor/SMAD phosphorylation rate. Maps to SBML symbol `k_phosphorylation`.'), 'ligand_degradation_rate': ('kin_deg_Ligand', 0.720198437381795, 'native SBML rate', 'ligand degradation rate. Maps to SBML symbol `kin_deg_Ligand`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_surface_tgf_beta_receptor_1': ('TGFb_R1_surface', 16.1097160260841, 'native SBML value', 'initial surface receptor 1 pool. Maps to SBML symbol `TGFb_R1_surface`.'), 'initial_surface_tgf_beta_receptor_2': ('TGFb_R2_surface', 6.94111873244591, 'native SBML value', 'initial surface receptor 2 pool. Maps to SBML symbol `TGFb_R2_surface`.')}
    _HEADLINE_OUTPUTS = {'surface_tgf_beta_receptor_1': ('TGFb_R1_surface', 'native SBML value', 'Surface TGF Beta Receptor 1. Maps to SBML symbol `TGFb_R1_surface`.'), 'surface_tgf_beta_receptor_2': ('TGFb_R2_surface', 'native SBML value', 'Surface TGF Beta Receptor 2. Maps to SBML symbol `TGFb_R2_surface`.'), 'endosomal_tgf_beta_receptor_1': ('TGFb_R1_endo', 'native SBML value', 'Endosomal TGF Beta Receptor 1. Maps to SBML symbol `TGFb_R1_endo`.'), 'endosomal_tgf_beta_receptor_2': ('TGFb_R2_endo', 'native SBML value', 'Endosomal TGF Beta Receptor 2. Maps to SBML symbol `TGFb_R2_endo`.'), 'tgf_beta_ligand': ('TGFb', 'native SBML value', 'TGF Beta Ligand. Maps to SBML symbol `TGFb`.'), 'internalized_tgf_beta': ('TGFb_In', 'native SBML value', 'Internalized TGF Beta. Maps to SBML symbol `TGFb_In`.'), 'active_receptor_2': ('Active_R2', 'native SBML value', 'Active Receptor 2. Maps to SBML symbol `Active_R2`.'), 'active_tgf_beta_receptor_complex': ('Active_Rec', 'native SBML value', 'Active TGF Beta Receptor Complex. Maps to SBML symbol `Active_Rec`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/BIOMD0000000989.xml", integration_step: float = 0.2) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
