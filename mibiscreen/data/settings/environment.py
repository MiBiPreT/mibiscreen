"""Specifications of geochemicals.

List of geochemicals measured in groundwater samples useful
for biodegredation and bioremediation analysis

@author: A. Zech
"""

import mibiscreen.data.settings.standard_names as names

properties_geochemicals = dict()

properties_geochemicals[names.name_redox]=dict(
    other_names = ["redox", "redoxpotential","redox potential","redox-potential",
                   "redox_potential","redoxpot","redox pot","redox-pot","redox_pot",
                   "reduction potential","reductionpotential","reduction_potential",'eh'],
    standard_unit = names.unit_millivolt,
    )

properties_geochemicals[names.name_pH]=dict(
    other_names = ["ph"],
    standard_unit = names.unit_less,
    )

properties_geochemicals[names.name_EC]=dict(
    other_names = ["ec"],
    standard_unit = names.unit_microsimpercm,
    )

properties_geochemicals[names.name_pE]=dict(
    other_names = ["pe",'pε','p epsilon'],
    standard_unit = names.unit_less
    )

properties_geochemicals[names.name_DOC]=dict(
    other_names = ["doc",'dissolved organic carbon','dissolved-organic-carbon',
                   'dissolved_organic_carbon'],
    standard_unit = names.unit_mgperl,
    )

properties_geochemicals[names.name_NPOC]=dict(
    other_names = ["npoc",'non purgeable organic carbon','non-purgeable organic carbon',
                   'non-purgeable-organic-carbon', 'non_purgeable_organic_carbon'],
    standard_unit = names.unit_mgperl,
    )

properties_geochemicals[names.name_TOC]=dict(
    other_names = ["toc",'total organic carbon','total-organic-carbon',
                   'total_organic_carbon'],
    standard_unit = names.unit_mgperl,
    )

properties_geochemicals[names.name_oxygen]=dict(
    chemical_formula = 'o2',
    molecular_mass = 32.,
    # factor_stoichiometry = 4.,
    other_names = ["oxygen","o2","o-2","o_2","o 2","o"],
    standard_unit = names.unit_mgperl,
    )

properties_geochemicals[names.name_nitrate]=dict(
    chemical_formula = 'no3',
    molecular_mass = 62.,
    # factor_stoichiometry = 5.,
    other_names = ["nitrate","no3","no_3","no 3","no3-","no_3-","no 3-"],
    standard_unit = names.unit_mgperl,
    )

properties_geochemicals[names.name_nitrite]=dict(
    chemical_formula = 'no2',
    molecular_mass = 46.,
    # factor_stoichiometry = 0.,
    other_names = ["nitrite","no2","no_2","no 2","no2-","no_2-","no 2-"],
    standard_unit = names.unit_mgperl,
    )

properties_geochemicals[names.name_sulfate]=dict(
    chemical_formula = "so42-",
    molecular_mass = 96.1,
    # factor_stoichiometry = 8.,
    other_names = ["sulfate","sulphate","so4","so_4","so 4",
                   "so42-","so4_2-","so4 2-",
                   "so_42-","so_4_2-","so_4 2-",
                   "so 42-","so 4_2-","so 4 2-"],
    standard_unit = names.unit_mgperl,
    )

properties_geochemicals[names.name_sulfide]=dict(
    chemical_formula = "s2-",
    other_names = ["sulfide","sulphide","s2","s_2","s 2",
                   "s2-","s_2-","s 2-","s2min","s_2min","s 2min"],
    standard_unit = names.unit_mgperl,
    )

properties_geochemicals[names.name_iron2]=dict(
    chemical_formula = "fe2+",
    other_names = ['iron2','iron_2','iron 2','iron-2','iron(2)',
                   'ironii','iron_ii','iron ii','iron-ii','iron(ii)'
                   'iron2+','iron_2+','iron 2+','iron-2+','iron(2+)',
                   'ironii+','iron_ii+','iron ii+','iron-ii+','iron(ii+)',
                   'fe2','fe_2','fe 2','fe-2','fe(2)',
                   'feii','fe_ii','fe ii','fe-ii','fe(ii)'
                   'fe2+','fe_2+','fe 2+','fe-2+','fe(2+)',
                   'feii+','fe_ii+','fe ii+','fe-ii+','fe(ii+)',],
    standard_unit = names.unit_mgperl,
    )

properties_geochemicals[names.name_iron3]=dict(
    chemical_formula = "fe3+",
    other_names = ['iron3','iron_3','iron 3','iron-3','iron(3)',
                   'ironiii','iron_iii','iron iii','iron-iii','iron(iii)'
                   'iron3+','iron_3+','iron 3+','iron-3+','iron(3+)',
                   'ironiii+','iron_iii+','iron iii+','iron-iii+','iron(iii+)',
                   'fe3','fe_3','fe 3','fe-3','fe(3)',
                   'feiii','fe_iii','fe iii','fe-iii','fe(iii)'
                   'fe3+','fe_3+','fe 3+','fe-3+','fe(3+)',
                   'feiii+','fe_iii+','fe iii+','fe-iii+','fe(iii+)',],
    standard_unit = names.unit_mgperl,
    )

