"""Specifications of petroleum hydrocarbon related contaminants.

List of (PAH) contamiants measured in groundwater samples useful
for biodegredation and bioremediation analysis

@author: A. Zech
"""

import mibiscreen.data.settings.standard_names as names

properties_contaminants = dict()

###############################################################################
### MAHs

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
    other_names = ["xylene","xyleen",
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
    other_names =  ["o-xylene","o xylene","o_xylene","oxylene",
                    "o-xyleen","o xyleen","o_xyleen","oxyleen"],
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
###############################################################################
### PAHs

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

properties_contaminants[names.name_naphthalene_VOC]=dict(
    chemical_formula = "c10h8",
    molecular_mass = 128.,
    carbon_atoms = 10,
    hydrogen_atoms = 8,
    # factor_stoichiometry = 48.,
    # thresholds_for_intervention_NL = 70.,
    other_names = ['naphthalene_voc',"naphthalene_voc","naphthalenevoc","naphthalene-voc","naphthalene voc",
                   "naphtalene_voc","naphtalenevoc","naphtalene-voc","naphtalenevoc",
                   "naphthaline_voc","naphthalinevoc","naphthaline-voc","naphthaline voc",
                   "naphtaline_voc","naphtalinevoc","naphtaline-voc","naphtaline voc",
                   "naphthaleen_voc","naphthaleenvoc","naphthaleen-voc","naphthaleen voc",
                   "naphtaleen_voc","naphtaleenvoc","naphtaleen-voc","naphtaleen voc",
                   "c10h8_voc"],
    standard_unit = names.unit_microgperl,
    )

properties_contaminants[names.name_naphthalene_PAH]=dict(
    chemical_formula = "c10h8",
    molecular_mass = 128.,
    carbon_atoms = 10,
    hydrogen_atoms = 8,
    # factor_stoichiometry = 48.,
    # thresholds_for_intervention_NL = 70.,
    other_names = ["naphthalene_pah","naphthalenepah","naphthalene-pah","naphthalene pah",
                   "naphtalene_pah","naphtalenepah","naphtalene-pah","naphtalenepah",
                   "naphthaline_pah","naphthalinepah","naphthaline-pah","naphthaline pah",
                   "naphtaline_pah","naphtalinepah","naphtaline-pah","naphtaline pah",
                   "naphthaleen_pah","naphthaleenpah","naphthaleen-pah","naphthaleen pah",
                   "naphtaleen_pah","naphtaleenpah","naphtaleen-pah","naphtaleen pah",
                   "c10h8_pah"],
    standard_unit = names.unit_microgperl,
    )

properties_contaminants[names.name_naphthalene] = dict(
    chemical_formula = "C10H8",
    molecular_mass = 128.0,
    carbon_atoms = 10,
    hydrogen_atoms = 8,
    other_names = ["naphthalene","naphthaleen","naphthaline",
                   "naphtaline","naphtalene","naphtaleen","C10H8"],
    standard_unit = names.unit_microgperl,
)

# New ones:

properties_contaminants[names.name_acenaphthylene] = dict(
    chemical_formula = "C12H8",
    molecular_mass = 152.192,
    carbon_atoms = 12,
    hydrogen_atoms = 8,
    other_names = ["acenaphthylene","cyclopenta[de]naphthalene","C12H8"],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_acenaphthene] = dict(
    chemical_formula = "C12H10",
    molecular_mass = 154.212,  # approximate
    carbon_atoms = 12,
    hydrogen_atoms = 10,
    other_names = ["acenaphthene","acenaphthene (C12H10)","C12H10"],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_fluorene] = dict(
    chemical_formula = "C13H10",
    molecular_mass = 166.22,
    carbon_atoms = 13,
    hydrogen_atoms = 10,
    other_names = ["fluorene","C13H10"],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_phenanthrene] = dict(
    chemical_formula = "C14H10",
    molecular_mass = 178.226,
    carbon_atoms = 14,
    hydrogen_atoms = 10,
    other_names = ["phenanthrene","C14H10"],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_anthracene] = dict(
    chemical_formula = "C14H10",
    molecular_mass = 178.226,
    carbon_atoms = 14,
    hydrogen_atoms = 10,
    other_names = ["anthracene","C14H10"],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_fluoranthene] = dict(
    chemical_formula = "C16H10",
    molecular_mass = 202.26,
    carbon_atoms = 16,
    hydrogen_atoms = 10,
    other_names = ["fluoranthene","C16H10"],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_pyrene] = dict(
    chemical_formula = "C16H10",
    molecular_mass = 202.26,
    carbon_atoms = 16,
    hydrogen_atoms = 10,
    other_names = ["pyrene","C16H10"],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_chrysene] = dict(
    chemical_formula = "C18H12",
    molecular_mass = 228.29,
    carbon_atoms = 18,
    hydrogen_atoms = 12,
    other_names = ["chrysene","C18H12"],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_benzo_a_anthracene] = dict(
    chemical_formula = "C18H12",
    molecular_mass = 228.29,
    carbon_atoms = 18,
    hydrogen_atoms = 12,
    other_names = ["benzo[a]anthracene","benzo(a)anthracene","benzoaanthracene",
                   "benzo-a-anthracene","C18H12","BaA"],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_benzo_b_fluoranthene] = dict(
    chemical_formula = "C20H12",
    molecular_mass = 252.31,
    carbon_atoms = 20,
    hydrogen_atoms = 12,
    other_names = ["benzo[b]fluoranthene","benzo(b)fluoranthene",
                   "benzobfluoranthene","benzo-b-fluoranthene","BbF","C20H12"],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_benzo_k_fluoranthene] = dict(
    chemical_formula = "C20H12",
    molecular_mass = 252.31,
    carbon_atoms = 20,
    hydrogen_atoms = 12,
    other_names = ["benzo[k]fluoranthene","benzo(k)fluoranthene"
                   "benzokfluoranthene","benzo-k-fluoranthene","BkF","C20H12"],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_benzo_a_pyrene] = dict(
    chemical_formula = "C20H12",
    molecular_mass = 252.31,
    carbon_atoms = 20,
    hydrogen_atoms = 12,
    other_names = ["benzo[a]pyrene","benzo(a)pyrene","benzoapyrene",
                   "benzo-a-pyrene","BaP","C20H12"],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_dibenz_ah_anthracene] = dict(
    chemical_formula = "C22H14",
    molecular_mass = 278.33,
    carbon_atoms = 22,
    hydrogen_atoms = 14,
    other_names = ["dibenz[a,h]anthracene","dibenz(a,h)anthracene","dibenzahanthracene","dibenz-a,h-anthracene",
                   "dibenz-a-h-anthracene","DBahA","C22H14"],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_benzo_ghi_perylene] = dict(
    chemical_formula = "C22H12",
    molecular_mass = 276.33,
    carbon_atoms = 22,
    hydrogen_atoms = 12,
    other_names = ["benzo[ghi]perylene","benzo(ghi)perylene","benzoghiperylene","benzo-ghi-perylene",
                   "C22H12","BghiP"],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_indeno_123cd_pyrene] = dict(
    chemical_formula = "C22H12",
    molecular_mass = 276.33,  # from data: 276.33 :contentReference[oaicite:0]{index=0}
    carbon_atoms = 22,
    hydrogen_atoms = 12,
    other_names = ["indeno[1,2,3-cd]pyrene","indeno(1,2,3‑cd)pyrene",
                   "indeno1,2,3‑cdpyrene","indeno-1,2,3‑cd-pyrene",
                   "C22H12"],
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

### Alkylphenols
properties_contaminants[names.name_phenol] = dict(
    chemical_formula = "C6H6O",
    molecular_mass = 94.11,
    carbon_atoms = 6,
    hydrogen_atoms = 6,
    other_names = ['phenol', 'hydroxybenzene', 'benzenol'],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_thymol] = dict(
    chemical_formula = "C10H14O",
    molecular_mass = 150.22,
    carbon_atoms = 10,
    hydrogen_atoms = 14,
    other_names = ['thymol', '2_isopropyl_5_methylphenol', '5_methyl_2_isopropylphenol'],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_cresol] = dict(
    chemical_formula = None,
    molecular_mass = None,
    carbon_atoms = None,
    hydrogen_atoms = None,
    other_names = ['cresol', 'methylphenol', 'hydroxytoluene'],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_m_cresol] = dict(
    chemical_formula = "C7H8O",
    molecular_mass = 108.14,
    carbon_atoms = 7,
    hydrogen_atoms = 8,
    other_names = ['m-cresol','m cresol','mcresol','m_cresol', 'methylphenol', '3_methylphenol', '3-methylphenol'],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_o_cresol] = dict(
    chemical_formula = "C7H8O",
    molecular_mass = 108.14,
    carbon_atoms = 7,
    hydrogen_atoms = 8,
    other_names = ['o-cresol','o cresol','ocresol''o_cresol', '2_methylphenol', '2-methylphenol'],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_p_cresol] = dict(
    chemical_formula = "C7H8O",
    molecular_mass = 108.14,
    carbon_atoms = 7,
    hydrogen_atoms = 8,
    other_names = ['p-cresol','p cresol','pcresol','p_cresol', '4_methylphenol', '4-methylphenol'],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_2_ethylphenol] = dict(
    chemical_formula = "C8H10O",
    molecular_mass = 122.16,
    carbon_atoms = 8,
    hydrogen_atoms = 10,
    other_names = ['2_ethylphenol', '2-ethylphenol'],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_3_ethylphenol] = dict(
    chemical_formula = "C8H10O",
    molecular_mass = 122.16,
    carbon_atoms = 8,
    hydrogen_atoms = 10,
    other_names = ['3_ethylphenol', '3-ethylphenol'],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_23_dimethylphenol] = dict(
    chemical_formula = "C8H10O",
    molecular_mass = 122.16,
    carbon_atoms = 8,
    hydrogen_atoms = 10,
    other_names = [
        '23_dimethylphenol','23-dimethylphenol','23 dimethylphenol','23dimethylphenol',
        '2,3_dimethylphenol','2,3-dimethylphenol','2,3 dimethylphenol','2,3dimethylphenol',
        '23_dimethylphenol','23-dimethylphenol','23 dimethylphenol','23dimethylphenol',
        '2,3_dimethylphenol','2,3-dimethylphenol','2,3 dimethylphenol','2,3dimethylphenol'
    ],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_24_dimethylphenol] = dict(
    chemical_formula = "C8H10O",
    molecular_mass = 122.16,
    carbon_atoms = 8,
    hydrogen_atoms = 10,
    other_names = [
        '24_dimethylphenol','24-dimethylphenol','24 dimethylphenol','24dimethylphenol',
        '2,4_dimethylphenol','2,4-dimethylphenol','2,4 dimethylphenol','2,4dimethylphenol',
        '24_dimethylphenol','24-dimethylphenol','24 dimethylphenol','24dimethylphenol',
        '2,4_dimethylphenol','2,4-dimethylphenol','2,4 dimethylphenol','2,4dimethylphenol'
    ],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_25_dimethylphenol] = dict(
    chemical_formula = "C8H10O",
    molecular_mass = 122.16,
    carbon_atoms = 8,
    hydrogen_atoms = 10,
    other_names = [
        '25_dimethylphenol','25-dimethylphenol','25 dimethylphenol','25dimethylphenol',
        '2,5_dimethylphenol','2,5-dimethylphenol','2,5 dimethylphenol','2,5dimethylphenol',
        '25_dimethylphenol','25-dimethylphenol','25 dimethylphenol','25dimethylphenol',
        '2,5_dimethylphenol','2,5-dimethylphenol','2,5 dimethylphenol','2,5dimethylphenol'
    ],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_26_dimethylphenol26] = dict(
    chemical_formula = "C8H10O",
    molecular_mass = 122.16,
    carbon_atoms = 8,
    hydrogen_atoms = 10,
    other_names = [
        '26_dimethylphenol','26-dimethylphenol','26 dimethylphenol','26dimethylphenol',
        '2,6_dimethylphenol','2,6-dimethylphenol','2,6 dimethylphenol','2,6dimethylphenol',
        '26_dimethylphenol','26-dimethylphenol','26 dimethylphenol','26dimethylphenol',
        '2,6_dimethylphenol','2,6-dimethylphenol','2,6 dimethylphenol','2,6dimethylphenol'
    ],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_34_dimethylphenol] = dict(
    chemical_formula = "C8H10O",
    molecular_mass = 122.16,
    carbon_atoms = 8,
    hydrogen_atoms = 10,
    other_names = [
        '34_dimethylphenol','34-dimethylphenol','34 dimethylphenol','34dimethylphenol',
        '3,4_dimethylphenol','3,4-dimethylphenol','3,4 dimethylphenol','3,4dimethylphenol',
        '34_dimethylphenol','34-dimethylphenol','34 dimethylphenol','34dimethylphenol',
        '3,4_dimethylphenol','3,4-dimethylphenol','3,4 dimethylphenol','3,4dimethylphenol'
    ],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_35_dimethylphenol] = dict(
    chemical_formula = "C8H10O",
    molecular_mass = 122.16,
    carbon_atoms = 8,
    hydrogen_atoms = 10,
    other_names = [
        '35_dimethylphenol','35-dimethylphenol','35 dimethylphenol','35dimethylphenol',
        '3,5_dimethylphenol','3,5-dimethylphenol','3,5 dimethylphenol','3,5dimethylphenol',
        '35_dimethylphenol','35-dimethylphenol','35 dimethylphenol','35dimethylphenol',
        '3,5_dimethylphenol','3,5-dimethylphenol','3,5 dimethylphenol','3,5dimethylphenol'
    ],
    standard_unit = names.unit_microgperl,
)


properties_contaminants[names.name_235_trimethylphenol] = dict(
    chemical_formula = "C9H12O",
    molecular_mass = 138.19,
    carbon_atoms = 9,
    hydrogen_atoms = 12,
    other_names = [
        '235_trimethylphenol', '235-trimethylphenol', '235 trimethylphenol', '235trimethylphenol',
        '2,3,5_trimethylphenol', '2,3,5-trimethylphenol', '2,3,5 trimethylphenol', '2,3,5trimethylphenol'
    ],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_345_trimethylphenol] = dict(
    chemical_formula = "C9H12O",
    molecular_mass = 138.19,
    carbon_atoms = 9,
    hydrogen_atoms = 12,
    other_names = [
        '345_trimethylphenol', '345-trimethylphenol', '345 trimethylphenol', '345trimethylphenol',
        '3,4,5_trimethylphenol', '3,4,5-trimethylphenol', '3,4,5 trimethylphenol', '3,4,5trimethylphenol'
    ],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_4_ethylphenol] = dict(
    chemical_formula = "C8H10O",
    molecular_mass = 122.16,
    carbon_atoms = 8,
    hydrogen_atoms = 10,
    other_names = [
        '4_ethylphenol', '4-ethylphenol', '4 ethylphenol', '4ethylphenol',
        'p_ethylphenol', 'p-ethylphenol', 'p ethylphenol', 'pethylphenol'
    ],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_2_isopropylphenol] = dict(
    chemical_formula = "C9H12O",
    molecular_mass = 136.19,
    carbon_atoms = 9,
    hydrogen_atoms = 12,
    other_names = [
        '2_isopropylphenol', '2-isopropylphenol', '2 isopropylphenol', '2isopropylphenol',
        'o_isopropylphenol', 'o-isopropylphenol', 'o isopropylphenol', 'oisopropylphenol'
    ],
    standard_unit = names.unit_microgperl,
)

properties_contaminants[names.name_ptertbutylphenol] = dict(
    chemical_formula = "C10H14O",
    molecular_mass = 150.22,
    carbon_atoms = 10,
    hydrogen_atoms = 14,
    other_names = [
        'p_[tert]butylphenol', 'p-(tert)butylphenol', 'p tert butyl phenol', 'ptertbutylphenol',
        'para_tert_butyl_phenol', 'para-(tert)-butyl-phenol', 'para tert butyl phenol'
    ],
    standard_unit = names.unit_microgperl,
)


###############################################################################
###############################################################################
###############################################################################


contaminants_analysis = dict()

contaminants_analysis[names.name_PAH_total_16] = dict(
    other_names = ['pah_total_16','pah_total 16','pah_total16','pah_total-16',
                   'pah total_16','pah total 16','pah total16','pah total-16',
                   'pahtotal_16','pahtotal 16','pahtotal16','pahtotal-16'
                   'pah-total_16','pah-total 16','pah-total16','pah-total-16',
                   'pah_16','pah 16','pah16','pah-16',
                   'total_pah_16','total_pah 16','total_pah16','total_pah-16',
                   'total pah_16','total pah 16','total pah16','total pah-16',
                   'totalpah_16','totalpah 16','totalpah16','totalpah-16',
                   'total-pah_16','total-pah 16','total-pah16','total-pah-16',
                   ],
    standard_unit = names.unit_microgperl,
    )

contaminants_analysis[names.name_PAH_total_10] = dict(
    other_names = ['pah_total_10','pah_total 10','pah_total10','pah_total-10',
                   'pah total_10','pah total 10','pah total10','pah total-10',
                   'pahtotal_10','pahtotal 10','pahtotal10','pahtotal-10'
                   'pah-total_10','pah-total 10','pah-total10','pah-total-10',
                   'pah_10','pah 10','pah10','pah-10',
                   'total_pah_10','total_pah 10','total_pah10','total_pah-10',
                   'total pah_10','total pah 10','total pah10','total pah-10',
                   'totalpah_10','totalpah 10','totalpah10','totalpah-10',
                   'total-pah_10','total-pah 10','total-pah10','total-pah-10',
                   ],
    standard_unit = names.unit_microgperl,
    )

contaminants_analysis[names.name_fraction_C10_C12] = dict(
    other_names = [
        'fraction_c10-c12','fraction c10-c12','fraction c10_c12',
        'c10-c12 fraction','c10_c12 fraction',
        'c10 to c12','c10_c12','c10–c12','c10–c12 fraction',
    ],
    standard_unit = names.unit_microgperl,
)

contaminants_analysis[names.name_fraction_C12_C22] = dict(
    other_names = [
        'fraction_c12-c22','fraction c12-c22','fraction c12_c22',
        'c12-c22 fraction','c12_c22 fraction',
        'c12 to c22','c12_c22','c12–c22','c12–c22 fraction',
    ],
    standard_unit = names.unit_microgperl,
)

contaminants_analysis[names.name_fraction_C22_C30] = dict(
    other_names = [
        'fraction_c22-c30','fraction c22-c30','fraction c22_c30',
        'c22-c30 fraction','c22_c30 fraction',
        'c22 to c30','c22_c30','c22–c30','c22–c30 fraction',
    ],
    standard_unit = names.unit_microgperl,
)


contaminants_analysis[names.name_fraction_C30_C40] = dict(
    other_names = [
        'fraction_c30-c40','fraction c30-c40','fraction c30_c40',
        'c30-c40 fraction','c30_c40 fraction',
        'c30 to c40','c30_c40','c30–c40','c30–c40 fraction',
    ],
    standard_unit = names.unit_microgperl,
)

contaminants_analysis[names.name_total_C10_C40] = dict(
    other_names = [
        'total_c10-c40','total c10-c40','total c10_c40',
        'c10-c40 total','c10_c40 total',
        'c10 to c40','c10_c40','c10–c40','c10–c40 total',
        'c10-c40','c10_c40',
    ],
    standard_unit = names.unit_microgperl,
)

contaminants_analysis[names.name_total_c2_alkylphenols] = dict(
    other_names = [
        'c2-alkylphenols_total',"c2_alkylphenols_total","c2alkylphenols_total", "c2 alkylphenols_total",
        "c2-alkylphenols-total","c2_alkylphenols-total","c2alkylphenols-total", "c2 alkylphenols-total",
        "c2 alkylphenols total","c2_alkylphenols total","c2alkylphenols total", "c2 alkylphenols total",
        "c2alkylphenolstotal","c2_alkylphenolstotal","c2alkylphenolstotal", "c2 alkylphenolstotal",
        "total_c2_alkylphenols", "total-c2-alkylphenols", "total c2 alkylphenols", "totalc2alkylphenols",
        "alkylphenols_c2_total", "alkylphenols-c2-total", "alkylphenols c2 total", "alkylphenolsc2total",
        "c2_alkylphenols", "c2-alkylphenols", "c2 alkylphenols", "c2alkylphenols",
        "alkylphenols_c2", "alkylphenols-c2", "alkylphenols c2", "alkylphenolsc2"
    ],
    standard_unit = names.unit_microgperl,
)

contaminants_analysis[names.name_total_c3_alkylphenols] = dict(
    other_names = [
        'c3-alkylphenols_total',"c3_alkylphenols_total","c3alkylphenols_total", "c3 alkylphenols_total",
        "c3-alkylphenols-total","c3_alkylphenols-total","c3alkylphenols-total", "c3 alkylphenols-total",
        "c3 alkylphenols total","c3_alkylphenols total","c3alkylphenols total", "c3 alkylphenols total",
        "c3alkylphenolstotal","c3_alkylphenolstotal","c3alkylphenolstotal", "c3 alkylphenolstotal",
        "c3_alkylphenols_total", "c3-alkylphenols-total", "c3 alkylphenols total", "c3alkylphenolstotal",
        "total_c3_alkylphenols", "total-c3-alkylphenols", "total c3 alkylphenols", "totalc3alkylphenols",
        "alkylphenols_c3_total", "alkylphenols-c3-total", "alkylphenols c3 total", "alkylphenolsc3total",
        "c3_alkylphenols", "c3-alkylphenols", "c3 alkylphenols", "c3alkylphenols",
        "alkylphenols_c3", "alkylphenols-c3", "alkylphenols c3", "alkylphenolsc3"
    ],
    standard_unit = names.unit_microgperl,
)

contaminants_analysis[names.name_total_c4_alkylphenols] = dict(
    other_names = [
        'c4-alkylphenols_total',"c4_alkylphenols_total","c4alkylphenols_total", "c4 alkylphenols_total",
        "c4-alkylphenols-total","c4_alkylphenols-total","c4alkylphenols-total", "c4 alkylphenols-total",
        "c4 alkylphenols total","c4_alkylphenols total","c4alkylphenols total", "c4 alkylphenols total",
        "c4alkylphenolstotal","c4_alkylphenolstotal","c4alkylphenolstotal", "c4 alkylphenolstotal",
        "c4_alkylphenols_total", "c4-alkylphenols-total", "c4 alkylphenols total", "c4alkylphenolstotal",
        "total_c4_alkylphenols", "total-c4-alkylphenols", "total c4 alkylphenols", "totalc4alkylphenols",
        "alkylphenols_c4_total", "alkylphenols-c4-total", "alkylphenols c4 total", "alkylphenolsc4total",
        "c4_alkylphenols", "c4-alkylphenols", "c4 alkylphenols", "c4alkylphenols",
        "alkylphenols_c4", "alkylphenols-c4", "alkylphenols c4", "alkylphenolsc4"
    ],
    standard_unit = names.unit_microgperl,
)

contaminants_analysis[names.name_total_contaminants] = dict(
    other_names = ["sum_contaminants","sum-contaminants","sum contaminants","sumcontaminants",
                   "total_contaminants","total-contaminants","total contaminants","totalcontaminants",
                   "contaminants concentration","contaminants_concentration","contaminants-concentration",
                   "contaminantsconcentration","contaminants"],
    standard_unit = names.unit_microgperl,
    )
contaminants_analysis[names.name_total_BTEX] = dict(
    other_names = ["sum_btex","sum-btex","sum btex","sumbtex",
                   "total_btex","total-btex","total btex","totalbtex",
                   "btex_total","btex-total","btex total","btextotal",
                   "concentration -btex","concentration-btex","concentration btex",
                   "concentrationbtex"],
    standard_unit = names.unit_microgperl,
    )
contaminants_analysis[names.name_total_BTEXIIN] = dict(
    other_names = ["sum_btexiin","sum-btexiin","sum btexiin","sumbtexiin",
                   "total_btexiin","total-btexiin","total btexiin","totalbtexiin",
                   "concentration -btexiin","concentration-btexiin","concentration btexiin",
                   "concentrationbtexiin"],
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
    other_names = ["np_avail"]
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
               names.name_naphthalene,
               # names.name_naphthalene_VOC,
               # names.name_naphthalene_PAC,
               ],
    MAH = [names.name_benzene,
           names.name_toluene,
           names.name_ethylbenzene,
           names.name_pm_xylene,
           names.name_o_xylene,
           names.name_xylene,
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
           names.name_diethylbenzene,
           names.name_12_diethylbenzene,
           names.name_13_diethylbenzene,
           names.name_14_diethylbenzene,
           names.name_tetramethylbenzene,
           names.name_1234_tetramethylbenzene,
           names.name_1245_tetramethylbenzene,
           names.name_1235_tetramethylbenzene,
           ],
    PAH = [names.name_indane,
           names.name_indene,
           names.name_naphthalene,
           names.name_naphthalene_VOC,
           names.name_naphthalene_PAH,
           names.name_acenaphthylene,
           names.name_acenaphthene,
           names.name_fluorene,
           names.name_phenanthrene,
           names.name_anthracene,
           names.name_fluoranthene,
           names.name_pyrene,
           names.name_chrysene,
           names.name_benzo_a_anthracene,
           names.name_benzo_b_fluoranthene,
           names.name_benzo_k_fluoranthene,
           names.name_benzo_a_pyrene,
           names.name_dibenz_ah_anthracene,
           names.name_benzo_ghi_perylene,
           names.name_indeno_123cd_pyrene,
           names.name_methylindene,
           names.name_1_methylindene,
           names.name_2_methylindene,
           names.name_methylnaphthalene,
           names.name_1_methylnaphthalene,
           names.name_2_methylnaphthalene,
           names.name_ethylnaphthalene,
           names.name_1_ethylnaphthalene,
           names.name_2_ethylnaphthalene,
           names.name_dimethylnaphthalene,
           names.name_12_dimethylnaphthalene,
           names.name_13_dimethylnaphthalene,
           names.name_14_dimethylnaphthalene,
           names.name_15_dimethylnaphthalene,
           names.name_16_dimethylnaphthalene,
           names.name_17_dimethylnaphthalene,
           names.name_18_dimethylnaphthalene,
           names.name_23_dimethylnaphthalene,
           names.name_26_dimethylnaphthalene,
           names.name_27_dimethylnaphthalene,
           ],
    PAH_total_10 = [#Dutch RIVM defines environmental quality objectives for 10 PAHs
                    names.name_naphthalene,
                    names.name_anthracene,
                    names.name_benzo_a_anthracene,
                    names.name_benzo_a_pyrene,
                    names.name_benzo_b_fluoranthene,
                    names.name_benzo_k_fluoranthene,
                    names.name_chrysene,
                    names.name_dibenz_ah_anthracene,
                    names.name_fluoranthene,
                    names.name_pyrene,
                    ],
    PAH_total_16 = [names.name_naphthalene, #the 16 EPA priority PAHs
                    names.name_acenaphthylene,
                    names.name_acenaphthene,
                    names.name_fluorene,
                    names.name_phenanthrene,
                    names.name_anthracene,
                    names.name_fluoranthene,
                    names.name_pyrene,
                    names.name_benzo_a_anthracene,
                    names.name_chrysene,
                    names.name_benzo_b_fluoranthene,
                    names.name_benzo_k_fluoranthene,
                    names.name_benzo_a_pyrene,
                    names.name_indeno_123cd_pyrene,
                    names.name_dibenz_ah_anthracene,
                    names.name_benzo_ghi_perylene,
                    ],
    all_cont = list(properties_contaminants.keys())
)
