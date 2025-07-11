"""Example of concentration data analysis.

For example field site data of Vetgas Amersfoort, the Netherlands.

For documented version with details to each step, consult similarly named
Jupyter-Notebook.

@author: Alraune Zech
"""

import mibiscreen as mbs

###------------------------------------------------------------------------###
### Script settings
verbose = False

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
### Basic analysis of contaminant concentrations per sample

mbs.total_concentration(contaminants,
                        name_list = 'all',
                        include_as = "concentration_contaminants",
                        verbose = verbose)


mbs.total_concentration(contaminants,
                        name_list = 'BTEXIIN',
                        include_as = "concentration_BTEXIIN",
                        verbose = verbose,
                        )


mbs.total_concentration(contaminants,
                        name_list = 'BTEX',
                        include_as = "concentration_BTEX",
                        verbose = verbose,
                        )

## the upper three are equivalent to:
# mbs.total_contaminant_concentration(contaminants,
#                                     contaminant_group = 'all_cont',
#                                     include = True,
#                                     verbose = verbose)

# mbs.total_contaminant_concentration(contaminants,
#                                     contaminant_group = 'BTEX',
#                                     include = True,
#                                     verbose = verbose)

# mbs.total_contaminant_concentration(contaminants,
#                                     contaminant_group = 'BTEXIIN',
#                                     include = True,
#                                     verbose = verbose)


mbs.total_concentration(contaminants,
                        name_list = ['benzene','toluene'],
                        include_as = "concentration_BT",
                        verbose = verbose,
                        )

###------------------------------------------------------------------------###
### Visualization of contaminant concentrations per sample

list_contaminants = ['concentration_contaminants','concentration_BTEXIIN','concentration_BTEX',
                     'concentration_BT','benzene']

mbs.contaminants_bar(contaminants,
                      list_contaminants,
                      list_labels = ['all','BTEXIIN','BTEX','BT','B'],
                      sort = True,
                      figsize = [5.2,3],
                      textsize = 12,
                      save_fig = 'contaminants_bar.png',
                      loc='upper left',
                      title_text = False,
                      )

###------------------------------------------------------------------------###
### Basic analysis of number of contaminants per sample

mbs.total_count(contaminants,
                name_list = 'all',
                include_as = "count_contaminants",
                verbose = verbose)

mbs.total_count(contaminants,
                name_list = 'BTEXIIN',
                include_as = "count_BTEXIIN",
                verbose = verbose)

mbs.total_count(contaminants,
                name_list = 'BTEX',
                include_as = "count_BTEX",
                verbose = verbose)

mbs.total_count(contaminants,
                name_list = ['benzene'],
                include_as = "count_benzene",
                verbose = verbose)

list_counts = ['count_contaminants','count_BTEXIIN','count_BTEX','count_benzene']

###------------------------------------------------------------------------###
### Visualizatin of contaminant counts per sample

mbs.contaminants_bar(contaminants,
                     list_counts,
                     list_labels = ['all','BTEXIIN','BTEX','B'],
                     sort = True,
                     figsize = [5.2,3],
                     textsize = 12,
                     ylabel = 'Total count',
                     yscale = 'linear',
                     save_fig = 'count_bar.png',
                     loc='upper left',
                     title_text = False,
                     )


# ###------------------------------------------------------------------------###
# ### Evaluation of intervention threshold exceedance

# threshold = mbs.thresholds_for_intervention_ratio(data,
#                                 verbose = verbose,
#                                 include = False,
#                                 contaminant_group='BTEXIIN'
#                                 )

# quantities = ['naphthalene','indene','pm_xylene','o_xylene','ethylbenzene','toluene','benzene']

# data_thresh = pd.DataFrame(index = data.index)

# for cont in quantities:
#     th_value = properties[cont]['thresholds_for_intervention_NL']
#     data_thresh[cont+'_thr_ratio'] = data[cont]/th_value

# plt.figure(num=7)
# plt.barh(quantities,data_thresh.iloc[9],color = 'lightblue')
# plt.plot([1,1],[-0.5,6.5],'k--')
# plt.xlabel(r'ratio to threshold concentration $sC/C_\mathrm{threshold}$')

# plt.figure(num=8)
# plt.barh(quantities,data_thresh.iloc[11],color = 'tomato')
# plt.plot([1,1],[-0.5,6.5],'k--')
# plt.xlabel(r'ratio to threshold concentration $C/C_\mathrm{threshold}$')

# plt.figure(num=9)
# plt.barh(quantities,data_thresh.iloc[31],color = 'olive')
# plt.plot([1,1],[-0.5,6.5],'k--')
# plt.xlabel(r'ratio to threshold concentration $C/C_\mathrm{threshold}$')


