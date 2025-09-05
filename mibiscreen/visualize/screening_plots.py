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
from mibiscreen.data.check_data import check_data_frame
from mibiscreen.data.set_data import determine_quantities

DEF_settings = dict(
    figsize = [3.75,2.8],
    textsize = 10,
    markersize = 45,
    ec = 'k',
    lw = 0.5,
    loc = 'lower right',
    dpi = 300,
    save_fig=False,
    grid = False,
    )


def contaminants_bar(data_frame,
                     list_contaminants,
                     list_labels = False,
                     sort = False,
                     name_sample = False,
                     xlabel = 'Samples',
                     ylabel = r'Total concentration [$\mu$g/l]',
                     yscale = 'linear',
                     title_text = 'Total concentration of contaminants per sample',
                     xtick_autorotate = False,
                     save_fig = False,
                     **kwargs,
                     ):
    """Creating a bar plot of contaminant concentrations (or counts) per sample.

    A selected list on quantities (at least 2) from a data frame is displayed as
    overlaying bars showing concentrations of individual components and/or sums
    of different contaminants with one bar per sample.
    The plot can also be used to display total counts of a selected range of
    contaminants per sample.

    Input
    -----
        data_frame : pd.DataFrame
            Contaminant concentrations in [ug/l], i.e. microgram per liter
        list_contaminants : list
            list of column names to select from data_frame
        list_labels: list or False, default: False
            list of quantity names to be displayed in legend
            if False, the names in 'list_contaminants' will be used
        sort: Boolean, default False
            weather to sort data and display concentrations bars
            in ascending order (based on values of first quantity in
            list_contaminants)
        name_sample: Boolean, default False
            weather to display sample_nr on x-axis (True) or
            just number all samples starting from 1 (False)
        xlabel: str, default 'Samples'
            x-axis label
        ylabel: str, default 'Total concentration',
            y-axis label
        yscale: str, default 'linear',
            scaling of y-axis, typically 'log' or 'linear'
        title_text: str or False, default 'Total concentration of contaminants per sample'
            text displayed as figure title,
            in case of False, no title will be displayed
        save_fig: Boolean or string, optional, default is False.
            Flag to save figure to file with name provided as string.
        **kwargs: dict
            dictionary with plot settings

    Returns:
    --------
        fig : Figure object
            Figure object of created activity plot.
        ax :  Axes object
            Axes object of created activity plot.

    """
    settings = copy.copy(DEF_settings)
    settings.update(**kwargs)

    ### Plotting data check

    data,cols= check_data_frame(data_frame,inplace = False)

    ### sorting out which columns in data to use for summation of electrons available
    quantities,_ = determine_quantities(cols,
                                        name_list = list_contaminants,
                                        )

    ### Plotting data preparation
    if sort:
        sort_args = np.argsort(data_frame[list_contaminants[0]].values)
    else:
        sort_args = np.arange(len(data_frame[list_contaminants[0]].values))

    if name_sample is False:
        n_bars = np.arange(len(data_frame[list_contaminants[0]].values))
    else:
        if names.name_sample not in cols:
            raise ValueError("No {} provided in data_frame.".format(names.name_sample))
        else:
            n_bars = data_frame[names.name_sample].values[sort_args]

    if list_labels is False:
        list_labels = list_contaminants
    else:
        if not isinstance(list_labels, list):
            raise ValueError("list_labels need to contain a list of string label names.")
        if len(list_labels)!=len(list_contaminants):
            raise ValueError("List of label names must be of same length of list of selected quantities.")

    ### plotting actual data
    fig, ax = plt.subplots(figsize=settings['figsize'])

    for i,cont_group in enumerate(list_contaminants):
        plt.bar(n_bars,data_frame[cont_group].values[sort_args],label=list_labels[i])

    ### ---------------------------------------------------------------------------
    ### Adapt plot optics
    plt.xlabel(xlabel,fontsize = settings['textsize'])
    plt.ylabel(ylabel,fontsize = settings['textsize'])
    plt.yscale(yscale)
    plt.legend(loc =settings['loc'],fontsize = settings['textsize'])
    if title_text:
        plt.title(title_text,fontsize = settings['textsize'])
    if xtick_autorotate:
        fig.autofmt_xdate(bottom=0.2, rotation=30, ha='right', which='major')

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

