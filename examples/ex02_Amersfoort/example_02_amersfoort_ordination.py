"""Unconstrained Ordination (PCA) with plot for Amersfoort data.

Example of diagnostic plotting using ordination with contaminant data from Amersfoort site.

@author: Alraune Zech
"""

import mibiscreen as mbs

###------------------------------------------------------------------------###
### Script settings
verbose = False #True

###------------------------------------------------------------------------###
### File path settings
file_path = './amersfoort.xlsx'
#file_standard = './grift_BTEXNII_standard.csv'

###------------------------------------------------------------------------###
### Load and standardize data of environmental quantities/chemicals
environment_raw,units = mbs.load_excel(file_path,
                                    sheet_name = 'environment',
                                    verbose = verbose)

environment,units = mbs.standardize(environment_raw,
                                reduce = True,
                                verbose=verbose)

###------------------------------------------------------------------------###
### Load and standardize data of contaminants
contaminants_raw,units = mbs.load_excel(file_path,
                                    sheet_name = 'contaminants',
                                    verbose = verbose)

contaminants,units = mbs.standardize(contaminants_raw,
                                  reduce = False,
                                  verbose = verbose)


mbs.total_contaminant_concentration(contaminants,
                                include = True,
                                verbose = verbose)

data = mbs.merge_data([environment,contaminants],clean = True)
#display(data)

###------------------------------------------------------------------------###
variables_1 = mbs.standard_names(['total_contaminants'])
variables_2 = mbs.standard_names(['nitrate','pH','nitrite','sulfate','Redox','EC','DOC',"Mn","Fe"])


data_ordination = mbs.extract_data(data,
                  name_list = variables_1 + variables_2,
                  keep_setting_data = True,
                  )

mbs.filter_values(data_ordination,
              replace_NaN = 'remove',
              inplace = True,
              verbose = True)

mbs.transform_values(data_ordination,
                 name_list = variables_1,
                 how = 'log_scale',
                 inplace = True,
                 )

mbs.transform_values(data_ordination,
                 name_list = variables_1,
                  how = 'standardize',
                  inplace = True,
                  )

mbs.transform_values(data_ordination,
                 name_list = variables_2,
                 how = 'standardize',
                 inplace = True,
                 )

###------------------------------------------------------------------------###
ordination_output = mbs.pca(data_ordination,
                        independent_variables = variables_1+variables_2,
                        verbose = True)

fig, ax = mbs.ordination_plot(ordination_output=ordination_output,
                plot_scores = True,
                plot_loadings = True,
                rescale_loadings_scores = True,
                title = "Unconstrained Ordination PCA",
                # plot_scores = False,
                # axis_ranges = [-0.6,0.8,-0.8,1.0],
                # save_fig = 'Amersfoort_PCA.png',
                )

