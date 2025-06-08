"""Specifications of petroleum hydrocarbon related contaminants.

List of (PAH) contamiants measured in groundwater samples useful
for biodegredation and bioremediation analysis

@author: A. Zech
"""

import mibiscreen.data.settings.standard_names as names

properties_contaminants = dict()
properties_contaminants[names.name_benzene]=dict(
    chemical_formula = 'c6h6',
    molecular_mass = 78.,
    carbon_atoms = 6,
    hydrogen_atoms = 6,
    # factor_stoichiometry = 30.,
    # thresholds_for_intervention_NL = 30,
    other_names = ["benzene", "c6h6", "benzeen", "benzen", "benzol"],
    standard_unit = names.unit_microgperl,
    )

properties_contaminants[names.name_toluene]=dict(
    chemical_formula = 'c6h5ch3',
    molecular_mass = 92.,
    carbon_atoms = 7,
    hydrogen_atoms = 8,
    # factor_stoichiometry = 36.,
    # thresholds_for_intervention_NL = 1000,
    other_names = ["toluene", "tolueen", "toluen", "c7h8","c6h5ch3"],
    standard_unit = names.unit_microgperl,
    )

properties_contaminants[names.name_ethylbenzene]=dict(
    chemical_formula = 'c6h5ch2ch3',
    molecular_mass = 106.,
    carbon_atoms = 8,
    hydrogen_atoms = 10,
#    factor_stoichiometry = 42.,
#    thresholds_for_intervention_NL = 150.,
    other_names = ["ethylbenzene","ethylbenzen","ethylbenzeen","c6h5ch2ch3"],
    standard_unit = names.unit_microgperl,
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
    standard_unit = names.unit_microgperl,
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
    standard_unit = names.unit_microgperl,
    )

properties_contaminants[names.name_o_xylene]=dict(
    chemical_formula = "c6h4ch3ch3" ,
    molecular_mass = 106.,
    carbon_atoms = 8,
    hydrogen_atoms = 10,
    # factor_stoichiometry = 42.,
    # thresholds_for_intervention_NL = 70.,
    other_names =  ["o-xylene","o xylene","o_xylene","oxylene"],
    standard_unit = names.unit_microgperl,
    )

properties_contaminants[names.name_indene]=dict(
    chemical_formula = "c9h8",
    molecular_mass = 116.,
    carbon_atoms = 9,
    hydrogen_atoms = 8,
    # factor_stoichiometry = 44.,
    # thresholds_for_intervention_NL = 70.,
    other_names = ["indene","indeen","c9h8"],
    standard_unit = names.unit_microgperl,
    )

properties_contaminants[names.name_indane]=dict(
    chemical_formula = "c9h10",
    molecular_mass = 118.,
    carbon_atoms = 9,
    hydrogen_atoms = 10,
    # factor_stoichiometry = 46.,
    # thresholds_for_intervention_NL = 70.,
    other_names = ["indane","c9h10"],
    standard_unit = names.unit_microgperl,
    )

properties_contaminants[names.name_naphthalene]=dict(
    chemical_formula = "c10h8",
    molecular_mass = 128.,
    carbon_atoms = 10,
    hydrogen_atoms = 8,
    # factor_stoichiometry = 48.,
    # thresholds_for_intervention_NL = 70.,
    other_names = ["naphthalene","naphthaleen","naphthaline",
                   "naphtaline","naphtalene","naphtaleen","c10h8"],
    standard_unit = names.unit_microgperl,
    )


