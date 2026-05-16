# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML BioModule for Qosa2014 - Mechanistic modeling that describes amyloid-Beta clearance across BBB."""
from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Qosa2014MechanisticModelingThatDescribesAmyModel1409240002Model(TelluriumSBMLBioModule):
    """Faithfully executes the bundled SBML source for Qosa2014 - Mechanistic modeling that describes amyloid-Beta clearance across BBB."""

    _SBML_ID = 'MODEL1409240002'
    _TITLE = 'Qosa2014 - Mechanistic modeling that describes amyloid-Beta clearance across BBB'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['IntactAbetahCMEC_D3', 'IntactAbetabEnd3', 'CcellhCMEC_D3', 'DcellhCMEC_D3', 'CcellbEnd3', 'DcellbEnd3', 'CmediahCMEC_D3', 'CmediabEnd3']
    _SPECIES_LABELS = {'IntactAbetahCMEC_D3': 'Intact Amyloid Beta Hcmec D3', 'IntactAbetabEnd3': 'Intact Amyloid Beta Bend3', 'CcellhCMEC_D3': 'Cellular Amyloid Beta Hcmec D3', 'DcellhCMEC_D3': 'Degraded Amyloid Beta Hcmec D3', 'CcellbEnd3': 'Cellular Amyloid Beta Bend3', 'DcellbEnd3': 'Degraded Amyloid Beta Bend3', 'CmediahCMEC_D3': 'Media Amyloid Beta Hcmec D3', 'CmediabEnd3': 'Media Amyloid Beta Bend3'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_cellular_amyloid_beta_hcmec_d3': ('CcellhCMEC_D3', 0.0, 'native SBML value', 'initial cellular amyloid-beta in HCMEC-D3 cells. Maps to SBML symbol `CcellhCMEC_D3`.'), 'initial_cellular_amyloid_beta_bend3': ('CcellbEnd3', 0.0, 'native SBML value', 'initial cellular amyloid-beta in bEnd3 cells. Maps to SBML symbol `CcellbEnd3`.'), 'initial_media_amyloid_beta_hcmec_d3': ('CmediahCMEC_D3', 3.0, 'native SBML value', 'initial media concentration for HCMEC-D3. Maps to SBML symbol `CmediahCMEC_D3`.'), 'initial_media_amyloid_beta_bend3': ('CmediabEnd3', 3.0, 'native SBML value', 'initial media concentration for bEnd3. Maps to SBML symbol `CmediabEnd3`.')}
    _HEADLINE_OUTPUTS = {'intact_amyloid_beta_hcmec_d3': ('IntactAbetahCMEC_D3', 'native SBML value', 'Intact Amyloid Beta Hcmec D3. Maps to SBML symbol `IntactAbetahCMEC_D3`.'), 'intact_amyloid_beta_bend3': ('IntactAbetabEnd3', 'native SBML value', 'Intact Amyloid Beta Bend3. Maps to SBML symbol `IntactAbetabEnd3`.'), 'cellular_amyloid_beta_hcmec_d3': ('CcellhCMEC_D3', 'native SBML value', 'Cellular Amyloid Beta Hcmec D3. Maps to SBML symbol `CcellhCMEC_D3`.'), 'degraded_amyloid_beta_hcmec_d3': ('DcellhCMEC_D3', 'native SBML value', 'Degraded Amyloid Beta Hcmec D3. Maps to SBML symbol `DcellhCMEC_D3`.'), 'cellular_amyloid_beta_bend3': ('CcellbEnd3', 'native SBML value', 'Cellular Amyloid Beta Bend3. Maps to SBML symbol `CcellbEnd3`.'), 'degraded_amyloid_beta_bend3': ('DcellbEnd3', 'native SBML value', 'Degraded Amyloid Beta Bend3. Maps to SBML symbol `DcellbEnd3`.'), 'media_amyloid_beta_hcmec_d3': ('CmediahCMEC_D3', 'native SBML value', 'Media Amyloid Beta Hcmec D3. Maps to SBML symbol `CmediahCMEC_D3`.'), 'media_amyloid_beta_bend3': ('CmediabEnd3', 'native SBML value', 'Media Amyloid Beta Bend3. Maps to SBML symbol `CmediabEnd3`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = "data/MODEL1409240002.xml", integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
