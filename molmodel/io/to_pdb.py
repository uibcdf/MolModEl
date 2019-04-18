from numpy import column_stack as _column_stack
from molmodel import PDB as _PDB
from .to_bioassembly import from_mmtf as _bioassembly_from_mmtf

def from_mmtf(mmtf):

    pdb=_PDB()

    pdb.method = mmtf.experimental_methods
    pdb.title = mmtf.title
    pdb.resolution = mmtf.resolution
    pdb.deposition_date = mmtf.deposition_date
    pdb.unit_cell = mmtf.unit_cell

    pdb.num_bioassemblies = len(mmtf.bio_assembly)
    pdb.num_chains = mmtf.num_chains
    pdb.num_entities = len(mmtf.entity_list)
    pdb.num_groups = mmtf.num_groups
    pdb.num_models = mmtf.num_models

    pdb.bioassembly = _bioassembly_from_mmtf(mmtf)

    num_atoms = int(pdb.coordinates.shape[0]/pdb.num_models)

    pdb.coordinates = _column_stack([mmtf.x_coord_list,
                                     mmtf.y_coord_list,
                                     mmtf.z_coord_list])
    pdb.coordinates = pdb.coordinates.reshape(pdb.num_models, num_atoms, 3)

    pdb.b_factors = mmtf.b_factor_list.reshape(pdb.num_models, num_atoms)

    del(num_atoms)

    return pdb

def from_pdb_id(pdb_id):

    from mmtf import fetch as _fetch_mmtf

    mmtf = _fetch_mmtf(pdb_id)
    pdb = from_mmtf(mmtf)
    del(mmtf,_fetch_mmtf)

    return pdb

def from_pdb_file(pdb_file,pdb=None):

    pass
