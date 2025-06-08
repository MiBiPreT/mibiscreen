#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Routines for calculating natural attenuation potential.

@author: Alraune Zech
"""

import numpy as np
import pandas as pd
import mibiscreen.data.settings.standard_names as names
from mibiscreen.data.check_data import check_data_frame
from mibiscreen.data.set_data import determine_quantities
from mibiscreen.data.set_data import extract_settings
from .properties import properties


def reductors(
    data_frame,
    ea_group = 'ONS',
    include = False,
    verbose = False,
    **kwargs,
    ):
    """Calculate the amount of electron reductors [mmol e-/l].

    It determines the amount of electrons availble from electron acceptors
    (default: mobile dissolved oxygen, nitrate, and sulfate).

    It relates concentrations to electrons using the stochimetry from the
    chemical reactions producting electrons and the molecular mass values
    for the quantities in [mg/mmol].

    Input
    -----
        data: pd.DataFrame
            concentration values of electron acceptors in [mg/l]
        ea_group: str
            Short name for group of electron acceptors to use
            default is 'ONS' (for oxygen, nitrate, and sulfate)
        include: bool, default False
            Whether to modify the DataFrame rather than creating a new one.
        verbose: Boolean
            verbose flag (default False)

    Output
    ------
        tot_reduct: pd.Series
        Total amount of electrons needed for reduction in [mmol e-/l]
    """
    if verbose:
        print('==============================================================')
        print(" Running function 'reductors()' on data")
        print('==============================================================')

    ### check on correct data input format and extracting column names as list
    data,cols= check_data_frame(data_frame,inplace = include)

    ### sorting out which columns in data to use for summation of electrons available
    quantities,_ = determine_quantities(cols,name_list = ea_group, verbose = verbose)

    ### actually performing summation
    try:
        tot_reduct = 0.
        for ea in quantities:
            tot_reduct += properties[ea]['factor_stoichiometry']* data[ea]/properties[ea]['molecular_mass']
    except TypeError:
        raise ValueError("Data not in standardized format. Run 'standardize()' first.")

    tot_reduct.rename(names.name_total_reductors,inplace = True)
    if verbose:
        print("Total amount of electron reductors per well in [mmol e-/l] is:\n{}".format(tot_reduct))
        print('----------------------------------------------------------------')

    ### additing series to data frame
    if include:
        data[names.name_total_reductors] = tot_reduct

    return tot_reduct

def oxidators(
    data_frame,
    contaminant_group = "BTEXIIN",
    name_column = False,
    include = False,
    verbose = False,
    **kwargs,
    ):
    """Calculate the amount of electron oxidators [mmol e-/l].

    Calculates the amount of electrons needed for oxidation of the contaminants.
    It transformes the concentrations of contaminants to molar concentrations using
    molecular masses in [mg/mmol] and further identifies number of electrons from
    the chemical reactions using stiochiometric ratios

    alternatively: based on nitrogen and phosphate availability

    Input
    -----
        data: pd.DataFrame
            Contaminant contentrations in [ug/l], i.e. microgram per liter
        contaminant_group: str
            Short name for group of contaminants to use
            default is 'BTEXIIN' (for benzene, toluene, ethylbenzene, xylene,
                                  indene, indane and naphthaline)
        inplace: bool, default False
            Whether to modify the DataFrame rather than creating a new one.
        verbose: Boolean
            verbose flag (default False)

    Output
    ------
        tot_oxi: pd.Series
            Total amount of electrons oxidators in [mmol e-/l]
    """
    if verbose:
        print('==============================================================')
        print(" Running function 'oxidators()' on data")
        print('==============================================================')

    ### check on correct data input format and extracting column names as list
    data,cols= check_data_frame(data_frame,inplace = include)

    ### sorting out which columns in data to use for summation of electrons available
    quantities,_ = determine_quantities(cols,name_list = contaminant_group, verbose = verbose)

    try:
        tot_oxi = 0.
        for cont in quantities:
            cm_cont = data[cont]* 0.001/properties[cont]['molecular_mass'] # molar concentration in mmol/l
            tot_oxi += cm_cont *  properties[cont]['factor_stoichiometry']
    except TypeError:
        raise ValueError("Data not in standardized format. Run 'standardize()' first.")

    if name_column is False:
        name_column = names.name_total_oxidators + '_'+ contaminant_group

    tot_oxi.rename(name_column,inplace = True)

    if verbose:
        print("Total amount of oxidators per well in [mmol e-/l] is:\n{}".format(tot_oxi))
        print('-----------------------------------------------------')

    ### additing series to data frame
    if include:
        data[name_column] = tot_oxi

    return tot_oxi

def electron_balance(
        data_frame,
        include = False,
        verbose = False,
        **kwargs,
        ):
    """Calculating electron balance between reductors and oxidators.

    Determines ratio between the amount of electrons available and those
    needed for oxidation of the contaminants based on values determined by
    the routines "reductors()" and "oxidators()".

    Ratio higher then one indicates sufficient electrons available for degredation,
    values smaller 1 indicates not sufficient supply of electrons to reduce
    the present amount of contaminants.

    Input
    -----
        data_frame: pd.DataFrame
            tabular data containinng "total_reductors" and "total_oxidators"
                -total amount of electrons available for reduction [mmol e-/l]
                -total amount of electrons needed for oxidation [mmol e-/l]
        include: bool, default False
            Whether to modify the DataFrame rather than creating a new one.
        verbose: Boolean
            verbose flag (default False)

    Output
    ------
        e_bal : pd.Series
            Ratio of electron availability: electrons available for reduction
            devided by electrons needed for oxidation

    """
    if verbose:
        print('==============================================================')
        print(" Running function 'electron_balance()' on data")
        print('==============================================================')

    ### check on correct data input format and extracting column names as list
    data,cols= check_data_frame(data_frame,inplace = include)

    if names.name_total_reductors in cols:
        tot_reduct = data[names.name_total_reductors]
    else:
        tot_reduct = reductors(data,**kwargs)

    if names.name_total_oxidators in cols:
        tot_oxi = data[names.name_total_oxidators]
    else:
        tot_oxi = oxidators(data,**kwargs)

    e_bal = tot_reduct.div(tot_oxi, axis=0)
    e_bal.name = names.name_e_balance

    if include:
        data[names.name_e_balance] = e_bal

    if verbose:
        print("Electron balance e_red/e_cont is:\n{}".format(e_bal))
        print('---------------------------------')

    return e_bal

def sample_NA_traffic(
        data_frame,
        include = False,
        verbose = False,
        **kwargs,
        ):
    """Evaluating availability of electrons for biodegredation interpreting electron balance.

    Function builds on 'electron_balance()', based on electron availability
    calculated from concentrations of contaminant and electron acceptors.

    Sufficient supply of electrons is a prerequite for biodegradation and thus the
    potential of natural attenuation (NA) as remediation strategy. The functions
    interprets the electron balance giving it a traffic light of:
        - green: amount of electrons available for (bio-)degradation is higher than
                 amount needed for degrading present contaminant mass/concentration
            --> potential for natural attenuation
        - yellow: electron balance unknown because data is not sufficient
            --> more information needed
        - red: amount of electrons available for (bio-)degradation is lower than
                 amount needed for degrading present contaminant mass/concentration
            --> limited potential for natural attenuation

    Input
    -----
        data_frame: pd.DataFrame
            Ratio of electron availability
        include: bool, default False
            Whether to modify the DataFrame rather than creating a new one.
        verbose: Boolean
            verbose flag (default False)

    Output
    ------
        traffic : pd.Series
            Traffic light (decision) based on ratio of electron availability

    """
    if verbose:
        print('==============================================================')
        print(" Running function 'sample_NA_traffic()' on data")
        print('==============================================================')

    ### check on correct data input format and extracting column names as list
    data,cols= check_data_frame(data_frame,inplace = include)

    if names.name_e_balance in cols:
        e_balance = data[names.name_e_balance]
    else:
        e_balance = electron_balance(data,**kwargs)

    e_bal = e_balance.values
    traffic = np.where(e_bal<1,"red","green")
    traffic[np.isnan(e_bal)] = "y"

    NA_traffic = pd.Series(name =names.name_na_traffic_light,
                           data = traffic,
                           index = e_balance.index
                           )

    if include:
        data[names.name_na_traffic_light] = NA_traffic

    if verbose:
        print("Evaluation if natural attenuation (NA) is ongoing:")#" for {}".format(contaminant_group))
        print('--------------------------------------------------')
        print("Red light: Reduction is limited at {} out of {} locations".format(
            np.sum(traffic == "red"),len(e_bal)))
        print("Green light: Reduction is limited at {} out of {} locations".format(
            np.sum(traffic == "green"),len(e_bal)))
        print("Yellow light: No decision possible at {} out of {} locations".format(
            np.sum(np.isnan(e_bal)),len(e_bal)))
        print('________________________________________________________________')

    return NA_traffic

def sample_NA_screening(
    data_frame,
    ea_group = 'ONS',
    contaminant_group = "BTEXIIN",
    include = False,
    verbose = False,
    **kwargs,
    ):
    """Screening of NA potential for each sample in one go.

    Determines for each sample, the availability of electrons for (bio)degradation of
    contaminants from concentrations of (mobile dissolved) electron acceptors
    (default: oxygen, nitrate, sulfate). It puts them into relation to electrons
    needed for degradation using contaminant concentrations. Resulting electron
    balance is linked to a color flag/traffic light indicating status:
        - green: amount of electrons available for (bio-)degradation is higher than
                 amount needed for degrading present contaminant mass/concentration
            --> potential for natural attenuation
        - yellow: electron balance unknown because data is not sufficient
            --> more information needed
        - red: amount of electrons available for (bio-)degradation is lower than
                 amount needed for degrading present contaminant mass/concentration
            --> limited potential for natural attenuation

        Sufficient supply of electrons is a prerequite for biodegradation and thus the
    potential of natural attenuation (NA) as remediation strategy.
    Input
    -----
        data_frame: pd.DataFrame
            Concentration values of
                - electron acceptors in [mg/l]
                - contaminants in [ug/l]
        ea_group: str, default 'ONS'
            Short name for group of electron acceptors to use
            'ONS' stands for oxygen, nitrate, sulfate and ironII
        contaminant_group: str, default 'BTEXIIN'
            Short name for group of contaminants to use
            'BTEXIIN' stands for benzene, toluene, ethylbenzene, xylene,
                                   indene, indane and naphthaline
        include: bool, default False
            Whether to modify the DataFrame rather than creating a new one.
        verbose: Boolean, default False
            verbose flag

    Output
    ------
        na_data: pd.DataFrame
            Tabular data with all quantities of NA screening listed per sample
    """
    if verbose:
        print('==============================================================')
        print(" Running function 'sample_NA_screening()' on data")
        print('==============================================================')

    ### check on correct data input format and extracting column names as list
    data,_= check_data_frame(data_frame,inplace = include)

    tot_reduct = reductors(data,
                           ea_group = ea_group,
                           include = include,
                           verbose = verbose)
    tot_oxi = oxidators(data,
                        contaminant_group = contaminant_group,
                        include = include,
                        verbose = verbose)
    e_bal = electron_balance(data,
                             include = include,
                             verbose = verbose)
    na_traffic = sample_NA_traffic(data,
                            contaminant_group = contaminant_group,
                            include = include,
                            verbose = verbose)

    list_new_quantities = [tot_reduct,tot_oxi,e_bal,na_traffic]

    if include is False:
       na_data = extract_settings(data)

       for add in list_new_quantities:
           na_data.insert(na_data.shape[1], add.name, add)
    else:
        na_data = data

    return na_data
