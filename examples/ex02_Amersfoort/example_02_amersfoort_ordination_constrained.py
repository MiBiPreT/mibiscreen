"""Constrained Ordination including plots for Amersfoort data.

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

###------------------------------------------------------------------------###
### Load and standardize data of contaminants
dna_raw,units = mbs.load_excel(file_path,
                           sheet_name = 'sequencing',
                           verbose = verbose)

dna,units = mbs.standardize(dna_raw,
                        reduce = False,
                        verbose = verbose)


###------------------------------------------------------------------------###
### specify quantities to include in the analysis

#selected group of contaminant to analyse
contaminant_group = ['benzene','toluene','ethylbenzene','pm_xylene','indene','naphthalene']

#selected group of geochemical parameters to include to the analysis
geochemicals_group = ['nitrate','sulfate','redoxpot','iron2','manganese2']

#list of sequencing data to include to the analysis
variables_dna = ['Total bacteria 16SRrna', 'Benzene carboxylase', 'NirS', 'NarG', 'BssA SRB',
                 'BssA nitraat', 'Peptococcus']

###------------------------------------------------------------------------###
### Data selection and preproocessing

#extract data of geochemical quantities of interest
geochem_selected = environment[['sample_nr']+geochemicals_group]

#extract data of contaminant of interest
cont_selected = contaminants[['sample_nr']+contaminant_group]

#extend data of contaminants with a few additional variables of interest
mbs.total_concentration(cont_selected,
                    include = True,
                    verbose = verbose)
cont_selected.loc[:, 'BT_ratio'] = cont_selected.loc[:,'benzene']/cont_selected.loc[:,'toluene']*100
cont_selected.loc[:,'TB_ratio'] = cont_selected.loc[:,'toluene']/cont_selected.loc[:,'benzene']*100
contaminant_group_analysis = list(cont_selected.columns)
contaminant_group_analysis.remove('sample_nr')

### concatenate all relevant data
data_ordination = mbs.merge_data([geochem_selected,cont_selected,dna],clean = True)

### store data for statistical analysis in separate excel file
#data_ordination.to_excel('./ordination_data.xlsx')

###------------------------------------------------------------------------###
# Data preprocessing (filtering and transformation) for PCA

data_pca = data_ordination.copy()

mbs.filter_values(data_pca,
              replace_NaN = 'zero',
              inplace = True,
              verbose = True)

# if (part of) data is log-transformed (before standardization):
# transform_values(data_pcr,
#                  name_list = variables_dna,
#                  how = 'log_scale',
#                  inplace = True,
#                  )

mbs.transform_values(data_pca,
                 how = 'standardize',
                 inplace = True,
                 )

###------------------------------------------------------------------------###
# Data preprocessing (filtering and transformation) for CCA

data_cca = data_ordination.copy()

mbs.filter_values(data_cca,
              replace_NaN = 'average',  #'remove' #'zero'
              inplace = True,
              verbose = True)

mbs.transform_values(data_cca,
                 name_list = variables_dna,
                 how = 'log_scale',
                 inplace = True,
                 )

###------------------------------------------------------------------------###
# Data preprocessing (filtering and transformation) for RDA

data_rda = data_ordination.copy()

mbs.filter_values(data_rda,
              replace_NaN = 'zero',
              # replace_NaN = 'average',
              # replace_NaN = 'remove',
              inplace = True,
              verbose = True)

### if (part of) data is log-transformed (before standardization):
mbs.transform_values(data_rda,
                  name_list = variables_dna,
                  how = 'log_scale',
                  inplace = True,
                  )

mbs.transform_values(data_rda,
                  how = 'standardize',
                  inplace = True,
                  )

###------------------------------------------------------------------------###
### perform PCA and plot results

pca_output = mbs.pca(data_pca,
                        independent_variables = contaminant_group_analysis + geochemicals_group,
                        dependent_variables = variables_dna,
                        verbose = True)

fig, ax = mbs.ordination_plot(ordination_output=pca_output,
                plot_scores = False,
                plot_loadings = True,
                rescale_loadings_scores = False,
                title = "Unconstrained Ordination PCA",
                # axis_ranges = [-0.2,0.4,-0.4,0.6],
                # save_fig = 'pca_dna.png',
                )

###------------------------------------------------------------------------###
### perform CCA and plot results

cca_output = mbs.cca(data_cca,
                  independent_variables = contaminant_group_analysis + geochemicals_group,
                  dependent_variables = variables_dna,
                  verbose = True)

fig, ax = mbs.ordination_plot(ordination_output=cca_output,
                plot_scores = False,
                plot_loadings = True,
                rescale_loadings_scores = False,
                title ="Constrained Ordination CCA",
                # save_fig = 'cca_dna.png',
                )

# ###------------------------------------------------------------------------###
# ### perform RDA and plot results

rda_output = mbs.rda(data_rda,
                  independent_variables = contaminant_group_analysis + geochemicals_group,
                  dependent_variables = variables_dna,
                  verbose = True)

fig, ax = mbs.ordination_plot(ordination_output=rda_output,
                plot_scores = False,
                plot_loadings = True,
                rescale_loadings_scores = False,
                title = "Constrained Ordination RDA",
                # axis_ranges = [-0.6,0.8,-0.8,1.0],
                # save_fig = 'rda_dna.png',
                )
