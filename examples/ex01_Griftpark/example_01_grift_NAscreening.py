"""Example of data analysis of contaminant data from Griftpark, Utrecht.

@author: Alraune Zech
"""

<<<<<<< HEAD

# path = '/home/alraune/GitHub/MiBiPreT/mibiscreen/mibiscreen/'
# sys.path.append(path) # append the path to module
# import analysis.sample.screening_NA as na
# import data.data as md
# from visualize.activity import activity

import mibiscreen.analysis.sample.screening_NA as na
import mibiscreen.analysis.sample.concentrations as co
from mibiscreen.data.check_data import standardize
from mibiscreen.data.load_data import load_csv

#from mibiscreen.data.check_data import check_columns,check_units,check_values, standardize
from mibiscreen.visualize.activity import activity

###------------------------------------------------------------------------###
### Script settings


###------------------------------------------------------------------------###
### File path settings
file_path = './grift_BTEXIIN.csv'
file_standard = './grift_BTEXIIN_standard.csv'

###------------------------------------------------------------------------###
### Load and standardize data
data_raw,units = load_csv(file_path,
                          verbose = False
                          )

# column_names_known,column_names_unknown,column_names_standard = check_columns(data, verbose = True)
# # # print("\nQuantities to be checked on column names: \n",column_names_unknown)

# check_list = check_units(data,verbose = True)
# # # print("\nQuantities to be checked on units: \n",check_list)

# data_pure = check_values(data, verbose = True)

data,units = standardize(data_raw,
                         reduce = True,
                         # store_csv=file_standard,
                         verbose=False)

###------------------------------------------------------------------------###
### perform NA screening step by step

tot_reduct = na.reductors(data,
                          include = False,
                          verbose = True,
                          ea_group = 'ONS',
                          )

tot_oxi = na.oxidators(data,
                       include = False,
                       contaminant_group='BTEXIIN',
                       verbose = True,
                       )

# tot_oxi_nut = na.oxidators(data,
#                            verbose = True,
#                            nutrient = True
#                            )

e_bal = na.electron_balance(data,
                            include = False,
                            verbose = True
                            )

na_traffic = na.sample_NA_traffic(data,
                                  include = True,
                                  verbose = True,
                                  )

### NA screening for samples in one go:

### run full NA screening with results in separate DataFrame
data_na = na.sample_NA_screening(data,
                          include = False,
                          contaminant_group='BTEXIIN',
                          verbose = True,
                          )


###------------------------------------------------------------------------###
### Evaluation of total concentrations and intervention threshold exceedance

tot_cont = co.total_contaminant_concentration(data,
                                              contaminant_group='BTEXIIN',
                                              include = True,
                                              verbose = True,
                                              )

na_intervention = co.thresholds_for_intervention(data,
                                                 contaminant_group='BTEXIIN',
                                                 include = False,
                                                 verbose = True,
                                                 )


###------------------------------------------------------------------------###
### Create activity plot linking contaminant concentration to metabolite occurence
### and NA screening

fig, ax = activity(data,
                   # save_fig='grift_NA_activity.png',dpi = 300
                   )
