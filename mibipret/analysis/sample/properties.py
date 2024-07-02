#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Properties for Natural Attenuation Screening.

File containing name specifications of quantities and parameters measured in
groundwater samples useful for biodegredation and bioremediation analysis

@author: A. Zech
"""
from mibipret.data.names import name_benzene
from mibipret.data.names import name_ethylbenzene
from mibipret.data.names import name_indane
from mibipret.data.names import name_indene
from mibipret.data.names import name_ironII
from mibipret.data.names import name_naphthalene
from mibipret.data.names import name_nitrate
from mibipret.data.names import name_o_xylene
from mibipret.data.names import name_oxygen
from mibipret.data.names import name_pm_xylene
from mibipret.data.names import name_sulfate
from mibipret.data.names import name_toluene
from mibipret.data.names import name_xylene

#name_phosphate,name_nitrite
#name_sulfide,name_ammonium,name_methane,name_manganese,

properties = dict()

properties[name_benzene]=dict(
    chemical_formula = 'c6h6',
    molecular_mass = 78.,
    cs = 6,
    factor_stoichiometry = 30.,
    thresholds_for_intervention_NL = 30,
    other_names = ["Benzene", "benzene", "C6H6", "c6h6", "Benzeen", "benzeen", "Benzol", "benzol"],
    )

properties[name_toluene]=dict(
    chemical_formula = 'c6h5ch3',
    molecular_mass = 106.,
    cs = 7.,
    factor_stoichiometry = 36.,
    thresholds_for_intervention_NL = 1000,
    other_names = ["toluene", "Toluene","Tolueen", "tolueen", "C7H8", "c7h8","C6H5CH3",'c6h5ch3'],
    )

properties[name_ethylbenzene]=dict(
    chemical_formula = 'c6h5ch2ch3',
    molecular_mass = 106.,
    cs = 8.,
    factor_stoichiometry = 42.,
    thresholds_for_intervention_NL = 150.,
    other_names = ["C6H5CH2CH3","c6h5ch2ch3","ethylbenzene","Ethylbenzene","ethylbenzeen","Ethylbenzeen"],
    )

properties[name_pm_xylene]=dict(
    chemical_formula =  "c6h4ch3ch3",
    molecular_mass = 106.,
    cs = 8.,
    factor_stoichiometry = 42.,
    thresholds_for_intervention_NL = 70.,
    other_names = ["pm-xylene","PM-Xylene","pm_xylene","PM_Xylene","p/m xylene","P/M Xylene", "c6h4ch3ch3",\
                   "C6H4CH3CH3","c6h4c2h6","C6H4C2H6","c8h14","C8H14"],
    )

properties[name_o_xylene]=dict(
    chemical_formula = "c6h4ch3ch3" ,
    molecular_mass = 106.,
    cs = 8.,
    factor_stoichiometry = 42.,
    thresholds_for_intervention_NL = 70.,
    other_names =  ["o-xylene", "O-Xylene", "O xylene", "O Xylene", "c6h4ch3ch3","C6H4CH3CH3","c6h4c2h6",\
                    "C6H4C2H6","c8h14","C8H14"],
    )

properties[name_xylene]=dict(
    chemical_formula = "c6h4ch3ch3",
    molecular_mass = 106.,
    cs = 8.,
    factor_stoichiometry = 42.,
    thresholds_for_intervention_NL = 70.,
    other_names = ["xylene", "Xylene", "c6h4ch3ch3","C6H4CH3CH3","c6h4c2h6","C6H4C2H6","c8h14","C8H14"],
    )

properties[name_indene]=dict(
    chemical_formula = "c9h8",
    molecular_mass = 116.,
    cs = 9.,
    factor_stoichiometry = 44.,
    thresholds_for_intervention_NL = 70.,
    other_names = ["indene", "Indene", "c9h8", "C9H8"],
    )

properties[name_indane]=dict(
    chemical_formula = "c9h10",
    molecular_mass = 118.,
    cs = 9.,
    factor_stoichiometry = 46.,
    thresholds_for_intervention_NL = 70.,
    other_names = ["indane", "Indane", "c9h10", "C9H10"],
    )

properties[name_naphthalene]=dict(
    chemical_formula = "c10h8",
    molecular_mass = 128,
    cs = 10.,
    factor_stoichiometry = 48.,
    thresholds_for_intervention_NL = 70.,
    other_names = ["naphthalene","Naphthalene","c10h8","C10H8"],
    )

properties[name_oxygen]=dict(
    chemical_formula = 'o2',
    molecular_mass = 32.,
    factor_stoichiometry = 4.,
    other_names = ["oxygen","Oxygen","o2","O2"] ,
    )

properties[name_nitrate]=dict(
    chemical_formula = 'no3',
    molecular_mass = 62.,
    factor_stoichiometry = 5.,
    other_names = ["nitrate","Nitrate","NO3","no3"],
    )
properties[name_sulfate]=dict(
    chemical_formula = "so42-",
    molecular_mass = 96.1,
    factor_stoichiometry = 8.,
    other_names = ["sulfate", "Sulfate","so4", "so42-", "SO4", "SO42-"],
    )
properties[name_ironII]=dict(
    chemical_formula = "fe2+",
    molecular_mass = 106.,
    factor_stoichiometry = 1,
    other_names = ["Iron","iron","Fe","fe","Fe II","fe II","FeII","feII",\
                   "Fe_II","fe_II","Fe2",'fe2',"Fe 2","fe 2","Fe_2","fe_2",\
                   "Fe2+",'fe2+',"Fe 2+","fe 2+","Iron2","iron2","Iron 2",\
                   "iron 2","Iron2+","iron2+","Iron 2+","iron 2+","IronII",\
                   "ironII","Iron II","iron II"],
    )

