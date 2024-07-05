"""Example of data analysis of contaminant data from Griftpark, Utrecht.

@author: Alraune Zech
"""

from mibipret.data.data import check_columns
from mibipret.data.data import check_units
from mibipret.data.data import check_values
from mibipret.data.data import load_csv
from mibipret.data.data import standardize

# import sys
# path = '/home/alraune/GitHub/MiBiPreT/mibipret/mibipret/data/'
# sys.path.append(path) # append the path to module

# from data import check_columns
# from data import check_units
# from data import check_values
# from data import load_csv
# from data import standardize


file_path = './grift_BTEXNII.csv'
file_standard = './grift_BTEXNII_standard.csv'

data,units = load_csv(file_path,verbose = True)

column_names_known,column_names_unknown,column_names_standard = check_columns(data, verbose = True)
print("\nQuantities to be checked on column names: \n",column_names_unknown)

check_list = check_units(data,verbose = True)
print("\nQuantities to be checked on units: \n",check_list)

data_pure = check_values(data, verbose = True)

data_standard,units = standardize(data,reduce = True, store_csv=file_standard,  verbose=True)
