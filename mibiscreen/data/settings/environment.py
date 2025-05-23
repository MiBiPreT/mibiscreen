"""Specifications of geochemicals.

List of geochemicals measured in groundwater samples useful
for biodegredation and bioremediation analysis

@author: A. Zech
"""

import mibiscreen.data.settings.standard_names as names

geochemicals = dict(
    environmental_conditions = [names.name_redox,
                                names.name_pH,
                                names.name_EC,
                                names.name_pE,
                                names.name_NOPC
                                ],
    chemical_composition = [names.name_oxygen,
                            names.name_nitrate,
                            names.name_sulfate,
                            names.name_ironII,
                            names.name_manganese,
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
                            names.name_DOC
                            ],
    ONS = [names.name_oxygen,
           names.name_nitrate,
           names.name_sulfate
           ], # non reduced electron acceptors
    ONSFe = [names.name_oxygen,
             names.name_nitrate,
             names.name_sulfate,
             names.name_ironII
             ], # selected electron acceptors
    all_ea = [names.name_oxygen,
              names.name_nitrate,
              names.name_sulfate,
              names.name_ironII,
              names.name_manganese,
              names.name_methane], # all electron acceptors
    NP = [names.name_nitrate,
          names.name_nitrite,
          names.name_phosphate], # nutrients
)

properties_geochemicals = dict()

properties_geochemicals[names.name_redox]=dict(
    other_names = ["redox", "redoxpotential","redox potential","redox-potential",
                   "redox_potential","redoxpot","redox pot","redox-pot","redox_pot"] ,
    )

properties_geochemicals[names.name_pH]=dict(
    other_names = ["ph"],
    )

properties_geochemicals[names.name_EC]=dict(
    other_names = ["ec"],
    )

properties_geochemicals[names.name_pE]=dict(
    other_names = ["pe"],
    )

properties_geochemicals[names.name_NOPC]=dict(
    other_names = ["nopc"],
    )

properties_geochemicals[names.name_DOC]=dict(
    other_names = ["doc"],
    )

# properties_geochemicals[names.]=dict(
#     other_names = [] ,
#     )


# properties[names.name_oxygen]=dict(
#     chemical_formula = 'o2',
#     molecular_mass = 32.,
#     factor_stoichiometry = 4.,
#     other_names = ["oxygen","Oxygen","o2","O2"] ,
#     )

# properties[names.name_nitrate]=dict(
#     chemical_formula = 'no3',
#     molecular_mass = 62.,
#     factor_stoichiometry = 5.,
#     other_names = ["nitrate","Nitrate","NO3","no3"],
#     )

# properties[names.name_nitrite]=dict(
#     chemical_formula = 'no2',
#     molecular_mass = 46.,
#     factor_stoichiometry = 0.,
#     other_names = ["nitrite","Nitrite","NO2","no2"],
#     )

# properties[names.name_sulfate]=dict(
#     chemical_formula = "so42-",
#     molecular_mass = 96.1,
#     factor_stoichiometry = 8.,
#     other_names = ["sulfate", "Sulfate","so4", "so42-", "SO4", "SO42-"],
#     )

# properties[names.name_sulfide]=dict(
#     chemical_formula = "s2-",
#     mo
#     )