properties_contaminants[names.name_styrene]=dict(
    chemical_formula = "c6h5chch2",
    molecular_mass = 104.15,
    carbon_atoms = 8,
    hydrogen_atoms = 8,
    other_names = ['styrene','styren''styrol','styrolene','styropol',
                   'ethenylbenzene','vinylbenzene','phenylethene','phenylethylene',
                   'cinnamene'],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_isopropylbenzene]=dict(
    chemical_formula = "c6h5c3h7",
    molecular_mass = 120.195,
    carbon_atoms = 9,
    hydrogen_atoms = 12 ,
    other_names = ['isopropylbenzene','cumene',
                   "iso-propylbenzene","iso_propylbenzene","iso propylbenzene"],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_n_propylbenzene]=dict(
    chemical_formula = "c6h5ch2ch2ch3",
    molecular_mass = 120.195,
    carbon_atoms = 9,
    hydrogen_atoms = 12,
    other_names = ["n_propylbenzene","n-propylbenzene","n propylbenzene",
                   "npropylbenzene","propylbenzene"],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_ethyltoluene]=dict(
    chemical_formula = "c6h4ch3c2h5",
    molecular_mass = 120.195,
    carbon_atoms = 9,
    hydrogen_atoms = 12,
    other_names = ['ethyltoluene'],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_2_ethyltoluene]=dict(
    chemical_formula = "c6h4ch3c2h5",
    molecular_mass = 120.195,
    carbon_atoms = 9,
    hydrogen_atoms = 12,
    other_names = ['2_ethyltoluene','2-ethyltoluene','2 ethyltoluene',
                   '2ethyltoluene','ortho_ethyltoluene','ortho-ethyltoluene',
                   'ortho ethyltoluene','orthoethyltoluene','o_ethyltoluene',
                   'o-ethyltoluene','o ethyltoluene'],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_3_ethyltoluene]=dict(
    chemical_formula = "c6h4ch3c2h5",
    molecular_mass = 120.195,
    carbon_atoms = 9,
    hydrogen_atoms = 12,
    other_names = ['3_ethyltoluene','3-ethyltoluene','3ethyltoluene',
                   'meta_ethyltoluene','meta-ethyltoluene','meta ethyltoluene',
                   'metaethyltoluene','m_ethyltoluene','m-ethyltoluene','m ethyltoluene'],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_4_ethyltoluene]=dict(
    chemical_formula = "c6h4ch3c2h5",
    molecular_mass = 120.195,
    carbon_atoms = 9,
    hydrogen_atoms = 12,
    other_names = ['4_ethyltoluene','4-ethyltoluene','4 ethyltoluene','4ethyltoluene',
                   'para_ethyltoluene','para-ethyltoluene','para ethyltoluene',
                   'paraethyltoluene','p_ethyltoluene','p-ethyltoluene','p ethyltoluene'],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_trimethylbenzene]=dict(
    chemical_formula = "c6h3ch3ch3ch3",
    molecular_mass = 120.195,
    carbon_atoms = 9,
    hydrogen_atoms = 12,
    other_names = ['trimethylbenzene'],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_123_trimethylbenzene]=dict(
    chemical_formula = "c6h3ch3ch3ch3",
    molecular_mass = 120.195,
    carbon_atoms = 9,
    hydrogen_atoms = 12,
    other_names = ['123_trimethylbenzene','123-trimethylbenzene','123 trimethylbenzene',
                   '123trimethylbenzene','1,2,3_trimethylbenzene','1,2,3-trimethylbenzene',
                   '1,2,3 trimethylbenzene','1,2,3trimethylbenzene'],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_124_trimethylbenzene]=dict(
    chemical_formula = "c6h3ch3ch3ch3",
    molecular_mass = 120.195,
    carbon_atoms = 9,
    hydrogen_atoms = 12,
    other_names = ['124_trimethylbenzene','124-trimethylbenzene','124 trimethylbenzene',
                   '124trimethylbenzene','1,2,4_trimethylbenzene','1,2,4-trimethylbenzene',
                   '1,2,4 trimethylbenzene','1,2,4trimethylbenzene'],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_135_trimethylbenzene]=dict(
    chemical_formula = "c6h3ch3ch3ch3",
    molecular_mass = 120.195,
    carbon_atoms = 9,
    hydrogen_atoms = 12,
    other_names = ['135_trimethylbenzene','135-trimethylbenzene','135 trimethylbenzene',
                   '135trimethylbenzene','1,3,5_trimethylbenzene','1,3,5-trimethylbenzene',
                   '1,3,5 trimethylbenzene','1,3,5trimethylbenzene'],
    standard_unit = names.unit_microgperl,
)