def threshold_ratio_bar(data_threshold_ratios,
                        list_contaminants = False,
                        list_labels = False,
                        list_samples = False,
                        nrows=1,
                        ncols=False,
                        unity_line = False,
                        list_sort = False,
                        list_colors = False,
                        sharex=False,
                        sharey=False,
                        xlabel = r'ratio to threshold concentration $C/C_\mathrm{threshold}$',
                        ylabel = False,
                        xscale = False,
                        title_text = False,
                        save_fig = False,
                        **kwargs,
                        ):
    """Horizontal bar plots showing relative threshold exceedance of contaminants per sample.

    Creates a figure with subfigures for each (selected) sample displaying the
    relative exceedance of contaminant concentrations are ratio of concentration
    to exceedance value (with <1 being lower then exceedance value).

    The required input data frame can be create with the function:
    'thresholds_for_intervention_ratio()'
    using the recommended keywords:
        - include = False
        - keep_setting_data = False

    Input
    -----
        data_threshold_ratios: pd.Data_frame
            each column contains a relative contaminant concentration
            each rows contains a sample

        list_contaminants : list
            list of column names to select from data_frame
        list_labels: list or False, default: False
            list of quantity names to be displayed in legend
            if False, the names in 'list_contaminants' will be used
        list_samples: list or False, default: False
            if False, bars for all samples are displayed
            if list, bars are only displayed for selected samples (given by indexs)
        nrows, ncolsint, default: 1
            Number of rows/columns of the subplot grid.
            Number of total subfigures need to fit to number of selected samples.
        unity_line: Boolean, default False
            weather to include unity line (i.e. solid black line at 1 indicating
            equality of contaminant concentration and exceedance threshold value)
        list_sort: list or False, default False
            list representing order of display of quantities
        list_colors: list or False, default False
            list of colors to use for individual bars
            in case of False the standard color order in python is used
        sharex, sharey: bool or {'none', 'all', 'row', 'col'}, default: False
            Controls sharing of properties among x (sharex) or y (sharey) axes
            See matplotlib.pyplot.subplots() for more details
        xlabel: str, default r'ratio to threshold concentration'
            x-axis label
        ylabel: str, default False
            y-axis label
        xscale: str or False, default 'False',
            scaling of y-axis, when False --> 'linear', typical other option: 'log'
        title_text: str or False, default 'False'
            text displayed as figure title,
            in case of False, no title will be displayed
        save_fig: Boolean or string, optional, default is False.
            Flag to save figure to file with name provided as string.
        **kwargs: dict
            dictionary with plot settings

    Returns:
    --------
        fig : Figure object
            Figure object of created activity plot.
        ax :  Axes object
            Axes object of created activity plot.

    """
    settings = copy.copy(DEF_settings)
    settings.update(**kwargs)

    ### data prepration
    if list_contaminants:
        data_threshold_ratios = data_threshold_ratios[list_contaminants]
    else:
        list_contaminants = data_threshold_ratios.columns.to_list()

    if list_labels:
        if len(list_labels)<len(list_contaminants):
            raise ValueError("Number of label names too short.")
    else:
        list_labels = list_contaminants

    if list_samples:
        data_threshold_ratios = data_threshold_ratios.iloc[list_samples]
    else:
        list_samples = data_threshold_ratios.index.values

    if ncols and nrows:
        if len(list_samples) != nrows * ncols:
            raise ValueError("Number of subplots does not match selection of samples\n \
                             check keywords 'nrows' and 'ncols'.")
    elif ncols:
        nrows = int(np.ceil(len(list_samples)/ncols))
    elif nrows:
        ncols = int(np.ceil(len(list_samples)/nrows))
    else:
        ncols = len(list_samples)
        nrows = 1

    if list_colors:
        if len(list_colors)<len(list_samples):
            raise ValueError("Number of colors too short.")
    else:
        list_colors = ['C{}'.format(i) for i in range(len(list_contaminants))]

    if list_sort:
        if len(list_sort) != len(list_contaminants):
            raise ValueError("Lenght of list for resorting does not match number of quantities.")
        list_contaminants = [list_contaminants[i] for i in list_sort]
        data_threshold_ratios = data_threshold_ratios.iloc[:,list_sort]


    ### creating figure
    fig, ax = plt.subplots(figsize=settings['figsize'],
                            nrows=nrows,
                            ncols=ncols,
                            sharex=sharex,
                            sharey=sharey,
                            )
    if len(list_samples)>1:
        axs = ax.flatten()

    for i in range(len(list_samples)):

        if len(list_samples)>1:
            axi = axs[i]
        else:
            axi = ax

        # plt.bar(n_bars,value['height'][sort_args],color = value['color'],zorder = 1)
        axi.barh(list_labels,data_threshold_ratios.iloc[i,:],color = list_colors[i])
        if unity_line:
            axi.plot([1,1],[-0.5,len(list_labels)-.5],'k--')

        ### ---------------------------------------------------------------------------
        ### Adapt plot optics

        axi.set_xlabel(xlabel,fontsize=settings['textsize'])
        if ylabel:
            axi.set_ylabel(ylabel, fontsize=settings['textsize'])
        if xscale:
            axi.set_xscale(xscale)

        axi.grid(settings['grid'])
        axi.tick_params(axis="both", which="major", labelsize=settings['textsize'])

    if title_text:
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

