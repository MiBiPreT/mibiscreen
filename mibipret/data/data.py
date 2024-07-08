#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Functions for data I/O handling.

@author: Alraune Zech
"""

import os.path
import numpy as np
import pandas as pd

try:
    from names import col_dict
    from names import contaminants
    from names import electron_acceptors
    from names import environmental_conditions
    from names import name_redox
    from names import name_sample_depth
    from names import standard_units
except ImportError:
    from .names import col_dict
    from .names import contaminants
    from .names import electron_acceptors
    from .names import environmental_conditions
    from .names import name_redox
    from .names import name_sample_depth
    from .names import standard_units

all_units = [item for sublist in list(standard_units.values()) for item in sublist]

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
        file_path: str
            Name of the path to the file
        sheet_name: int
            Number of the sheet in the excel file to load
        verbose: Boolean
            verbose flag
        store_provenance: Boolean
            To add!
        **kwargs: optional keyword arguments to pass to pandas' routine
            read_excel()

    Returns:
    -------
        data: pd.DataFrame
            Tabular data
        units: pd.DataFrame
            Tabular data on units

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
        raise OSError('Cannot access file at : ',file_path)

    data = pd.read_excel(file_path,
                         sheet_name = sheet_name,
                         **kwargs)
    if ";" in data.iloc[1].iloc[0]:
        data = pd.read_excel(file_path,
                             sep=";",
                             sheet_name = sheet_name,
                             **kwargs)

    units = data.drop(labels = np.arange(1,data.shape[0]))

    return data, units

def load_csv(
        file_path = None,
        verbose = False,
        store_provenance = False,
        ):
    """Function to load data from csv file.

    Args:
    -------
        file_path: str
            Name of the path to the file
        verbose: Boolean
            verbose flag
        store_provenance: Boolean
            To add!

    Returns:
    -------
        data: pd.DataFrame
            Tabular data
        units: pd.DataFrame
            Tabular data on units

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
        raise OSError('Cannot access file at : ',file_path)

    data = pd.read_csv(file_path, encoding="unicode_escape")
    if ";" in data.iloc[1].iloc[0]:
        data = pd.read_csv(file_path, sep=";", encoding="unicode_escape")
    units = data.drop(labels = np.arange(1,data.shape[0]))

    if verbose:
        print('==============================================================')
        print("Unit of quantities:")
        print('-------------------')
        print(units)
        print('==============================================================')
        print("Loaded data as pandas DataFrame:")
        print('--------------------------------')
        print(data)
    return data, units


def check_columns(data, verbose = True):
    """Function checking names of columns of data frame.

    Function that looks at the column names and renames the columns to
    the standard names of the model.

    Args:
    -------
        data: pd.DataFrame (df)
            dataframe with the measurements
        verbose: Boolean
            verbose statement (default True)

    Returns:
    -------
        tuple: three list containing names of
                list with identitied quantities in data (but not standardized names)
                list with unknown quantities in data (not in list of standardized names)
                list with standard names of identified quantities

    Raises:
    -------
    None (yet).

    Example:
    -------
    Todo's:
        - complete list of potential contaminants, environmental factors
        - add name check for metabolites?
    """
    column_names_standard = []
    column_names_known = []
    column_names_unknown = []

    for x in data.columns:
        y = col_dict.get(x, False)
        if y is False:
            column_names_unknown.append(x)
        else:
            column_names_known.append(x)
            column_names_standard.append(y)
    if verbose:
        print('==============================================================')
        print("{} quantities identified in provided data.".format(len(column_names_known)))
        print("These need to be renamed to standard names:")
        print('-------------------------------------------')
        for i,name in enumerate(column_names_known):
            print(name," --> ",column_names_standard[i])
        print("\nRenaming of column names by running standardize().")

        print('==============================================================')
        print("{} quantities have not bee identified in provided data:".format(len(column_names_unknown)))
        print('-------------------------------------------------------')
        for i,name in enumerate(column_names_unknown):
            print(name)

    return (column_names_known,column_names_unknown,column_names_standard)

