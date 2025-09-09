#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Routines for calculating total concentrations and counts for samples.

@author: Alraune Zech
"""

import mibiscreen.data.settings.standard_names as names
from mibiscreen.data.check_data import check_data_frame
from mibiscreen.data.set_data import determine_quantities


def total_concentration(
        data_frame,
        name_list = "all",
        include_as = False,
        verbose = False,
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
        include_as: str or False, default is 'False'
            optional name of column to include new pd.series to data_frame
        verbose: Boolean
            verbose flag (default False)

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
    data,cols= check_data_frame(data_frame,inplace = include_as)

    ### sorting out which columns in data to use for summation of concentrations
    quantities, _ = determine_quantities(cols,name_list = name_list, verbose = verbose)

    ### actually performing summation
    # try:
    tot_conc = data[quantities].sum(axis = 1)
    # except TypeError:
    #     raise ValueError("Data not in standardized format. Run 'standardize()' first.")

    if verbose:
        print('________________________________________________________________')
        print("total concentration in [ug/l] is:\n{}".format(tot_conc))
        print('--------------------------------------------------')

    ### additing series to data frame
    if include_as:
        if not isinstance(include_as, str):
            raise ValueError("Keyword 'include_as' needs to be a string or False.")
        data[include_as] = tot_conc
        if verbose:
            print("Series saved as column '{}' within provided DataFrame".format(include_as))
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
            default is 'all_cont'
        include: bool, default False
            Whether to include total concentration to DataFrame or not.
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

    if contaminant_group in ["all","cont_all","all_cont","contaminants"]:
        name_column = names.name_total_contaminants
    elif contaminant_group == 'BTEX':
        name_column = names.name_total_BTEX
    elif contaminant_group == 'BTEXIIN':
        name_column = names.name_total_BTEXIIN
    else:
        raise ValueError("Contaminant_group name short cut not known: {}.".format(contaminant_group))

    if include is True:
        include_as = name_column
    else:
        include_as = include

    tot_conc = total_concentration(
        data_frame,
        name_list = contaminant_group,
        include_as = include_as,
        verbose = verbose,
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
            Whether to include total concentration to DataFrame or not.
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

    if include is True:
        include_as = names.name_metabolites_conc
    else:
        include_as = include

    tot_conc = total_concentration(
        data_frame,
        name_list = 'all',
        include_as = include_as,
        verbose = verbose,
        )

    return tot_conc

def total_count(
        data_frame,
        name_list = "all",
        threshold = 0.,
        verbose = False,
        include_as = False,
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
        threshold: float, default 0
            threshold concentration value in [ug/l] to test on exceedence
        verbose: Boolean
            verbose flag (default False)
        include_as: str or False, default is 'False'
            optional name of column to include new pd.series to data_frame

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
    data,cols= check_data_frame(data_frame,inplace = include_as)

    ### sorting out which column in data to use for summation of concentrations
    quantities, _ = determine_quantities(cols,name_list = name_list, verbose = verbose)

    ### actually performing count of values above threshold:
    try:
        total_count = (data[quantities]>threshold).sum(axis = 1)
    except TypeError:
        raise ValueError("Data not in standardized format. Run 'standardize()' first.")

    if verbose:
        print('________________________________________________________________')
        print("Number of quantities out of {} exceeding \
              concentration of {:.2f} ug/l :\n{}".format(len(quantities),threshold,total_count))
        print('--------------------------------------------------')

    ### additing series to data frame
    if include_as:
        if not isinstance(include_as, str):
            raise ValueError("Keyword 'include_as' needs to be a string or False.")
        data[include_as] = total_count
        if verbose:
            print("Series saved as column '{}' within provided DataFrame".format(include_as))
            print('---------------------------------------------------------------------------')

    return total_count

def total_contaminant_count(
        data_frame,
        contaminant_group = 'all',
        threshold = 0.,
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
                                  indene, indane and naphthalene)
        threshold: float, default 0
            threshold concentration value in [ug/l] to test on exceedence
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

    if contaminant_group in ["all","cont_all","all_cont","contaminants"]:
        name_column = names.name_total_contaminants_count
    elif contaminant_group == 'BTEX':
        name_column = names.name_total_BTEX_count
    elif contaminant_group == 'BTEXIIN':
        name_column = names.name_total_BTEXIIN_count
    else:
        raise ValueError("Contaminant_group name short cut not known: {}.".format(contaminant_group))

    if include is True:
        include_as = name_column
    else:
        include_as = include

    tot_count = total_count(
        data_frame,
        name_list = contaminant_group,
        threshold = threshold,
        include_as = include_as,
        verbose = verbose,
        )

    return tot_count

def total_metabolites_count(
        data_frame,
        threshold = 0.,
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

    if include is True:
        include_as = names.name_metabolites_count
    else:
        include_as = include

    tot_count = total_count(
        data_frame,
        name_list = 'all',
        threshold = threshold,
        include_as = include_as,
        verbose = verbose,
        )

    return tot_count
