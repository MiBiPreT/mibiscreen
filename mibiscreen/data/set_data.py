#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Functions for data extraction and merging in preparation of analysis and plotting.

@author: Alraune Zech
"""
import pandas as pd
import mibiscreen.data.settings.standard_names as names
from mibiscreen.data.check_data import check_data_frame
from mibiscreen.data.settings.contaminants import contaminant_groups
from mibiscreen.data.settings.environment import environment_groups
from mibiscreen.data.settings.sample_settings import sample_settings


def determine_quantities(cols,
         name_list = 'all',
         verbose = False,
         ):
    """Select a subset of column names (from DataFrame).

    Input
    -----
        cols: list
            Names of quantities (column names) from pd.DataFrame
        name_list: str or list of str, default is 'all'
            quantities to extract from column names.

            If a list of strings is provided, these will be selected from the list of column names (col)
            If a string is provided, this is a short name for a specific group of quantities:
                - 'all' (all quantities given in data frame except settings)
                - short name for group of contaminants:
                    - 'BTEX' (for benzene, toluene, ethylbenzene, xylene)
                    - 'BTEXIIN' (for benzene, toluene, ethylbenzene, xylene,
                                  indene, indane and naphthaline)
                    - 'all_cont' (for all contaminant in name list)
                - short name for group of environmental parameters/geochemicals:
                    - 'environmental_conditions'
                    - 'geochemicals'
                    - 'ONS':  non reduced electron acceptors (oxygen, nitrate, sulfate)
                    - 'ONSFe': selected electron acceptors  (oxygen, nitrate, sulfate + iron II)
                    - 'all_ea': all potential electron acceptors (non reduced & reduced)
                    - 'NP': nutrients (nitrate, nitrite, phosphate)
                See also file mibiscreen/data/name_data for lists of quantities
        verbose: Boolean
            verbose flag (default False)

    Output
    ------
        quantities: list
            list of strings with names of selected quantities present in dataframe
        remainder: list
            list of strings with names of selected quantities not present in dataframe

    """
    if name_list == 'all':
        ### choosing all column names except those of settings
        list_names = list(set(cols) - set(sample_settings))
        if verbose:
            print("Selecting all data columns except for those with settings.")

    elif isinstance(name_list, str):
        if name_list in contaminant_groups.keys():
            verbose_text = "Selecting specific group of contaminants:"
            list_names = contaminant_groups[name_list].copy()
            if (names.name_o_xylene in cols) and (names.name_pm_xylene in cols):
                list_names.remove(names.name_xylene) # handling of xylene isomeres

        elif name_list in environment_groups.keys():
            verbose_text = "Selecting specific group of geochemicals:"
            list_names = environment_groups[name_list].copy()

        else:
            verbose_text = "Selecting single quantity:"
            list_names = [name_list]

        if verbose:
            print(verbose_text,name_list)
            print('_____________________________________________________________')

    elif isinstance(name_list, list): # choosing specific list of column names except those of settings
        if not all(isinstance(item, str) for item in name_list):
            raise ValueError("Keyword 'name_list' needs to be a string or a list of strings.")
        list_names = name_list
        if verbose:
            print("Selecting all names from provided list.")

    else:
        raise ValueError("Keyword 'name_list' needs to be a string or a list of strings.")

    quantities,_,remainder_list2 = compare_lists(cols,list_names)

    if not quantities:
        raise ValueError("No quantities from name list '{}' provided in data.\
                         Presumably data not in standardized format. \
                         Run 'standardize()' first.".format(name_list))

    if verbose:
        print("Selected set of quantities: \n---------------------------")
        print(*quantities,sep='\n')
        print('_____________________________________________________________')

    if remainder_list2:
        print("WARNING: There are quantities from name list not in data")
        if verbose:
            print(*remainder_list2,sep='\n')
        print("Maybe data not in standardized format. Run 'standardize()' first.")
        print("_________________________________________________________________")


    return quantities,remainder_list2

def extract_settings(data_frame,
                     verbose = False,
                     ):
    """Extracting data of specified variables from dataframe.

    Args:
    -------
        data_frame: pandas.DataFrames
            dataframe with the measurements
        verbose: Boolean
            verbose flag (default False)

    Returns:
    -------
        data: pd.DataFrame
            dataframe with settings

    Raises:
    -------
    None (yet).

    Example:
    -------
    To be added.

    """
    ### check on correct data input format and extracting column names as list
    data,cols= check_data_frame(data_frame,inplace = False)

    settings,r1,r2 = compare_lists(cols,sample_settings)

    if verbose:
        print("Settings available in data: ", settings)

    return data[settings]


def extract_data(data_frame,
                 name_list,
                 keep_setting_data = True,
                 verbose = False,
                 ):
    """Extracting data of specified variables from dataframe.

    Args:
    -------
        data_frame: pandas.DataFrames
            dataframe with the measurements
        name_list: list of strings
            list of column names to extract from dataframe
        keep_setting_data: bool, default True
            Whether to keep setting data in the DataFrame.
        verbose: Boolean
            verbose flag (default False)

    Returns:
    -------
        data: pd.DataFrame
            dataframe with the measurements

    Raises:
    -------
    None (yet).

    Example:
    -------
    To be added.

    """
    ### check on correct data input format and extracting column names as list
    data,cols= check_data_frame(data_frame,inplace = False)

    quantities, _ = determine_quantities(cols,
                                      name_list = name_list,
                                      verbose = verbose)

    if keep_setting_data:
        settings,_,_ = compare_lists(cols,sample_settings)
        i1,quantities_without_settings,_ = compare_lists(quantities,settings)
        columns_names = settings + quantities_without_settings

    else:
        columns_names = quantities

    return data[columns_names]


def merge_data(data_frames_list,
               how='outer',
               on=[names.name_sample],
               clean = True,
               **kwargs,
               ):
    """Merging dataframes along columns on similar sample name.

    Args:
    -------
        data_frames_list: list of pd.DataFrame
            list of dataframes with the measurements
        how: str, default 'outer'
            Type of merge to be performed.
            corresponds to keyword in pd.merge()
            {‘left’, ‘right’, ‘outer’, ‘inner’, ‘cross’}, default ‘outer’
        on: list, default "sample_nr"
            Column name(s) to join on.
            corresponds to keyword in pd.merge()
        clean: Boolean, default True
            Whether to drop columns which are in all provided data_frames
            (on which not to merge, potentially other settings than sample_name)
        **kwargs: dict
            optional keyword arguments to be passed to pd.merge()

    Returns:
    -------
        data: pd.DataFrame
            dataframe with the measurements

    Raises:
    -------
    None (yet).

    Example:
    -------
    To be added.

    """
    if len(data_frames_list)<2:
        raise ValueError('Provide List of DataFrames.')


    data_merge = data_frames_list[0]
    for data_add in data_frames_list[1:]:
        if clean:
            intersection,remainder_list1,remainder_list2 = compare_lists(
                data_merge.columns.to_list(),data_add.columns.to_list())
            intersection,remainder_list1,remainder_list2 = compare_lists(intersection,on)
            data_add = data_add.drop(labels = remainder_list1+remainder_list2,axis = 1)
        data_merge = pd.merge(data_merge,data_add, how=how, on=on,**kwargs)
        # complete data set, where values of porosity are added (otherwise nan)

    return data_merge

### ===========================================================================
### Auxilary Functions
### ===========================================================================

def compare_lists(list1,
                  list2,
                  verbose = False,
                  ):
    """Checking overlap of two given list.

    Input
    -----
        list1: list of strings
            given extensive list (usually column names of a pd.DataFrame)
        list2: list of strings
            list of names to extract/check overlap with strings in list 'column'
        verbose: Boolean, default True
            verbosity flag

    Output
    ------
        (intersection, remainder_list1, reminder_list2): tuple of lists
            * intersection: list of strings present in both lists 'list1' and 'list2'
            * remainder_list1: list of strings only present in 'list1'
            * remainder_list2: list of strings only present in 'list2'

    Example:
    -------
    list1 = ['test1','test2']
    list2 =  ['test1','test3']

    (['test1'],['test2']['test3']) = compare_lists(list1,list2)

    """
    intersection = list(set(list1) & set(list2))
    remainder_list1 = list(set(list1) - set(list2))
    remainder_list2 = list(set(list2) - set(list1))

    if verbose:
        print('================================================================')
        print(" Running function 'extract_variables()'")
        print('================================================================')
        print("strings present in both lists:", intersection)
        print("strings only present in either of the lists:", remainder_list1 +  remainder_list2)

    return (intersection,remainder_list1,remainder_list2)
