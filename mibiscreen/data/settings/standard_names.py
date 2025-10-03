"""Name specifications of data!

Listed are all standard names of quantities and parameters measured in
groundwater samples useful for biodegredation and bioremediation analysis

@author: A. Zech
"""

### Standard names for units
unit_mgperl = "mg/l"
unit_microgperl  = "ug/l"
unit_millivolt = "mV"
unit_meter = 'm'
unit_microsimpercm = 'uS/cm'
unit_permil = 'permil'
unit_count = 'nr'
unit_date = 'date'
unit_less = ''
unit_mgNperl = "mg/l"
unit_mgPperl = "mg/l"
unit_celsius = 'C'
unit_date = 'date'

### Standard names for settings
name_sample = "sample_nr"
name_observation_well = "obs_well"
name_well_type = "well_type"
name_sample_depth = "depth"
name_aquifer = 'aquifer'
name_date = 'date'

### Standard names for environmental parameters
name_redox = "redoxpot"
name_pH = "pH"
name_temperature = 'temperature'
name_EC = "EC"
#name_Eh = "Eh" #Reduction potential
name_pE = "pE" #Alternative mathematical formulation of redox potential/reduction potential
# In analogy to pε is a measure of the solution activity of hypothetical free electrons,
# pε = −log{e−}, and is related to E via pε = (F/2.3RT)/E

name_DOC = "DOC" # Dissolved Organic Carbon
name_NPOC = "NPOC" # Non-Purgeable Organic Carbon
name_TOC = "TOC" # Total Organic Carbon

name_oxygen = 'oxygen' #o2
name_nitrate = 'nitrate' #no3- -- full nitrate ion
name_nitrateN = 'nitrate_N' #no3-N -- amount of nitrogen (N) within the nitrate ion.
name_sulfate = 'sulfate' #"so4"
name_iron2 = "iron2" #"fe_II"
name_iron3 = "iron3" #"fe_II"
name_manganese2 = 'manganese2' #"mn_II"
name_manganese4 = 'manganese4' #"mn_II"
name_methane = 'methane' #"ch4"
name_nitrite = 'nitrite' #no2 -- full nitrite ion
name_nitriteN = 'nitrite_N' #no2- - amount of nitrogen (N) within the nitrite ion.
name_sulfide = 'sulfide' #"s2min"
name_ammonium = 'ammonium' #"nh4+"
name_phosphate = 'phosphate' # "po4" - orthosphosphate ion, bioavailable form of phosphorus
name_phosphorus = 'phosphorus_total' #P - all phosphorus containing compounds
name_chloride = 'chloride'
name_bromide = 'bromide'
name_fluoride = 'fluoride'
name_sodium = 'sodium'
name_magnesium = 'magnesium'
name_potassium = 'potassium'
name_calcium = 'calcium'
name_acetate = 'acetate'
name_cyanide = 'cyanide_total' # sum of all cyanide species that can potentially release free cyanide

### Standard names for main contaminants
### MAHs - MONOCYCLIC AROMATIC HYDROCARBONS
name_benzene = 'benzene'
name_toluene = 'toluene'
name_ethylbenzene = 'ethylbenzene'
name_pm_xylene = 'pm_xylene'
name_o_xylene = 'o_xylene'
name_xylene = 'xylene'

### Standard names for additional MAH contaminants
name_styrene = 'styrene'
name_isopropylbenzene = 'isopropylbenzene'
name_n_propylbenzene = 'n_propylbenzene'
name_ethyltoluene = 'ethyltoluene'
name_2_ethyltoluene = '2_ethyltoluene'
name_3_ethyltoluene = '3_ethyltoluene'
name_4_ethyltoluene = '4_ethyltoluene'
name_trimethylbenzene = 'trimethylbenzene'
name_123_trimethylbenzene = '123_trimethylbenzene'
name_124_trimethylbenzene = '124_trimethylbenzene'
name_135_trimethylbenzene = '135_trimethylbenzene'
name_4_isopropyltouene = '4_isopropyltouene'
name_diethylbenzene = 'diethylbenzene'
name_12_diethylbenzene = '12_diethylbenzene'
name_13_diethylbenzene = '13_diethylbenzene'
name_14_diethylbenzene = '14_diethylbenzene'
name_tetramethylbenzene = 'tetramethylbenzene'
name_1234_tetramethylbenzene = '1234_tetramethylbenzene'
name_1245_tetramethylbenzene = '1245_tetramethylbenzene'
name_1235_tetramethylbenzene = '1235_tetramethylbenzene'



### PAHs - POLYCYCLIC AROMATIC HYDROCARBONS
name_indane = 'indane'
name_indene = 'indene'
name_naphthalene = 'naphthalene'

