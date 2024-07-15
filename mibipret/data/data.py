#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Functions for data I/O handling.

@author: Alraune Zech
"""

import os.path
import numpy as np
import pandas as pd

try:
    from names import chemical_composition
    from names import col_dict
    from names import contaminants
    from names import environmental_conditions
    from names import name_EC
    from names import name_redox
    from names import name_sample_depth
    from names import standard_units
    from names_metabolites import metabolites
    from names_metabolites import names_metabolites
except ImportError:
    from .names import chemical_composition
    from .names import col_dict
    from .names import contaminants
    from .names import environmental_conditions
    from .names import name_EC
    from .names import name_redox
    from .names import name_sample_depth
    from .names import standard_units
    from .names_metabolites import metabolites
    from .names_metabolites import names_metabolites

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

    if verbose:
        print('==============================================================')
        print(" Running function 'load_excel()' on data file ", file_path)
        print('==============================================================')
        print("Unit of quantities:")
        print('-------------------')
        print(units)
        print('________________________________________________________________')
        print("Loaded data as pandas DataFrame:")
        print('--------------------------------')
        print(data)
        print('================================================================')

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
        print('================================================================')
        print(" Running function 'load_csv()' on data file ", file_path)
        print('================================================================')
        print("Units of quantities:")
        print('-------------------')
        print(units)
        print('________________________________________________________________')
        print("Loaded data as pandas DataFrame:")
        print('--------------------------------')
        print(data)
        print('================================================================')
    return data, units

def check_columns(data,
                  standardize = False,
                  reduce = False,
                  check_metabolites = False,
                  verbose = True):
    """Function checking names of columns of data frame.

    Function that looks at the column names and links it to standard names.
    Optionally, it renames identified column names to the standard names of the model.

    Args:
    -------
        data: pd.DataFrame
            dataframe with the measurements
        standardize: Boolean, default False
            flat to standardize identified column names
        reduce: Boolean, default False
            flag to reduce data to known quantities
        check_metabolites: Boolean, default False
            flag to check on metabolite names
        verbose: Boolean, default True
            verbosity flag

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

    if check_metabolites:
        dict_names = {
            **col_dict,
            **names_metabolites}
    else:
        dict_names = col_dict

    for x in data.columns:
        y = dict_names.get(x, False)
        if y is False:
            column_names_unknown.append(x)
        else:
            column_names_known.append(x)
            column_names_standard.append(y)

    if standardize:
        data.columns = [dict_names.get(x, x) for x in data.columns]

    if reduce:
        data.drop(labels = column_names_unknown,axis = 1,inplace=True)

    if verbose:
        print('================================================================')
        print(" Running function 'check_columns()' on data")
        print('================================================================')
        print("{} quantities identified in provided data.".format(len(column_names_known)))
        print("List of names with standard names:")
        print('----------------------------------')
        for i,name in enumerate(column_names_known):
            print(name," --> ",column_names_standard[i])
        print('----------------------------------')
        if standardize:
            print("Identified column names have been standardized")
        else:
            print("\nRenaming can be done by setting keyword 'standardize' to True.\n")
        print('________________________________________________________________')
        print("{} quantities have not been identified in provided data:".format(len(column_names_unknown)))
        print('---------------------------------------------------------')
        for i,name in enumerate(column_names_unknown):
            print(name)
        print('---------------------------------------------------------')
        if reduce:
            print("Not identified quantities have been removed from data frame")
        else:
            print("\nReduction to known quantities can be done by setting keyword 'reduce' to True.\n")
        print('================================================================')

    return (column_names_known,column_names_unknown,column_names_standard)

