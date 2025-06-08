#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Routines for calculating total concentrations and counts for samples.

@author: Alraune Zech
"""

import numpy as np
import pandas as pd
from IPython.display import display
import mibiscreen.data.settings.standard_names as names
from mibiscreen.data.check_data import check_data_frame
from mibiscreen.data.set_data import determine_quantities
from mibiscreen.data.set_data import extract_settings
from .properties import properties


def total_concentration(
        data_frame,
        name_list = "all",
        name_column = False,
        verbose = False,
        include = False,
        **kwargs,
        ):
    """Calculate total concentration of given list of quantities.

    Input
    -----
        data: pd.DataFrame
            Contaminant concentrations in [ug/l], i.e. microgram per liter
        name_list: str or list, dafault is 'all'
            either short name for group of quantities to use, such as:
                    - 'all' (all qunatities given in data frame except settings)
                    - 'BTEX' (for contaminant group: benzene, toluene, ethylbenzene, xylene)
                    - 'BTEXIIN' (for contaminant group: benzene, toluene, ethylbenzene, xylene,
                                  indene, indane and naphthaline)
            or list of strings with names of quantities to use
        name_column: str or False, default is 'False'
            optional name of column
        verbose: Boolean
            verbose flag (default False)
        include: bool, default False
            whether to include calculated values to DataFrame


    Output
    ------
        tot_conc: pd.Series
            Total concentration of contaminants in [ug/l]

    """
    if verbose:
        print('==============================================================')
        print(" Running function 'total_concentration()' on data")
        print('==============================================================')

    ### check on correct data input format and extracting column names as list
    data,cols= check_data_frame(data_frame,inplace = include)

    ### sorting out which columns in data to use for summation of concentrations
    quantities, _ = determine_quantities(cols,name_list = name_list, verbose = verbose)

    ### actually performing summation
    # try:
    tot_conc = data[quantities].sum(axis = 1)
    # except TypeError:
    #     raise ValueError("Data not in standardized format. Run 'standardize()' first.")

    if name_column is False:
        if isinstance(name_list, str):
            name_column = 'total concentration {}'.format(name_list)
        elif isinstance(name_list, list):
            name_column = 'total concentration selection'
    else:
        if not isinstance(name_column, str):
            raise ValueError("Keyword 'name_column' needs to be a string or False.")

    tot_conc.rename(name_column,inplace = True)
    if verbose:
        print('________________________________________________________________')
        print("{} in [ug/l] is:\n{}".format(name_column,tot_conc))
        print('--------------------------------------------------')

    ### additing series to data frame
    if include:
        data[name_column] = tot_conc
        if verbose:
            print("Series {} saved as column within provided DataFrame".format(name_column))
            print('---------------------------------------------------------------------------')

    return tot_conc

def total_contaminant_concentration(
        data_frame,
        contaminant_group = "all_cont",
        include = False,
        verbose = False,
        ):
    """Function to calculate total concentration of contaminants.

    Input
    -----
        data: pd.DataFrame
            Contaminant contentrations in [ug/l], i.e. microgram per liter
        contaminant_group: str
            Short name for group of contaminants to use
            default is 'all_cont' (for benzene, toluene, ethylbenzene, xylene,
                                  indene, indane and naphthaline)
        include: bool, default False
            Whether to modify the DataFrame rather than creating a new one.
        verbose: Boolean
            verbose flag (default False)

    Output
    ------
        tot_conc: pd.Series
            Total concentration of contaminants in [ug/l]

    """
    if verbose:
        print('==============================================================')
        print(" Running function 'total_contaminant_concentration()' on data")
        print('==============================================================')

    if contaminant_group == "all_cont":
        name_column = names.name_total_contaminants
    elif contaminant_group == 'BTEX':
        name_column = names.name_total_BTEX
    elif contaminant_group == 'BTEXIIN':
        name_column = names.name_total_BTEXIIN
    else:
        name_column = False

    tot_conc = total_concentration(
        data_frame,
        name_list = contaminant_group,
        name_column = name_column,
        verbose = verbose,
        include = include,
        )

    return tot_conc

def total_metabolites_concentration(
        data_frame,
        include = False,
        verbose = False,
        ):
    """Function to calculate total concentration of metabolites.

    Input
    -----
        data: pd.DataFrame
            metabolites contentrations in [ug/l], i.e. microgram per liter
        include: bool, default False
            Whether to modify the DataFrame rather than creating a new one.
        verbose: Boolean
            verbose flag (default False)

    Output
    ------
        tot_conc: pd.Series
            Total concentration of metabolites in [ug/l]

    """
    if verbose:
        print('==============================================================')
        print(" Running function 'total_metabolites_concentration()' on data")
        print('==============================================================')

    tot_conc = total_concentration(
        data_frame,
        name_list = 'all',
        name_column = names.name_metabolites_conc,
        verbose = verbose,
        include = include,
        )

    return tot_conc

def total_count(
        data_frame,
        name_list = "all",
        name_column = False,
        threshold = 0.,
        verbose = False,
        include = False,
        **kwargs,
        ):
    """Calculate total number of quantities with concentration exceeding threshold value.

    Input
    -----
        data: pd.DataFrame
            Contaminant concentrations in [ug/l], i.e. microgram per liter
        name_ist: str or list, dafault is 'all'
            either short name for group of quantities to use, such as:
                    - 'all' (all qunatities given in data frame except settings)
                    - 'BTEX' (for benzene, toluene, ethylbenzene, xylene)
                    - 'BTEXIIN' (for benzene, toluene, ethylbenzene, xylene,
                                  indene, indane and naphthaline)
            or list of strings with names of quantities to use
        name_column: str or False, default is 'False'
            optional name of column
        threshold: float, default 0
            threshold concentration value in [ug/l] to test on exceedence
        verbose: Boolean
            verbose flag (default False)
        include: bool, default False
            whether to include calculated values to DataFrame

    Output
    ------
        tot_count: pd.Series
            Total number of quantities with concentration exceeding threshold value

    """
    if verbose:
        print('==============================================================')
        print(" Running function 'total_count()' on data")
        print('==============================================================')

    threshold = float(threshold)
    if threshold<0:
        raise ValueError("Threshold value '{}' not valid.".format(threshold))

    ### check on correct data input format and extracting column names as list
    data,cols= check_data_frame(data_frame,inplace = include)

    ### sorting out which column in data to use for summation of concentrations
    quantities, _ = determine_quantities(cols,name_list = name_list, verbose = verbose)

    ### actually performing count of values above threshold:
    try:
        total_count = (data[quantities]>threshold).sum(axis = 1)
    except TypeError:
        raise ValueError("Data not in standardized format. Run 'standardize()' first.")

    if name_column is False:
        if isinstance(name_list, str):
            name_column = 'total count {}'.format(name_list)
        elif isinstance(name_list, list):
            name_column = 'total count selection'
    else:
        if not isinstance(name_column, str):
            raise ValueError("Keyword 'name_column' needs to be a string or False.")
    total_count.rename(name_column,inplace = True)

    if verbose:
        print('________________________________________________________________')
        print("Number of quantities out of {} exceeding \
              concentration of {:.2f} ug/l :\n{}".format(len(quantities),threshold,total_count))
        print('--------------------------------------------------')

    if include:
        data[name_column] = total_count

    return total_count

def total_contaminant_count(
        data_frame,
        include = False,
        verbose = False,
        ):
    """Function to calculate total count of contaminants.

    Input
    -----
        data: pd.DataFrame
            Contaminant contentrations in [ug/l], i.e. microgram per liter
        contaminant_group: str
            Short name for group of contaminants to use
            default is 'all_cont' (for benzene, toluene, ethylbenzene, xylene,
                                  indene, indane and naphthaline)
        include: bool, default False
            Whether to modify the DataFrame rather than creating a new one.
        verbose: Boolean
            verbose flag (default False)

    Output
    ------
        tot_conc: pd.Series
            Total count of contaminants in [ug/l]

    """
    if verbose:
        print('==============================================================')
        print(" Running function 'total_contaminant_count()' on data")
        print('==============================================================')

    tot_conc = total_concentration(
        data_frame,
        name_list = "all_cont",
        name_column = names.name_total_contaminants,
        verbose = verbose,
        include = include,
        )

    return tot_conc


def total_metabolites_count(
        data_frame,
        include = False,
        verbose = False,
        ):
    """Function to calculate total count of metabolites.

    Input
    -----
        data: pd.DataFrame
            metabolites contentrations in [ug/l], i.e. microgram per liter
        include: bool, default False
            Whether to modify the DataFrame rather than creating a new one.
        verbose: Boolean
            verbose flag (default False)

    Output
    ------
        tot_count: pd.Series
            Total count of metabolites in [ug/l]

    """
    if verbose:
        print('==============================================================')
        print(" Running function 'total_metabolites_count()' on data")
        print('==============================================================')

    tot_count = total_count(
        data_frame,
        name_list = 'all',
        name_column = names.name_metabolites_count,
        verbose = verbose,
        include = include,
        )

    return tot_count

def thresholds_for_intervention_ratio(
        data_frame,
        contaminant_group = "BTEXIIN",
        include = False,
        keep_setting_data = False,
        verbose = False,
        ):

    """Evaluting ratio of contaminant concentration to intervention threshold.

        Determines ratio of contaminant concentration to thresholds set by
        the Dutch government for intervention.

    Input
    -----
        data_frame: pd.DataFrame
            Contaminant contentrations in [ug/l], i.e. microgram per liter
        contaminant_group: str
            Short name for group of contaminants to use
            default is 'BTEXIIN' (for benzene, toluene, ethylbenzene, xylene,
                                  indene, indane and naphthaline)
        include: bool, default False
            Whether to modify the DataFrame rather than creating a new one.
        verbose: Boolean, default False
            verbose flag

    Output
    ------
        intervention_ratio: pd.DataFrame
            DataFrame of similar format as input data with well specification and
            three columns on intervention threshold exceedance analysis:
                - traffic light if well requires intervention
                - number of contaminants exceeding the intervention value
                - list of contaminants above the threshold of intervention
    """
    if verbose:
        print('==============================================================')
        print(" Running function 'thresholds_for_intervention_ratio()' on data")
        print('==============================================================')

    ### check on correct data input format and extracting column names as list
    data,cols= check_data_frame(data_frame,inplace = include)

    ### sorting out which columns in data to evaluate
    quantities, _ = determine_quantities(cols,
                                      name_list = contaminant_group,
                                      verbose = verbose)

    if include:
        data_thresh = data
    else:
        if keep_setting_data:
            data_thresh= extract_settings(data)
        else:
            data_thresh = pd.DataFrame(index = data.index)
    list_names = []

    for cont in quantities:
        th_value = properties[cont]['thresholds_for_intervention_NL']
        data_thresh[cont+'_thr_ratio'] = data[cont]/th_value
        list_names.append(cont+'_thr_ratio')

    if verbose:
        print("Evaluting ratio of contaminant concentration to intervention threshold {}:".format(
            contaminant_group))
        display(data_thresh[list_names])
        # data_thresh[list_names].style
        print('__________________________________________________________________________________')

    return data_thresh
    

def thresholds_for_intervention_traffic(
        data_frame,
        contaminant_group = "BTEXIIN",
        include = False,
        verbose = False,
        ):
    """Function to evalute intervention threshold exceedance.

        Determines which contaminants exceed concentration thresholds set by
        the Dutch government for intervention.

    Input
    -----
        data_frame: pd.DataFrame
            Contaminant contentrations in [ug/l], i.e. microgram per liter
        contaminant_group: str
            Short name for group of contaminants to use
            default is 'BTEXIIN' (for benzene, toluene, ethylbenzene, xylene,
                                  indene, indane and naphthaline)
        include: bool, default False
            Whether to modify the DataFrame rather than creating a new one.
        verbose: Boolean, default False
            verbose flag

    Output
    ------
        intervention: pd.DataFrame
            DataFrame of similar format as input data with well specification and
            three columns on intervention threshold exceedance analysis:
                - traffic light if well requires intervention
                - number of contaminants exceeding the intervention value
                - list of contaminants above the threshold of intervention
    """
    if verbose:
        print('==============================================================')
        print(" Running function 'thresholds_for_intervention()' on data")
        print('==============================================================')

    ### check on correct data input format and extracting column names as list
    data,cols= check_data_frame(data_frame,inplace = include)

    ### sorting out which columns in data to evaluate
    quantities, _ = determine_quantities(cols,
                                      name_list = contaminant_group,
                                      verbose = verbose)

    if include:
        intervention = data
    else:
        intervention= extract_settings(data)

    nr_samples = data.shape[0] # number of samples
    traffic_nr = np.zeros(nr_samples,dtype=int)
    traffic_list = [[] for _ in range(nr_samples)]

    try:
        for cont in quantities:
            th_value = properties[cont]['thresholds_for_intervention_NL']
            traffic_nr += (data[cont].values > th_value)
            for i in range(nr_samples):
                if data[cont].values[i] > th_value:
                    traffic_list[i].append(cont)
    except TypeError:
        raise ValueError("Data not in standardized format. Run 'standardize()' first.")

    traffic_light = np.where(traffic_nr>0,"red","green")
    traffic_light[np.isnan(traffic_nr)] = 'y'
    intervention[names.name_intervention_traffic] = traffic_light
    intervention[names.name_intervention_number] = traffic_nr
    intervention[names.name_intervention_contaminants] = traffic_list

    if verbose:
        print("Evaluation of contaminant concentrations exceeding intervention values for {}:".format(
            contaminant_group))
        print('------------------------------------------------------------------------------------')
        print("Red light: Intervention values exceeded for {} out of {} locations".format(
            np.sum(traffic_nr >0),data.shape[0]))
        print("green light: Concentrations below intervention values at {} out of {} locations".format(
            np.sum(traffic_nr == 0),data.shape[0]))
        print("Yellow light: No decision possible at {} out of {} locations".format(
            np.sum(np.isnan(traffic_nr)),data.shape[0]))
        print('________________________________________________________________')

    return intervention
