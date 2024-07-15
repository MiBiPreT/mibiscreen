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
name_ironII = "ironII" #"fe_II"
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

### Dictionary with potential names of quantities to be replaced by standard name
names_settings = {
    "sample": name_sample,
    "Sample":name_sample,
    "sample number": name_sample,
    "Sample Number": name_sample,
    "Sample number": name_sample,
    "sample_number": name_sample,
    "Sample_Number": name_sample,
    "Sample_number": name_sample,
    "sample nr": name_sample,
    "Sample Nr": name_sample,
    "Sample nr": name_sample,
    "sample_nr": name_sample,
    "Sample_nr": name_sample,
    "Sample_Nr": name_sample,
    "sample name": name_sample,
    "Sample name": name_sample,
    "Sample Name": name_sample,
    "sample_name": name_sample,
    "Sample_name": name_sample,
    "Sample_Name": name_sample,
    "well": name_observation_well,
    "Well": name_observation_well,
    "observation well": name_observation_well,
    "Observation Well": name_observation_well,
    "Observation well": name_observation_well,
    "obs_well": name_observation_well,
    "Obs_well": name_observation_well,
    "obs well": name_observation_well,
    "Obs well": name_observation_well,
    "welltype" :name_well_type,
    "Welltype" : name_well_type,
    "well type" :name_well_type,
    "Well Type" : name_well_type,
    "Well type" : name_well_type,
    "well_type" :name_well_type,
    "Well_Type" : name_well_type,
    "Well_type" : name_well_type,
    "Depth":name_sample_depth,
    "depth":name_sample_depth,
    'aquifer': name_aquifer,
    'Aquifer': name_aquifer,
}

names_environment = {
    "Redox": name_redox,
    "redox": name_redox,
    "Redox potential": name_redox,
    "redox potential": name_redox,
    "redoxpot": name_redox,
    "pH": name_pH,
    "ph": name_pH,
    "PH": name_pH,
    "ec": name_EC,
    "Ec": name_EC,
    "EC": name_EC,
    "pe": name_pE,
    "pE": name_pE,
    "PE": name_pE,
    "NPOC": name_NOPC,
    "NOPC": name_NOPC,
    "DOC": name_DOC,
    "doc": name_DOC,
}