def check_units(data,
                check_metabolites = False,
                verbose = True):
    """Function to check the units of the measurements.

    Args:
    -------
        data: pandas.DataFrames
            dataframe with the measurements where first row contains
            the units or a dataframe with only the column names and units
        check_metabolites: Boolean, default False
            flag to check on metabolites' units
        verbose: Boolean
            verbose statement (default True)

    Returns:
    -------
        col_check_list: list
            quantities whose units need checking/correction

    Raises:
    -------
        None (yet).

    Example:
    -------
        To be added.
    """
    if verbose:
        print('================================================================')
        print(" Running function 'check_units()' on data")
        print('================================================================')

    if not isinstance(data, pd.DataFrame):
        raise ValueError("Provided data is not a data frame.")
    elif data.shape[0]>1:
        units = data.drop(labels = np.arange(1,data.shape[0]))
    else:
        units = data.copy()

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
    check_columns(units,standardize = True, check_metabolites=check_metabolites, verbose = False)

    col_check_list= []

    for quantity in chemical_composition:
        if quantity in units.columns:
            if units[quantity][0] not in standard_units['mgperl']:
                col_check_list.append(quantity)
                if verbose:
                    print("Warning: Check unit of {}!\n Given in {}, but must be milligramm per liter (e.g. {})."
                              .format(quantity,units[quantity][0],standard_units['mgperl'][0]))

    for quantity in contaminants['all_cont']:
        if quantity in units.columns:
            if units[quantity][0] not in standard_units['microgperl']:
                col_check_list.append(quantity)
                if verbose:
                    print("Warning: Check unit of {}!\n Given in {}, but must be microgramm per liter (e.g. {})."
                              .format(quantity,units[quantity][0],standard_units['microgperl'][0]))

    #environmental_conditions:
    env_cond = [name_sample_depth,name_EC,name_redox]
    unit_types = ['meter','microsimpercm','millivolt']

    for quantity,units_type in zip(env_cond,unit_types):
        if quantity in units.columns:
            if units[quantity][0] not in standard_units[units_type]:
                col_check_list.append(quantity)
                if verbose:
                    print("Warning: Check unit of {}!\n Given in {}, but must be in {} (e.g. {}).".format(
                            quantity,units[quantity][0],units_type,standard_units[units_type][0]))

    if check_metabolites:
        for quantity in metabolites['all_meta']:
            if quantity in units.columns:
                if units[quantity][0] not in standard_units['microgperl']:
                    col_check_list.append(quantity)
                    if verbose:
                        print("Warning: Check unit of {}!\n Given in {}, but must be microgramm per liter (e.g. {})."
                                  .format(quantity,units[quantity][0],standard_units['microgperl'][0]))

    if verbose:
        print('________________________________________________________________')
        if len(col_check_list) == 0:
            print(" All identified quantities given in requested units.")
        else:
            print(" All other identified quantities given in requested units.")
        print('================================================================')

    return col_check_list

def check_values(
        data,
        contaminant_group = "all_cont",
        check_metabolites = False,
        verbose = True,
        ):
    """Function that checks on value types and replaces non-measured values.

    Args:
    -------
        data: pandas.DataFrames
            dataframe with the measurements (without first row of units)
        contaminant_group: string
            shortcut string specifying group of contaminant to check on:
                -- "all_cont": all contaminants listed and specified in names
                -- "BTEX": benzene, toluene, ethylbenzene, xylene
                -- "BTEXIIN": benzene, toluene, ethylbenzene, xylene, indene, indane, naphthalene
            default: "all_cont"
        check_metabolites: Boolean, default False
            flag to check on metabolites' values
        verbose: Boolean
            verbose statement (default True)

    Returns:
    -------
        data_pure: pandas.DataFrame
            Tabular data with standard column names and without units

    Raises:
    -------
        None (yet).

    Example:
    -------
        To be added.
    """
    if verbose:
        print('================================================================')
        print(" Running function 'check_values()' on data")
        print('================================================================')

    if not isinstance(data, pd.DataFrame):
        raise ValueError("Provided data is not a data frame.")

    data_pure = data.copy()

    ### testing if provided data frame contains first row with units
    for u in data_pure.iloc[0].to_list():
        if u in all_units:
            print("WARNING: First row identified as units, has been removed for value check")
            print('________________________________________________________________')
            data_pure.drop(labels = 0,inplace = True)
            break

    # standardize column names (as it might not has happened for data yet)
    check_columns(data_pure,standardize = True, check_metabolites=check_metabolites, verbose = False)

    # transform data to numeric values
    quantities_transformed = []
    cont_list = contaminants[contaminant_group]
    if check_metabolites:
        metabolites_list = metabolites['all_meta']
    else:
        metabolites_list = []

    for quantity in [name_sample_depth]+environmental_conditions+chemical_composition+cont_list+metabolites_list:
        if quantity in data_pure.columns:
            try:
                data_pure[quantity] = pd.to_numeric(data_pure[quantity])
                quantities_transformed.append(quantity)
            except ValueError:
                print("WARNING: Cound not transform '{}' to numerical values".format(quantity))
                print('________________________________________________________________')
    if verbose:
        print("Quantities with values transformed to numerical (int/float):")
        print('-----------------------------------------------------------')
        for name in quantities_transformed:
            print(name)
        print('================================================================')

    to_replace_list = ["-",'--']
    to_replace_value = np.nan
    for sign in to_replace_list:
        data_pure.iloc[:,:] = data_pure.iloc[:,:].replace(to_replace=sign, value=to_replace_value)

    return data_pure

