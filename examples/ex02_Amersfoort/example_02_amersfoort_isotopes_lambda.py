#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lambda plot of isotopes.

Script reproducing figure 8 in Paper van Leeuwen et al., 2022
'Anaerobic degradation of benzene and other aromatic hydrocarbons in a
tar-derived plume: Nitrate versus iron reducing conditions', J. of Cont. Hydrol

data provided on personal basis
Note: data does not match to data provided along manuscript, but is reconstructed
from different data files

@author: Alraune Zech
"""

import matplotlib.pyplot as plt
import numpy as np
import mibiscreen as mbs

###------------------------------------------------------------------------###
### Script settings
verbose = True
molecules = ['benzene','toluene','ethylbenzene','pm_xylene','naphthalene','indene']
molecules_analysis = []
###------------------------------------------------------------------------###

### File path settings
file_path = './amersfoort.xlsx'
# file_path = "./amersfoort_isotopes_match.csv"

###------------------------------------------------------------------------###
### Load and standardize data of isotopes
# isotopes_raw,units = md.load_csv(file_path,
#                                  verbose = verbose)

isotopes_raw,units = mbs.load_excel(file_path,
                                   sheet_name = 'isotopes',
                                   verbose = verbose)

isotopes,units = mbs.standardize(isotopes_raw,
                                reduce = True,
                                verbose=verbose)


###------------------------------------------------------------------------###
### Lambda regression and Lambda regression plot for single moleculeq

C_data,H_data = mbs.extract_isotope_data(isotopes,'toluene')
results = mbs.Lambda_regression(C_data,
                                H_data,
                                validate_indices = True,
                                verbose = True,
                                )
mbs.Lambda_plot(**results,
                title = 'toluene',
               fit_color = 'k',
               marker_color = 'C1',
               # save_fig = 'Amersfoort_isotope_Lambda_toluene.pdf'
               )

###------------------------------------------------------------------------###
### Lambda regression and Lambda regression plot for all molecules (separately)

for j,molecule in enumerate(molecules):

    C_data,H_data = mbs.extract_isotope_data(isotopes,molecule)

    results = mbs.Lambda_regression(C_data,
                                H_data,
                                validate_indices = True,
                                verbose = verbose,
                                )

    molecules_analysis.append(results)
    mbs.Lambda_plot(**results)

###------------------------------------------------------------------------###
### Lambda regression and plot of results of all molecules in one plot

plt.figure(j)
fig, axes = plt.subplots(figsize=[7.5,9],
                          ncols = 2,
                          nrows = 3)
ax = axes.flat
for j,molecule in enumerate(molecules):

    results =  molecules_analysis[j]

    x,y = results['delta_C'], results['delta_H']

    # Plot the scatter plot
    ax[j].scatter(x,y, zorder = 3,label = 'data')
    ax[j].set_title(molecule)
    ax[j].grid(True,zorder = 0)

    # plot trendlines
    polynomial = np.poly1d(results['coefficients'])
    trendline_x = np.linspace(np.min(x), np.max(x), 50)
    trendline_y = polynomial(trendline_x)
    ax[j].plot(trendline_x, trendline_y, label=r'$\Lambda = {:.0f}$'.format(results['coefficients'][0]))

    if j%2 == 0:
        ax[j].set_ylabel(r'$\delta^2$H')

    if j >= len(ax)-2:
        ax[j].set_xlabel(r'$\delta^{{13}}$C')

    ax[j].legend()

fig.tight_layout()
