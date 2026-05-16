# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule for Koschorreck2008_InsulinClearance."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Koschorreck2008InsulinclearanceBiomd0000000345Model(TelluriumSBMLBioModule):
    """Faithfully executes the bundled SBML source for Koschorreck2008_InsulinClearance."""

    _SBML_ID = 'BIOMD0000000345'
    _TITLE = 'Koschorreck2008_InsulinClearance'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['R', 'IR', 'I2R', 'Rp', 'IRp', 'Ren', 'IRen']
    _SPECIES_LABELS = {'R': 'Free Receptor', 'IR': 'Insulin Receptor Complex', 'I2R': 'Two Insulin Receptor Complex', 'Rp': 'Phosphorylated Receptor', 'IRp': 'Phosphorylated Insulin Receptor Complex', 'Ren': 'Endosomal Receptor', 'IRen': 'Endosomal Insulin Receptor Complex'}
    _PARAMETER_INPUTS = {'liver_insulin_clearance_density': ('rholiver', 1051.0, 'native SBML rate', 'liver clearance density parameter. Maps to SBML symbol `rholiver`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_free_receptor': ('R', 35.3837, 'native SBML value', 'initial free receptor state. Maps to SBML symbol `R`.'), 'initial_insulin_receptor_complex': ('IR', 0.0, 'native SBML value', 'initial insulin-receptor complex. Maps to SBML symbol `IR`.'), 'initial_internalized_receptor': ('Ren', 4.6163, 'native SBML value', 'initial endosomal receptor state. Maps to SBML symbol `Ren`.')}
    _HEADLINE_OUTPUTS = {'free_receptor': ('R', 'native SBML value', 'Free Receptor. Maps to SBML symbol `R`.'), 'insulin_receptor_complex': ('IR', 'native SBML value', 'Insulin Receptor Complex. Maps to SBML symbol `IR`.'), 'two_insulin_receptor_complex': ('I2R', 'native SBML value', 'Two Insulin Receptor Complex. Maps to SBML symbol `I2R`.'), 'phosphorylated_receptor': ('Rp', 'native SBML value', 'Phosphorylated Receptor. Maps to SBML symbol `Rp`.'), 'phosphorylated_insulin_receptor_complex': ('IRp', 'native SBML value', 'Phosphorylated Insulin Receptor Complex. Maps to SBML symbol `IRp`.'), 'endosomal_receptor': ('Ren', 'native SBML value', 'Endosomal Receptor. Maps to SBML symbol `Ren`.'), 'endosomal_insulin_receptor_complex': ('IRen', 'native SBML value', 'Endosomal Insulin Receptor Complex. Maps to SBML symbol `IRen`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/BIOMD0000000345.xml", integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
