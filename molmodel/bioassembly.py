
class BioAssembly:

    def __init__(self, bioassembly_id=None, index=None, name=None, bioassembly_type=None):

        self.id = bioassembly_id
        self.index = index
        self.name = name
        self.type = bioassembly_type

        self.chain = []
        self.entity = []
        self.segment = []
        self.group = []
        self.atom = []
        self.bond = []

        self.num_chains = []
        self.num_entities = []
        self.num_groups = []
        self.num_atoms = []
        self.num_bonds = []

