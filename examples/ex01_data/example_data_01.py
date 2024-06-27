"""Example of data analysis of contaminant data from Griftpark, Utrecht.

@author: Alraune Zech
"""

from mibipret.data.data import check_columns  #, example_data #, check_values
from mibipret.data.data import check_units  #, example_data #, check_values
from mibipret.data.data import load_csv  #, example_data #, check_values

file_path = './grift_BTEXNII.csv'

data,units = load_csv(file_path,verbose = True)
data_standard = check_columns(data,verbose = True)

check_list = check_units(data_standard)
print("quantities to be checked on units: \n",check_list)
