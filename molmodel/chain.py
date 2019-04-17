
class Chain:

    def __init__(self, chain_id=None, index=None, name=None, chain_type=None,
                 bioassembly_id=None):

        self.id = chain_id
        self.index = index
        self.name = name
        self.type = chain_type

        self.bioassembly_id = bioassembly_id

        self.entity = []
        self.segment = []
        self.group = []
        self.atom = []
        self.bond = []

        self.num_entities = 0
        self.num_groups = 0
        self.num_atoms = 0
        self.num_bonds = 0

