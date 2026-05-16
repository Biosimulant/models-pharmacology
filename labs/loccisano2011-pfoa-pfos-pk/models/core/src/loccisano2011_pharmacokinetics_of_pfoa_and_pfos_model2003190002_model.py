# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule for Loccisano2011-pharmacokinetics of PFOA and PFOS in the monkey."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Loccisano2011PharmacokineticsOfPfoaAndPfosModel2003190002Model(TelluriumSBMLBioModule):
    """Faithfully executes the bundled SBML source for Loccisano2011-pharmacokinetics of PFOA and PFOS in the monkey."""

    _SBML_ID = 'MODEL2003190002'
    _TITLE = 'Loccisano2011-pharmacokinetics of PFOA and PFOS in the monkey'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Plasma_0', 'Liver_0', 'Kidney_0', 'Gut_0', 'Fat_0', 'Skin_0', 'Urine', 'FIltrate']
    _SPECIES_LABELS = {'Plasma_0': 'Plasma Toxicant Burden', 'Liver_0': 'Liver Toxicant Burden', 'Kidney_0': 'Kidney Toxicant Burden', 'Gut_0': 'Gut Toxicant Burden', 'Fat_0': 'Fat Toxicant Burden', 'Skin_0': 'Skin Toxicant Burden', 'Urine': 'Urine Toxicant Burden', 'FIltrate': 'Filtrate Toxicant Burden'}
    _PARAMETER_INPUTS = {'oral_toxicant_input': ('input', 10.0, 'native SBML value', 'oral input amount/rate as defined by source. Maps to SBML symbol `input`.'), 'iv_toxicant_input': ('inputIV', 10.0, 'native SBML value', 'IV input amount/rate as defined by source. Maps to SBML symbol `inputIV`.'), 'urinary_elimination_rate': ('kurinec', 50.0, 'native SBML rate', 'urinary elimination parameter. Maps to SBML symbol `kurinec`.'), 'free_fraction': ('Free', 0.02, 'fraction', 'free toxicant fraction. Maps to SBML symbol `Free`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_plasma_toxicant_burden': ('Plasma_0', 448.0, 'native SBML amount', 'initial plasma burden. Maps to SBML symbol `Plasma_0`.')}
    _HEADLINE_OUTPUTS = {'plasma_toxicant_burden': ('Plasma_0', 'native SBML amount', 'Plasma Toxicant Burden. Maps to SBML symbol `Plasma_0`.'), 'liver_toxicant_burden': ('Liver_0', 'native SBML amount', 'Liver Toxicant Burden. Maps to SBML symbol `Liver_0`.'), 'kidney_toxicant_burden': ('Kidney_0', 'native SBML amount', 'Kidney Toxicant Burden. Maps to SBML symbol `Kidney_0`.'), 'gut_toxicant_burden': ('Gut_0', 'native SBML amount', 'Gut Toxicant Burden. Maps to SBML symbol `Gut_0`.'), 'fat_toxicant_burden': ('Fat_0', 'native SBML amount', 'Fat Toxicant Burden. Maps to SBML symbol `Fat_0`.'), 'skin_toxicant_burden': ('Skin_0', 'native SBML amount', 'Skin Toxicant Burden. Maps to SBML symbol `Skin_0`.'), 'urine_toxicant_burden': ('Urine', 'native SBML amount', 'Urine Toxicant Burden. Maps to SBML symbol `Urine`.'), 'filtrate_toxicant_burden': ('FIltrate', 'native SBML amount', 'Filtrate Toxicant Burden. Maps to SBML symbol `FIltrate`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/MODEL2003190002.xml", integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
