#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Routines for performing ordination statistics on sample data.

@author: Alraune Zech, Jorrit Bakker
"""

# import numpy as np
# import pandas as pd
# import skbio.stats.ordination as sciord
# from scipy.stats import zscore
# from sklearn import decomposition
# from mibipret.data.names import name_sample
# # from mibipret.data.data import compare_lists

# import sys
# path = '/home/alraune/GitHub/MiBiPreT/mibipret/mibipret/'
# sys.path.append(path) # append the path to module
# from data.data import compare_lists
# try:
#     from data.names import setting_data
# except ImportError:
#     from .data.names import setting_data


def filter_values(data_frame, 
                  replace_NaN = 'remove', 
                  drop_rows = [], 
                  inplace = True,
                  verbose = False):

    """
    Filtering values of dataframes for ordination to assure all are numeric.
    
    Ordination methods require all cells to be filled. This method checks the
    provided data frame if values are missing/NaN or not numeric and handles
    missing/NaN values accordingly. 
       
    Then removes select rows and mutates the cells containing NULL values based 
    on the input parameters.

    Input
    -----
        data_frame : pd.dataframe
            Tabular data containing variables to be evaluated with standard
            column names and rows of sample data.
        replace_NaN : string or float, default "remove"
            Keyword specifying how to handle missing/NaN/non-numeric values, options:
                - remove: remove rows with missing values
                - zero: replace values with 0.0
                - average: replace the missing values with the average of the variable 
                            (using all other available samples)
                - median: replace the missing values with the median of the variable 
                                        (using all other available samples)
                - float-value: replace all empty cells with that numeric value
        drop_rows : List, default [] (empty list)
            List of rows that should be removed from dataframe.
        inplace: bool, default True
            If False, return a copy. Otherwise, do operation in place.
        verbose : Boolean, The default is False.
           Set to True to get messages in the Console about the status of the run code.

    Output
    ------
        data_filtered : pd.dataframe
            Tabular data containing filtered data.
    """
    data,cols= check_data_frame(data_frame,inplace = inplace)

    if verbose:
        print("==============================================================================")
        print('Perform filtering of values since ordinatin requires all values to be numeric.')

    if len(drop_rows)>0:
        data.drow(drop_rows, inplace = True)
        if verbose:
            print('The samples of rows {} have been removed'.format(drop_rows))

    # Identifying which rows and columns contain any amount of NULL cells and putting them in a list.
    NaN_rows = data[data.isna().any(axis=1)].index.tolist()
    NaN_cols = data.columns[data.isna().any()].tolist()
      
    # If there are any rows containing NULL cells, the NULL values will be filter
    if len(NaN_rows)>0:
        if replace_NaN == 'remove':
            data.drop(NaN_rows, inplace = True)
            text = 'The sample row(s) have been removed since they contain NaN values: {}'.format(NaN_rows)
        elif replace_NaN == 'zero':
            set_NaN = 0.0
            data.fillna(set_NaN, inplace = True)
            text = 'The values of the empty cells have been set to zero (0.0)'
        elif isinstance(replace_NaN, (float, int)):
            set_NaN = float(replace_NaN)
            data.fillna(set_NaN, inplace = True)
            text = 'The values of the empty cells have been set to the value of {}'.format(set_NaN)
        elif replace_NaN == "average":
            for var in NaN_cols:
                data[var] = data[var].fillna(data[var].mean(skipna = True))
            text = 'The values of the empty cells have been replaced by the average of\
                  the corresponding variables (using all other available samples).'
        elif replace_NaN == "median":
            for var in NaN_cols:
                data[var] = data[var].fillna(data[var].median(skipna = True))
            text = 'The values of the empty cells have been replaced by the median of\
                  the corresponding variables (using all other available samples).'
        else:
            raise ValueError("Value of 'replace_NaN' unknown:", replace_NaN)
        
        if verbose:
            print(text)
    else:
        if verbose:
            print("No data to be filtered out.")
        
    return data

def transform_values(data_frame,
                     name_list = 'all',
                     how = 'log_scale',
                     log_scale_A = 1, 
                     log_scale_B = 1,
                     inplace = True,
                     verbose = False,
                     ):

    """Function extracting data from dataframe for specified variables.

    Args:
    -------
        data_frame: pandas.DataFrames
            dataframe with the measurements
        name_variables: string or list of strings, default 'all'
            list of quantities (column names) to perfrom transformation on
        how: string, default 'standardize'
            Type of transformation:
                * standardize
                * log_scale: 
                * center
        inplace: bool, default True
            If False, return a copy. Otherwise, do operation in place and return None.
        verbose : Boolean, The default is False.
           Set to True to get messages in the Console about the status of the run code.

    Returns:
    -------
        data: pd.DataFrame
            dataframe with the measurements

    Raises:
    -------
    None (yet).

    Example:
    -------
    """
    data,cols= check_data_frame(data_frame,inplace = inplace)

    if verbose:
        print('==============================================================')
        print(" Running function 'transform_values()' on data")
        print('==============================================================')

    if name_list == 'all':
        intersection = list(set(cols) - set(setting_data))

    else:
        intersection,remainder,remainder_list1,remainder_list2 = compare_lists(cols,name_list)
        if len(intersection) < len(name_list):
            print("WARNING: not all variables in name_list are found in dataframe.")
            print('----------------------------------------------------------------')
            print("Column names identified:", intersection)
            print("Column names not identified in data:", remainder_list2)
            print('________________________________________________________________')

    for quantity in intersection:
        if how == 'log_scale':
            data[quantity] = np.log10(log_scale_A * data[quantity] + log_scale_B)
        elif how == 'center':
            data[quantity] =  data[quantity]-data[quantity].mean()
        elif how == 'standardize':
            data[quantity] = zscore(data[quantity].values)

    return data

# def transform(dataframe, Center = False, Standardize = True, LogScale = False, LogScale_A = 1, LogScale_B = 1, verbose = False):
#     """A function that performs certain transformations on the input data based on the input parameters.

