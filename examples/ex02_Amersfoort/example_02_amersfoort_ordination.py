"""Ordination plots for Amersfoort data.

Example of diagnostic plotting using ordination with contaminant data from Amersfoort site.

@author: Alraune Zech
"""

#import pandas as pd


from mibipret.data.load_data import load_excel
from mibipret.data.check_data import standardize, standard_names
#from mibipret.data.set_data import merge_data, extract_data

# from mibipret.analysis.reduction.transformation import filter_values,transform_values
from mibipret.analysis.reduction.ordination import pca,cca,rda
from mibipret.visualize.ordination_plot import ordination_plot

import sys
path = '/home/alraune/GitHub/MiBiPreT/mibipret/mibipret/analysis/reduction'
sys.path.append(path) # append the path to module
from transformation import filter_values,transform_values

path = '/home/alraune/GitHub/MiBiPreT/mibipret/mibipret/data'
sys.path.append(path) # append the path to module
from set_data import merge_data, extract_data


###------------------------------------------------------------------------###
### Script settings
verbose = False #True

###------------------------------------------------------------------------###
### File path settings
file_path = './amersfoort.xlsx'
#file_standard = './grift_BTEXNII_standard.csv'

###------------------------------------------------------------------------###
### Load and standardize data of environmental quantities/chemicals
environment_raw,units = load_excel(file_path,
                                    sheet_name = 'environment',
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
                                  reduce = False,
                                  verbose = verbose)


data = merge_data([environment,contaminants],clean = True)
#display(data)


variables_1 = standard_names(['Sum GC'])
variables_2 = standard_names(['nitrate','pH','nitrite','sulfate','Redox','EC','DOC',"Mn","Fe"])


data_null = extract_data(data,
             name_list = variables_1 + variables_2,
             keep_setting_data = True,
             inplace = True)

filter_values(data_null, 
              replace_NaN = 'remove', 
              inplace = True,
              verbose = True)

transform_values(data_null,
                 name_list = variables_1,
                 how = 'log_scale',
                 inplace = True,
                 )

transform_values(data_null,
                  name_list = variables_1,
                  how = 'standardize',
                  inplace = True,
                  )

transform_values(data_null,
                  name_list = variables_2,
                  how = 'standardize',
                  inplace = True,
                )

ordination_output = pca(data_null,
                        independent_variables = variables_1+variables_2,
                        verbose = True)

# # ordination_output = cca(df,
# #                         independent_variables = environment,
# #                         dependent_variables = species,
# #                   )

# # ordination_output = rda(data,
# #                         independent_variables = environment,
# #                         dependent_variables = species,
# #                   )
# # loadings_independent = ordination_output["loadings_independent"]
# # names_independent = ordination_output["names_independent"]
# # loadings_dependent = ordination_output["loadings_dependent"]
# # names_dependent = ordination_output["names_dependent"]
# # loadings = np.append(loadings_independent, loadings_dependent, axis=0)

fig, ax = ordination_plot(ordination_output=ordination_output,
                plot_scores = True, 
                plot_loadings = True,
                rescale_loadings_scores = True, 
                # plot_scores = False, 
                # axis_ranges = [-0.6,0.8,-0.8,1.0],
                # save_fig = 'save3.png',
                )