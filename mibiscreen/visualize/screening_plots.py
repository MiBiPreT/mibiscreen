#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Activity plot.

@author: alraune
"""

import copy
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mibiscreen.data.settings.standard_names as names
from mibiscreen.data.set_data import determine_quantities
from mibiscreen.data.check_data import check_data_frame
from mibiscreen.analysis.sample.concentrations import thresholds_for_intervention_ratio

DEF_settings = dict(
    figsize = [3.75,2.8],
    textsize = 10,
    markersize = 45,
    ec = 'k',
    lw = 0.5,
    loc = 'lower right',
    dpi = 300,
    save_fig=False,
    )


def contaminants_bar(data,
                     list_contaminants = [names.name_total_contaminants],
                     list_labels = ['all'],
                     sort = False,
                     sample_nr = False,
                     xlabel = 'Samples',
                     ylabel = r'Total concentration [$\mu$g/l]',
                     yscale = 'log',
                     title_text = 'Total concentration of contaminants per sample',
                     save_fig = False,
                     **kwargs,
                     ):
    
    settings = copy.copy(DEF_settings)
    settings.update(**kwargs)

    if sort:
        sort_args = np.argsort(data[list_contaminants[0]].values)
    else:
        sort_args = np.arange(len(data[list_contaminants[0]].values))

    if sample_nr is False:        
        n_bars = np.arange(len(data[list_contaminants[0]].values))
    if sample_nr == 'sample_nr':
        n_bars = data[names.name_sample].values[sort_args]

    # if isinstance(samples, list):

    fig, ax = plt.subplots(figsize=settings['figsize'])

    for i,cont_group in enumerate(list_contaminants):
        plt.bar(n_bars,data[cont_group].values[sort_args],label=list_labels[i])
    
    ### ---------------------------------------------------------------------------
    ### Adapt plot optics
    plt.xlabel(xlabel,fontsize = settings['textsize'])
    plt.ylabel(ylabel,fontsize = settings['textsize'])
    plt.yscale(yscale)
    plt.legend(loc =settings['loc'],fontsize = settings['textsize'])
    plt.title(title_text,fontsize = settings['textsize'])
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

def electron_balance_bar_data_prep(data,
                                   sample_selection = False,
                                   ):

    electron_balance_bar_dict = dict()
  
    electron_balance_bar_dict['EA capacity'] = dict(
        height = data[names.name_total_reductors].values,
        color = 'C1',
        sample_nr = data[names.name_sample],
    )       
    electron_balance_bar_dict['BTEXIIN'] = dict(
        # height = data[names.name_total_oxidators_BTEXIIN],
        height = data['total_oxidators_BTEXIIN'].values,
        color = 'C0',
    )        
    electron_balance_bar_dict['BTEX'] = dict(
        # height = data[names.name_total_oxidators_BTEX],
        height = data['total_oxidators_BTEX'].values,
        color = 'C2',
    )     
    
    electron_balance_bar_dict['EA capacity minor'] = dict(
        height = data[names.name_total_reductors].where(data[names.name_e_balance] < 1, 0).values,
        color = 'C1',
    )       

    if sample_selection:
        for key, value in electron_balance_bar_dict.items():
            value['height'] = value['height'][sample_selection]
        electron_balance_bar_dict['EA capacity']['sample_nr'] = electron_balance_bar_dict['EA capacity']['sample_nr'][sample_selection]

    return electron_balance_bar_dict

def electron_balance_bar(electron_balance_bar_dict,
                         sample_nr = False,    
                         sort = False,
                         xlabel = 'Sample locations',
                         ylabel = r'Electron capacity/needed [mmol e-/l]',
                         yscale = 'linear',
                         title_text = 'Electron balance per sample',
                         save_fig = False,
                         **kwargs,
                         ):
    
    settings = copy.copy(DEF_settings)
    settings.update(**kwargs)

    if sort:
        sort_args = np.argsort(electron_balance_bar_dict['EA capacity']['height'])
    else:
        sort_args = np.arange(len(electron_balance_bar_dict['EA capacity']['height']))

    if sample_nr:        
        n_bars = electron_balance_bar_dict['EA capacity']['sample_nr'][sort_args]
    else:
        n_bars = np.arange(1,len(electron_balance_bar_dict['EA capacity']['height'])+1)

    fig, ax = plt.subplots(figsize=settings['figsize'])

    for key, value in electron_balance_bar_dict.items():
        # print(f"{key}: {value}")
        if key != 'EA capacity minor':
            plt.bar(n_bars,value['height'][sort_args],color = value['color'],label = key)
        else:
            plt.bar(n_bars,value['height'][sort_args],color = value['color'],zorder = 1)                 
    
    ### ---------------------------------------------------------------------------
    ### Adapt plot optics
    plt.xlabel(xlabel,fontsize = settings['textsize'])
    plt.ylabel(ylabel,fontsize = settings['textsize'])
    plt.yscale(yscale)
    plt.legend(loc =settings['loc'],fontsize = settings['textsize'])
    plt.title(title_text,fontsize = settings['textsize'])
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

def threshold_ratio_bar_data_prep(data,
                                  name_list = 'BTEXIIN',
                                  sample_selection = False,
                                  ):
    
    quantities, _ = determine_quantities(data.columns.to_list(),
                                         name_list = name_list,
                                         verbose = False)


    data_thresh_for_bar = thresholds_for_intervention_ratio(data,
                                            include = False,
                                            keep_setting_data = False,
                                            verbose = False)

    if sample_selection:
        data_thresh_for_bar = data_thresh_for_bar.iloc[sample_selection]

    return quantities,data_thresh_for_bar

def threshold_ratio_bar(quantities,
                        data_thresh_for_bar,
                        nrows=1,
                        ncols=1,
                        sort = False,
                        unity_line = False,
                        colorlist = False,
                        sharex=False,
                        sharey=False,
                        xlabel = r'ratio to threshold concentration $C/C_\mathrm{threshold}$',
                        ylabel = False,
                        xscale = False,
                        title_text = 'Concentration treshold ratio',
                        save_fig = False,
                        **kwargs,
                        ):
    
    settings = copy.copy(DEF_settings)
    settings.update(**kwargs)

    if len(data_thresh_for_bar) != nrows * ncols:
        raise ValueError("Number of subplots does not match selection of samples\n \
                         check keywords 'nrows' and 'ncols'.")
    if colorlist:
        if len(colorlist)<len(data_thresh_for_bar):
            raise ValueError("Number of colors too short.")
    else:
        colorlist = ['C{}'.format(i) for i in range(len(data_thresh_for_bar))]
        
        
    if sort:
        if len(sort) != len(quantities):
            raise ValueError("Lenght of list for resorting does not match number of quantities.")        
        quantities = [quantities[i] for i in sort]
        data_thresh_for_bar = data_thresh_for_bar.iloc[:,sort]
        
    fig, ax = plt.subplots(figsize=settings['figsize'],
                            nrows=nrows,
                            ncols=ncols,
                            sharex=sharex,
                            sharey=sharey,
                            )
    axs = ax.flatten()  
      
    for i in range(len(data_thresh_for_bar)):

        # plt.bar(n_bars,value['height'][sort_args],color = value['color'],zorder = 1)                 
        axs[i].barh(quantities,data_thresh_for_bar.iloc[i,:],color = colorlist[i])
        if unity_line:
            axs[i].plot([1,1],[-0.5,len(quantities)-.5],'k--')

        ### ---------------------------------------------------------------------------
        ### Adapt plot optics
 
        axs[i].set_xlabel(xlabel,fontsize=settings['textsize'])
        if ylabel:
            axs[i].set_ylabel(ylabel, fontsize=settings['textsize'])
        if xscale:
            axs[i].set_xscale(xscale)

    # ax.grid(True)
    # ax.minorticks_on()
    # ax.tick_params(axis="both", which="major", labelsize=settings['textsize'])
    # ax.tick_params(axis="both", which="minor", labelsize=settings['textsize'])
    # plt.title(title_text,fontsize = settings['textsize'])
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
    
def activity_data_prep(data):

    """Preparing data required for activity plot.

    Activity plot requires data analysis of:
        - contaminant concentrations
        - metabolites counts
        - NA screening
    
    Functions checks if required quantities are provided as columns in DataFrame, 
    extracts it from DataFrame and saves it to dictionary.
    
    When data is provided as list of pd.Series/np.arrays/lists it checks data
    on compatibility and saves it to dictionary.
        
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

    Output
    -------
        activity_data_dict: dict
            of np.arrays containing quantities required in activity plot:
            - total concentration of contaminants per sample
            - total count of metabolites per sample
            - traffic light on NA activity per sample
    """

    if isinstance(data, pd.DataFrame):
        ### check on correct data input format and extracting column names as list
        data_frame,cols= check_data_frame(data)
    
        if names.name_metabolites_count not in cols:
            raise ValueError("Count of metabolites not in DataFrame. Run 'total_metabolites_count()' first.")
        else:
            meta_count = data_frame[names.name_metabolites_count].values
    
        if names.name_total_contaminants not in cols:
            raise ValueError("Total concentration of contaminants not in DataFrame. Run 'total_contaminant_concentration()' first.")
        else:
            tot_cont = data_frame[names.name_total_contaminants].values
            
        if names.name_na_traffic_light not in cols:
            raise ValueError("Traffic light on NA activity per sample not in DataFrame. Run 'sample_NA_traffic()' first.")
        else:
            well_color = data_frame[names.name_na_traffic_light].values

    elif isinstance(data, list) and len(data)>=3:
        if isinstance(data[0], pd.Series) and isinstance(data[1], pd.Series) and isinstance(data[2], pd.Series):
            for series in data:
                if series.name == names.name_metabolites_count:
                    meta_count = series.values
                if series.name == names.name_total_contaminants:
                    tot_cont = series.values
                if series.name == names.name_na_traffic_light:
                    well_color = series.values
        elif isinstance(data[0], (np.ndarray, list)):
            tot_cont = data[0]
            meta_count = data[1]
            well_color = data[2]
        else:
            raise ValueError("List elements in data must be lists, np.arrays or pd.series.")
        if len(tot_cont) != len(meta_count) or len(tot_cont) != len(well_color):
            raise ValueError("Provided arrays/lists/series of data must have the same length.")
    else:
        raise ValueError("Data needs to be DataFrame or list of at least three lists/np.arrays/pd.series.")

    return dict(
        meta_count = meta_count,
        tot_cont = tot_cont,
        well_color = well_color,
        )


def activity_plot(
        activity_data_dict,
        save_fig=False,
        xlabel = r"Concentration contaminants [$\mu$g/L]",
        ylabel = "Metabolite count",
        **kwargs,
        ):
    """Creating activity plot.

    Activity plot shows scatter of total number of metabolites vs total concentration
    of contaminant per well with color coding of NA traffic lights: red/yellow/green
    corresponding to no natural attenuation going on (red), limited/unknown NA activity (yellow)
    or active natural attenuation (green)

    Input
    ----------
        activity_data_dict: dict
            list or pandas.DataFrame
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
    
    if len(activity_data_dict['tot_cont']) <= 1:
        raise ValueError("Too little data for activity plot. At least two values per quantity required.")

    ### ---------------------------------------------------------------------------
    ### Creating Figure
    fig, ax = plt.subplots(figsize=settings['figsize'])
    ax.scatter(activity_data_dict['tot_cont'],
               activity_data_dict['meta_count'],
               c=activity_data_dict['well_color'],
               zorder = 3,
               s = settings['markersize'],
               ec = settings['ec'],
               lw = settings['lw'],
               )

    ### generate legend labels
    if "green" in activity_data_dict['well_color']:
        ax.scatter([], [],
                   label="available",
                   c="green",
                   s = settings['markersize'],
                   ec = settings['ec'],
                   lw = settings['lw'],
                   )
    if "y" in activity_data_dict['well_color']:
        ax.scatter([], [],
                   label="unknown",
                   c="y",
                   s = settings['markersize'],
                   ec = settings['ec'],
                   lw = settings['lw'],
                   )
    if "red" in activity_data_dict['well_color']:
        ax.scatter([], [],
                   label="depleted",
                   c="red",
                   s = settings['markersize'],
                   ec = settings['ec'],
                   lw = settings['lw'],
                   )

    ### ---------------------------------------------------------------------------
    ### Adapt plot optics
    ax.set_xlabel(xlabel,fontsize=settings['textsize'])
    ax.set_ylabel(ylabel, fontsize=settings['textsize'])
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