#     Parameters
#     ----------
#     dataframe : Dataframe
#         A dataframe containing data to be transformed.
#     Center : Boolean, optional
#         Parameter. When set to true, the data will be centered per variable, giving it an average of 0. The default is False.
#     Standardize : Boolean, optional
#         Parameter. When set to true, the data will be standardized per variable, giving it an average of 0 and a range between 0 and 1. The default is False.. The default is True.
#     LogScale : Boolean or List, optional
#         Parameter. Set to false to disable log transformation, set to True when wanting to log transform every variable. Otherwise provide a list of all variable column names you want to transform The default is False.
#     LogScale_A : Integer or float, optional
#         Parameter. Determines the method of Log transformation, where this is A in log10(Ax+B). The default is 1.
#     LogScale_B : Interger or float, optional
#        Parameter. Determines the method of Log transformation, where this is B in log10(Ax+B). The default is 1.
#     verbose : Boolean, optional
#          Set to True to get messages in the Console about the status of the run code. The default is False.

#     Returns
#     -------
#     dataframe : Dataframe
#         A dataframe containing the transformed input data.
#     """
#     # If the LogScale parameter is in the form of a list, log transform every column of which the name is in the list.
#     if type(LogScale) == list:
#         for Variable in LogScale:
#             dataframe[Variable] = np.log10(LogScale_A * dataframe[Variable] + LogScale_B)
#     # Otherwise, if the LogScale parameter is set to true, log scale every value in the dataframe.
#     elif LogScale:
#         if verbose: print("Data is being log scaled...")
#         dataframe = np.log10(LogScale_A * dataframe + LogScale_B)
    
#     # If the Center parameter is true, but not the Standardize parameter, center the data by subtracting the mean of every column from its values.
#     if Center and not Standardize:
#         if verbose: print("Data is being centered...")
#         dataframe = dataframe.apply(lambda col: col-col.mean())
#     # If the Standardize parameter is true, standardize all columns.
#     elif Standardize:
#         if verbose: print("Data is being standardized...")
#         dataframe = stats.zscore(dataframe, axis=0)
    
#     return(dataframe)