properties_geochemicals[names.name_manganese2]=dict(
    chemical_formula = "mn2+",
    other_names = ['manganese2','manganese_2','manganese 2','manganese-2','manganese(2)',
                   'manganeseii','manganese_ii','manganese ii','manganese-ii','manganese(ii)'
                   'manganese2+','manganese_2+','manganese 2+','manganese-2+','manganese(2+)',
                   'manganeseii+','manganese_ii+','manganese ii+','manganese-ii+','manganese(ii+)',
                   'mn2','mn_2','mn 2','mn-2','mn(2)',
                   'mnii','mn_ii','mn ii','mn-ii','mn(ii)'
                   'mn2+','mn_2+','mn 2+','mn-2+','mn(2+)',
                   'mnii+','mn_ii+','mn ii+','mn-ii+','mn(ii+)',
                   ],
    standard_unit = names.unit_mgperl,
    )

properties_geochemicals[names.name_manganese4]=dict(
    chemical_formula = "mn4+",
    other_names = ['manganese4','manganese_4','manganese 4','manganese-4','manganese(4)',
                   'manganeseiv','manganese_iv','manganese iv','manganese-iv','manganese(iv)'
                   'manganese4+','manganese_4+','manganese 4+','manganese-4+','manganese(4+)',
                   'manganeseiv+','manganese_iv+','manganese iv+','manganese-iv+','manganese(iv+)',
                   'mn4','mn_4','mn 4','mn-4','mn(4)',
                   'mniv','mn_iv','mn iv','mn-iv','mn(iv)'
                   'mn4+','mn_4+','mn 4+','mn-4+','mn(4+)',
                   'mniv+','mn_iv+','mn iv+','mn-iv+','mn(iv+)',
                   ],
    standard_unit = names.unit_mgperl,
    )

properties_geochemicals[names.name_methane]=dict(
    chemical_formula = "ch4",
    other_names = ['methane',"ch4","ch_4","ch 4"],
    standard_unit = names.unit_mgperl,
    )

properties_geochemicals[names.name_ammonium]=dict(
    chemical_formula = "nh4+",
    other_names = ["ammonium","nh4","nh_4","nh 4",'nh4+','nh_4+','nh 4+'],
    standard_unit = names.unit_mgperl,
    )

properties_geochemicals[names.name_phosphate]=dict(
    chemical_formula = "po4_3-",
    other_names = ["phosphate","po4","po_4","po 4",
                   "po43-","po_43-","po 43-",
                   "po4_3-","po_4_3-","po 4_3-",
                   "po4 3-","po_4 3-","po 4 3-",
                   ],
    standard_unit = names.unit_mgperl,
    )

properties_geochemicals[names.name_chloride]=dict(
    chemical_formula = "cl-",
    other_names = ['chloride','cl','cl-'],
    standard_unit = names.unit_mgperl,
    )

properties_geochemicals[names.name_bromide]=dict(
    chemical_formula = "br-",
    other_names = ['bromide','br','br-'],
    standard_unit = names.unit_mgperl,
    )

properties_geochemicals[names.name_fluoride]=dict(
    chemical_formula = "f-",
    other_names = ['fluoride','f','f-'],
    standard_unit = names.unit_mgperl,
    )

properties_geochemicals[names.name_sodium]=dict(
    chemical_formula = "na+",
    other_names = ['sodium','na','na+'],
    standard_unit = names.unit_mgperl,
    )

properties_geochemicals[names.name_magnesium]=dict(
    chemical_formula = "",
    other_names = ['magnesium','mg','mg2+','mg_2+','mg 2+'],
    standard_unit = names.unit_mgperl,
    )

properties_geochemicals[names.name_potassium]=dict(
    chemical_formula = 'k+',
    other_names = ['potassium','k','k+'],
    standard_unit = names.unit_mgperl,
    )

properties_geochemicals[names.name_calcium]=dict(
    chemical_formula = "ca2+",
    other_names = ['calcium','ca','ca2+','ca_2+','ca 2+'],
    standard_unit = names.unit_mgperl,
    )

properties_geochemicals[names.name_acetate]=dict(
    chemical_formula = 'c2h3o2-',
    other_names = ['acetate','c2h3o2-'],
    standard_unit = names.unit_mgperl,
    )

### List with all quantities of particular data type in standard names:
environment = list(properties_geochemicals.keys())

environment_groups = dict(
    environmental_conditions = [names.name_redox,
                                names.name_pH,
                                names.name_EC,
                                names.name_pE,
                                ],
    geochemicals = [names.name_oxygen,
                            names.name_nitrate,
                            names.name_sulfate,
                            names.name_iron2,
                            names.name_iron3,
                            names.name_manganese2,
                            names.name_manganese4,
                            names.name_methane,
                            names.name_nitrite,
                            names.name_sulfide,
                            names.name_ammonium,
                            names.name_phosphate,
                            names.name_chloride,
                            names.name_bromide,
                            names.name_fluoride,
                            names.name_sodium,
                            names.name_magnesium,
                            names.name_potassium,
                            names.name_calcium,
                            names.name_acetate,
                            names.name_DOC,
                            names.name_NPOC,
                            names.name_TOC,
                            ],
    ONS = [names.name_oxygen,
           names.name_nitrate,
           names.name_sulfate
           ], # non reduced electron acceptors
    ONSFe = [names.name_oxygen,
             names.name_nitrate,
             names.name_sulfate,
             names.name_iron3,
             ], # selected electron acceptors
    all_ea = [names.name_oxygen,
              names.name_nitrate,
              names.name_sulfate,
              names.name_iron2,
              names.name_manganese2,
              names.name_methane], # all electron acceptors (unreduced/reduced form)
    NP = [names.name_nitrate,
          names.name_nitrite,
          names.name_phosphate], # nutrients
)