def check_units(data,
                verbose = True):
    """Function to check the units of the measurements.

    Args:
    -------
        data (df): dataframe with the measurements where first row contains
                   the units or a dataframe with only the column names and units
        verbose (Boolean): verbose statement (default True)

    Returns:
    -------
        col_check_list (list): quantities whose units need checking/correction

    Raises:
    -------
        None (yet).

    Example:
    -------
        To be added.
    """
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Provided data is not a data frame.")
    elif data.shape[0]>1:
        units = data.drop(labels = np.arange(1,data.shape[0]))
    else:
        units = data

    ### testing if provided data frame contains any unit
    test_unit = False
    for u in all_units:
        if u in units.iloc[0].to_list():
            test_unit = True
            break
    if not test_unit:
        raise ValueError("Error: The second line in the dataframe is supposed\
                         to specify the units. No units were detected in this\
                         line, check www.mibipretdocs.nl/dataloading.")

    # standardize column names (as it might not has happened for data yet)
    units.columns = [col_dict.get(x, x) for x in units.columns]

    cols = units.columns
    col_check_list= []

    for quantity in electron_acceptors['all_ea']:
        if quantity in cols:
            if units[quantity][0] not in standard_units['mgperl']:
                col_check_list.append(quantity)
                if verbose:
                    print("Warning: Check unit of {}!\n Given in {}, but must be milligramm per liter (e.g. {})."
                              .format(quantity,data[quantity][0],standard_units['mgperl'][0]))

    for quantity in contaminants['all_cont']:
        if quantity in cols:
            if units[quantity][0] not in standard_units['microgperl']:
                col_check_list.append(quantity)
                if verbose:
                    print("Warning: Check unit of {}!\n Given in {}, but must be microgramm per liter (e.g. {})."
                              .format(quantity,data[quantity][0],standard_units['microgperl'][0]))

    #environmental_conditions:
    if name_redox in units.columns:
        if units[name_redox][0] not in standard_units['millivolt']:
            col_check_list.append(name_redox)
            if verbose:
                print("Warning: Check unit of {}!\n Given in {}, but must be in millivolt (e.g. {}).".format(
                        name_redox,data[quantity][0],standard_units['millivolt'][0]))

    #environmental_conditions:
    if name_sample_depth in units.columns:
        if units[name_sample_depth][0] not in standard_units['meter']:
            col_check_list.append(name_sample_depth)
            if verbose:
                print("Warning: Check unit of {}!\n Given in {}, but must be in meter (e.g. {}).".format(
                        name_sample_depth,data[quantity][0], standard_units['meter'][0]))

    if len(col_check_list) == 0 and verbose:
        print('==============================================================')
        print("All identified quantities given in requested units.")

    return col_check_list

def check_values(
        data,
        verbose = True,
        contaminant_group = "all_cont",
        ):
    """Function that checks on value types and replaces non-measured values.

    Args:
    -------
        data (df): dataframe with the measurements (without first row of units)
        verbose (Boolean): verbose statement (default True)

    Returns:
    -------
        pandas.DataFrame: Tabular data with standard column names

    Raises:
    -------
        None (yet).

    Example:
    -------
        To be added.
    """
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Provided data is not a data frame.")

    data_pure = data.copy()

    ### testing if provided data frame contains first row with units
    for u in data_pure.iloc[0].to_list():
        if u in all_units:
            print('==============================================================')
            print("WARNING: First row identified as units, has been removed for value check")
            data_pure.drop(labels = 0,inplace = True)
            break

    # standardize column names (as it might not has happened for data yet)
    data_pure.columns = [col_dict.get(x, x) for x in data_pure.columns]

    # transform data to numeric values
    quantities_transformed = []
    cont_list = contaminants[contaminant_group]
    ea_list = electron_acceptors['all_ea']
    for quantity in [name_sample_depth]+environmental_conditions+ea_list+cont_list:
        if quantity in data_pure.columns:
            try:
                data_pure[quantity] = pd.to_numeric(data_pure[quantity])
                quantities_transformed.append(quantity)
            except ValueError:
                print('==============================================================')
                print("WARNING: Cound not transform '{}' to numerical values".format(quantity))

    if verbose:
        print('==============================================================')
        print("Quantities with values transformed to numerical(int/float):")
        print('-----------------------------------------------------------')
        for name in quantities_transformed:
            print(name)

    # data_pure.iloc[:,:] = data_pure.iloc[:,:].replace(to_replace="-", value=replace)

    return data_pure

