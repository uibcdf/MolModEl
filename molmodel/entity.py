
class Entity:

    def __init__(self, entity_id=None, index=None, name=None, entity_type=None,
                 bioassembly_id=None, chain_id=None):

        self.id = entity_id
        self.index = index
        self.name = name
        self.type = entity_type

        self.bioassembly_id = bioassembly_id
        self.chain_id = chain_id

        self.segment = []
        self.group = []
        self.bond = []

        self.num_segments = 0
        self.num_groups = 0
        self.num_atoms = 0
        self.num_bonds = 0

