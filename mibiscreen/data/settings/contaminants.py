"""Specifications of petroleum hydrocarbon related contaminants.

List of (PAH) contamiants measured in groundwater samples useful
for biodegredation and bioremediation analysis

@author: A. Zech
"""

import mibiscreen.data.settings.standard_names as names

contaminants = dict(
    BTEX = [names.name_benzene,
            names.name_toluene,
            names.name_ethylbenzene,
            names.name_pm_xylene,
            names.name_o_xylene,
            names.name_xylene],
    BTEXIIN = [names.name_benzene,
               names.name_toluene,
               names.name_ethylbenzene,
               names.name_pm_xylene,
               names.name_o_xylene,
               names.name_xylene,
               names.name_indane,
               names.name_indene,
               names.name_naphthalene],
    all_cont = [names.name_benzene,
                names.name_toluene,
                names.name_ethylbenzene,
                names.name_pm_xylene,
                names.name_o_xylene,
                names.name_xylene,
                names.name_indane,
                names.name_indene,
                names.name_naphthalene,
                names.name_styrene,
                names.name_isopropylbenzene,
                names.name_n_propylbenzene,
                names.name_ethyltoluene,
                names.name_2_ethyltoluene,
                names.name_3_ethyltoluene,
                names.name_4_ethyltoluene,
                names.name_trimethylbenzene,
                names.name_123_trimethylbenzene,
                names.name_124_trimethylbenzene,
                names.name_135_trimethylbenzene,
                names.name_4_isopropyltouene,
                names.name_13_diethylbenzene,
                names.name_1245_tetramethylbenzene,
                names.name_2_methylindene,
                names.name_1_methylnaphtalene,
                names.name_2_ethylnaphtalene,
                names.name_16_dimethylnaphtalene,
                names.name_26_dimethylnaphtalene
                ],
)

properties_contaminants = dict()

properties_contaminants[names.name_benzene]=dict(
    chemical_formula = 'c6h6',
    molecular_mass = 78.,
    carbon_atoms = 6,
    hydrogen_atoms = 6,
    # factor_stoichiometry = 30.,
    # thresholds_for_intervention_NL = 30,
    other_names = ["benzene", "c6h6", "benzeen", "benzen", "benzol"],
    )

properties_contaminants[names.name_toluene]=dict(
    chemical_formula = 'c6h5ch3',
    molecular_mass = 92.,
    carbon_atoms = 7,
    hydrogen_atoms = 8,
    # factor_stoichiometry = 36.,
    # thresholds_for_intervention_NL = 1000,
    other_names = ["toluene", "tolueen", "toluen", "c7h8","c6h5ch3"],
    )

properties_contaminants[names.name_ethylbenzene]=dict(
    chemical_formula = 'c6h5ch2ch3',
    molecular_mass = 106.,
    carbon_atoms = 8,
    hydrogen_atoms = 10,
#    factor_stoichiometry = 42.,
#    thresholds_for_intervention_NL = 150.,
    other_names = ["ethylbenzene","ethylbenzen","ethylbenzeen","c6h5ch2ch3"],
    )

properties_contaminants[names.name_xylene]=dict(
    chemical_formula = "c6h4ch3ch3",
    molecular_mass = 106.,
    carbon_atoms = 8,
    hydrogen_atoms = 10,
    # factor_stoichiometry = 42.,
    # thresholds_for_intervention_NL = 70.,
    other_names = ["xylene",
                   "c6h4ch3ch3"],
    )

properties_contaminants[names.name_pm_xylene]=dict(
    chemical_formula =  "c6h4ch3ch3",
    molecular_mass = 106.,
    carbon_atoms = 8,
    hydrogen_atoms = 10,
    # factor_stoichiometry = 42.,
    # thresholds_for_intervention_NL = 70.,
    other_names = ["pm_xylene","pm-xylene","pm xylene","pmxylene",
                   "p/m_xylene","p/m-xylene","p/m xylene","p/mxylene",
                   "p,m_xylene","p,m-xylene","p,m xylene","p,mxylene",
                   "p m_xylene","p m-xylene","p m xylene","p mxylene",
                   "p-m_xylene","p-m-xylene","p-m xylene","p-mxylene",
                   "p_m_xylene","p_m-xylene","p_m xylene","p_mxylene",
                   "mp_xylene","mp-xylene","mp xylene","mpxylene",
                   "m/p_xylene","m/p-xylene","m/p xylene","m/pxylene",
                   "m,p_xylene","m,p-xylene","m,p xylene","m,pxylene",
                   "m p_xylene","m p-xylene","m p xylene","m pxylene",
                   "m-p_xylene","m-p-xylene","m-p xylene","m-pxylene",
                   "m_p_xylene","m_p-xylene","m_p xylene","m_pxylene"
                   ],
    )

properties_contaminants[names.name_o_xylene]=dict(
    chemical_formula = "c6h4ch3ch3" ,
    molecular_mass = 106.,
    carbon_atoms = 8,
    hydrogen_atoms = 10,
    # factor_stoichiometry = 42.,
    # thresholds_for_intervention_NL = 70.,
    other_names =  ["o-xylene",
                    "o xylene",
                    "o_xylene",
                    "oxylene"],
    )

properties_contaminants[names.name_indene]=dict(
    chemical_formula = "c9h8",
    molecular_mass = 116.,
    carbon_atoms = 9,
    hydrogen_atoms = 8,
    # factor_stoichiometry = 44.,
    # thresholds_for_intervention_NL = 70.,
    other_names = ["indene",
                   "indeen",
                   "c9h8"],
    )

properties_contaminants[names.name_indane]=dict(
    chemical_formula = "c9h10",
    molecular_mass = 118.,
    carbon_atoms = 9,
    hydrogen_atoms = 10,
    # factor_stoichiometry = 46.,
    # thresholds_for_intervention_NL = 70.,
    other_names = ["indane",
                   "indan",
                   "c9h10"
                   ],
    )

properties_contaminants[names.name_naphthalene]=dict(
    chemical_formula = "c10h8",
    molecular_mass = 128.,
    carbon_atoms = 10,
    hydrogen_atoms = 8,
    # factor_stoichiometry = 48.,
    # thresholds_for_intervention_NL = 70.,
    other_names = ["naphthalene",
                   "naphthaleen",
                   "naphthaline",
                   "naphtaline",
                   "naphtalene",
                   "naphtaleen",
                   "c10h8"],
    )
