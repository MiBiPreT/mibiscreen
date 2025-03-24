#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Unit specifications of data!

File containing unit specifications of quantities and parameters measured in
groundwater samples useful for biodegredation and bioremediation analysis.

@author: Alraune Zech
"""

from mibiscreen.data.names_data import name_EC
from mibiscreen.data.names_data import name_redox
from mibiscreen.data.names_data import name_sample_depth

### potential units
standard_units = dict(
    mgperl = ["mg/l",'ppm'],
    microgperl = [
        "ug/l",
        "micro g/l",
        r"$\mu$ g/l",
    ],
    millivolt = ["mV","mv"],
    meter = ['m',"meter"],
    microsimpercm = ['uS/cm','us/cm'],
    permil = ['permil','mur','‰','per mil','per mill','per mille','permill','permille','promille']
    )

all_units = [item for sublist in list(standard_units.values()) for item in sublist]

units_env_cond = dict()
units_env_cond[name_sample_depth] = 'meter'
units_env_cond[name_EC] = 'microsimpercm'
units_env_cond[name_redox] = 'millivolt'
