#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Routines for performing ordination statistics on sample data.

@author: Alraune Zech, Jorrit Bakker
"""

import numpy as np
import pandas as pd
import skbio.stats.ordination as sciord
from scipy.stats import zscore
from sklearn import decomposition
from mibipret.data.names import name_sample
# from mibipret.data.data import compare_lists

import sys
path = '/home/alraune/GitHub/MiBiPreT/mibipret/mibipret/'
sys.path.append(path) # append the path to module
from data.data import compare_lists
try:
    from data.names import setting_data
except ImportError:
    from .data.names import setting_data

def pca(data_frame,
        independent_variables = False,
        dependent_variables = False,
        n_comp = 2,
        replace_NaN = 'remove',
        verbose = False,
        ):
    """Function that performs Principal Component Analysis.

    Makes use of routine sklearn.decomposition.PCA on the input data and gives
    the site scores and loadings.

    Principal component analysis (PCA) is a linear dimensionality reduction
    technique with applications in exploratory data analysis, visualization
    and data preprocessing. The data is linearly transformed onto a new
    coordinate system such that the directions (principal components) capturing
    the largest variation in the data can be easily identified.

    Input
    -----
        data_frame : pd.dataframe
            Tabular data containing variables to be evaluated with standard
            column names and rows of sample data.
        independent_variables : Boolean or list of strings; default False
            list with column names to select from data_frame
            being characterized as independent variables (= environment)
        dependent_variables : Boolean or list of strings; default is False
            list with column names to select from data_frame
            being characterized as dependent variables (= species)
        n_comp : int, default is 2
            Number of components to report
        replace_NaN : string or float, default "remove"
            Keyword specifying how to handle missing/NaN/non-numeric values,
            for all options see filter_values().        
        verbose : Boolean, The default is False.
           Set to True to get messages in the Console about the status of the run code.

    Output
    ------
        results : Dictionary
            containing the scores and loadings of the PCA,
            the percentage of the variation explained by the first principal components,
            the correlation coefficient between the first two PCs,
            names of columns (same length as loadings)
            names of indices (same length as scores)
    """
    if verbose:
        print('==============================================================')
        print(" Running function 'pca()' on data")
        print('==============================================================')

    data,cols= check_data_frame(data_frame)

    if independent_variables is False and dependent_variables is False:
        data_pca = data
        names_independent = cols
        names_dependent = []

    elif independent_variables is not False and dependent_variables is False:
        names_independent = extract_variables(cols,
                              independent_variables,
                              name_variables = 'independent variables'
                              )
        names_dependent = []
        data_pca = data[names_independent]
    elif independent_variables is False and dependent_variables is not False:
        names_dependent = extract_variables(cols,
                              dependent_variables,
                              name_variables = 'dependent variables'
                              )
        names_independent = []
        data_pca = data[names_dependent]

    else:
        names_independent = extract_variables(cols,
                              independent_variables,
                              name_variables = 'independent variables'
                              )
        names_dependent = extract_variables(cols,
                              dependent_variables,
                              name_variables = 'dependent variables'
                              )
        data_pca = data[names_independent + names_dependent]

    # Checking that all values are numeric and replacing according to specified method

    if replace_NaN is not False:
        filter_values(data_pca, replace_NaN = replace_NaN, verbose = verbose)

    # Checking if the dimensions of the dataframe allow for PCA
    if data_pca.shape[0] < data_pca.shape[1]:
        raise ValueError("PCA not possible with more variables than samples.")

    try:
        # Using scikit.decomposoition.PCA with an amount of components equal
        # to the amount of variables, then getting the loadings, scores and explained variance ratio.
        pca = decomposition.PCA(n_components=len(data_pca.columns))
        pca.fit(data_pca)
        loadings = pca.components_.T
        PCAscores = pca.transform(data_pca)
        variances = pca.explained_variance_ratio_
    except(ValueError,TypeError):
        raise TypeError("Not all column values are numeric values (or NaN). Consider standardizing data first.")

    # Taking the first two PC for plotting
    if dependent_variables is False:
        loadings_independent = loadings[:, 0:n_comp]
        loadings_dependent = np.array([[],[]]).T
    else:
        loadings_independent = loadings[:-len(names_dependent), 0:n_comp]
        loadings_dependent = loadings[-len(names_dependent):, 0:n_comp]
    scores = PCAscores[:, 0:n_comp]
    percent_explained = np.around(100*variances/np.sum(variances), decimals=2)
    coef = np.corrcoef(scores[:,0], scores[:,1])[0,1]

    if verbose:
        print("Information about the success of the PCA:")
        print('----------------------------------------------------------------')
        for i in range(len(percent_explained)):
            print('Principle component {} explains {}% of the total variance.'.format(i,percent_explained[i]))
        print('\nThe correlation coefficient between PC1 and PC2 is {}.'.format(coef))
        print('----------------------------------------------------------------')

    results = {"method": 'pca',
               "loadings_dependent": loadings_dependent,
               "loadings_independent": loadings_independent,
               "names_independent" : names_independent,
               "names_dependent" : names_dependent,
               "scores": scores,
               "sample_index" : list(data_pca.index),
               "percent_explained": percent_explained,
               "corr_PC1_PC2": coef,
               }

    return results

def cca(data_frame,
        independent_variables,
        dependent_variables,
        n_comp = 2,
        verbose = False,
        ):
    """Function that performs Canonical Correspondence Analysis.

    Function makes use of skbio.stats.ordination.CCA on the input data and gives
    the site scores and loadings.

    Input
    -----
        data_frame : pd.dataframe
            Tabular data containing variables to be evaluated with standard
            column names and rows of sample data.
        independent_variables : list of strings
            list with column names data to be the independent variables (=environment)
        dependent_variables : list of strings
            list with column names data to be the dependen variables (=species)
        n_comp : int, default is 2
            number of dimensions to return
        verbose : Boolean, The default is False.
            Set to True to get messages in the Console about the status of the run code.

    Output
    ------
        results : Dictionary
            * method: name of ordination method (str)
            * loadings_independent: loadings of independent variables (np.ndarray)
            * loadings_dependent: loadings of dependent variables (np.ndarray)
            * names_independent: names of independent varialbes (list of str)
            * names_dependent: names of dependent varialbes (list of str)
            * scores: scores (np.ndarray)
            * sample_index: names of samples (list of str)
    """
    if verbose:
        print('==============================================================')
        print(" Running function 'cca()' on data")
        print('==============================================================')

    results = constrained_ordination(data_frame,
                           independent_variables,
                           dependent_variables,
                           method = 'cca',
                           n_comp = n_comp,
                           )
    return results

def rda(data_frame,
        independent_variables,
        dependent_variables,
        n_comp = 2,
        verbose = False,
        ):
    """Function that performs Redundancy Analysis.

    Function makes use of skbio.stats.ordination.RDA on the input data and gives
    the site scores and loadings.

    Input
    -----
        data_frame : pd.dataframe
            Tabular data containing variables to be evaluated with standard
            column names and rows of sample data.
        independent_variables : list of strings
            list with column names data to be the independent variables (=envirnoment)
        dependent_variables : list of strings
            list with column names data to be the dependent variables (=species)
        n_comp : int, default is 2
            number of dimensions to return
        verbose : Boolean, The default is False.
            Set to True to get messages in the Console about the status of the run code.

    Output
    ------
        results : Dictionary
            * method: name of ordination method (str)
            * loadings_independent: loadings of independent variables (np.ndarray)
            * loadings_dependent: loadings of dependent variables (np.ndarray)
            * names_independent: names of independent varialbes (list of str)
            * names_dependent: names of dependent varialbes (list of str)
            * scores: scores (np.ndarray)
            * sample_index: names of samples (list of str)
    """
    if verbose:
        print('==============================================================')
        print(" Running function 'rda()' on data")
        print('==============================================================')

    results = constrained_ordination(data_frame,
                           independent_variables,
                           dependent_variables,
                           method = 'rda',
                           n_comp = n_comp,
                           )
    return results


def constrained_ordination(data_frame,
                           independent_variables,
                           dependent_variables,
                           method = 'cca',
                           n_comp = 2,
        ):
    """Function that performs constrained ordination.

    Function makes use of skbio.stats.ordination on the input data and gives
    the scores and loadings.

    Input
    -----
        data_frame : pd.DataFrame
            Tabular data containing variables to be evaluated with standard
            column names and rows of sample data.
        independent_variables : list of strings
           list with column names data to be the independent variables (=environment)
        dependent_variables : list of strings
           list with column names data to be the dependen variables (=species)
        method : string, default is cca
            specification of ordination method of choice. Options 'cca' & 'rda'
        n_comp : int, default is 2
            number of dimensions to return

    Output
    ------
        results : Dictionary
            * method: name of ordination method (str)
            * loadings_independent: loadings of independent variables (np.ndarray)
            * loadings_dependent: loadings of dependent variables (np.ndarray)
            * names_independent: names of independent varialbes (list of str)
            * names_dependent: names of dependent varialbes (list of str)
            * scores: scores (np.ndarray)
            * sample_index: names of samples (list of str)
    """
    data,cols= check_data_frame(data_frame)

    intersection = extract_variables(cols,
                          independent_variables,
                          name_variables = 'independent variables'
                          )
    data_independent_variables = data[intersection]

    intersection = extract_variables(cols,
                          dependent_variables,
                          name_variables = 'dependent variables'
                          )
    data_dependent_variables = data[intersection]

    # Checking if the dimensions of the dataframe allow for CCA
    if (data_dependent_variables.shape[0] < data_dependent_variables.shape[1]) or \
        (data_independent_variables.shape[0] < data_independent_variables.shape[1]):
        raise ValueError("Ordination method {} not possible with more variables than samples.".format(method))

    try:
        # Performing constrained ordination using function from scikit-bio.
        if method == 'cca':
            sci_ordination = sciord.cca(data_dependent_variables, data_independent_variables, scaling = n_comp)
        elif method == 'rda':
            sci_ordination = sciord.rda(data_dependent_variables, data_independent_variables, scaling = n_comp)
        else:
            raise ValueError("Ordination method {} not a valid option.".format(method))

        loadings_independent = sci_ordination.biplot_scores.to_numpy()[:,0:n_comp]
        loadings_dependent = sci_ordination.features.to_numpy()[:,0:n_comp]
        scores = sci_ordination.samples.to_numpy()[:,0:n_comp]

    except(TypeError):
        raise TypeError("Not all column values are numeric values. Consider standardizing data first.")

    if loadings_independent.shape[1]<n_comp:
        raise ValueError("Number of dependent variables too small.")

    results = {"method": method,
               "loadings_dependent": loadings_dependent,
               "loadings_independent": loadings_independent,
               "names_independent" : data_independent_variables.columns.to_list(),
               "names_dependent" : data_dependent_variables.columns.to_list(),
               "scores": scores,
               "sample_index" : list(data.index),
               }

    return results

def check_data_frame(data_frame,
                     inplace = False,
                     ):
    """Checking data on correct format.

    Input
    -----
        data_frame: pd.DataFrame
            quantities for data analysis given per sample

    Output
    ------
        data: pd.DataFrame
            copy of given dataframe with index set to sample name
        cols: list
            List of column names
    """
    if not isinstance(data_frame, pd.DataFrame):
        raise ValueError("Calculation not possible with given data. \
                          Data has to be a panda-DataFrame or Series \
                          but is given as type {}".format(type(data_frame)))
    else:
        if inplace is False:
            data = data_frame.copy()
        else:
            data = data_frame
        cols = data.columns.to_list()
        if name_sample in data.columns:
            data.set_index(name_sample,inplace = True)
            cols.remove(name_sample)

    return data, cols

def extract_variables(columns,
                      variables,
                      name_variables = 'variables',
                      ):
    """Checking overlap of two given list.

    Function is used for checking if a list of variables is present in
    the column names of a given dataframe (of quantities for data analysis)

    Input
    -----
        columns: list of strings
            given extensive list (usually column names of a pd.DataFrame)
        variables: list of strings
            list of names to extract/check overlap with strings in list 'column'
        name_variables: str, default is 'variables'
            name of type of variables given in list 'variables'

    Output
    ------
        intersection: list
            list of strings present in both lists 'columns' and 'variables'

    """

    if not isinstance(variables,list):
        raise ValueError("List of column names for '{}' empty or in wrong format.".format(name_variables))

    intersection,remainder,remainder_list1,remainder_list2 = compare_lists(columns,variables)

    if len(intersection) == 0:
        raise ValueError("No column names for '{}' identified in columns of dataframe.".format(name_variables))
    elif len(intersection) < len(variables):
        print("WARNING: not all column names for '{}' are found in dataframe.".format(name_variables))
        print('----------------------------------------------------------------')
        print("Columns used in analysis:", intersection)
        print("Column names not identified in data:", remainder_list2)
        print('________________________________________________________________')
        
    # if isinstance(variables,list):
    #     intersection = list(set(columns) & set(variables))
    #     remainder = list(set(variables) - set(columns))
    #     if len(intersection) == 0:
    #         raise ValueError("No column names for '{}' identified in columns of dataframe.".format(name_variables))
    #     elif len(intersection) < len(variables):
    #         print("WARNING: not all column names for '{}' are found in dataframe.".format(name_variables))
    #         print('----------------------------------------------------------------')
    #         print("Columns used in analysis:", intersection)
    #         print("Column names not identified in data:", remainder)
    #         print('________________________________________________________________')
    # else:
    #     raise ValueError("List of column names for '{}' empty or in wrong format.".format(name_variables))

    return intersection

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