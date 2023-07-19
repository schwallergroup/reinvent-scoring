from typing import List
import rdkit.Chem as Chem

from reinvent_chemistry.similarity import Similarity
from reinvent_scoring.scoring.component_parameters import ComponentParameters
from reinvent_scoring.scoring.score_components import BaseScoreComponent
from reinvent_scoring.scoring.score_summary import ComponentSummary


class EspsimSimilarity(BaseScoreComponent):
    def __init__(self, parameters: ComponentParameters):
        super().__init__(parameters)
        self._similarity = Similarity()
        self._smiles = self.parameters.specific_parameters.get(self.component_specific_parameters.SMILES, [])
        self._ref_mols = self._similarity.smiles_to_mol(self._smiles)
        print(self._ref_mols)

    def calculate_score(self, molecules: List) -> ComponentSummary:
        query_smis = [Chem.MolToSmiles(mol) for mol in molecules]
        print(query_smis)
        esp_sim_score = self._similarity.calc_espsim(self._smiles, query_smis)

        score_summary = ComponentSummary(total_score=esp_sim_score, parameters=self.parameters)
        return score_summary