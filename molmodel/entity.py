
class Entity:

    def __init__(self):

        self.id = None
        self.index = None
        self.name = None
        self.type = None

        self.bioassembly_id = None
        self.bioassembly_index = None
        self.bioassembly_name = None
        self.bioassembly_type = None

        self.chain_id = None
        self.chain_index = None
        self.chain_name = None
        self.chain_type = None

        self.segment = []
        self.group = []
        self.atom = []
        self.bond = []

        self.num_segments = 0
        self.num_groups = 0
        self.num_atoms = 0
        self.num_bonds = 0

