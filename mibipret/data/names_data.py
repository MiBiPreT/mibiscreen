#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Name specifications of data!

File containing name specifications of quantities and parameters measured in
groundwater samples useful for biodegredation and bioremediation analysis

@author: A. Zech
"""

### Standard names for settings
name_sample = "sample_nr"
name_observation_well = "obs_well"
name_well_type = "well_type"
name_sample_depth = "depth"
name_aquifer = 'aquifer'

setting_data = [name_sample,
                name_observation_well,
                name_well_type,
                name_sample_depth]

### Standard names for environmental parameters
name_redox = "redoxpot"
name_pH = "pH"
name_EC = "EC"
name_pE = "pE"
name_NOPC = "NOPC"
name_DOC = "DOC"

name_oxygen = 'oxygen' #o2
name_nitrite = 'nitrite' #no2
name_sulfate = 'sulfate' #"so4"
name_ironII = "iron2" #"fe_II"
name_manganese = 'manganese' #"mn_II"
name_methane = 'methane' #"ch4"

name_nitrate = 'nitrate' #no3
name_sulfide = 'sulfide' #"s2min"
name_ammonium = 'ammonium' #"nh4+"
name_phosphate = 'phosphate' # "po4"
name_chloride = 'chloride'
name_bromide = 'bromide'
name_fluoride = 'fluoride'
name_sodium = 'sodium'
name_magnesium = 'magnesium'
name_potassium = 'potassium'
name_calcium = 'calcium'
name_acetate = 'acetate'

environmental_conditions = [name_redox,name_pH,name_EC,name_pE,name_NOPC]

chemical_composition = [
    name_oxygen, name_nitrate, name_sulfate, name_ironII, name_manganese,
    name_methane, name_nitrite, name_sulfide, name_ammonium, name_phosphate,
    name_chloride,name_bromide,name_fluoride,name_sodium,name_magnesium,
    name_potassium,name_calcium,name_acetate,name_DOC]

electron_acceptors = dict(
    ONS = [name_oxygen, name_nitrate, name_sulfate],
    ONSFe = [name_oxygen, name_nitrate, name_sulfate, name_ironII],
    all_ea = [name_oxygen, name_nitrate, name_sulfate,
               name_ironII, name_manganese, name_methane]
)

### Standard names for contaminants
name_benzene = 'benzene'
name_toluene = 'toluene'
name_ethylbenzene = 'ethylbenzene'
name_pm_xylene = 'pm_xylene'
name_o_xylene = 'o_xylene'
name_xylene = 'xylene'
name_indane = 'indane'
name_indene = 'indene'
name_naphthalene = 'naphthalene'

### todo: complete and potentially choose other names
contaminants = dict(
    BTEX = [name_benzene,name_toluene,name_ethylbenzene, name_pm_xylene,
                name_o_xylene, name_xylene],
    BTEXIIN = [name_benzene,name_toluene,name_ethylbenzene, name_pm_xylene,
                name_o_xylene, name_xylene, name_indane,name_indene, name_naphthalene],
    all_cont = [name_benzene,name_toluene,name_ethylbenzene, name_pm_xylene,
                name_o_xylene, name_xylene, name_indane,name_indene, name_naphthalene],
)

### Standard names for NA screening related quantities
name_total_oxidators = "total_oxidators"
name_total_reductors = "total_reductors"
name_NP_avail = "NP_avail"
name_e_balance = 'e_balance'
name_na_traffic_light = 'na_traffic_light'
name_total_contaminants = "total_contaminants"
name_intervention_traffic = 'intervention_traffic'
name_intervention_number = 'intervention_number'
name_intervention_contaminants = 'intervention_contaminants'

### Standard names for metabolite related quantities
name_metabolites_conc = "metabolites_concentration"
name_metabolites_variety = 'metabolites_variety'

### standard names/prefixes for isotopes:
name_13C = 'delta_13C'
name_2H = 'delta_2H'
isotopes = ['delta_13C','delta_2H']

### Dictionary with potential names of quantities to be replaced by standard name
names_settings = {
    "sample": name_sample,
    "sample number": name_sample,
    "sample-number": name_sample,
    "sample_number": name_sample,
    "sample nr": name_sample,
    "sample-nr": name_sample,
    "sample_nr": name_sample,
    "sample name": name_sample,
    "sample-name": name_sample,
    "sample_name": name_sample,
    "sample id": name_sample,
    "sample-id": name_sample,
    "sample_id": name_sample,
    "well": name_observation_well,
    "observation well": name_observation_well,
    "observation-well": name_observation_well,
    "observation_well": name_observation_well,
    "obs well": name_observation_well,
    "obs_well": name_observation_well,
    "obs-well": name_observation_well,
    "welltype" :name_well_type,
    "well type" :name_well_type,
    "well-type" : name_well_type,
    "well_type" :name_well_type,
    "depth":name_sample_depth,
    'aquifer': name_aquifer,
}

names_environment = {
    "redox": name_redox,
    "redoxpotential": name_redox,
    "redox potential": name_redox,
    "redox-potential": name_redox,
    "redox_potential": name_redox,
    "redoxpot": name_redox,
    "redox pot": name_redox,
    "redox-pot": name_redox,
    "redox_pot": name_redox,
    "ph": name_pH,
    "ec": name_EC,
    "pe": name_pE,
    "nopc": name_NOPC,
    "doc": name_DOC,
}

names_chemicals = {
    "oxygen": name_oxygen,
    "o":name_oxygen,
    "o2":name_oxygen,
    "nitrite": name_nitrite,
    "no2": name_nitrite,
    "nitrate": name_nitrate,
    "no3": name_nitrate,
    "sulfate": name_sulfate,
    "so4": name_sulfate,
    "so42-": name_sulfate,
    "so4 2-": name_sulfate,
    "so4-2-": name_sulfate,
    "so4_2-": name_sulfate,
    "sulfide": name_sulfide,
    "s": name_sulfide,
    "s2": name_sulfide,
    "s 2": name_sulfide,
    "s-2": name_sulfide,
    "s_2": name_sulfide,
    "s2-": name_sulfide,
    "s 2-": name_sulfide,
    "s-2-": name_sulfide,
    "s_2-": name_sulfide,
    "s2min": name_sulfide,
    "s 2min": name_sulfide,
    "s-2min": name_sulfide,
    "s_2min": name_sulfide,
    "ammonium": name_ammonium,
    "nh4": name_ammonium,
    "nh4+": name_ammonium,
    "methane": name_methane,
    "ch4": name_methane,
    "manganese": name_manganese,
    "mn": name_manganese,
    "mn2": name_manganese,
    "mn 2": name_manganese,
    "mn-2": name_manganese,
    "mn_2": name_manganese,
    "mnii": name_manganese,
    "mn ii": name_manganese,
    "mn-ii": name_manganese,
    "mn_ii": name_manganese,
    "mn2+": name_manganese,
    "mn 2+": name_manganese,
    "mn-2+": name_manganese,
    "mn_2+": name_manganese,
    "mnii+": name_manganese,
    "mn ii+": name_manganese,
    "mn-ii+": name_manganese,
    "mn_ii+": name_manganese,
    "iron": name_ironII,
    "iron2": name_ironII,
    "iron 2": name_ironII,
    "iron-2": name_ironII,
    "iron_2": name_ironII,
    "iron2+": name_ironII,
    "iron 2+": name_ironII,
    "iron-2+": name_ironII,
    "iron_2+": name_ironII,
    "ironii": name_ironII,
    "iron ii": name_ironII,
    "iron-ii": name_ironII ,
    "iron_ii": name_ironII,
    "ironii+": name_ironII,
    "iron ii+": name_ironII ,
    "iron-ii+": name_ironII,
    "iron_ii+": name_ironII ,
    "fe": name_ironII,
    "fe2": name_ironII,
    "fe 2": name_ironII,
    "fe-2": name_ironII,
    "fe_2": name_ironII,
    "fe2+": name_ironII,
    "fe 2+": name_ironII,
    "fe-2+": name_ironII,
    "fe_2+": name_ironII,
    "feii": name_ironII,
    "fe ii": name_ironII,
    "fe-ii": name_ironII,
    "fe_ii": name_ironII,
    "feii+": name_ironII,
    "fe ii+": name_ironII,
    "fe-ii+": name_ironII,
    "fe_ii+": name_ironII,
    "phosphate": name_phosphate,
    "po4": name_phosphate,
    "po43-": name_phosphate,
    "po4 3-": name_phosphate,
    "po4-3-": name_phosphate,
    "po4_3-": name_phosphate,
    'chloride': name_chloride,
    'cl': name_chloride,
    'cl-': name_chloride,
    'bromide': name_bromide,
    'br': name_bromide,
    'br-': name_bromide,
    'fluoride': name_fluoride,
    'f': name_fluoride,
    'f-': name_fluoride,
    'sodium': name_sodium,
    'na': name_sodium,
    'na+': name_sodium,
    'magnesium': name_magnesium,
    'mg': name_magnesium,
    'mg2+': name_magnesium,
    'potassium': name_potassium,
    'k': name_potassium,
    'k+': name_potassium,
    'calcium': name_calcium,
    'ca': name_calcium,
    'ca2+': name_calcium,
    'acetate': name_acetate,
    'c2h3o2-': name_acetate,
}

names_contaminants = {
    "benzene": name_benzene,
    "c6h6": name_benzene,
    "benzeen": name_benzene,
    "tolueen": name_toluene,
    "toluene": name_toluene,
    "c7h8": name_toluene,
    "c6h5ch3": name_toluene,
    "c6h5ch2ch3":name_ethylbenzene,
    "ethylbenzene": name_ethylbenzene,
    "ethylbenzeen": name_ethylbenzene,
    "mp_xylene":name_pm_xylene,
    "mp-xylene": name_pm_xylene,
    "mp xylene": name_pm_xylene,
    "m,p-xylene": name_pm_xylene,
    "m,p_xylene": name_pm_xylene,
    "m,p xylene": name_pm_xylene,
    "m/p_xylene": name_pm_xylene,
    "m/p-xylene": name_pm_xylene,
    "m/p xylene": name_pm_xylene,
    "pm_xylene":name_pm_xylene,
    "pm-xylene": name_pm_xylene,
    "pm xylene": name_pm_xylene,
    "p,m_xylene": name_pm_xylene,
    "p,m-xylene": name_pm_xylene,
    "p,m xylene": name_pm_xylene,
    "p/m_xylene": name_pm_xylene,
    "p/m-xylene": name_pm_xylene,
    "p/m xylene": name_pm_xylene,
    "o_xylene": name_o_xylene,
    "o-xylene": name_o_xylene,
    "o xylene": name_o_xylene,
    "xylene": name_xylene,
    "c6h4c2h6": name_xylene,
    "indene": name_indene,
    "c9h8": name_indene,
    "indane": name_indane,
    "c9h10": name_indane,
    "naphtalene": name_naphthalene,
    "naphthalene": name_naphthalene,
    "naphtaline": name_naphthalene,
    "naphthaline": name_naphthalene,
    "c10h8": name_naphthalene,
    }

names_metabolites_sum = {
    "metaboliteconcentration": name_metabolites_conc,
    "metabolite concentration": name_metabolites_conc,
    "metabolite_concentration": name_metabolites_conc,
    "Metabolite-concentration": name_metabolites_conc,
    'metabolitevariety': name_metabolites_variety,
    'metabolite variety': name_metabolites_variety,
    'metabolite-variety': name_metabolites_variety,
    'metabolite_variety': name_metabolites_variety,
    'metabolitesvariety': name_metabolites_variety,
    'metabolites variety': name_metabolites_variety,
    'metabolites-variety': name_metabolites_variety,
    'metabolites_variety': name_metabolites_variety,
    "number of detected metabolites":  name_metabolites_variety,
}

names_isotopes = {
    'delta_c' : name_13C,
    'delta_13c' : name_13C,
    'delta_c13' : name_13C,
    'delta_carbon' : name_13C,
    'delta_13carbon' : name_13C,
    'delta_carbon13' : name_13C,
    'deltac' : name_13C,
    'delta13c' : name_13C,
    'deltac13' : name_13C,
    'deltacarbon' : name_13C,
    'delta13carbon' : name_13C,
    'deltacarbon13' : name_13C,
    'delta c' : name_13C,
    'delta 13c' : name_13C,
    'delta c13' : name_13C,
    'delta carbon' : name_13C,
    'delta 13carbon' : name_13C,
    'delta carbon13' : name_13C,
    'δ_c' : name_13C,
    'δ_13c' : name_13C,
    'δ_c13' : name_13C,
    'δ_carbon' : name_13C,
    'δ_13carbon' : name_13C,
    'δ_carbon13' : name_13C,
    'δc' : name_13C,
    'δ13c' : name_13C,
    'δc13' : name_13C,
    'δcarbon' : name_13C,
    'δ13carbon' : name_13C,
    'δcarbon13' : name_13C,
    'δ c' : name_13C,
    'δ 13c' : name_13C,
    'δ c13' : name_13C,
    'δ carbon' : name_13C,
    'δ 13carbon' : name_13C,
    'δ carbon13' : name_13C,
    'delta_h' : name_2H,
    'delta_2h' : name_2H,
    'delta_h2' : name_2H,
    'delta_hydrogen' : name_2H,
    'delta_2hydrogen' : name_2H,
    'delta_hydrogen2' : name_2H,
    'deltah' : name_2H,
    'delta2h' : name_2H,
    'deltah2' : name_2H,
    'deltahydrogen' : name_2H,
    'delta2hydrogen' : name_2H,
    'deltahydrogen2' : name_2H,
    'delta-h' : name_2H,
    'delta-2h' : name_2H,
    'delta-h2' : name_2H,
    'delta-hydrogen' : name_2H,
    'delta-2hydrogen' : name_2H,
    'delta-hydrogen2' : name_2H,
    'delta h' : name_2H,
    'delta 2h' : name_2H,
    'delta h2' : name_2H,
    'delta hydrogen' : name_2H,
    'delta 2hydrogen' : name_2H,
    'delta hydrogen2' : name_2H,
    }

col_dict = {
    **names_settings,
    **names_environment,
    **names_chemicals,
    **names_contaminants,
    **names_metabolites_sum,
}
