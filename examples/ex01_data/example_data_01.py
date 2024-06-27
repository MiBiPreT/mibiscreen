#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example of data analysis of contaminant data from Griftpark, Utrecht
using mibipret 

@author: Alraune Zech
"""

from mibipret.data.data import load_csv, check_columns, check_units #, example_data #, check_values

file_path = './grift_BTEXNII.csv'

data,units = load_csv(file_path,verbose = True)
data_standard = check_columns(data,verbose = True)

check_list = check_units(data_standard)
print("quantities to be checked on units: \n",check_list)