names_chemicals = {
    "oxygen": name_oxygen,
    "Oxygen": name_oxygen,
    "o":name_oxygen,
    "O": name_oxygen,
    "o2":name_oxygen,
    "O2": name_oxygen,
    "nitrite": name_nitrite,
    "Nitrite": name_nitrite,
    "no2": name_nitrite,
    "No2": name_nitrite,
    "NO2": name_nitrite,
    "nitrate": name_nitrate,
    "Nitrate": name_nitrate,
    "no3": name_nitrate,
    "No3": name_nitrate,
    "NO3": name_nitrate,
    "sulfate": name_sulfate,
    "Sulfate": name_sulfate,
    "so4": name_sulfate,
    "So4": name_sulfate,
    "SO4": name_sulfate,
    "so42-": name_sulfate,
    "So42-": name_sulfate,
    "SO42-": name_sulfate,
    "sulfide": name_sulfide,
    "Sulfide": name_sulfide,
    "S": name_sulfide,
    "s": name_sulfide,
    "s2": name_sulfide,
    "S2": name_sulfide,
    "s2-": name_sulfide,
    "S2-": name_sulfide,
    "s2min": name_sulfide,
    "S2min": name_sulfide,
    "ammonium": name_ammonium,
    "Ammonium": name_ammonium,
    "nh4": name_ammonium,
    "NH4": name_ammonium,
    "nh4+": name_ammonium,
    "NH4+": name_ammonium,
    "methane": name_methane,
    "Methane": name_methane,
    "ch4": name_methane,
    "CH4": name_methane,
    "manganese": name_manganese,
    "Manganese": name_manganese,
    "mn": name_manganese,
    "Mn": name_manganese,
    "mn2": name_manganese,
    "Mn2": name_manganese,
    "mn 2": name_manganese,
    "Mn 2": name_manganese,
    "mn_2": name_manganese,
    "Mn_2": name_manganese,
    "mnII": name_manganese,
    "MnII": name_manganese,
    "mn II": name_manganese,
    "Mn II": name_manganese,
    "mn_II": name_manganese,
    "Mn_II": name_manganese,
    "mn2+": name_manganese,
    "Mn2+": name_manganese,
    "mn 2+": name_manganese,
    "Mn 2+": name_manganese,
    "mn_2+": name_manganese,
    "Mn_2+": name_manganese,
    "mnII+": name_manganese,
    "MnII+": name_manganese,
    "mn II+": name_manganese,
    "Mn II+": name_manganese,
    "mn_II+": name_manganese,
    "Mn_II+": name_manganese,
    "iron": name_ironII,
    "Iron": name_ironII,
    "iron2": name_ironII,
    "Iron2": name_ironII,
    "iron2+": name_ironII,
    "Iron2+": name_ironII,
    "iron 2": name_ironII,
    "Iron 2": name_ironII,
    "iron 2+": name_ironII,
    "Iron 2+": name_ironII,
    "iron_2": name_ironII,
    "Iron_2": name_ironII,
    "iron_2+": name_ironII,
    "Iron_2+": name_ironII,
    "ironII": name_ironII,
    "IronII": name_ironII,
    "ironII+": name_ironII ,
    "IronII+": name_ironII,
    "iron II": name_ironII,
    "Iron II": name_ironII,
    "iron II+": name_ironII ,
    "Iron II+": name_ironII,
    "iron_II": name_ironII,
    "Iron_II": name_ironII,
    "iron_II+": name_ironII ,
    "Iron_II+": name_ironII,
    "fe": name_ironII,
    "Fe": name_ironII,
    "fe2": name_ironII,
    "Fe2": name_ironII,
    "fe2+": name_ironII,
    "Fe2+": name_ironII,
    "fe 2": name_ironII,
    "Fe 2": name_ironII,
    "fe 2+": name_ironII,
    "Fe 2+": name_ironII,
    "fe_2": name_ironII,
    "Fe_2": name_ironII,
    "fe_2+": name_ironII,
    "Fe_2+": name_ironII,
    "feII": name_ironII,
    "FeII": name_ironII,
    "feII+": name_ironII,
    "FeII+": name_ironII,
    "fe II": name_ironII,
    "Fe II": name_ironII,
    "fe II+": name_ironII,
    "Fe II+": name_ironII,
    "fe_II": name_ironII,
    "Fe_II": name_ironII,
    "fe_II+": name_ironII,
    "Fe_II+": name_ironII,
    "phosphate": name_phosphate,
    "Phosphate": name_phosphate,
    "po4": name_phosphate,
    "Po4": name_phosphate,
    "PO4": name_phosphate,
    "po43-": name_phosphate,
    "Po43-": name_phosphate,
    "PO43-": name_phosphate,
    "po4_3-": name_phosphate,
    "Po4_3-": name_phosphate,
    "PO4_3-": name_phosphate,
    "po4 3-": name_phosphate,
    "Po4 3-": name_phosphate,
    "PO4 3-": name_phosphate,
    'chloride': name_chloride,
    'Chloride': name_chloride,
    'cl': name_chloride,
    'Cl': name_chloride,
    'CL': name_chloride,
    'cl-': name_chloride,
    'Cl-': name_chloride,
    'CL-': name_chloride,
    'bromide': name_bromide,
    'Bromide': name_bromide,
    'br': name_bromide,
    'Br': name_bromide,
    'BR': name_bromide,
    'br-': name_bromide,
    'Br-': name_bromide,
    'BR-': name_bromide,
    'fluoride': name_fluoride,
    'Fluoride': name_fluoride,
    'f': name_fluoride,
    'F': name_fluoride,
    'f-': name_fluoride,
    'F-': name_fluoride,
    'sodium': name_sodium,
    'Sodium': name_sodium,
    'na': name_sodium,
    'Na': name_sodium,
    'NA': name_sodium,
    'na+': name_sodium,
    'Na+': name_sodium,
    'NA+': name_sodium,
    'magnesium': name_magnesium,
    'Magnesium': name_magnesium,
    'mg': name_magnesium,
    'Mg': name_magnesium,
    'MG': name_magnesium,
    'mg2+': name_magnesium,
    'Mg2+': name_magnesium,
    'MG2+': name_magnesium,
    'potassium': name_potassium,
    'Potassium': name_potassium,
    'k': name_potassium,
    'K': name_potassium,
    'k+': name_potassium,
    'K+': name_potassium,
    'calcium': name_calcium,
    'Calcium': name_calcium,
    'ca': name_calcium,
    'Ca': name_calcium,
    'CA': name_calcium,
    'ca2+': name_calcium,
    'Ca2+': name_calcium,
    'CA2+': name_calcium,
    'acetate': name_acetate,
    'Acetate': name_acetate,
    'c2h3o2-': name_acetate,
    'C2H3O2-': name_acetate,
}

