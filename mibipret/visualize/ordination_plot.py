#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 14:06:50 2024

@author: alraune
"""

import numpy as np
import pandas as pd
import copy
import matplotlib.pyplot as plt
plt.close('all')

from ordination import pca #, cca, rda

DEF_settings = dict(
    figsize = [3.75,3.75],
    dpi = 300,
    textsize = 10,
    arrow_color_head = 'blue',
    arrow_color = 'red',
    arrow_width = 0.002, 
    arrowhead_width = 0.02, 
    arrowhead_length = 0.02,     
    score_color = 'gray',
    score_edgecolor = 'gray',
    score_facecolor = 'none',
    score_marker = 'o',
    score_marker_size = 45,       
    # adjust_text = True, 
    axis_ranges = False,
    )

data = pd.read_csv('data_pcs.csv')

# pca_results = pca(data,verbose = True)
pca_output = pca(data,
                  # select_columns = ['nitrate','pH','nitrite','sulfate','Redox'],
                  # n_comp=2,
                  verbose = True)

print(pca_output)
data = pca_output 
# mibipret.visualize.ordination(data=pca_output)

# def ordination_plot(data,
#                     plot_loadings = True, 
#                     plot_scores = True, 
#                     rescale_loadings_scores = False, 
#                     scale_focus = "Loadings", 
#                     save_fig=False,
#                     **kwargs,
#                     ):
#     """Function creating ordination plot.

#         Based on ordination analysis providing ordination loadings and scores.

#     """            

# Adjust_text = True, 

save_fig = 'save.png'
plot_loadings = True
plot_scores = True    #False #
rescale_loadings_scores = False #True 
scale_focus = "loadings"

settings = copy.copy(DEF_settings)
# settings.update(**kwargs)

### ---------------------------------------------------------------------------
### check on completeness of input data
if not isinstance(data,dict):
    raise ValueError()
elif "loadings" not in data.keys():
    raise ValueError()
elif "scores" not in data.keys():
    raise ValueError()

loadings = data["loadings"]
scores = data["scores"]

### ---------------------------------------------------------------------------
### Rescale data given plot specifics

# Determing the largest values in the PCA scores for axis dimensions.
max_load = np.max(np.abs(loadings))
if len(scores):
    max_score = np.max(np.abs(scores))
else:
    max_score = 1    

# Rescale scores and loadings to range between -1 and 1
if rescale_loadings_scores:
    if max_load >= 1:
        loadings = loadings / max_load
        max_load = np.max(np.abs(loadings))
    if max_score >= 1:
        scores = scores / max_score
        max_score = np.max(np.abs(scores))

if settings['axis_ranges'] is not False:
    # Takes the given axis dimensions for both ordination axes
    x_lim_neg,x_lim_pos,y_lim_neg,y_lim_pos = settings['axis_ranges']
else:
    # Adjusts axis dimensions for both ordination axes to data
    if plot_scores and plot_loadings:
        # When plotting both scores and loadings, scores or loadings are scaled depending on the extent of the other. Depends on the input of Scale_focus.
        if scale_focus == "loadings":
            scores = scores * max_load
        elif scale_focus == "scores":
            loadings = loadings * max_score
        full_coords = np.append(loadings, scores, axis=0)
    elif plot_loadings:
        full_coords = loadings
    else:
        full_coords = scores

    x_lim_pos = 0.11*np.ceil(np.max(full_coords[:,0])*10)
    y_lim_pos = 0.11*np.ceil(np.max(full_coords[:,1])*10)
    x_lim_neg = 0.11*np.floor(np.min(full_coords[:,0])*10)
    y_lim_neg = 0.11*np.floor(np.min(full_coords[:,1])*10)

### ---------------------------------------------------------------------------
### Create Figure, finally!    
plt.figure(figsize = settings['figsize'],dpi=settings['dpi'])

# Plotting the ordination scores by iterating over every coordinate in the scores array, if the Plot_scores parameter is set to true.
if plot_scores:
    for i, (x, y) in enumerate(scores):
        plt.scatter(x, y, 
                    color=settings['score_color'], 
                    marker = settings['marker'],
                    s = settings['s'],
                    facecolor=settings['facecolor'], 
                    edgecolor=settings['edgecolor'],
                    zorder = 10,
                    # **settings,
                    )
        # Plotting the name of the scores and storing it in a list for the purpose of adjusting the position later
        # tex = plt.text(x, y, wells[i], color='black', fontsize = settings['textsize'])
        # texts.append(tex)

