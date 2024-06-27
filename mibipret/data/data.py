#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Functions for data I/O handling.

@author: Alraune Zech
"""

import os.path
import pandas as pd
from .names import col_dict
from .names import contaminants
from .names import electron_acceptors


#print(electron_acceptors)
def load_excel(
        file_path = None,
        sheet_name = 'Sheet1',
        verbose = False,
        store_provenance = False,
        **kwargs,
        ):
    """Function to load data from excel file.
    
    Args:
    -------
        file_path (str): Name of the path to the file
        sheet_name (int): Number of the sheet in the excel file to load
        verbose (bool): flag 
        store_provenance (bool): ...
        **kwargs - optional keyword arguments to pass to pandas' routine 
            read_excel()

    Returns:
    -------
        pandas.DataFrame: Tabular data
        
    Raises:
    -------
        ValueError: If `file_path` is not a valid file location

    Example:
    -------
       This function can be called with the file path of the example data as 
       argument using:

        >>> from mibipret.data import load_excel
        >>> load_excel(example_data.xlsx)
        
    """
    if file_path is None:
        raise ValueError('Specify file path and file name!')
    if not os.path.isfile(file_path):
        raise ValueError('Specified file does not exist: ',file_path)
    
    data = pd.read_excel(file_path, 
                         sheet_name = sheet_name,
                         **kwargs)
    if ";" in data.iloc[1][0]:
        data = pd.read_excel(file_path, 
                             sep=";", 
                             sheet_name = sheet_name,
                             **kwargs)
    units = data.iloc[0]

    return data, units
    
def load_csv(        
        file_path = None,
        verbose = False,
        store_provenance = False,
        ):
    """Function to load data from csv file.
    
    Args:
    -------
        file_path (str): Name of the path to the file
        verbose (bool): flag 
        store_provenance (bool): ...

    Returns:
    -------
        pandas.DataFrame: Tabular data
        
    Raises:
    -------
        ValueError: If `file_path` is not a valid file location


    Example:
    -------
       This function can be called with the file path of the example data as 
       argument using:

        >>> from mibipret.data import load_excel
        >>> load_excel(example_data.csv)


    """
    if file_path is None:
        raise ValueError('Specify file path and file name!')
    if not os.path.isfile(file_path):
        raise ValueError('Specified file does not exist!')
    
    data = pd.read_csv(file_path, encoding="unicode_escape")
    if ";" in data.iloc[1][0]:
        data = pd.read_csv(file_path, sep=";", encoding="unicode_escape")
    units = data.iloc[0]

    if verbose:
        print("Unit of quantities: \n", units)
        print("Loaded data:\n", data)
    return data, units

def check_columns(data, verbose = True):
    """Function that looks at the column names and renames the columns to
        the standard names of the model
    
    Args:
    -------
        data (df): dataframe with the measurements
    
    
    Returns:
    -------
        pandas.DataFrame: Tabular data with standard column names
    
        
    Raises:
    -------
    
    Example:
    -------
    Todo's:
        - complete list of potential contaminants, environmental factors
        - add name check for metabolites?
        - return column names that have not been identified
        - option to return only columns identified
        - add key-word to specify which data to extract
            (i.e. data columns to return)
    
    """
    data.columns = [col_dict.get(x, x) for x in data.columns]
    # Todo: modify to first only report renaming of column names 
    data = data.fillna(0)

    if verbose:
        print("Data with modified column names:\n", data)    

    return data
   
def check_units(data):
    """Function to check the units of the measurements

    Args:
    -------
        data (df): dataframe with the measurements


    Returns:
    -------
        None

        
    Raises:
    -------

    Example:
    -------
    """
    mgperl = ["mg/L", "mg/l", "MG/L"]
    microgperl = [
        "ug/l",
        "ug/L",
        "micro g/l",
        "micro g/L",
        "MICRO G/L",
        r"$\mu$ g/l",
        r"$\mu$ g/L",
    ]
    
    cols = data.columns
    # print(cols)
    col_check_list= []

    for quantity in electron_acceptors:
        if quantity in cols:
            if data[quantity][0] not in mgperl:
                print("Warning: Check unit of {}!\n Given in {}, \
                      but must be mg/L.".format(quantity,data[quantity][0]))
                # raise ValueError("Check unit of {} - 
                # it must be mg/L.".format(quantity))
                col_check_list.append(quantity)

    for quantity in contaminants:
        if quantity in cols:
            if data[quantity][0] not in microgperl:
                print("Warning: Check unit of {}!\n Given in {}, but must \
                      be microgramm/L.".format(quantity,data[quantity][0]))
                # raise ValueError(r"Check unit of {} - it must be $\mu$g/L.".format(quantity))
                col_check_list.append(quantity)

    if "redoxpot" in data.columns:
        if data["redoxpot"][0] != "mV":
            print("Warning: Check unit of {}!\n Given in {}, but must be \
                  mV.".format("redoxpot",data[quantity][0]))
            col_check_list.append("redoxpot")

    if len(col_check_list) == 0:
        print("All quantities given in proper units")

    return col_check_list

def check_values(
        data,
        replace = 0,
        ):
    """Function that checks on value types and replaces non-measured values.
    
    Args:
    -------
        data (df): dataframe with the measurements
        replace (float,nan): value to replace missing entries with (default 0)
    
    Returns:
    -------
        pandas.DataFrame: Tabular data with standard column names
    
    
    Raises:
    -------
    
    Example:
    -------
    
    """
    if "redoxpot" in data.columns:
        data["redoxpot"].iloc[1:] = data["redoxpot"].iloc[1:].astype(float)
    data.iloc[:,1:] = data.iloc[:,1:].apply(
        lambda i: i.apply(
            lambda x: float(x)
            if str(x).replace(".", "", 1).isnumeric()
            else x
        )
    )
    data.iloc[:,1:] = data.iloc[:,1:].replace(to_replace="-", value=replace)

    return data
       
def example_data(
        data_type = 'all'):
    """Function provinging test data for mibipret data analysis
    
    Args:
    -------
        data_type (str) - type of data to return:
                            -- "all": all types of data available
                            -- "setting": well setting data only
                            -- "contaminants": data on contaminants
                            -- "environment": data on environmental
                            -- "metabolites": data on metabolites
                            -- "hydro": data on hydrogeolocial conditions
    
    Returns:
    -------
        pandas.DataFrame: Tabular data with standard column names    
    
    Raises:
    -------
    
    Example:
    -------
    
    """
    setting = ["sample_nr","obs_well","depth"]
    setting_units = [' ',' ','m']
    setting_s01 = ['2000-001', 'B-MLS1-3-12', -12]
    setting_s02 = ['2000-002', 'B-MLS1-5-15', -15.5]
    setting_s03 = ['2000-003', 'B-MLS1-6-17', -17]
    setting_s04 = ['2000-004', 'B-MLS1-7-19', -19]
    
    environment = ['pH', 'redox', 'sulfate', 'ammonium', 'sulfide', 
                   'methane', 'ironII', 'manganese']
    environment_units = [' ','mV', 'mg/L', 'mg/L', 'mg/L', 
                         'mg/L', 'mg/L', 'mg/L']
    environment_s01 = [7.23, -208, 23, 5, 0, 748, 3, 1]
    environment_s02 = [7.67, -231, 0, 6, 0, 2022, 1, 0]
    environment_s03 = [7.75, -252, 1, 13, 0, 200, 1, 0]
    environment_s04 = [7.53, -317, 9, 15, 6, 122, 0, 0]
    
    contaminants = ['benzene', 'toluene', 'ethylbenzene', 'pm_xylene', 
                    'o_xylene', 'indane', 'indene', 'naphthalene']
    contaminants_units = ['ug/L', 'ug/L', 'ug/L', 'ug/L', 
                          'ug/L', 'ug/L', 'ug/L', 'ug/L']
    contaminants_s01 = [263, 2, 269, 14, 51, 1254, 41, 2207]
    contaminants_s02 = [179, 7, 1690, 751, 253, 1352, 15, 5410]
    contaminants_s03 = [853, 17, 1286, 528, 214, 1031, 31, 3879]
    contaminants_s04 = [1254, 10, 1202, 79, 61, 814, 59, 1970]

    if  data_type == 'all':
        units = setting_units+environment_units+contaminants_units
        columns = setting+environment+contaminants
        sample_01 = setting_s01+environment_s01+contaminants_s01
        sample_02 = setting_s02+environment_s02+contaminants_s02
        sample_03 = setting_s03+environment_s03+contaminants_s03
        sample_04 = setting_s04+environment_s04+contaminants_s04
        
        data = pd.DataFrame([units,sample_01,sample_02,sample_03,sample_04],
                            columns = columns)
 
    elif  data_type == 'setting':
        data = pd.DataFrame([setting_units,setting_s01,setting_s02,setting_s03,
                             setting_s04],columns = setting)

    elif  data_type == 'environment':
        units = setting_units+environment_units
        columns = setting+environment
        sample_01 = setting_s01+environment_s01
        sample_02 = setting_s02+environment_s02
        sample_03 = setting_s03+environment_s03
        sample_04 = setting_s04+environment_s04
        
        data = pd.DataFrame([units,sample_01,sample_02,sample_03,sample_04],
                            columns = columns)

    elif  data_type == 'contaminants':
        units = setting_units+contaminants_units
        columns = setting+contaminants
        sample_01 = setting_s01+contaminants_s01
        sample_02 = setting_s02+contaminants_s02
        sample_03 = setting_s03+contaminants_s03
        sample_04 = setting_s04+contaminants_s04
        
        data = pd.DataFrame([units,sample_01,sample_02,sample_03,sample_04],
                            columns = columns)

    # columns = ['sample nr','well','depth',	'pH', 'redox', 'sulfate', 'ammonium', 'sulfide', 'methane', 'iron II', 'manganese', 'benzene', 'toluene', 'ethylbenzene', 'pm_xylene', 'o_xylene', 'indane', 'indene', 'naphthalene']
    # units = [' ',' ','m',' ','mV', 'mg/L', 'mg/L', 'mg/L', 'mg/L', 'mg/L', 'mg/L', 'ug/L', 'ug/L', 'ug/L', 'ug/L', 'ug/L', 'ug/L', 'ug/L', 'ug/L']
    # sample_01 = ['2000-001', 'B-MLS1-3-12', -12, 7.23, -208, 23, 5, 0, 748, 3, 1, 263, 2, 269, 14, 51, 1254, 41, 2207]
    # sample_02 = ['2000-002', 'B-MLS1-5-15', -15.5, 7.67, -231, 0, 6, 0, 2022, 1, 0, 179, 7, 1690, 751, 253, 1352, 15, 5410]
    # sample_03 = ['2000-003', 'B-MLS1-6-17', -17, 7.75, -252, 1, 13, 0, 200, 1, 0, 853, 17, 1286, 528, 214, 1031, 31, 3879]
    # sample_04 = ['2000-004', 'B-MLS1-7-19', -19, 7.53, -317, 9, 15, 6, 122, 0, 0, 1254, 10, 1202, 79, 61, 814, 59, 1970]
    # data = pd.DataFrame([units,sample_01,sample_02,sample_03,sample_04],columns = columns)

    return data    
 
# def validate():

# def standardize(data):
#     data = check_columns(data)
#     check_units(data)
#     data = check_format(data)
# # standardize runs check_units, check_columns and/or validation under the hood
# # validation is similar to standardize, it combines various checks, but it does not create a new standardized dataset as standardize does
# # st_sample_data = mibipret.data.standardize(data=[contaminants, metabolites], data_type="sample", store_csv=True, verbose=True, store_provenance=True)
    
# def preprocess():