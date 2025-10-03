"""Unit specifications of data!

File containing unit specifications of quantities and parameters measured in
groundwater samples useful for biodegredation and bioremediation analysis.

@author: Alraune Zech
"""

import numpy as np
import mibiscreen.data.settings.standard_names as names

properties_units = dict()
properties_units[names.unit_mgperl]=dict(
    other_names = ["mg/l",'ppm'],
    )

properties_units[names.unit_mgNperl]=dict(
    other_names = ["mg/l", 'ppm', "mgN/l",'ppm N','ppmN','ppm-N','ppm_N',"mg/l as N","ppm as N"],
    )

properties_units[names.unit_mgPperl]=dict(
    other_names = ["mg/l", 'ppm', "mgP/l",'ppm P','ppmP','ppm-P','ppm_P',"mg/l as P","ppm as P"],
    )

properties_units[names.unit_microgperl]=dict(
    other_names = ["ug/l","µg/l","\u00B5g/l","\u03BCg/l","micro g/l",r"$\mu$ g/l",],
    )

properties_units[names.unit_millivolt]=dict(
    other_names = ["mV","mv"],
    )

properties_units[names.unit_celsius]=dict(
    other_names = ["C","c","Celsius","celsius",
                   "\u00B0C","\u00B0c","\u00B0Celsius","\u00B0celsius",
                   "\u00B0 C","\u00B0 c","\u00B0 Celsius","\u00B0 celsius"],
    )

properties_units[names.unit_meter]=dict(
    other_names = ['m',"meter"],
    )

properties_units[names.unit_microsimpercm]=dict(
    other_names = ['uS/cm','us/cm'],
    )

properties_units[names.unit_permil]=dict(
    other_names = ['permil','mur','‰','per mil','per mill','per mille',
                   'permill','permille','promille'],
    )

properties_units[names.unit_count]=dict(
    other_names =['nr','number','count'],
    )

properties_units[names.unit_date]=dict(
    other_names = ['date','time','hr'],
    )

properties_units[names.unit_less]=dict(
    other_names = ['',' ','  ','-',np.nan],
    )

all_units = []
for key in properties_units.keys():
    if key != names.unit_less:
        all_units = all_units + properties_units[key]['other_names']

