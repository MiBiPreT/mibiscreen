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

mbs.total_concentration(contaminants,
                        name_list = ['benzene','toluene'],
                        include_as = "concentration_BT",
                        verbose = verbose,
                        )

## the first three are equivalent to:
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
                     loc='upper left',
                     title_text = False,
                     # save_fig = 'count_bar.png',
                     )


###------------------------------------------------------------------------###
### Evaluation of threshold exceedance

data_thresh_ratio = mbs.thresholds_for_intervention_ratio(contaminants)

quantities = ['toluene','naphthalene','indene','pm_xylene','ethylbenzene','o_xylene','benzene']

fig,ax = mbs.threshold_ratio_bar(data_thresh_ratio,
                                 list_samples =  [31,9,11],
                                 figsize = [12,3],
                                 list_colors = ['olive','lightblue','tomato'],
                                 nrows=1,ncols=3,
                                 sharey = True,
                                 grid = True,
                                )

mbs.threshold_ratio_bar(data_thresh_ratio,
                        list_samples = [9],
                        list_labels =  quantities,
                        figsize = [6,3],
                        unity_line = True,
                        title_text= 'Evaluation of threshold exceedance for BTEXIIN',
                        )

