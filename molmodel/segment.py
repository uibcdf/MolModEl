# polymer segment

class Segment:

    def __init__(self, segment_id=None, index=None, name=None, segment_type=None,
                 index_start=None, index_end=None, pdb_start=None, pdb_end=None,
                 uniprot_start=None, uniprot_end=None, sequence=None,
                 bioassembly_id=None, entity_id=None, chain_id=None):

        self.id = segment_id
        self.index = index
        self.name = name
        self.type = segment_type

        self.index_start = index_start
        self.index_end = index_end
        self.pdb_start = pdb_start
        self.pdb_end = pdb_end
        self.uniprot_start = uniprot_start
        self.uniprot_end = uniprot_end
        self.length = 0

        self.sequence = sequence
        self.secondary_structure_dssp = None
        self.secondary_structure_abc = None

        self.bioassembly_id = bioassembly_id
        self.entity_id = entity_id
        self.chain_id = chain_id

        self.group = []
        self.atom = []
        self.bond = []

        self.num_groups = 0
        self.num_atoms = 0
        self.num_bonds = 0
