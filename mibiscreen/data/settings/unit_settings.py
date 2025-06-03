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

properties_units[names.unit_microgperl]=dict(
    other_names = ["ug/l","micro g/l",r"$\mu$ g/l",],
    )

properties_units[names.unit_millivolt]=dict(
    other_names = ["mV","mv"],
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

properties_units[names.unit_less]=dict(
    other_names = ['',' ','  ','-',np.nan],
    )


all_units = []
for key in properties_units.keys():
    if key != names.unit_less:
        all_units = all_units + properties_units[key]['other_names']

