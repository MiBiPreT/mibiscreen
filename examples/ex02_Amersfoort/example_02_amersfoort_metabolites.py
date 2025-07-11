"""Example of concentration data analysis.

For example field site data of Vetgas Amersfoort, the Netherlands.

For documented version with details to each step, consult similarly named
Jupyter-Notebook.

@author: Alraune Zech
"""

import matplotlib.pyplot as plt
import numpy as np
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
                                    verbose = False)

###------------------------------------------------------------------------###
### Visualization of metabolite concentrations per sample

plt.figure(figsize = [18,5])
plt.bar(np.arange(len(metabolites_total.values)),metabolites_total.values,label='all')
plt.xlabel('Samples')
plt.ylabel(r'Total metabolites concentration [$\mu$g/l]')
plt.title('Total concentration of metabolites per sample')

fig = plt.figure(figsize = [18,5])
sort_args = np.argsort(metabolites['metabolites_concentration'].values)
plt.bar(metabolites.sample_nr.values[sort_args],metabolites['metabolites_concentration'].values[sort_args],label='all')
plt.xlabel('Samples')
plt.ylabel(r'Total metabolites concentration [$\mu$g/l]')
plt.title('Total concentration of metabolites per sample')
fig.autofmt_xdate(bottom=0.2, rotation=30, ha='right', which='major')

###------------------------------------------------------------------------###
### Visualization of metabolite count per sample

plt.bar(np.arange(len(metabolites_count.values)),np.sort(metabolites_count.values))
plt.xlabel('Samples')
plt.ylabel('Total number')
plt.title('Total number of metabolites per sample')
# plt.legend()

fig = plt.figure(figsize = [18,5])
sort_args = np.argsort(metabolites_count.values)
plt.bar(metabolites.sample_nr.values[sort_args],metabolites_count.values[sort_args],label='all')
plt.xlabel('Samples')
plt.ylabel(r'Total metabolites count')
plt.title('Total counts of metabolites per sample')
fig.autofmt_xdate(bottom=0.2, rotation=30, ha='right', which='major')

###------------------------------------------------------------------------###
### Relating Metabolite activity to electron availability

contaminants_raw,_ = mbs.load_excel(file_path,
                                    sheet_name = 'contaminants',
                                    verbose = False)
contaminants,units = mbs.standardize(contaminants_raw,verbose = False)
environment_raw,_ = mbs.load_excel(file_path,
                                    sheet_name = 'environment',
                                    verbose = False)
environment,units = mbs.standardize(environment_raw,verbose = False)

mbs.total_contaminant_concentration(contaminants,include = True)
mbs.total_metabolites_count(metabolites,include = True)
data_NA = mbs.merge_data([environment,contaminants,metabolites])
mbs.sample_NA_traffic(data_NA,include = True)

data_activity =  mbs.activity_data_prep(data_NA)
data_activity['tot_cont'] = data_activity['tot_cont']*0.001

#fig, ax = mbs.activity_plot(data_activity)
fig, ax = mbs.activity_plot(data_activity,
                        figsize = [6,4],
                        textsize = 12,
                        xscale = 'log',
                        markersize = 60,
                        loc='center right',
                        xlabel = r"Concentration contaminants [mg/L]",
                        #save_fig = 'activity.png'
                        )

