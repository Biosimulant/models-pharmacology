# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule for Grange2001 - L Dopa PK model."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Grange2001LDopaPkModelBiomd0000000321Model(TelluriumSBMLBioModule):
    """Faithfully executes the bundled SBML source for Grange2001 - L Dopa PK model."""

    _SBML_ID = 'BIOMD0000000321'
    _TITLE = 'Grange2001 - L Dopa PK model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['A_dopa', 'C_dopa', 'C_OMD']
    _SPECIES_LABELS = {'A_dopa': 'L Dopa Amount', 'C_dopa': 'L Dopa Concentration', 'C_OMD': 'Three Omd Concentration'}
    _PARAMETER_INPUTS = {'l_dopa_dose_per_kg_rat': ('L_Dopa_per_kg_rat', 404.0, 'native SBML value', 'L-DOPA dose per kg rat. Maps to SBML symbol `L_Dopa_per_kg_rat`.'), 'l_dopa_clearance_rate': ('CL_dopa0', 0.823, 'native SBML rate', 'baseline L-DOPA clearance rate. Maps to SBML symbol `CL_dopa0`.'), 'omd_clearance_rate': ('CL_OMD', 0.012, 'native SBML rate', '3-OMD clearance rate. Maps to SBML symbol `CL_OMD`.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'l_dopa_amount': ('A_dopa', 'native SBML amount', 'L Dopa Amount. Maps to SBML symbol `A_dopa`.'), 'l_dopa_concentration': ('C_dopa', 'native SBML concentration', 'L Dopa Concentration. Maps to SBML symbol `C_dopa`.'), 'three_omd_concentration': ('C_OMD', 'native SBML concentration', 'Three Omd Concentration. Maps to SBML symbol `C_OMD`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/BIOMD0000000321.xml", integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
