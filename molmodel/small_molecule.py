from .entity import Entity as _Entity

class SmallMolecule(_Entity):

    def __init__(self, entity_id=None, index=None, name=None, entity_type=None,
                 bioassembly_id=None, chemical_id=None, inchikey=None, chembl_id=None):

        super(_Entity,self).__init__(entity_id=entity_id, index=index, name=name,
                                    entity_type=entity_type, bioassembly_id=bioassembly_id)

        self.chemical_id = chemical_id
        self.inchikey = inchikey
        self.chembl_id = chembl_id

