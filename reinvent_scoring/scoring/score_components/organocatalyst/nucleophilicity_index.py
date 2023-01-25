from reinvent_scoring.scoring.component_parameters import ComponentParameters
from reinvent_scoring.scoring.score_components.organocatalyst.base_morfeus_component import BaseMorfeusComponent


class NucleophilicityIndex(BaseMorfeusComponent):
    def __init__(self, parameters: ComponentParameters):
        super().__init__(parameters)

    def _calculate_morfeus_property(self, mol):
        return self._morfeus_descriptors.nucleophilicity_index(mol)