names_contaminants = {
    "Benzene": name_benzene,
    "benzene": name_benzene,
    "C6H6": name_benzene,
    "c6h6": name_benzene,
    "Benzeen": name_benzene,
    "benzeen": name_benzene,
    "tolueen": name_toluene,
    "Tolueen": name_toluene,
    "toluene": name_toluene,
    "Toluene": name_toluene,
    "C7H8": name_toluene,
    "c7h8": name_toluene,
    "C6H5CH3": name_toluene,
    "c6h5ch3": name_toluene,
    "C6H5CH2CH3": name_ethylbenzene,
    "c6h5ch2ch3":name_ethylbenzene,
    "ethylbenzene": name_ethylbenzene,
    "Ethylbenzene":name_ethylbenzene,
    "ethylbenzeen": name_ethylbenzene,
    "Ethylbenzeen": name_ethylbenzene,
    "pm-xylene": name_pm_xylene,
    "pm_xylene":name_pm_xylene,
    "P/M Xylene": name_pm_xylene,
    "o-xylene": name_o_xylene,
    "O-Xylene": name_o_xylene,
    "O Xylene": name_o_xylene,
    "o xylene": name_o_xylene,
    "o_xylene": name_o_xylene,
    "O_Xylene": name_o_xylene,
    "xylene": name_xylene,
    "Xylene": name_xylene,
    "c6h4c2h6": name_xylene,
    "C6H4C2H6": name_xylene,
    "indene": name_indene,
    "Indene": name_indene,
    "c9h8": name_indene,
    "C9H8": name_indene,
    "indane": name_indane,
    "Indane": name_indane,
    "c9h10": name_indane,
    "c9H10": name_indane,
    "naphtalene": name_naphthalene,
    "Naphtalene": name_naphthalene,
    "naphthalene": name_naphthalene,
    "Naphthalene": name_naphthalene,
    "c10h8": name_naphthalene,
    "C10H8": name_naphthalene,
    }

names_metabolites_sum = {
    "metabolite_concentration": name_metabolites_conc,
    "Metabolite_concentration": name_metabolites_conc,
    "Metabolite_Concentration": name_metabolites_conc,
    "metabolite concentration": name_metabolites_conc,
    "Metabolite concentration": name_metabolites_conc,
    "Metabolite Concentration": name_metabolites_conc,
    "metabolites_concentration": name_metabolites_conc,
    "Metabolites_concentration": name_metabolites_conc,
    "Metabolites_Concentration": name_metabolites_conc,
    "metabolites concentration": name_metabolites_conc,
    "Metabolites concentration": name_metabolites_conc,
    "Metabolites Concentration": name_metabolites_conc,
    'metabolite_variety': name_metabolites_variety,
    'Metabolite_variety': name_metabolites_variety,
    'Metabolite_Variety': name_metabolites_variety,
    'metabolite variety': name_metabolites_variety,
    'Metabolite variety': name_metabolites_variety,
    'Metabolite Variety': name_metabolites_variety,
    'metabolites_variety': name_metabolites_variety,
    'Metabolites_variety': name_metabolites_variety,
    'Metabolites_Variety': name_metabolites_variety,
    'metabolites variety': name_metabolites_variety,
    'Metabolites variety': name_metabolites_variety,
    'Metabolites Variety': name_metabolites_variety,
    "Number of detected metabolites":  name_metabolites_variety,
}

col_dict = {
    **names_settings,
    **names_environment,
    **names_chemicals,
    **names_contaminants,
    **names_metabolites_sum,
}

### potential units
standard_units = dict(
    mgperl = ["mg/l", "mg/L", "MG/L",'ppm'],
    microgperl = [
        "ug/l",
        "ug/L",
        "micro g/l",
        "micro g/L",
        "MICRO G/L",
        r"$\mu$ g/l",
        r"$\mu$ g/L",
    ],
    millivolt = ["mV"],
    meter = ['m',"M"],
    microsimpercm = ['uS/cm','us/cm','uS/CM','us/CM'],
    )
