#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Activity plot.

@author: alraune
"""

import copy
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mibiscreen.data.settings.standard_names import name_metabolites_variety
from mibiscreen.data.settings.standard_names import name_na_traffic_light
from mibiscreen.data.settings.standard_names import name_total_contaminants

DEF_settings = dict(
    figsize = [3.75,2.8],
    textsize = 10,
    markersize = 45,
    ec = 'k',
    lw = 0.5,
    loc = 'lower right',
    dpi = 300,
    )

def activity(
        data,
        save_fig=False,
        **kwargs,
        ):
    """Function creating activity plot.

    Activity plot showing scatter of total number of metabolites vs total concentration
    of contaminant per well with color coding of NA traffic lights: red/yellow/green
    corresponding to no natural attenuation going on (red), limited/unknown NA activity (yellow)
    or active natural attenuation (green)

    Input
    ----------
        data: list or pandas.DataFrame
            quantities required in plot:
                - total concentration of contaminants per sample
                - total count of metabolites per sample
                - traffic light on NA activity per sample
            if DataFrame, it contains the three required quantities with their standard names
            if list of arrays: the three quantities are given order above
            if list of pandas-Series, quantities given in standard names
        save_fig: Boolean or string, optional, default is False.
            Flag to save figure to file with name provided as string. =
        **kwargs: dict
            dictionary with plot settings

    Output
    -------
        fig : Figure object
            Figure object of created activity plot.
        ax :  Axes object
            Axes object of created activity plot.

    """
    settings = copy.copy(DEF_settings)
    settings.update(**kwargs)

    ### ---------------------------------------------------------------------------
    ### Handling of input data
    if isinstance(data, pd.DataFrame):
        meta_count = data[name_metabolites_variety].values
        tot_cont = data[name_total_contaminants].values
        well_color = data[name_na_traffic_light].values
    elif isinstance(data, list) and len(data)>=3:
        if isinstance(data[0], pd.Series) and isinstance(data[1], pd.Series) and isinstance(data[2], pd.Series):
            for series in data:
                if series.name == name_metabolites_variety:
                    meta_count = series.values
                if series.name == name_total_contaminants:
                    tot_cont = series.values
                if series.name == name_na_traffic_light:
                    well_color = series.values
        elif isinstance(data[0], (np.ndarray, list)):
            tot_cont = data[0]
            meta_count = data[1]
            well_color = data[2]
            # print("MATCH")
        else:
            raise ValueError("List elements in data must be lists, np.arrays or pd.series.")
        if len(tot_cont) != len(meta_count) or len(tot_cont) != len(well_color):
            raise ValueError("Provided arrays/lists/series of data must have the same length.")
    else:
        raise ValueError("Data needs to be DataFrame or list of at least three lists/np.arrays/pd.series.")

    if len(tot_cont) <= 1:
        raise ValueError("Too little data for activity plot. At least two values per quantity required.")

    ### ---------------------------------------------------------------------------
    ### Creating Figure
    fig, ax = plt.subplots(figsize=settings['figsize'])
    ax.scatter(tot_cont,
               meta_count,
               c=well_color,
               zorder = 3,
               s = settings['markersize'],
               ec = settings['ec'],
               lw = settings['lw'],
               )

    ### generate legend labels
    if "green" in well_color:
        ax.scatter([], [],
                   label="available",
                   c="green",
                   s = settings['markersize'],
                   ec = settings['ec'],
                   lw = settings['lw'],
                   )
    if "y" in well_color:
        ax.scatter([], [],
                   label="unknown",
                   c="y",
                   s = settings['markersize'],
                   ec = settings['ec'],
                   lw = settings['lw'],
                   )
    if "red" in well_color:
        ax.scatter([], [],
                   label="depleted",
                   c="red",
                   s = settings['markersize'],
                   ec = settings['ec'],
                   lw = settings['lw'],
                   )

    ### ---------------------------------------------------------------------------
    ### Adapt plot optics
    ax.set_xlabel(r"Concentration contaminants [$\mu$g/L]",fontsize=settings['textsize'])
    ax.set_ylabel("Metabolite variety", fontsize=settings['textsize'])
    ax.grid()
    ax.minorticks_on()
    ax.tick_params(axis="both", which="major", labelsize=settings['textsize'])
    ax.tick_params(axis="both", which="minor", labelsize=settings['textsize'])
    plt.legend(title = 'Electron acceptors:',loc =settings['loc'], fontsize=settings['textsize'] )
    fig.tight_layout()

    ### ---------------------------------------------------------------------------
    ### Save figure to file if file path provided
    if save_fig is not False:
        try:
            plt.savefig(save_fig,dpi = settings['dpi'])
            print("Save Figure to file:\n", save_fig)
        except OSError:
            print("WARNING: Figure could not be saved. Check provided file path and name: {}".format(save_fig))

    return fig, ax
