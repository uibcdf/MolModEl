from molmodel import BioAssembly as _BioAssembly
from molmodel import Chain as _Chain

def from_mmtf(mmtf):

    bioassemblies = []
    index=0

    for mmtf_bioassembly in mmtf.bio_assembly:

        bioassembly = _BioAssembly()

        bioassembly.index = index
        bioassembly.name = mmtf_bioassembly['name']
        bioassembly.id = mmtf_bioassembly['name']
        bioassembly.type = None

        # chains

        bioassembly.chain = []
        for transform_list in mmtf_bioassembly['transformList']:
            for chain_index in transform_list['chainIndexList']:
                chain = _Chain

                chain.bioassembly_id = bioassembly.id
                chain.bioassembly_index = bioassembly.index
                chain.bioassembly_name = bioassembly.name

                chain.index = chain_index
                chain.id = mmtf.chain_id_list[chain_index]
                chain.name = mmtf.chain_name_list[chain_index]
                chain.type = None

                chain.entity = []
                chain.segment = []
                chain.group = []
                chain.atom = []
                chain.bond = []


        bioassemblies.append(bioassembly)
        index+=1

    return bioassemblies

###    ## bioAssemblies
###
###    for ii in _mmtf_pdb.bio_assembly:
###        _tmp_item = _deepcopy(_bioAssemblies_card)
###        _tmp_item['Name']=ii['name']
###        _tmp_item['Chains']=ii['transformList'][0]['chainIndexList']
###        tmp_card['bioAssembly'][ii['name']]=_tmp_item
###        del(_tmp_item)
###
###    ## Groups
###
###    for ii in range(_mmtf_pdb.num_groups):
###        _tmp_item = _deepcopy(_group_card)
###        _tmp_item['Id'] = _mmtf_pdb.group_id_list[ii]
###        _tmp_group = _mmtf_pdb.group_list[_mmtf_pdb.group_type_list[ii]]
###        _tmp_item['Name'] = _tmp_group['groupName']
###        _tmp_item['Atom Name List'] = _tmp_group['atomNameList']
###        _tmp_item['Element List'] = _tmp_group['elementList']
###        _tmp_item['Bond Order List'] = _tmp_group['bondOrderList']
###        _tmp_item['Bond Atom List'] = _tmp_group['bondAtomList']
###        _tmp_item['Formal Charge List'] = _tmp_group['formalChargeList']
###        _tmp_item['Letter Code'] = _tmp_group['singleLetterCode']
###        _tmp_item['Type'] = _tmp_group['chemCompType']
###        tmp_card['Group'][ii]=_tmp_item
###        del(_tmp_item)
###
###    ## Chains
###
###    ind_start=0
###    _tmp_dssp = [_sec_struct_codes[ii] for ii in _mmtf_pdb.sec_struct_list]
###    for ii in range(_mmtf_pdb.num_chains):
###        _tmp_item = _deepcopy(_chain_card)
###        _tmp_item['Index'] = ii
###        _tmp_item['Id'] = _mmtf_pdb.chain_id_list[ii]
###        _tmp_item['Name'] = _mmtf_pdb.chain_name_list[ii]
###        _tmp_item['Groups'] = list(range(ind_start,ind_start+_mmtf_pdb.groups_per_chain[ii]))
###        ind_start+=_mmtf_pdb.groups_per_chain[ii]
###        tmp_seq = [tmp_card['Group'][ii]['Letter Code'] for ii in _tmp_item['Groups']]
###        _tmp_item['Sequence'] = ''.join(tmp_seq)
###        _aux_ss =[_tmp_dssp[jj] for jj in _tmp_item['Groups']]
###        _tmp_item['Secondary Structure DSSP'] =''.join(_aux_ss)
###        _tmp_item['Secondary Structure ABC'] = ''.join([_dssp_to_abc[jj] for jj in _aux_ss])
###        tmp_card['Chain'][_mmtf_pdb.chain_id_list[ii]]=_tmp_item
###        del(_tmp_item,tmp_seq,_aux_ss)
###    del(ind_start,_tmp_dssp)
###
###    ## Entities
###
###    entity_id=1
###    for _tmp_item in _mmtf_pdb.entity_list:
###        _tmp_entity = _deepcopy(_entity_card)
###        _tmp_entity['Id'] = entity_id
###        _tmp_entity['Description']=_tmp_item['description']
###        _tmp_entity['Type']=_tmp_item['type']
###        _tmp_entity['Sequence']=_tmp_item['sequence']
###        _tmp_entity['Chains']=[_mmtf_pdb.chain_name_list[ii] for ii in _tmp_item['chainIndexList']]
###        tmp_card['Entity'][entity_id]=_tmp_entity
###        entity_id+=1
###        del(_tmp_entity)
###    del(_tmp_item)
###