name_naphthalene_VOC = 'naphthalene_VOC' #measured via volatile organic carbon
name_naphthalene_PAH = 'naphthalene_PAH' #measured via polyaromatic hydrocarbons
name_acenaphthylene = 'acenaphthylene'
name_acenaphthene = 'acenaphthene'
name_fluorene = 'fluorene'
name_phenanthrene = 'phenanthrene'
name_anthracene = 'anthracene'
name_fluoranthene = 'fluoranthene'
name_pyrene = 'pyrene'
name_chrysene = 'chrysene'
name_benzo_a_anthracene = 'benzo[a]anthracene'
name_benzo_b_fluoranthene = 'benzo[b]fluoranthene'
name_benzo_k_fluoranthene = 'benzo[k]fluoranthene'
name_benzo_a_pyrene = 'benzo[a]pyrene'
name_dibenz_ah_anthracene = 'dibenz[a,h]anthracene'
name_benzo_ghi_perylene = 'benzo[ghi]perylene'
name_indeno_123cd_pyrene = 'indeno[1,2,3-cd]pyrene'

### Standard names for additional PAH contaminants
name_methylindene = 'methylindene'
name_1_methylindene = '1_methylindene'
name_2_methylindene = '2_methylindene'
name_methylnaphthalene = 'methylnaphthalene'
name_1_methylnaphthalene = '1_methylnaphthalene'
name_2_methylnaphthalene = '2_methylnaphthalene'
name_ethylnaphthalene = 'ethylnaphthalene'
name_1_ethylnaphthalene = '1_ethylnaphthalene'
name_2_ethylnaphthalene = '2_ethylnaphthalene'
name_dimethylnaphthalene = 'dimethylnaphthalene'
name_12_dimethylnaphthalene = '12_dimethylnaphthalene'
name_13_dimethylnaphthalene = '13_dimethylnaphthalene'
name_14_dimethylnaphthalene = '14_dimethylnaphthalene'
name_15_dimethylnaphthalene = '15_dimethylnaphthalene'
name_16_dimethylnaphthalene = '16_dimethylnaphthalene'
name_17_dimethylnaphthalene = '17_dimethylnaphthalene'
name_18_dimethylnaphthalene = '18_dimethylnaphthalene'
name_23_dimethylnaphthalene = '23_dimethylnaphthalene'
name_26_dimethylnaphthalene = '26_dimethylnaphthalene'
name_27_dimethylnaphthalene = '27_dimethylnaphthalene'


### Standard names for a selection of metabolites
name_phenol = "phenol"
name_cinnamic_acid = "cinnamic_acid"
name_benzoic_acid = "benzoic_acid"
name_dimethyl_benzoic_acid = 'dimethyl_benzoic_acid'
name_benzylacetate = 'benzylacetate'
name_benzoylacetic_acid = "benzoylacetic_acid"
name_p_coumaric_acid = "p-coumaric_acid"
name_hydroxycinnamate = "hydroxycinnamate"
name_acetylphenol = "acetylphenol"
name_methyl_benzoic_acid = 'methyl_benzoic_acid'
name_benzylsuccinic_acid = "benzylsuccinic_acid"
name_3o_toluoyl_propionic_acid = "3o_toluoyl_propionic_acid"

### Standard names for summed up quantities
#name_total_contaminants = "total_contaminants"
name_total_contaminants = "concentration_contaminants"
name_total_BTEX = "concentration_BTEX"
name_total_BTEXIIN = "concentration_BTEXIIN"
name_total_contaminants_count = "count_contaminants"
name_total_BTEX_count = "count_BTEX"
name_total_BTEXIIN_count = "count_BTEXIIN"

name_PAH_total_10 = 'PAH_total_10'
name_PAH_total_16 = 'PAH_total_16'
name_fraction_C10_C12 = 'fraction_C10-C12'
name_fraction_C12_C22 = 'fraction_C12-C22'
name_fraction_C22_C30 = 'fraction_C22-C30'
name_fraction_C30_C40 = 'fraction_C30-C40'
name_total_C10_C40 = 'total_C10-C40'
### Standard names for metabolite related quantities
name_metabolites_conc = "metabolites_concentration"
# name_metabolites_variety = 'metabolites_count'
name_metabolites_count = 'metabolites_count'

### standard names/prefixes for isotopes:
name_13C = 'delta_13C'
name_2H = 'delta_2H'

### Standard names for NA screening related quantities
name_total_reductors = "total_reductors"
name_total_oxidators = "total_oxidators"
name_total_oxidators_BTEX = "total_oxidators_BTEX"
name_total_oxidators_BTEXIIN = "total_oxidators_BTEXIIN"
name_NP_avail = "NP_avail"
name_e_balance = 'e_balance'
name_na_traffic_light = 'na_traffic_light'

name_intervention_traffic = 'intervention_traffic'
name_intervention_number = 'intervention_number'
name_intervention_contaminants = 'intervention_contaminants'

name_benzene_thr_ratio = name_benzene+'_thr_ratio'
name_toluene_thr_ratio = name_toluene+'_thr_ratio'
name_ethylbenzene_thr_ratio = name_ethylbenzene+'_thr_ratio'
name_pm_xylene_thr_ratio = name_pm_xylene+'_thr_ratio'
name_o_xylene_thr_ratio = name_o_xylene+'_thr_ratio'
name_xylene_thr_ratio = name_xylene+'_thr_ratio'
name_indane_thr_ratio = name_indane+'_thr_ratio'
name_indene_thr_ratio = name_indene+'_thr_ratio'
name_naphthalene_thr_ratio = name_naphthalene+'_thr_ratio'
