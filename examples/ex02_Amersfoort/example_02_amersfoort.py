"""Example of data analysis of contaminant data from Griftpark, Utrecht.

@author: Alraune Zech
"""

from mibipret.data.check_data import check_columns
from mibipret.data.check_data import check_units
from mibipret.data.check_data import check_values
from mibipret.data.check_data import standardize
from mibipret.data.load_data import load_excel

#import mibipret.analysis.sample.screening_NA as na
#from mibipret.visualize.activity import activity

###------------------------------------------------------------------------###
### Script settings
verbose = True

###------------------------------------------------------------------------###
### File path settings
file_path = './amersfoort.xlsx'

###------------------------------------------------------------------------###
### Load and standardize data of environmental quantities/chemicals
environment_raw,units = load_excel(file_path,
                                      sheet_name = 'environment',
                                      verbose = verbose)

###------------------------------------------------------------------------###
### Details of standardization process
column_names_known,column_names_unknown,column_names_standard = check_columns(
    environment_raw,
    verbose = verbose)
check_list = check_units(environment_raw,
                         verbose = verbose)
environment_pure = check_values(environment_raw,
                                verbose = verbose)

environment,units = standardize(environment_raw,
                                   reduce = True,
                                   verbose=verbose)

###------------------------------------------------------------------------###
### Load and standardize data of contaminants
contaminants_raw,units = load_excel(file_path,
                                       sheet_name = 'contaminants',
                                       verbose = verbose)

contaminants,units = standardize(contaminants_raw,
                                    reduce = True,
                                    verbose=verbose)

###------------------------------------------------------------------------###
### Load and standardize data of metabolites
metabolites_raw,units = load_excel(file_path,
                                    sheet_name = 'metabolites',
                                    verbose = verbose)

# column_names_known,column_names_unknown,column_names_standard = md.check_columns(metabolites_raw,
#                                                                              check_metabolites = True,
#                                                                              verbose = verbose,)
# check_list = md.check_units(metabolites_raw,
#                             check_metabolites = True,
#                             verbose = verbose)

# metabolites_pure = md.check_values(metabolites_raw,
#                                    check_metabolites = True,
#                                    verbose = verbose)

# metabolites,units = standardize(metabolites_raw,
#                                 reduce = True,
#                                 check_metabolites = True,
#                                 verbose=verbose)

# ###------------------------------------------------------------------------###
# ### perform NA screening step by step

# tot_reduct = na.reductors(data,verbose = verbose,ea_group = 'ONSFe')

# tot_oxi = na.oxidators(data,verbose = verbose, contaminant_group='BTEXIIN')
# #tot_oxi_nut = na.oxidators(data,verbose = verbose,nutrient = True)

# e_bal = na.electron_balance(data,verbose = verbose)

# na_traffic = na.NA_traffic(data,verbose = verbose)

# ###------------------------------------------------------------------------###
# ### Evaluation of intervention threshold exceedance

# tot_cont = na.total_contaminant_concentration(data,verbose = verbose,contaminant_group='BTEXIIN')

# na_intervention = na.thresholds_for_intervention(data,verbose = verbose,contaminant_group='BTEXIIN')

# ###------------------------------------------------------------------------###
# ### NA screening and evaluation of intervention threshold exceedance in one go

# ### run full NA screening with results in separate DataFrame
# data_na = na.screening_NA(data,verbose = verbose)

# ### run full NA screening with results added to data
# na.screening_NA(data,inplace = True,verbose = verbose)

# ###------------------------------------------------------------------------###
# ### Create activity plot linking contaminant concentration to metabolite occurence
# ### and NA screening

# fig, ax = activity(data)