# Plotting the ordination loadings by iterating over every coordinate in the loadings array, if the Plot_scores parameter is set to true.
if plot_loadings:
    for i, (x, y) in enumerate(loadings):
        # Plots Environmental and Species variables with different colours and text formatting.
        # if heads[i] in Environment_head:
        #     plt.arrow(0, 0, x, y, 
        #               color='blue', 
        #               width = Arrow_width, 
        #               head_length = Arrowhead_length, 
        #               head_width = Arrowhead_width
        #               )
        #     #Plotting the name of the loading and storing it in a list for the purpose of adjusting the position later
        #     tex = plt.text(x, y, heads[i], 
        #                    color='black', 
        #                    fontstyle='italic', 
        #                    fontsize = Loadingtext_font
        #                    )
        #     c_arrow = settings['arrow_color_head']
        # else:
        #     c_arrow = settings['arrow_color']
        #     #Plotting the name of the loading and storing it in a list for the purpose of adjusting the position later
        #     tex = plt.text(x, y, heads[i], 
        #                    color='black', 
        #                    weight="bold", 
        #                    fontsize = Loadingtext_font
        #                    )
        # texts.append(tex)
        c_arrow = settings['arrow_color_head']
        plt.arrow(0, 0, x, y, 
                  color=c_arrow, 
                  width = settings['arrow_width'], 
                  head_length = settings['arrow_head_length'], 
                  head_width = settings['arrow_head_width'],
                  zorder = 9,
                  )

# Plotting lines that indicate the origin
plt.plot([-1, 1], [0, 0], color='grey', linewidth=0.75, linestyle='--')
plt.plot([0, 0], [-1, 1], color='grey', linewidth=0.75, linestyle='--')
 
### ---------------------------------------------------------------------------
### Adapt plot optics
       
# Setting the x and y axis limits with the previously determined values
plt.xlim(x_lim_neg, x_lim_pos)
plt.ylim(y_lim_neg, y_lim_pos)

# Plots the axis title with the percentage of variation explained if the method was PCA
if data["method"]=='pca':
    percent_explained = data["percent_explained"]
    plt.xlabel('PC1 (%s%%)' % percent_explained[0], fontsize = settings['textsize'])
    plt.ylabel('PC2 (%s%%)' % percent_explained[1], fontsize = settings['textsize'])
# Otherwise just plots a general axis title.
else:
    plt.xlabel('ordination axis 1', fontsize = settings['textsize'])
    plt.ylabel('ordination axis 2', fontsize = settings['textsize'])


# Changing the axis ticks and removing all but the first and last tick labels
# ax = plt.gca()
# x_ticks = np.around(ax.get_xticks(), decimals=1)
# y_ticks = np.around(ax.get_yticks(), decimals=1)
# x_tick_labels = [str(x_ticks[0])] + [''] * (len(x_ticks) - 2) + [str(x_ticks[-1])]
# y_tick_labels = [str(y_ticks[0])] + [''] * (len(y_ticks) - 2) + [str(y_ticks[-1])]
# ax.set_xticklabels(x_tick_labels, fontsize = settings['textsize'])
# ax.set_yticklabels(y_tick_labels, fontsize = settings['textsize'])
plt.tick_params(axis="both",which="major",labelsize=settings['textsize']-2)

# if settings['adjust_text']:
#     try:
#         from adjustText import adjust_text
#         import warnings
#         #adjust_text gives an irrelevant warning for the purpose of this scipt. The statement below will make sure that warning does not show up.
#         warnings.filterwarnings("ignore")
#         adjust_text(texts)
#     except() 

### ---------------------------------------------------------------------------
### Save figure to file if file path provided

plt.tight_layout()
if save_fig is not False:
    try:
        plt.savefig(save_fig)
        print("Save Figure to file:\n", save_fig)
    except OSError:
        print("WARNING: Figure could not be saved. Check provided file path and name: {}".format(save_fig))

# return fig, ax
