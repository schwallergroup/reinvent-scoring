import pickle
from typing import List

import numpy as np
from rdkit.Chem import Mol
from rdkit.Chem.Descriptors import ExactMolWt

from reinvent_chemistry import Descriptors

from reinvent_scoring.scoring.component_parameters import ComponentParameters
from reinvent_scoring.scoring.score_components import BaseScoreComponent
from reinvent_scoring.scoring.score_components.synthetic_accessibility.sascorer import calculateScore
from reinvent_scoring.scoring.score_summary import ComponentSummary


class BasicSAScore(BaseScoreComponent):
    def __init__(self, parameters: ComponentParameters):
        super().__init__(parameters)

    def calculate_score(self, molecules: List[Mol], step=-1) -> ComponentSummary:
        score = [calculateScore(mol) for mol in molecules]
        score_summary = ComponentSummary(total_score=score, parameters=self.parameters)
        return score_summary
