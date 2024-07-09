#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Name specifications of data!

File containing name specifications of quantities and parameters measured in
groundwater samples useful for biodegredation and bioremediation analysis

@author: A. Zech
"""

name_sample = "sample_nr"
name_observation_well = "obs_well"
name_well_type = "well_type"
name_sample_depth = "depth"

setting_data = [name_sample,
                name_observation_well,
                name_well_type,
                name_sample_depth]

name_redox = "redoxpot"
name_pH = "pH"
name_EC = "EC"
name_pE = "pE"
name_NOPC = "NOPC"

environmental_conditions = [name_redox,name_pH,name_EC,name_pE,name_NOPC]

name_oxygen = 'oxygen' #o2
name_nitrite = 'nitrite' #no2
name_nitrate = 'nitrate' #no3
name_sulfate = 'sulfate' #"so4"
name_sulfide = 'sulfide' #"s2min"
name_ammonium = 'ammonium' #"nh4+"
name_methane = 'methane' #"ch4"
name_manganese = 'manganese' #"mn_II"
name_ironII = "ironII" #"fe_II"
name_phosphate = 'phosphate' # "po4"

electron_acceptors = dict(
    ONSFe = [name_oxygen, name_nitrate, name_sulfate, name_ironII],
    all_ea = [name_oxygen, name_nitrate, name_nitrite, name_sulfate, name_sulfide,
                name_ammonium, name_methane, name_ironII, name_manganese, name_phosphate]
)

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

col_dict = {
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
    "oxygen": name_oxygen,
    "o2":name_oxygen,
    "O2": name_oxygen,
    "Oxygen": name_oxygen,
    "nitrite": name_nitrite,
    "Nitrite": name_nitrite,
    "NO2": name_nitrite,
    "no2": name_nitrite,
    "nitrate": name_nitrate,
    "Nitrate": name_nitrate,
    "NO3": name_nitrate,
    "no3": name_nitrate,
    "sulfate": name_sulfate,
    "Sulfate": name_sulfate,
    "SO4": name_sulfate,
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
    "nh4+": name_ammonium,
    "nh4": name_ammonium,
    "NH4+": name_ammonium,
    "NH4": name_ammonium,
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
    "fe": name_ironII,
    "Fe": name_ironII,
    "iron": name_ironII,
    "Iron": name_ironII,
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
    "phosphate": name_phosphate,
    "Phosphate": name_phosphate,
    "po4": name_phosphate,
    "PO4": name_phosphate,
    "po43-": name_phosphate,
    "PO43-": name_phosphate,
    "po4_3-": name_phosphate,
    "PO4_3-": name_phosphate,
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
    "indane": name_indane,
    "Indane": name_indane,
    "c9h10": name_indane,
    "naphtalene": name_naphthalene,
    "Naphtalene": name_naphthalene,
    "naphthalene": name_naphthalene,
    "Naphthalene": name_naphthalene,
    "c10h8": name_naphthalene
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
