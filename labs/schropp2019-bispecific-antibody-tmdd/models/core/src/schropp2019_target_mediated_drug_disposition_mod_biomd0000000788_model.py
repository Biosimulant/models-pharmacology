# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule for Schropp2019 - Target-Mediated Drug Disposition Model for Bispecific Antibodies."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Schropp2019TargetMediatedDrugDispositionModBiomd0000000788Model(TelluriumSBMLBioModule):
    """Faithfully executes the bundled SBML source for Schropp2019 - Target-Mediated Drug Disposition Model for Bispecific Antibodies."""

    _SBML_ID = 'BIOMD0000000788'
    _TITLE = 'Schropp2019 - Target-Mediated Drug Disposition Model for Bispecific Antibodies'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['C_free', 'R_A', 'R_B', 'RC_A', 'RC_B', 'RC_AB', 'AP', 'AD']
    _SPECIES_LABELS = {'C_free': 'Free Bispecific Antibody', 'R_A': 'Free Target A', 'R_B': 'Free Target B', 'RC_A': 'Antibody Target A Complex', 'RC_B': 'Antibody Target B Complex', 'RC_AB': 'Bispecific Bridge Complex', 'AP': 'Peripheral Antibody', 'AD': 'Depot Antibody'}
    _PARAMETER_INPUTS = {'target_a_association_rate': ('k_on_1', 10.0, 'native SBML rate', 'antibody-target A association rate. Maps to SBML symbol `k_on_1`.'), 'target_b_association_rate': ('k_on_2', 1.0, 'native SBML rate', 'antibody-target B association rate. Maps to SBML symbol `k_on_2`.'), 'central_elimination_rate': ('k_el', 0.1, 'native SBML rate', 'central antibody elimination rate. Maps to SBML symbol `k_el`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_free_bispecific_antibody': ('C_free', 50.0, 'native SBML value', 'initial free antibody concentration. Maps to SBML symbol `C_free`.'), 'initial_target_a_concentration': ('R_A', 10.0, 'native SBML concentration', 'initial target A concentration. Maps to SBML symbol `R_A`.'), 'initial_target_b_concentration': ('R_B', 100.0, 'native SBML concentration', 'initial target B concentration. Maps to SBML symbol `R_B`.')}
    _HEADLINE_OUTPUTS = {'free_bispecific_antibody': ('C_free', 'native SBML value', 'Free Bispecific Antibody. Maps to SBML symbol `C_free`.'), 'free_target_a': ('R_A', 'native SBML value', 'Free Target A. Maps to SBML symbol `R_A`.'), 'free_target_b': ('R_B', 'native SBML value', 'Free Target B. Maps to SBML symbol `R_B`.'), 'antibody_target_a_complex': ('RC_A', 'native SBML value', 'Antibody Target A Complex. Maps to SBML symbol `RC_A`.'), 'antibody_target_b_complex': ('RC_B', 'native SBML value', 'Antibody Target B Complex. Maps to SBML symbol `RC_B`.'), 'bispecific_bridge_complex': ('RC_AB', 'native SBML value', 'Bispecific Bridge Complex. Maps to SBML symbol `RC_AB`.'), 'peripheral_antibody': ('AP', 'native SBML value', 'Peripheral Antibody. Maps to SBML symbol `AP`.'), 'depot_antibody': ('AD', 'native SBML value', 'Depot Antibody. Maps to SBML symbol `AD`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/BIOMD0000000788.xml", integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
