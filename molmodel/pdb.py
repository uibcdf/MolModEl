from .atom import Atom
from .group import Group
from .bioassemply import BioAssembly
from copy import deepcopy as _deepcopy

class PDB:

    def __init__(self, pdb_id=None, method=None, resolution=None, title=None,
                deposition_date=None, mmtf=None, unit_cell=None):

        self.id = pdb_id
        self.method = method
        self.resolution = resolution
        self.title = title
        self.deposition_date = deposition_date
        self.mmtf = mmtf                         # mmtf-python
        self.unit_cell = unit_cell

        self.bioassembly = {}
        self.group = {}
        self.entity = {}
        self.chain = {}

        self.num_bioassemblies = 0
        self.num_groups = 0
        self.num_entities = 0
        self.num_chains = 0
        self.num_ligands = 0

        self.ion = {}
        self.water = {}
        self.small_molecule = {}
        self.protein = {}
        self.peptide = {}
        self.dna = {}
        self.rna = {}

        self.num_ions = {}
        self.num_waters = {}
        self.num_small_molecules = {}
        self.num_proteins = {}
        self.num_peptides = {}
        self.num_dnas = {}
        self.num_rnas = {}

    def from_mmtf(self,mmtf):

        self.mmtf = mmtf


        pass

    def from_pdb_id(self,pdb_id):
        pass

    def from_pdb_file(self,pdb_id):
        pass

def identity(item1=None, item2=None):

    return item1.id==item2['Id']

def merge(cards=None):

    pass

def depuration(cards=None):

    num_cards = len(cards)
    pairs_equal=[]
    for ii in range(num_cards):
        for jj in range(ii+1,num_cards):
            if equal_pdb_cards(cards[ii],cards[jj]):
                pairs_equal.append([ii,jj])

    result=[]
    while pairs_equal:
        bb=pairs_equal.pop(0)
        cc=[]
        for ii in range(len(pairs_equal)):
            if set.intersection(set(bb),set(pairs_equal[ii])):
                bb=list(set.union(set(bb),set(pairs_equal[ii])))
                cc.append(ii)
        aa2=[]
        for ii in range(len(pairs_equal)):
            if ii not in cc:
                aa2.append(pairs_equal[ii])
        pairs_equal=aa2
        result.append(bb)

    pairs_equal=result

    list_depurated=[]

    for ii in pairs_equal:
        list_depurated.append(merge_pdb_cards([cards[jj] for jj in ii]))

    flat_pairs_equal = [item for sublist in pairs_equal for item in sublist]

    for ii in range(num_cards):
        if ii not in flat_pairs_equal:
            list_depurated.append(cards[ii])

    return list_depurated