def standardize(data,
                reduce = True,
                store_csv = False,
                check_metabolites = False,
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
        data: pandas.DataFrames
            dataframe with the measurements
        reduce: Boolean
            flag to reduce data to known quantities (default True),
            otherwise full dataframe with renamed columns is returned
        store_csv: Boolean
            flag to save dataframe in standard format to csv-file
        check_metabolites: Boolean, default False
            flag to check on metabolites' values
        verbose: Boolean
            verbose statement (default True)

    Returns:
    -------
        data_numeric, units: pandas.DataFrames
            Tabular data with standardized column names, values in numerics etc
            and table with units for standardized column names

    Raises:
    -------
        None (yet).

    Example:
    -------
    Todo's:
        - complete list of potential contaminants, environmental factors
        - add name check for metabolites?
        - add key-word to specify which data to extract
            (i.e. data columns to return)

    """
    if verbose:
        print('================================================================')
        print(" Running function 'standardize()' on data")
        print('================================================================')

    data_standard = data.copy()

    # general column check & standardize column names
    column_names_known,column_names_unknown,column_names_standard = check_columns(data_standard,
                                                              standardize = True,
                                                              reduce = reduce,
                                                              check_metabolites = check_metabolites,
                                                              verbose = verbose)

    # general unit check
    units = data_standard.drop(labels = np.arange(1,data_standard.shape[0]))
    col_check_list = check_units(units,
                                 check_metabolites = check_metabolites,
                                 verbose = verbose)

    # transform data to numeric values
    data_numeric = check_values(data_standard.drop(labels = 0),
                                check_metabolites = check_metabolites,
                                verbose = verbose)

    # store standard data to file
    if store_csv:
        if len(col_check_list) != 0:
            print('________________________________________________________________')
            print("Data could not be saved because not all identified \nquantities are given in requested units.")
        else:
            try:
                data_standard.to_csv(store_csv,index=False)
                if verbose:
                    print('________________________________________________________________')
                    print("Save standardized dataframe to file:\n", store_csv)
            except OSError:
                print("WARNING: data could not be saved. Check provided file path and name: {}".format(store_csv))
    if verbose:
        print('================================================================')

    return data_numeric, units

def example_data(data_type = 'all',
                 with_units = False,
                 standardize = True,
                 ):
    """Function provinging test data for mibipret data analysis.

    Args:
    -------
        data_type: string
            Type of data to return:
                -- "all": all types of data available
                -- "set_env_cont": well setting, environmental and contaminants data
                -- "setting": well setting data only
                -- "environment": data on environmental
                -- "contaminants": data on contaminants
                -- "metabolites": data on metabolites
                -- "hydro": data on hydrogeolocial conditions
        with_units: Boolean
            flag to provide first row with units (default: True)
        standardize: Boolean
            flag to run check_values on data to transform into numerical value
            only applicable when with_units is False

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

    environment = ['pH','EC', 'redox','oxygen','nitrate','nitrite', 'sulfate', 'ammonium', 'sulfide',
                   'methane', 'ironII', 'manganese','phosphate']
    environment_units = [' ','uS/cm','mV', 'mg/L', 'mg/L', 'mg/L', 'mg/L',
                         'mg/L', 'mg/L', 'mg/L', 'mg/L', 'mg/L', 'mg/L']
    environment_s01 = [7.23, 322., -208.,0.3,122.,0.58, 23., 5., 0., 748., 3., 1.,1.6]
    environment_s02 = [7.67, 405., -231.,0.9,5.,0.0, 0., 6., 0., 2022., 1., 0.,0]
    environment_s03 = [7.75, 223., -252.,0.1,3.,0.03, 1., 13., 0., 200., 1., 0.,0.8]
    environment_s04 = [7.53, 58., -317.,0., 180.,1., 9., 15., 6., 122., 0., 0.,0.1]

    contaminants = ['benzene', 'toluene', 'ethylbenzene', 'pm_xylene',
                    'o_xylene', 'indane', 'indene', 'naphthalene']

    contaminants_units = ['ug/L', 'ug/L', 'ug/L', 'ug/L',
                          'ug/L', 'ug/L', 'ug/L', 'ug/L']
    contaminants_s01 = [263., 2., 269., 14., 51., 1254., 41., 2207.]
    contaminants_s02 = [179., 7., 1690., 751., 253., 1352., 15., 5410.]
    contaminants_s03 = [853., 17., 1286., 528., 214., 1031., 31., 3879.]
    contaminants_s04 = [1254., 10., 1202., 79., 61., 814., 59., 1970.]

    metabolites = ['Phenol',    "Cinnamic acid", "benzoic_acid"]
    metabolites_units = ['ug/L', 'ug/L', 'ug/L']
    metabolites_s01 = [0.2, 0.4, 1.4]
    metabolites_s02 = [np.nan,'-', 0]
    metabolites_s03 = [0, 11.4, 5.4]
    metabolites_s04 = [0.3, 0.5, 0.7]

    if  data_type == 'setting':
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

    elif  data_type == 'metabolites':

        units = setting_units+metabolites_units
        columns = setting+metabolites
        sample_01 = setting_s01+metabolites_s01
        sample_02 = setting_s02+metabolites_s02
        sample_03 = setting_s03+metabolites_s03
        sample_04 = setting_s04+metabolites_s04

        data = pd.DataFrame([units,sample_01,sample_02,sample_03,sample_04],
                            columns = columns)

    elif data_type == "set_env_cont":

        units = setting_units+environment_units+contaminants_units
        columns = setting+environment+contaminants
        sample_01 = setting_s01+environment_s01+contaminants_s01
        sample_02 = setting_s02+environment_s02+contaminants_s02
        sample_03 = setting_s03+environment_s03+contaminants_s03
        sample_04 = setting_s04+environment_s04+contaminants_s04

        data = pd.DataFrame([units,sample_01,sample_02,sample_03,sample_04],
                            columns = columns)

    elif data_type == 'all':
        units = setting_units+environment_units+contaminants_units+metabolites_units
        columns = setting+environment+contaminants+metabolites
        sample_01 = setting_s01+environment_s01+contaminants_s01+metabolites_s01
        sample_02 = setting_s02+environment_s02+contaminants_s02+metabolites_s02
        sample_03 = setting_s03+environment_s03+contaminants_s03+metabolites_s03
        sample_04 = setting_s04+environment_s04+contaminants_s04+metabolites_s04

        data = pd.DataFrame([units,sample_01,sample_02,sample_03,sample_04],
                            columns = columns)

    else:
        raise ValueError("Specified data type '{}' not available".format(data_type))

    if not with_units:
        data.drop(0,inplace = True)
        if standardize:
            data = check_values(data,verbose = False)
    return data