properties_contaminants[names.name_4_isopropyltouene]=dict(
    chemical_formula = "c6h4ch3c3h7",
    molecular_mass = 134.22,
    carbon_atoms = 10,
    hydrogen_atoms = 14,
    other_names = ['4_isopropyltouene','4-isopropyltouene','4 isopropyltouene',
                   '4isopropyltouene','p_cymene','p-cymene','p cymene','pcymene'],
    standard_unit = names.unit_microgperl,
)


properties_contaminants[names.name_diethylbenzene]=dict(
    chemical_formula = "c6h4c2h5c2h5",
    molecular_mass = 134.22,
    carbon_atoms = 10,
    hydrogen_atoms = 14,
    other_names = ['diethylbenzene'],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_12_diethylbenzene]=dict(
    chemical_formula = "c6h4c2h5c2h5",
    molecular_mass = 134.22,
    carbon_atoms = 10,
    hydrogen_atoms = 14,
    other_names = ['12_diethylbenzene','12-diethylbenzene','12 diethylbenzene','12diethylbenzene',
                   '1,2_diethylbenzene','1,2-diethylbenzene','1,2 diethylbenzene','1,2diethylbenzene',
                   'o_diethylbenzene','o-diethylbenzene','o diethylbenzene','odiethylbenzene'],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_13_diethylbenzene]=dict(
    chemical_formula = "c6h4c2h5c2h5",
    molecular_mass = 134.22,
    carbon_atoms = 10,
    hydrogen_atoms = 14,
    other_names = ['13_diethylbenzene','13-diethylbenzene','13 diethylbenzene','13diethylbenzene',
                   '1,3_diethylbenzene','1,3-diethylbenzene','1,3 diethylbenzene','1,3diethylbenzene',
                   'm_diethylbenzene','m-diethylbenzene','m diethylbenzene','mdiethylbenzene'],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_14_diethylbenzene]=dict(
    chemical_formula = "c6h4c2h5c2h5",
    molecular_mass = 134.22,
    carbon_atoms = 10,
    hydrogen_atoms = 14,
    other_names = ['14_diethylbenzene','14-diethylbenzene','14 diethylbenzene','14diethylbenzene',
                   '1,4_diethylbenzene','1,4-diethylbenzene','1,4 diethylbenzene','1,4diethylbenzene',
                   'p_diethylbenzene','p-diethylbenzene','p diethylbenzene','pdiethylbenzene'],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_tetramethylbenzene]=dict(
    chemical_formula = "c6h2ch3ch3ch3ch3",
    molecular_mass = 134.22,
    carbon_atoms = 10,
    hydrogen_atoms = 14,
    other_names = ['tetramethylbenzene','tetramethylbenzeen'],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_1234_tetramethylbenzene]=dict(
    chemical_formula = "",
    molecular_mass = 134.22,
    carbon_atoms = 10,
    hydrogen_atoms = 14,
    other_names = ['1234_tetramethylbenzene','1234-tetramethylbenzene','1234 tetramethylbenzene',
                   '1234tetramethylbenzene','1,2,3,4_tetramethylbenzene','1,2,3,4-tetramethylbenzene',
                   '1,2,3,4 tetramethylbenzene','1,2,3,4tetramethylbenzene','prehnitene'],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_1245_tetramethylbenzene]=dict(
    chemical_formula = "",
    molecular_mass = 134.22,
    carbon_atoms = 10,
    hydrogen_atoms = 14,
    other_names = ['1245_tetramethylbenzene','1245-tetramethylbenzene','1245 tetramethylbenzene',
                   '1245tetramethylbenzene','1,2,4,5_tetramethylbenzene','1,2,4,5-tetramethylbenzene',
                   '1,2,4,5 tetramethylbenzene','1,2,4,5tetramethylbenzene','durene'],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_1235_tetramethylbenzene]=dict(
    chemical_formula = "",
    molecular_mass = 134.22,
    carbon_atoms = 10,
    hydrogen_atoms = 14,
    other_names = ['1235_tetramethylbenzene','1235-tetramethylbenzene','1235 tetramethylbenzene',
                   '1235tetramethylbenzene','1,2,3,5_tetramethylbenzene','1,2,3,5-tetramethylbenzene',
                   '1,2,3,5 tetramethylbenzene','1,2,3,5tetramethylbenzene','isodurene'],
    standard_unit = names.unit_microgperl,
)