def standardize(data,
                reduce = True,
                store_csv = False,
                verbose=True,
                ):
    """Function providing condensed data frame with standardized names.

    Function is checking names of columns and renames columns,
    condenses data to identified column names, checks units and  names
    sof data frame.

    Function that looks at the column names and renames the columns to
    the standard names of the model.

    Args:
    -------
        data (df): dataframe with the measurements
        verbose (Boolean): verbose statement (default True)
        reduce (Boolean): flag to reduce data to known quantities (default True),
                            otherwise full dataframe with renamed columns is returned
        store_csv (Boolean): flag to save dataframe in standard format to csv-file

    Returns:
    -------
        pandas.DataFrame: Tabular data with standard column names

    Raises:
    -------
    None (yet).

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
    # general column check
    column_names_known,column_names_unknown,column_names_standard = check_columns(data,verbose = False)

    data_standard = data.copy()
    data_standard.columns = [col_dict.get(x, x) for x in data_standard.columns]

    if reduce:
        data_standard = data_standard.drop(labels = column_names_unknown,axis = 1)

    if verbose:
        print('==============================================================')
        print("{} quantities identified and renamed:".format(len(column_names_known)))
        print('-------------------------------------')
        for i,name in enumerate(column_names_known):
            print(name," --> ",column_names_standard[i])

        print('==============================================================')
        print("{} quantities not identified (and removed) from data:".format(len(column_names_unknown)))
        print('-----------------------------------------------------')
        for i,name in enumerate(column_names_unknown):
            print(name)

    # general unit check
    units = data_standard.drop(labels = np.arange(1,data_standard.shape[0]))
    col_check_list = check_units(units,verbose = verbose)

    # transform data to numeric values
    data_numeric = check_values(data_standard.drop(labels = 0),verbose = verbose)

    # store standard data to file
    if store_csv:
        if len(col_check_list) != 0:
            print('==============================================================')
            print("Data could not be saved because not all identified \nquantities are given in requested units.")
        else:
            try:
                data_standard.to_csv(store_csv,index=False)
                if verbose:
                    print('==============================================================')
                    print("Save standardized dataframe to file:\n", store_csv)
            except OSError:
                print("WARNING: data could not be saved. Check provided file path and name: {}".format(store_csv))

    return data_numeric, units

def example_data(data_type = 'all',
                 units = True,
                 ):
    """Function provinging test data for mibipret data analysis.

    Args:
    -------
        data_type (str): type of data to return:
                        -- "all": all types of data available
                        -- "setting": well setting data only
                        -- "contaminants": data on contaminants
                        -- "environment": data on environmental
                        -- "metabolites": data on metabolites
                        -- "hydro": data on hydrogeolocial conditions
        units (boolean): flag to provide first row with units (default: True)

    Returns:
    -------
        pandas.DataFrame: Tabular data with standard column names

    Raises:
    -------
    None

    Example:
    -------
    To be added!
    """
    setting = ["sample_nr","obs_well","depth"]
    setting_units = [' ',' ','m']
    setting_s01 = ['2000-001', 'B-MLS1-3-12', -12.]
    setting_s02 = ['2000-002', 'B-MLS1-5-15', -15.5]
    setting_s03 = ['2000-003', 'B-MLS1-6-17', -17.]
    setting_s04 = ['2000-004', 'B-MLS1-7-19', -19.]

    environment = ['pH', 'redox', 'sulfate', 'ammonium', 'sulfide',
                   'methane', 'ironII', 'manganese']
    environment_units = [' ','mV', 'mg/L', 'mg/L', 'mg/L',
                         'mg/L', 'mg/L', 'mg/L']
    environment_s01 = [7.23, -208., 23., 5., 0., 748., 3., 1.]
    environment_s02 = [7.67, -231., 0., 6., 0., 2022., 1., 0.]
    environment_s03 = [7.75, -252., 1., 13., 0., 200., 1., 0.]
    environment_s04 = [7.53, -317., 9., 15., 6., 122., 0., 0.]

    contaminants = ['benzene', 'toluene', 'ethylbenzene', 'pm_xylene',
                    'o_xylene', 'indane', 'indene', 'naphthalene']
    contaminants_units = ['ug/L', 'ug/L', 'ug/L', 'ug/L',
                          'ug/L', 'ug/L', 'ug/L', 'ug/L']
    contaminants_s01 = [263., 2., 269., 14., 51., 1254., 41., 2207.]
    contaminants_s02 = [179., 7., 1690., 751., 253., 1352., 15., 5410.]
    contaminants_s03 = [853., 17., 1286., 528., 214., 1031., 31., 3879.]
    contaminants_s04 = [1254., 10., 1202., 79., 61., 814., 59., 1970.]

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

    if not units:
        data.drop(0)

    return data