def electron_balance_bar_data_prep(data_frame,
                                   color_order = ['C1','C0','C2'],
                                   list_samples = False,
                                   ):
    """Preparing dictionary from data_frame for electron balance plot.

    Requires data_frame to contain the following quantities:
        - "total_reductors"
        - 'total_oxidators_BTEXIIN'
        - 'total_oxidators_BTEX'

    Input
    -----
        data_frame : pd.DataFrame
            Contaminant concentrations in [ug/l], i.e. microgram per liter
        color_order: list of colors, default = ['C1','C0','C2']
            colors to be used in the plot for the three quantities
        list_samples: list or False, default: False
            if False, bars for all samples are displayed
            if list, bars are only displayed for selected samples (given by indexs)

    Returns:
    --------
        electron_balance_bar_dict : dict
            dictionary with plot relevant specifics
    """
    electron_balance_bar_dict = dict()

    electron_balance_bar_dict['EA capacity'] = dict(
        height = data_frame[names.name_total_reductors].values,
        color = color_order[0],
        sample_nr = data_frame[names.name_sample],
    )
    electron_balance_bar_dict['BTEXIIN'] = dict(
        height = data_frame[names.name_total_oxidators_BTEXIIN].values,
        color = color_order[1],
    )
    electron_balance_bar_dict['BTEX'] = dict(
        # height = data_frame[names.name_total_oxidators_BTEX],
        height = data_frame[names.name_total_oxidators_BTEX].values,
        color = color_order[2],
    )

    electron_balance_bar_dict['EA capacity minor'] = dict(
        height = data_frame[names.name_total_reductors].where(data_frame[names.name_e_balance] < 1, 0).values,
        color = color_order[0],
    )

    if list_samples:
        for key, value in electron_balance_bar_dict.items():
            value['height'] = value['height'][list_samples]
        val = electron_balance_bar_dict['EA capacity']['sample_nr'][list_samples]
        electron_balance_bar_dict['EA capacity']['sample_nr'] = val

    return electron_balance_bar_dict