properties_contaminants[names.name_methylindene]=dict(
    chemical_formula = "c9h7ch3",
    molecular_mass = 130.1864,
    carbon_atoms = 10,
    hydrogen_atoms = 10,
    other_names = ['methylindene','methyl-indene'],
    standard_unit = names.unit_microgperl,
)


properties_contaminants[names.name_1_methylindene]=dict(
    chemical_formula = "c9h7ch3",
    molecular_mass = 130.1864,
    carbon_atoms = 10,
    hydrogen_atoms = 10,
    other_names = ['1_methylindene','1-methylindene','1 methylindene','1methylindene',
                   '1_methyl-indene','1-methyl-indene','1 methyl-indene','1methyl-indene',
                   '1_methyl-1h-indene','1-methyl-1h-indene','1 methyl-1h-indene','1methyl-1h-indene',
                   'alpha_methylindene','alpha-methylindene','alpha methylindene','alphamethylindene',
                   ],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_2_methylindene]=dict(
    chemical_formula = "c9h7ch3",
    molecular_mass = 130.1864,
    carbon_atoms = 10,
    hydrogen_atoms = 10,
    other_names = ['2_methylindene','2-methylindene','2 methylindene','2methylindene',
                   '2_methyl-indene','2-methyl-indene','2 methyl-indene','2methyl-indene',
                   '2_methyl-1h-indene','2-methyl-1h-indene','2 methyl-1h-indene','2methyl-1h-indene',
                   ],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_methylnaphthalene]=dict(
    chemical_formula = "c10h7ch3",
    molecular_mass = 142.2,
    carbon_atoms = 11,
    hydrogen_atoms = 10,
    other_names = ['methylnaphthalene','methyl-naphthalene','methyl-naphtalene','methylnaphtalene'],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_1_methylnaphthalene]=dict(
    chemical_formula = "c10h7ch3",
    molecular_mass = 142.2,
    carbon_atoms = 11,
    hydrogen_atoms = 10,
    other_names = ['1_methylnaphthalene','1-methylnaphthalene','1 methylnaphthalene',
                   '1methylnaphthalene','alpha_methylnaphthalene','alpha-methylnaphthalene',
                   'alpha methylnaphthalene','alphamethylnaphthalene','methyl-1-naphthalene',
                   'methyl-1-naphtalene','1_methylnaphtalene','1-methylnaphtalene',
                   '1 methylnaphtalene','1methylnaphtalene','alpha_methylnaphtalene',
                   'alpha-methylnaphtalene','alpha methylnaphtalene','alphamethylnaphtalene'],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_2_methylnaphthalene]=dict(
    chemical_formula = "c10h7ch3",
    molecular_mass = 142.2,
    carbon_atoms = 11,
    hydrogen_atoms = 10,
    other_names = ['2_methylnaphthalene','2-methylnaphthalene','2 methylnaphthalene','2methylnaphthalene',
                   'beta_methylnaphthalene','beta-methylnaphthalene','beta methylnaphthalene','betamethylnaphthalene',
                   'methyl-2-naphthalene','methyl-2-naphtalene',
                   '2_methylnaphtalene','2-methylnaphtalene','2 methylnaphtalene','2methylnaphtalene'
                   'beta_methylnaphtalene','beta-methylnaphtalene','beta methylnaphtalene','betamethylnaphtalene'
                   ],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_ethylnaphthalene]=dict(
    chemical_formula = "c10h7c2h5",
    molecular_mass = 156.22,
    carbon_atoms = 12,
    hydrogen_atoms = 12,
    other_names = ['ethylnaphthalene','ethyl-naphthalene','ethylnaphtalene','ethyl-naphtalene'],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_1_ethylnaphthalene]=dict(
    chemical_formula = "c10h7c2h5",
    molecular_mass = 156.22,
    carbon_atoms = 12,
    hydrogen_atoms = 12,
    other_names = ['1_ethylnaphthalene','1-ethylnaphthalene','1 ethylnaphthalene','1ethylnaphthalene',
                   'alpha_ethylnaphthalene','alpha-ethylnaphthalene','alpha ethylnaphthalene','alphaethylnaphthalene',
                   '1_ethylnaphtalene','1-ethylnaphtalene','1 ethylnaphtalene','1ethylnaphtalene',
                   'alpha_ethylnaphtalene','alpha-ethylnaphtalene','alpha ethylnaphtalene','alphaethylnaphtalene',
                   ],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_2_ethylnaphthalene]=dict(
    chemical_formula = "c10h7c2h5",
    molecular_mass = 156.22,
    carbon_atoms = 12,
    hydrogen_atoms = 12,
    other_names = ['2_ethylnaphthalene','2-ethylnaphthalene','2 ethylnaphthalene',
                   '2ethylnaphthalene','beta_ethylnaphthalene','beta-ethylnaphthalene',
                   'beta ethylnaphthalene','betaethylnaphthalene','2_ethylnaphtalene',
                   '2-ethylnaphtalene','2 ethylnaphtalene','2ethylnaphtalene','beta_ethylnaphtalene',
                   'beta-ethylnaphtalene','beta ethylnaphtalene','betaethylnaphtalene'],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_dimethylnaphthalene]=dict(
    chemical_formula = "c10h7c2h5",
    molecular_mass = 156.22,
    carbon_atoms = 12,
    hydrogen_atoms = 12,
    other_names = ['dimethylnaphthalene','dimethyl-naphthalene','dimethyl-naphtalene',
                   'dimethylnaphtalene'],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_12_dimethylnaphthalene]=dict(
    chemical_formula = "c10h7c2h5",
    molecular_mass = 156.22,
    carbon_atoms = 12,
    hydrogen_atoms = 12,
    other_names = ['12_dimethylnaphthalene','12-dimethylnaphthalene','12 dimethylnaphthalene',
                   '12dimethylnaphthalene','1,2_dimethylnaphthalene','1,2-dimethylnaphthalene',
                   '1,2 dimethylnaphthalene','1,2dimethylnaphthalene',
                   '12_dimethylnaphtalene','12-dimethylnaphtalene','12 dimethylnaphtalene',
                   '12dimethylnaphtalene','1,2_dimethylnaphtalene','1,2-dimethylnaphtalene',
                   '1,2 dimethylnaphtalene','1,2dimethylnaphtalene'],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_13_dimethylnaphthalene]=dict(
    chemical_formula = "c10h7c2h5",
    molecular_mass = 156.22,
    carbon_atoms = 12,
    hydrogen_atoms = 12,
    other_names = ['13_dimethylnaphthalene','13-dimethylnaphthalene','13 dimethylnaphthalene',
                   '13dimethylnaphthalene','1,3_dimethylnaphthalene','1,3-dimethylnaphthalene',
                   '1,3 dimethylnaphthalene','1,3dimethylnaphthalene',
                   '13_dimethylnaphtalene','13-dimethylnaphtalene','13 dimethylnaphtalene',
                   '13dimethylnaphtalene','1,3_dimethylnaphtalene','1,3-dimethylnaphtalene',
                   '1,3 dimethylnaphtalene','1,3dimethylnaphtalene'],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_14_dimethylnaphthalene]=dict(
    chemical_formula = "c10h7c2h5",
    molecular_mass = 156.22,
    carbon_atoms = 12,
    hydrogen_atoms = 12,
    other_names = ['14_dimethylnaphthalene','14-dimethylnaphthalene','14 dimethylnaphthalene',
                   '14dimethylnaphthalene','1,4_dimethylnaphthalene','1,4-dimethylnaphthalene',
                   '1,4 dimethylnaphthalene','1,4dimethylnaphthalene',
                   '14_dimethylnaphtalene','14-dimethylnaphtalene','14 dimethylnaphtalene',
                   '14dimethylnaphtalene','1,4_dimethylnaphtalene','1,4-dimethylnaphtalene',
                   '1,4 dimethylnaphtalene','1,4dimethylnaphtalene'],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_15_dimethylnaphthalene]=dict(
    chemical_formula = "c10h7c2h5",
    molecular_mass = 156.22,
    carbon_atoms = 12,
    hydrogen_atoms = 12,
    other_names = ['15_dimethylnaphthalene','15-dimethylnaphthalene','15 dimethylnaphthalene',
                   '15dimethylnaphthalene','1,5_dimethylnaphthalene','1,5-dimethylnaphthalene',
                   '1,5 dimethylnaphthalene','1,5dimethylnaphthalene',
                   '15_dimethylnaphtalene','15-dimethylnaphtalene','15 dimethylnaphtalene',
                   '15dimethylnaphtalene','1,5_dimethylnaphtalene','1,5-dimethylnaphtalene',
                   '1,5 dimethylnaphtalene','1,5dimethylnaphtalene'],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_16_dimethylnaphthalene]=dict(
    chemical_formula = "c10h7c2h5",
    molecular_mass = 156.22,
    carbon_atoms = 12,
    hydrogen_atoms = 12,
    other_names = ['16_dimethylnaphthalene','16-dimethylnaphthalene','16 dimethylnaphthalene',
                   '16dimethylnaphthalene','1,6_dimethylnaphthalene','1,6-dimethylnaphthalene',
                   '1,6 dimethylnaphthalene','1,6dimethylnaphthalene',
                   '16_dimethylnaphtalene','16-dimethylnaphtalene','16 dimethylnaphtalene',
                   '16dimethylnaphtalene','1,6_dimethylnaphtalene','1,6-dimethylnaphtalene',
                   '1,6 dimethylnaphtalene','1,6dimethylnaphtalene'],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_17_dimethylnaphthalene]=dict(
    chemical_formula = "c10h7c2h5",
    molecular_mass = 156.22,
    carbon_atoms = 12,
    hydrogen_atoms = 12,
    other_names = ['17_dimethylnaphthalene','17-dimethylnaphthalene','17 dimethylnaphthalene',
                   '17dimethylnaphthalene','1,7_dimethylnaphthalene','1,7-dimethylnaphthalene',
                   '1,7 dimethylnaphthalene','1,7dimethylnaphthalene'
                   '17_dimethylnaphtalene','17-dimethylnaphtalene','17 dimethylnaphtalene',
                   '17dimethylnaphtalene','1,7_dimethylnaphtalene','1,7-dimethylnaphtalene',
                   '1,7 dimethylnaphtalene','1,7dimethylnaphtalene'],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_18_dimethylnaphthalene]=dict(
    chemical_formula = "c10h7c2h5",
    molecular_mass = 156.22,
    carbon_atoms = 12,
    hydrogen_atoms = 12,
    other_names = ['18_dimethylnaphthalene','18-dimethylnaphthalene','18 dimethylnaphthalene',
                   '18dimethylnaphthalene','1,8_dimethylnaphthalene','1,8-dimethylnaphthalene',
                   '1,8 dimethylnaphthalene','1,8dimethylnaphthalene',
                   '18_dimethylnaphtalene','18-dimethylnaphtalene','18 dimethylnaphtalene',
                   '18dimethylnaphtalene','1,8_dimethylnaphtalene','1,8-dimethylnaphtalene',
                   '1,8 dimethylnaphtalene','1,8dimethylnaphtalene'],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_23_dimethylnaphthalene]=dict(
    chemical_formula = "c10h7c2h5",
    molecular_mass = 156.22,
    carbon_atoms = 12,
    hydrogen_atoms = 12,
    other_names = ['23_dimethylnaphthalene','23-dimethylnaphthalene','23 dimethylnaphthalene',
                   '23dimethylnaphthalene','2,3_dimethylnaphthalene','2,3-dimethylnaphthalene',
                   '2,3 dimethylnaphthalene','2,3dimethylnaphthalene',
                   '23_dimethylnaphtalene','23-dimethylnaphtalene','23 dimethylnaphtalene',
                   '23dimethylnaphtalene','2,3_dimethylnaphtalene','2,3-dimethylnaphtalene',
                   '2,3 dimethylnaphtalene','2,3dimethylnaphtalene'],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_26_dimethylnaphthalene]=dict(
    chemical_formula = "c10h7c2h5",
    molecular_mass = 156.22,
    carbon_atoms = 12,
    hydrogen_atoms = 12,
    other_names = ['26_dimethylnaphthalene','26-dimethylnaphthalene','26 dimethylnaphthalene',
                   '26dimethylnaphthalene', '2,6_dimethylnaphthalene','2,6-dimethylnaphthalene',
                   '2,6 dimethylnaphthalene','2,6dimethylnaphthalene','26_dimethylnaphtalene',
                   '26-dimethylnaphtalene','26 dimethylnaphtalene','26dimethylnaphtalene',
                   '2,6_dimethylnaphtalene','2,6-dimethylnaphtalene','2,6 dimethylnaphtalene',
                   '2,6dimethylnaphtalene'],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_27_dimethylnaphthalene]=dict(
    chemical_formula = "c10h7c2h5",
    molecular_mass = 156.22,
    carbon_atoms = 12,
    hydrogen_atoms = 12,
    other_names = ['27_dimethylnaphthalene','27-dimethylnaphthalene','27 dimethylnaphthalene',
                   '27dimethylnaphthalene','2,7_dimethylnaphthalene','2,7-dimethylnaphthalene',
                   '2,7 dimethylnaphthalene','2,7dimethylnaphthalene'
                   '27_dimethylnaphtalene','27-dimethylnaphtalene','27 dimethylnaphtalene',
                   '27dimethylnaphtalene','2,7_dimethylnaphtalene','2,7-dimethylnaphtalene',
                   '2,7 dimethylnaphtalene','2,7dimethylnaphtalene'],
    standard_unit = names.unit_microgperl,
)


