
class Group:

    def __init__(self, group_id=None, index=None, name=None, group_type=None,
                 letter_code=None,
                 bioassembly_id=None, entity_id=None, chain_id=None, segment_id=None):

        self.id = group_id
        self.index = index
        self.name = name
        self.type = group_type
        self.letter_code = None

        self.bioassembly_id = bioassembly_id
        self.entity_id = entity_id
        self.chain_id = chain_id
        self.segment_id = segment_id

        self.atom = []
        self.bond = []

        self.num_atoms = 0
        self.num_bonds = 0


