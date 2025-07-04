"""Routines for calculating intervention analysis of contaminant concentrations.

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
