
class Atom:

    def __init__(self, atom_id=None, index=None, name=None,
                 element=None, formal_charge=None,
                 bioassembly_id=None, entity_id=None, chain_id=None,
                 segment_id=None, group_id=None):

        self.id = atom_id
        self.index = index
        self.name = name
        self.element = element
        self.formal_charge = formal_charge

        self.bioassembly_id = bioassembly_id
        self.entity_id = bioassembly_id
        self.chain_id = chain_id
        self.segment_id = segment_id
        self.group_id = group_id