###############################################################################
###############################################################################
###############################################################################

contaminants_analysis = dict()
contaminants_analysis[names.name_total_contaminants] = dict(
    other_names = ["sum_contaminants","sum-contaminants","sum contaminants","sumcontaminants",
                   "total_contaminants","total-contaminants","total contaminants","totalcontaminants",
                   "contaminants concentration","contaminants_concentration","contaminants-concentration",
                   "contaminantsconcentration","contaminants"],
    standard_unit = names.unit_microgperl,
    )
contaminants_analysis[names.name_total_BTEX] = dict(
    other_names = ["sum_BTEX","sum-BTEX","sum BTEX","sumBTEX",
                   "total_BTEX","total-BTEX","total BTEX","totalBTEX",
                   "concentration -BTEX","concentration-BTEX","concentration BTEX",
                   "concentrationBTEX"],
    standard_unit = names.unit_microgperl,
    )
contaminants_analysis[names.name_total_BTEXIIN] = dict(
    other_names = ["sum_BTEXIIN","sum-BTEXIIN","sum BTEXIIN","sumBTEXIIN",
                   "total_BTEXIIN","total-BTEXIIN","total BTEXIIN","totalBTEXIIN",
                   "concentration -BTEXIIN","concentration-BTEXIIN","concentration BTEXIIN",
                   "concentrationBTEXIIN"],
    standard_unit = names.unit_microgperl,
    )
contaminants_analysis[names.name_total_oxidators] = dict(
    other_names = ["total_oxidators"]
    )
contaminants_analysis[names.name_total_reductors] = dict(
    other_names = ["total_reductors"]
    )
contaminants_analysis[names.name_e_balance] = dict(
    other_names = ["e_balance"]
    )

contaminants_analysis[names.name_na_traffic_light] = dict(
    other_names = ["na_traffic_light"]
    )

contaminants_analysis[names.name_intervention_traffic] = dict(
    other_names = ["intervention_traffic"]
    )

contaminants_analysis[names.name_intervention_number] = dict(
    other_names = ["intervention_number"]
    )

contaminants_analysis[names.name_intervention_contaminants] = dict(
    other_names = ["intervention_contaminants"]
    )

contaminants_analysis[names.name_NP_avail] = dict(
    other_names = ["NP_avail"]
    )

### List with all quantities of particular data type in standard names:
contaminants = list(properties_contaminants.keys())
contaminants_analysis_quantities = list(contaminants_analysis.keys())

### -----------------------------------------------------------------------------
### dictionaries with specific selection lists of quantities of particular type

contaminant_groups = dict(
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
    all_cont = list(properties_contaminants.keys())
)
