#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File containing name specifications of quantities and parameters measured in 
groundwater samples useful for biodegredation and bioremediation analysis 

@author: A. Zech
"""

name_sample = "sample_nr"
name_observation_well = "obs_well"
name_well_type = "well_type"
name_sample_depth = "depth"

setting_data = [name_sample,name_observation_well,name_well_type,name_sample_depth]

name_redox = "redoxpot"
environmental_conditions = [name_redox,"pH","EC","pE","NOPC"]


name_oxygen = 'oxygen' #o2
name_nitrite = 'nitrite' #no2
name_nitrate = 'nitrite' #no3
name_sulfate = 'sulfate' #"so4"
name_sulfide = 'sulfide' #"s2min"
name_ammonium = 'ammonium' #"nh4+"
name_methane = 'methane' #"ch4"
name_manganese = 'manganese' #"mn_II"
name_ironII = "ironII" #"fe_II"
name_phosphate = 'phosphate' # "po4"

electron_acceptors = [name_oxygen,name_nitrite,name_nitrate,name_sulfate,name_sulfide,name_ammonium,name_methane,name_ironII,name_manganese,name_phosphate]
#electron_acceptors = ["o2","no2","no3","so4","s2min","nh4+","ch4","mn_II","fe_II","po4","NPOC"]
                      
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
contaminants = [name_benzene,name_toluene,name_ethylbenzene,name_pm_xylene,name_o_xylene,name_xylene,name_indane,name_indene,name_naphthalene]


col_dict = {
    "sample": name_sample,
    "Sample":name_sample,
    "sample number": name_sample,
    "Sample Number": name_sample,
    "Sample number": name_sample,
    "sample nr": name_sample,
    "Sample Nr": name_sample,
    "Sample nr": name_sample,
    "well": name_observation_well,
    "Well": name_observation_well,
    "observation well": name_observation_well,
    "Observation Well": name_observation_well,
    "Observation well": name_observation_well,
    "Obs_well": name_observation_well,
    "well type" :name_well_type,
    "Well Type" : name_well_type,
    "Well type" : name_well_type,
    "Depth":name_sample_depth, 
    "depth":name_sample_depth,

    "Redox": name_redox,
    "redox": name_redox,
    "Redox potential": name_redox,
    "redox potential": name_redox,
    "redoxpot": name_redox,

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
    "s2min": name_sulfide,
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
    "Mn": name_manganese,
    "mn": name_manganese,
    "mn_II": name_manganese,
    "Mn_II": name_manganese,       
    "Manganese": name_manganese,
    "manganese": name_manganese,
    "Iron": name_ironII,
    "iron": name_ironII,
    "Fe": name_ironII,
    "fe": name_ironII,
    "Fe II": name_ironII,
    "fe II": name_ironII,
    "Fe_II": name_ironII,
    "fe_II": name_ironII,
    "Fe2": name_ironII,
    "Fe2+": name_ironII,
    "Fe 2": name_ironII,
    "Fe 2+": name_ironII,
    "Iron2": name_ironII,
    "Iron2+": name_ironII,
    "Iron 2": name_ironII,
    "Iron 2+": name_ironII,
    "iron2": name_ironII,
    "iron2+": name_ironII,
    "iron 2": name_ironII,
    "iron 2+": name_ironII,
    "Iron II": name_ironII,
    "iron II": name_ironII,
    "Iron II": name_ironII,
    "iron II": name_ironII ,
    "phosphate": name_phosphate,
    "Phosphate": name_phosphate,
    "PO4": name_phosphate,
    "po4": name_phosphate,

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
    "xylene": name_xylene,
    "Xylene": name_xylene,
    "c6h4c2h6": name_xylene,
    "C6H4C2H6": name_xylene,
    "Indene": name_indene,
    "c9h8": name_indene,
    "Indane": name_indane,
    "c9h10": name_indane,
    "Naphthalene": name_naphthalene,
    "c10h8": name_naphthalene,
}