def electron_balance_bar(electron_balance_bar_dict,
                         sample_nr = False,
                         sort = False,
                         xlabel = 'Samples',
                         ylabel = r'Electron capacity/needed [mmol e-/l]',
                         yscale = 'linear',
                         title_text = 'Electron balance per sample',
                         xtick_autorotate = False,
                         save_fig = False,
                         **kwargs,
                         ):
    """Creating a bar plot for electron balance per sample.

    Displayed are bars of electron concentrations for:
    - "total_reductors"
    - 'total_oxidators_BTEXIIN'
    - 'total_oxidators_BTEX'

    The plot shows the three quantities as overlapping bars with the smallest in
    front and the largest to the back, indicating if an excess of or need for
    electrons is present at the sample location, including quantitative differences.

    Operates on dictionary containing electron concentration values extracted
    from data frame, color and sample selection. The dictionary can be prepared
    by running the function 'electron_balance_bar_data_prep()' on the data frame.

    Input
    -----
        electron_balance_bar_dict : dict
            dictionary with plot relevant specifics
        sort: Boolean, default False
            weather to sort data and display concentrations bars
            in ascending order (based on values of first quantity in
            list_contaminants)
        sample_nr: Boolean, default False
            weather to display sample_nr on x-axis (True) or
            just number all samples starting from 1 (False)
        xlabel: str, default 'Samples'
            x-axis label
        ylabel: str, default r'Electron capacity/needed [mmol e-/l]'
            y-axis label
        yscale: str, default 'linear',
            scaling of y-axis, typically 'log' or 'linear'
        title_text: str or False, default 'Total concentration of contaminants per sample'
            text displayed as figure title,
            in case of False, no title will be displayed
        xtick_autorotate: Boolean, default 'False'
            sample names at x-axis are rotated by 45 degrees
        save_fig: Boolean or string, optional, default is False.
            Flag to save figure to file with name provided as string.
        **kwargs: dict
            dictionary with plot settings

    Returns:
    --------
        fig : Figure object
            Figure object of created activity plot.
        ax :  Axes object
            Axes object of created activity plot.

    """
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
    if title_text:
        plt.title(title_text,fontsize = settings['textsize'])
    if xtick_autorotate:
        fig.autofmt_xdate(bottom=0.2, rotation=30, ha='right', which='major')


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

def activity_data_prep(data,
                       verbose = False,
                       ):
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
        verbose: Boolean, default True
            verbosity flag

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
            raise ValueError("Total concentration of contaminants not in DataFrame. \
                             Run 'total_contaminant_concentration()' first.")
        else:
            tot_cont = data_frame[names.name_total_contaminants].values

        if names.name_na_traffic_light not in cols:
            raise ValueError("Traffic light on NA activity per sample not in DataFrame. \
                             Run 'sample_NA_traffic()' first.")
        else:
            well_color = data_frame[names.name_na_traffic_light].values

    elif isinstance(data, list) and len(data)>=3:

        if len(data[0]) != len(data[1]) or len(data[0]) != len(data[2]):
           raise ValueError("Provided arrays/lists/series of data must have the same length.")

        if isinstance(data[0], (np.ndarray, list)) and isinstance(data[1], (np.ndarray, list)) \
            and isinstance(data[2], (np.ndarray, list)):
            tot_cont = data[0]
            meta_count = data[1]
            well_color = data[2]
            if verbose:
                print("List of arrays/lists interpreted as quantities for activity plot in the order:")
                print("  total concentration; metabolite count; NA traffic light color")

        elif isinstance(data[0], pd.Series) and isinstance(data[1], pd.Series) and isinstance(data[2], pd.Series):
            meta_count, tot_cont, well_color = False, False, False
            for series in data:
                if series.name == names.name_metabolites_count:
                    meta_count = series.values
                if series.name == names.name_total_contaminants:
                    tot_cont = series.values
                if series.name == names.name_na_traffic_light:
                    well_color = series.values
            if meta_count is False or tot_cont is False or well_color is False:
                raise ValueError("List of data frames does not contain all required quantities:\
                                 total concentration; metabolite count; NA traffic light color")
        else:
            raise ValueError("List elements in data must be lists, np.arrays or pd.series.")
    else:
        raise ValueError("Data needs to be DataFrame or list of at least three lists/np.arrays/pd.series.")

    return dict(
        meta_count = meta_count,
        tot_cont = tot_cont,
        well_color = well_color,
        )


def activity_plot(
        activity_data_dict,
        xlabel = r"Concentration contaminants [$\mu$g/L]",
        ylabel = "Metabolite count",
        save_fig=False,
        title_text = False,
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
        xlabel: str, default r"Concentration contaminants"
            x-axis label
        ylabel: str, default "Metabolite count"
            y-axis label
        save_fig: Boolean or string, optional, default is False.
            Flag to save figure to file with name provided as string.
        title_text: str or False, default False
            text displayed as figure title,
            in case of False, no title will be displayed
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
    if not isinstance(activity_data_dict,dict):
        raise ValueError("Input data needs to be dictionary containing keywords for quantities:\
                          tot_cont, meta_count, well_color. Consider running first 'activity_data_prep()'")

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
    if title_text:
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
