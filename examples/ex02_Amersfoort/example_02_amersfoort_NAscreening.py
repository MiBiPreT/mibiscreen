"""Example of data analysis of contaminant data from VetGas, Amerfoort field site.

@author: Alraune Zech
"""

import mibiscreen as mbs

###------------------------------------------------------------------------###
### Script settings
verbose = True

###------------------------------------------------------------------------###
### File path settings
file_path = './amersfoort.xlsx'

###------------------------------------------------------------------------###
### Load and standardize data of contaminants
contaminants_raw,units = mbs.load_excel(file_path,
                                        sheet_name = 'contaminants',
                                        verbose = verbose)

contaminants,units = mbs.standardize(contaminants_raw,
                                     reduce = True,
                                     verbose=verbose)

###------------------------------------------------------------------------###
### Load and standardize data of environmental quantities/chemicals
environment_raw,_ = mbs.load_excel(file_path,
                                   sheet_name = 'environment')
environment,units = mbs.standardize(environment_raw)

###------------------------------------------------------------------------###
### Electron balance: Simple NA screening analysis

mbs.reductors(environment,
              include = True,
              ea_group = 'ONS')

mbs.oxidators(contaminants,include = True,
              contaminant_group='BTEX')
mbs.oxidators(contaminants,include = True,
              contaminant_group='BTEXIIN')

data_NA = mbs.merge_data([environment,contaminants])
mbs.electron_balance(data_NA,include = True)

na_traffic = mbs.sample_NA_traffic(data_NA,include = True)

###------------------------------------------------------------------------###
### Visualization of Electron balance

electron_balance_bar_dict = mbs.electron_balance_bar_data_prep(data_NA)
mbs.electron_balance_bar(electron_balance_bar_dict,
                         sample_nr = True,
                         figsize = [12,3],
                         xtick_autorotate = True,
                         )

electron_balance_bar_dict = mbs.electron_balance_bar_data_prep(data_NA,
                                                               list_samples = [21,11,20,3,17,18])
mbs.electron_balance_bar(electron_balance_bar_dict,
                        loc = 'upper right')

