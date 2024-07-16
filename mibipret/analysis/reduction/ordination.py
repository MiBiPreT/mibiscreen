#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 13:59:36 2024

@author: alraune
"""

import numpy as np
import pandas as pd
from sklearn import decomposition
# import skbio.stats.ordination as sciord

from mibipret.data.names import name_sample

def pca(data, 
        select_columns = False,
        n_comp = 2,
        verbose = False,
        ):

    '''
    Function that performs Principal Component Analysis.
    
    Makes use of routine sklearn.decomposition.PCA on the input data and gives 
    the site scores and loadings.
    
    Principal component analysis (PCA) is a linear dimensionality reduction 
    technique with applications in exploratory data analysis, visualization 
    and data preprocessing. The data is linearly transformed onto a new 
    coordinate system such that the directions (principal components) capturing 
    the largest variation in the data can be easily identified. 

    Parameters
    ----------
        data : pd.dataframe
            Tabular data containing quantities to be evaluated with standard
            column names and rows of sample data.
        n_comp : int, default is 2
            Number of components to report
        select_columns: Boolean or list of strings; default False
           list with column names to select from dataframe for analysis             
        verbose : Boolean, The default is False.
           Set to True to get messages in the Console about the status of the run code. 

    Returns
    -------
        results : Dictionary
            containing the scores and loadings of the PCA, 
            the percentage of the variation explained by the first principal components
            and the correlation coefficient between the first two PCs
    '''

    if verbose:
        print('==============================================================')
        print(" Running function 'pca()' on data")
        print('==============================================================')

    cols= check_data(data)       
    data_pca = data.copy()
    
    if name_sample in cols:
        data_pca.set_index(name_sample,inplace = True)
        cols.remove(name_sample)
    
    if isinstance(select_columns,list):
        intersection = list(set(cols) & set(select_columns))
        remainder = list(set(select_columns) - set(cols))
        if len(intersection) == 0:
            raise ValueError("No specified column names identified in data.")     
        elif len(intersection) < len(select_columns):
            print("WARNING: not all specified column names are found in data.")
            print('----------------------------------------------------------------')
            print("Columns used in analysis:", intersection)
            print("Column names not identified in data:", remainder)
            print('________________________________________________________________')

        # data_pca = data_pca.get(intersection)
        data_pca = data_pca[intersection]

    # heads = data_pca.columns.to_list()
    # wells = list(data_pca.index)
    
    # Checking if the dimensions of the dataframe allow for PCA
    if data_pca.shape[0] < data_pca.shape[1]:
        raise Exception("PCA not possible with more variables than samples.")

    try:
        # Using scikit.decomposoition.PCA with an amount of components equal to the amount of variables, then getting the loadings, scores and explained variance ratio.
        pca = decomposition.PCA(n_components=len(data_pca.columns)) 
        pca.fit(data_pca)
        loadings = pca.components_.T
        PCAscores = pca.transform(data_pca)
        variances = pca.explained_variance_ratio_
    except(ValueError):
        raise ValueError("Not all column values are numeric values. Consider standardizing data first.")
    
    # Taking the first two PC for plotting
    loadings = loadings[:, 0:n_comp]
    scores = PCAscores[:, 0:n_comp]
    percent_explained = np.around(100*variances/np.sum(variances), decimals=2)
    coef = np.corrcoef(scores[:,0], scores[:,1])[0,1]
    
    if verbose:
        print("Information about the succes of the PCA:")
        print('----------------------------------------------------------------')        
        for i in range(len(percent_explained)):
            print('Principle component {} explains {} \% of the total variance.'.format(i,percent_explained[i]))
        print('\nThe correlation coefficient between PC1 and PC2 is {}.'.format(coef))
        print('----------------------------------------------------------------')
    
    results = {"method": 'pca',
               "loadings": loadings, 
               "scores": scores, 
               "percent_explained": percent_explained,
               "corr_PC1_PC2": coef,
               }

    # if sample_names is True:
    #     names = data[name_sample]

    # sample_names = False,
    # heads = data_pca.columns.to_list()
    # wells = list(data_pca.index)
    # names = {"heads": heads, "Species_head": Species_head, "Environment_head": Environment_head, "wells": wells}
    
    return results

def check_data(data):
    """Checking data on correct format.

    Input
    -----
        data: pd.DataFrame
            concentration values of quantities

    Output
    ------
        cols: list
        List of column names
    """
    if isinstance(data, pd.DataFrame):
        cols = data.columns.to_list()
    # elif isinstance(data, pd.Series):
    #     cols = [data.name]
    else:
        raise ValueError("Calculation not possible with given data. \
                          Data has to be a panda-DataFrame or Series \
                          but is given as type {}".format(type(data)))

    return cols
