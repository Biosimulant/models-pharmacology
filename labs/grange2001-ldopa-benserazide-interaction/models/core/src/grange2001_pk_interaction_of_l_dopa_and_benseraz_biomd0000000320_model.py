# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule for Grange2001 - PK interaction of L-dopa and benserazide."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Grange2001PkInteractionOfLDopaAndBenserazBiomd0000000320Model(TelluriumSBMLBioModule):
    """Faithfully executes the bundled SBML source for Grange2001 - PK interaction of L-dopa and benserazide."""

    _SBML_ID = 'BIOMD0000000320'
    _TITLE = 'Grange2001 - PK interaction of L-dopa and benserazide'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['A_dopa', 'C_dopa', 'A_B', 'A_M', 'C_OMD', 'C1_M', 'C1_B']
    _SPECIES_LABELS = {'A_dopa': 'L Dopa Amount', 'C_dopa': 'L Dopa Concentration', 'A_B': 'Benserazide Amount', 'A_M': 'Metabolite Amount', 'C_OMD': 'Three Omd Concentration', 'C1_M': 'Metabolite Compartment 1 Concentration', 'C1_B': 'Benserazide Compartment 1 Concentration'}
    _PARAMETER_INPUTS = {'l_dopa_dose_per_kg_rat': ('L_Dopa_per_kg_rat', 404.0, 'native SBML value', 'L-DOPA dose per kg rat. Maps to SBML symbol `L_Dopa_per_kg_rat`.'), 'benserazide_dose_per_kg_rat': ('Benserazide_per_kg_rat', 78.0, 'native SBML value', 'benserazide dose per kg rat. Maps to SBML symbol `Benserazide_per_kg_rat`.'), 'l_dopa_clearance_rate': ('CL_dopa0', 0.823, 'native SBML rate', 'baseline L-DOPA clearance rate. Maps to SBML symbol `CL_dopa0`.'), 'benserazide_clearance_rate': ('CL_B', 1.67, 'native SBML rate', 'benserazide clearance rate. Maps to SBML symbol `CL_B`.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'l_dopa_amount': ('A_dopa', 'native SBML amount', 'L Dopa Amount. Maps to SBML symbol `A_dopa`.'), 'l_dopa_concentration': ('C_dopa', 'native SBML concentration', 'L Dopa Concentration. Maps to SBML symbol `C_dopa`.'), 'benserazide_amount': ('A_B', 'native SBML amount', 'Benserazide Amount. Maps to SBML symbol `A_B`.'), 'metabolite_amount': ('A_M', 'native SBML amount', 'Metabolite Amount. Maps to SBML symbol `A_M`.'), 'three_omd_concentration': ('C_OMD', 'native SBML concentration', 'Three Omd Concentration. Maps to SBML symbol `C_OMD`.'), 'metabolite_compartment_1_concentration': ('C1_M', 'native SBML concentration', 'Metabolite Compartment 1 Concentration. Maps to SBML symbol `C1_M`.'), 'benserazide_compartment_1_concentration': ('C1_B', 'native SBML concentration', 'Benserazide Compartment 1 Concentration. Maps to SBML symbol `C1_B`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/BIOMD0000000320.xml", integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
