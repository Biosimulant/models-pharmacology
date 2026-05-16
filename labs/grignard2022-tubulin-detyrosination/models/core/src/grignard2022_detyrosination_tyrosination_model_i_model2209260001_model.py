# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule for Grignard2022 - Detyrosination/Tyrosination Model in neurons and proliferative cells."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Grignard2022DetyrosinationTyrosinationModelIModel2209260001Model(TelluriumSBMLBioModule):
    """Faithfully executes the bundled SBML source for Grignard2022 - Detyrosination/Tyrosination Model in neurons and proliferative cells."""

    _SBML_ID = 'MODEL2209260001'
    _TITLE = 'Grignard2022 - Detyrosination/Tyrosination Model in neurons and proliferative cells'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['s0', 's1', 's2', 's3', 's4', 's5']
    _SPECIES_LABELS = {'s0': 'Detyrosinated Tubulin', 's1': 'Detyrosinated Microtubules', 's2': 'Tyrosinated Tubulin', 's3': 'Tyrosinated Microtubules', 's4': 'Tcp Enzyme Pool', 's5': 'Ttl Enzyme Pool'}
    _PARAMETER_INPUTS = {'detyrosination_affinity_km': ('p8', 1.9, 'native SBML value', 'source Km2 affinity parameter, if source annotation confirms detyrosination step. Maps to SBML symbol `p8`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_detyrosinated_tubulin': ('s0', 0.0, 'native SBML value', 'initial detyrosinated tubulin pool. Maps to SBML symbol `s0`.'), 'initial_tyrosinated_tubulin': ('s2', 5.0, 'native SBML value', 'initial tyrosinated tubulin pool. Maps to SBML symbol `s2`.'), 'initial_tcp_enzyme_pool': ('s4', 1.0, 'native SBML amount', 'initial TCP enzyme pool. Maps to SBML symbol `s4`.'), 'initial_ttl_enzyme_pool': ('s5', 1.0, 'native SBML amount', 'initial TTL enzyme pool. Maps to SBML symbol `s5`.')}
    _HEADLINE_OUTPUTS = {'detyrosinated_tubulin': ('s0', 'native SBML value', 'Detyrosinated Tubulin. Maps to SBML symbol `s0`.'), 'detyrosinated_microtubules': ('s1', 'native SBML value', 'Detyrosinated Microtubules. Maps to SBML symbol `s1`.'), 'tyrosinated_tubulin': ('s2', 'native SBML value', 'Tyrosinated Tubulin. Maps to SBML symbol `s2`.'), 'tyrosinated_microtubules': ('s3', 'native SBML value', 'Tyrosinated Microtubules. Maps to SBML symbol `s3`.'), 'tcp_enzyme_pool': ('s4', 'native SBML amount', 'Tcp Enzyme Pool. Maps to SBML symbol `s4`.'), 'ttl_enzyme_pool': ('s5', 'native SBML amount', 'Ttl Enzyme Pool. Maps to SBML symbol `s5`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/MODEL2209260001.xml", integration_step: float = 0.05) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
