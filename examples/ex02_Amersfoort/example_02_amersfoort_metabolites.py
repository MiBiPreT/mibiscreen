"""Example of concentration data analysis.

For example field site data of Vetgas Amersfoort, the Netherlands.

For documented version with details to each step, consult similarly named
Jupyter-Notebook.

@author: Alraune Zech
"""

import mibiscreen as mbs

file_path = './amersfoort.xlsx'

###------------------------------------------------------------------------###
### Load and standardize data of metabolites

metabolites_raw,units = mbs.load_excel(file_path,
                                       sheet_name = 'metabolites',
                                       )

metabolites,units = mbs.standardize(metabolites_raw,
                                    reduce = False,
                                    verbose = False,
                                    )

###------------------------------------------------------------------------###
### Metabolites Concentration Analysis
metabolites_total = mbs.total_concentration(metabolites,
                                            name_list = 'all',
                                            include_as = False,
                                            )

metabolites_count = mbs.total_count(metabolites,
                                    name_list = 'all',
                                    include_as = False,
                                    )
###------------------------------------------------------------------------###
### Including total concentration and total count of metabolites per sample to dataframe

mbs.total_metabolites_concentration(metabolites,
                                    include = True,
                                    verbose = True)

mbs.total_metabolites_count(metabolites,
                            include = True,
                            verbose = True)

###------------------------------------------------------------------------###
### Visualization of metabolite concentrations per sample

mbs.contaminants_bar(metabolites,
                      list_contaminants = ['metabolites_concentration'],
                      list_labels = ['all metabolites'],
                      figsize = [18,5],
                      textsize = 12,
                      ylabel = r'Total metabolites concentration [$\mu$g/l]',
                      loc='upper left',
                      title_text = 'Total concentration of metabolites per sample',
                      # save_fig = 'metabolites_bar.png',
                      )

mbs.contaminants_bar(metabolites,
                     list_contaminants = ['metabolites_concentration'],
                     list_labels = ['all metabolite'],
                     sort = True,
                     name_sample = True,
                     figsize = [18,5],
                     textsize = 12,
                     ylabel = r'Total metabolites concentration [$\mu$g/l]',
                     loc='upper left',
                     title_text = 'Total concentration of metabolites per sample',
                     xtick_autorotate = True,
                      # save_fig = 'metabolites_bar.png',
                     )
###------------------------------------------------------------------------###
### Visualization of metabolite count per sample

mbs.contaminants_bar(metabolites,
                     list_contaminants = ['metabolites_count'],
                     list_labels = ['total metabolites count'],
                     sort = True,
                     name_sample = True,
                     figsize = [18,5],
                     textsize = 12,
                     ylabel = r'Total metabolites count',
                     loc='upper left',
                     title_text = 'Total count of metabolites per sample',
                     xtick_autorotate = True,
                      # save_fig = 'metabolites_count_bar.png',
                     )

###------------------------------------------------------------------------###
###------------------------------------------------------------------------###
### Relating Metabolite activity to electron availability
###------------------------------------------------------------------------###
###------------------------------------------------------------------------###

### Load and preprocess additional data needed
contaminants_raw,_ = mbs.load_excel(file_path,
                                    sheet_name = 'contaminants',
                                    verbose = False)
contaminants,units = mbs.standardize(contaminants_raw,verbose = False)
environment_raw,_ = mbs.load_excel(file_path,
                                    sheet_name = 'environment',
                                    verbose = False)
environment,units = mbs.standardize(environment_raw,verbose = False)


###------------------------------------------------------------------------###
### Perform data analysis needed
mbs.total_contaminant_concentration(contaminants,include = True)
mbs.total_metabolites_count(metabolites,include = True)
data_NA = mbs.merge_data([environment,contaminants,metabolites])
mbs.sample_NA_traffic(data_NA,include = True)

###------------------------------------------------------------------------###
### Data preparation for plot and plotting

data_activity =  mbs.activity_data_prep(data_NA)
data_activity['tot_cont'] = data_activity['tot_cont']*0.001 # rescale unit

fig, ax = mbs.activity_plot(data_activity,
                        figsize = [6,4],
                        textsize = 12,
                        xscale = 'log',
                        markersize = 60,
                        loc='center right',
                        xlabel = r"Concentration contaminants [mg/L]",
                        #save_fig = 'activity.png'
                        )

