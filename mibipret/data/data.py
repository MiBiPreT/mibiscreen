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
    from names import isotopes
    from names import name_EC
    from names import name_redox
    from names import name_sample
    from names import name_sample_depth
    from names import setting_data
    from names import names_contaminants
    from names import names_isotopes
    from names import standard_units
    from names_metabolites import metabolites
    from names_metabolites import names_metabolites
except ImportError:
    from .names import chemical_composition
    from .names import col_dict
    from .names import contaminants
    from .names import environmental_conditions
    from .names import isotopes
    from .names import name_EC
    from .names import name_redox
    from .names import name_sample
    from .names import name_sample_depth
    from .names import setting_data
    from .names import names_contaminants
    from .names import names_isotopes
    from .names import standard_units
    from .names_metabolites import metabolites
    from .names_metabolites import names_metabolites

all_units = [item for sublist in list(standard_units.values()) for item in sublist]
to_replace_list = ["-",'--','',' ','  ']
to_replace_value = np.nan

def load_excel(
        file_path = None,
        sheet_name = 0,
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
            flag to standardize identified column names
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

    (column_names_known, column_names_unknown, column_names_standard, column_names_transform) = standard_names(data.columns,
                   standardize = False,
                   reduce = False,
                   check_metabolites = check_metabolites,
                   verbose = False,
                   )

    if standardize:
        data.columns = [column_names_transform.get(x, x) for x in data.columns]

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

# def check_columns(data,
#                   standardize = False,
#                   reduce = False,
#                   check_metabolites = False,
#                   verbose = True):
#     """Function checking names of columns of data frame.

#     Function that looks at the column names and links it to standard names.
#     Optionally, it renames identified column names to the standard names of the model.

#     Args:
#     -------
#         data: pd.DataFrame
#             dataframe with the measurements
#         standardize: Boolean, default False
#             flag to standardize identified column names
#         reduce: Boolean, default False
#             flag to reduce data to known quantities
#         check_metabolites: Boolean, default False
#             flag to check on metabolite names
#         verbose: Boolean, default True
#             verbosity flag

#     Returns:
#     -------
#         tuple: three list containing names of
#                 list with identitied quantities in data (but not standardized names)
#                 list with unknown quantities in data (not in list of standardized names)
#                 list with standard names of identified quantities

#     Raises:
#     -------
#     None (yet).

#     Example:
#     -------
#     Todo's:
#         - complete list of potential contaminants, environmental factors
#         - add name check for metabolites?
#     """
#     column_names_standard = []
#     column_names_known = []
#     column_names_unknown = []

#     if check_metabolites:
#         dict_names = {
#             **col_dict,
#             **names_metabolites}
#     else:
#         dict_names = col_dict

#     dict_names_in_cols = {}
#     for x in data.columns:
#         y = dict_names.get(x, False)
#         x_isotope = x.split('-')[0]
#         y_isotopes = names_isotopes.get(x_isotope.lower(), False)

#         if y_isotopes is not False:
#             x_molecule = x.removeprefix(x_isotope+'-')
#             y_molecule = names_contaminants.get(x_molecule.lower(), False)
#             if y_molecule is False:
#                 column_names_unknown.append(x)
#             else:
#                 y = y_isotopes+'-'+y_molecule
#                 column_names_known.append(x)
#                 column_names_standard.append(y)
#                 dict_names_in_cols[x] = y
#         else:
#             y = dict_names.get(x.lower(), False)
#             if y is False:
#                 column_names_unknown.append(x)
#             else:
#                 column_names_known.append(x)
#                 column_names_standard.append(y)
#                 dict_names_in_cols[x] = y

#     if standardize:
#         data.columns = [dict_names_in_cols.get(x, x) for x in data.columns]

#     if reduce:
#         data.drop(labels = column_names_unknown,axis = 1,inplace=True)

#     if verbose:
#         print('================================================================')
#         print(" Running function 'check_columns()' on data")
#         print('================================================================')
#         print("{} quantities identified in provided data.".format(len(column_names_known)))
#         print("List of names with standard names:")
#         print('----------------------------------')
#         for i,name in enumerate(column_names_known):
#             print(name," --> ",column_names_standard[i])
#         print('----------------------------------')
#         if standardize:
#             print("Identified column names have been standardized")
#         else:
#             print("\nRenaming can be done by setting keyword 'standardize' to True.\n")
#         print('________________________________________________________________')
#         print("{} quantities have not been identified in provided data:".format(len(column_names_unknown)))
#         print('---------------------------------------------------------')
#         for i,name in enumerate(column_names_unknown):
#             print(name)
#         print('---------------------------------------------------------')
#         if reduce:
#             print("Not identified quantities have been removed from data frame")
#         else:
#             print("\nReduction to known quantities can be done by setting keyword 'reduce' to True.\n")
#         print('================================================================')

#     return (column_names_known,column_names_unknown,column_names_standard)

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
    #environmental_conditions:
    env_cond = [name_sample_depth,name_EC,name_redox]
    unit_types = ['meter','microsimpercm','millivolt']

    for quantity in units.columns:
        if quantity in chemical_composition:
            if units[quantity][0].lower() not in standard_units['mgperl']:
                col_check_list.append(quantity)
                if verbose:
                    print("Warning: Check unit of {}!\n Given in {}, but must be milligramm per liter (e.g. {})."
                              .format(quantity,units[quantity][0],standard_units['mgperl'][0]))

        if quantity in contaminants['all_cont']:
            if units[quantity][0].lower() not in standard_units['microgperl']:
                col_check_list.append(quantity)
                if verbose:
                    print("Warning: Check unit of {}!\n Given in {}, but must be microgramm per liter (e.g. {})."
                              .format(quantity,units[quantity][0],standard_units['microgperl'][0]))

        if quantity in env_cond:
            unit_type = unit_types[env_cond.index(quantity)]
            if units[quantity][0].lower() not in standard_units[unit_type]:
                col_check_list.append(quantity)
                if verbose:
                    print("Warning: Check unit of {}!\n Given in {}, but must be in {} (e.g. {}).".format(
                            quantity,units[quantity][0],unit_type,standard_units[unit_type][0]))

        if quantity.split('-')[0] in isotopes:
            if units[quantity][0].lower() not in standard_units['permil']:
                col_check_list.append(quantity)
                if verbose:
                    print("Warning: Check unit of {}!\n Given in {}, but must be per mille (e.g. {})."
                              .format(quantity,units[quantity][0],standard_units['permil'][0]))

        if check_metabolites:
            if quantity in metabolites['all_meta']:
                if units[quantity][0].lower() not in standard_units['microgperl']:
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

    for sign in to_replace_list:
        data_pure.iloc[:,:] = data_pure.iloc[:,:].replace(to_replace=sign, value=to_replace_value)

    # standardize column names (as it might not has happened for data yet)
    check_columns(data_pure,
                  standardize = True,
                  check_metabolites=check_metabolites,
                  verbose = False)

    # transform data to numeric values
    quantities_transformed = []
    # cont_list = contaminants[contaminant_group]

    for quantity in data_pure.columns:
        # if quantity in [name_sample_depth]+environmental_conditions+chemical_composition+cont_list\
        #     or (check_metabolites is True and quantity in metabolites['all_meta']) \
        #     or quantity.split('-')[0] in isotopes:
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
                -- "isotopes": data on isotopes
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
                   'methane', 'iron2', 'manganese','phosphate']
    environment_units = [' ','uS/cm','mV', 'mg/l', 'mg/l', 'mg/l', 'mg/l',
                         'mg/l', 'mg/l', 'mg/l', 'mg/l', 'mg/l', 'mg/l']
    environment_s01 = [7.23, 322., -208.,0.3,122.,0.58, 23., 5., 0., 748., 3., 1.,1.6]
    environment_s02 = [7.67, 405., -231.,0.9,5.,0.0, 0., 6., 0., 2022., 1., 0.,0]
    environment_s03 = [7.75, 223., -252.,0.1,3.,0.03, 1., 13., 0., 200., 1., 0.,0.8]
    environment_s04 = [7.53, 58., -317.,0., 180.,1., 9., 15., 6., 122., 0., 0.,0.1]

    contaminants = ['benzene', 'toluene', 'ethylbenzene', 'pm_xylene',
                    'o_xylene', 'indane', 'indene', 'naphthalene']

    contaminants_units = ['ug/l', 'ug/l', 'ug/l', 'ug/l',
                          'ug/l', 'ug/l', 'ug/l', 'ug/l']
    contaminants_s01 = [263., 2., 269., 14., 51., 1254., 41., 2207.]
    contaminants_s02 = [179., 7., 1690., 751., 253., 1352., 15., 5410.]
    contaminants_s03 = [853., 17., 1286., 528., 214., 1031., 31., 3879.]
    contaminants_s04 = [1254., 10., 1202., 79., 61., 814., 59., 1970.]

    # metabolites = ['Phenol',    "Cinnamic acid", "benzoic_acid"]
    metabolites = ['phenol',    "cinnamic_acid", "benzoic_acid"]
    metabolites_units = ['ug/l', 'ug/l', 'ug/l']
    metabolites_s01 = [0.2, 0.4, 1.4]
    metabolites_s02 = [np.nan,' ', 0]
    metabolites_s03 = [0, 11.4, 5.4]
    metabolites_s04 = [0.3, 0.5, 0.7]

    isotopes = ['delta_13C-benzene','delta_2H-benzene']
    isotopes_units = ['permil','permil']#,'per mil']
    # isotopes_units = ['mUr','‰']#,'per mil']
    isotopes_s01 = [-26.1,-106]
    isotopes_s02 = [-25.8,-110]
    isotopes_s03 = [-24.1,-118]
    isotopes_s04 = [-24.1,-117]

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

    elif  data_type == 'isotopes':

        units = setting_units+isotopes_units
        columns = setting+isotopes
        sample_01 = setting_s01+isotopes_s01
        sample_02 = setting_s02+isotopes_s02
        sample_03 = setting_s03+isotopes_s03
        sample_04 = setting_s04+isotopes_s04

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
        units = setting_units+environment_units+contaminants_units+metabolites_units + isotopes_units
        columns = setting+environment+contaminants+metabolites + isotopes
        sample_01 = setting_s01+environment_s01+contaminants_s01+metabolites_s01+isotopes_s01
        sample_02 = setting_s02+environment_s02+contaminants_s02+metabolites_s02+isotopes_s02
        sample_03 = setting_s03+environment_s03+contaminants_s03+metabolites_s03+isotopes_s03
        sample_04 = setting_s04+environment_s04+contaminants_s04+metabolites_s04+isotopes_s04

        data = pd.DataFrame([units,sample_01,sample_02,sample_03,sample_04],
                            columns = columns)

    else:
        raise ValueError("Specified data type '{}' not available".format(data_type))

    if not with_units:
        data.drop(0,inplace = True)
        if standardize:
            data = check_values(data,verbose = False)
    return data

def standard_names(names,
                   standardize = True,
                   reduce = False,
                   check_metabolites = False,
                   verbose = False,
                   ):

    """Function transforming list of names to standard names.

    Function that looks at the names (of e.g. environmental variables, contaminants,
    metabolites, isotopes, etc) and provides the corresponding standard names.

    Args:
    -------
        names: string or list of strings
            names of quantities to be transformed to standard

        standardize: Boolean, default False
            flag to standardize identified column names
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
    names_known = []
    names_unknown = []
    names_standard = []
    names_transform = {}

    if check_metabolites:
        dict_names = {
            **col_dict,
            **names_metabolites}
    else:
        dict_names = col_dict

    if isinstance(names, str):
        names = [names]
    elif isinstance(names, list):
        for name in names:
            if not isinstance(name, str):
                raise ValueError("Entry in provided list of names is not a string:", name)

    for x in names:
        y = dict_names.get(x, False)
        x_isotope = x.split('-')[0]
        y_isotopes = names_isotopes.get(x_isotope.lower(), False)

        if y_isotopes is not False:
            x_molecule = x.removeprefix(x_isotope+'-')
            y_molecule = names_contaminants.get(x_molecule.lower(), False)
            if y_molecule is False:
                names_unknown.append(x)
            else:
                y = y_isotopes+'-'+y_molecule
                names_known.append(x)
                names_standard.append(y)
                names_transform[x] = y
        else:
            y = dict_names.get(x.lower(), False)
            if y is False:
                names_unknown.append(x)
            else:
                names_known.append(x)
                names_standard.append(y)
                names_transform[x] = y

    if verbose:
        print('================================================================')
        print(" Running function 'standard_names()'")
        print('================================================================')
        print("{} of {} quantities identified in name list.".format(len(names_known),len(names)))
        print("List of names with standard names:")
        print('----------------------------------')
        for i,name in enumerate(names_known):
            print(name," --> ",names_standard[i])
        print('----------------------------------')
        if standardize:
            print("Identified column names have been standardized")
        else:
            print("\nRenaming can be done by setting keyword 'standardize' to True.\n")
        print('________________________________________________________________')
        print("{} quantities have not been identified in provided data:".format(len(names_unknown)))
        print('---------------------------------------------------------')
        for i,name in enumerate(names_unknown):
            print(name)
        print('---------------------------------------------------------')
        if reduce:
            print("Not identified quantities have been removed from data frame")
        else:
            print("\nReduction to known quantities can be done by setting keyword 'reduce' to True.\n")
        print('================================================================')

    if standardize:
        if reduce:
            return names_standard
        else:
            return names_standard + names_unknown
    else:
        return (names_known, names_unknown, names_standard, names_transform)

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
        (intersection, remainder): tuple of lists
            intersection is list of strings present in both lists 'list1' and 'list2'
            remainder is list of strings present either of both lists 'list1' and 'list2'

    """
    intersection = list(set(list1) & set(list2))
    remainder_list1 = list(set(list1) - set(list2))
    remainder_list2 = list(set(list2) - set(list1))
    remainder = remainder_list1 +  remainder_list2

    if verbose:
        print('================================================================')
        print(" Running function 'extract_variables()'")
        print('================================================================')
        print("strings present in both lists:", intersection)
        print("strings only present in either of the lists:", remainder)

    return (intersection,remainder,remainder_list1,remainder_list2)

def merge_data(data_list,
               how='outer',
               on=[name_sample],
               clean = True,
               **kwargs,
               ):

    """Function merging dataframes along columns.

    Args:
    -------
        data_list: list of pd.DataFrame
            list of dataframes with the measurements
        how: str 
            Type of merge to be performed.
            corresponds to keyword in pd.merge()
            {‘left’, ‘right’, ‘outer’, ‘inner’, ‘cross’}, default ‘outer’
        on: label
            Column name to join on.
            corresponds to keyword in pd.merge()
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
    """
    
    if len(data_list)<2:
        raise ValueError('Not sufficient elements in data_list for merging provided.')

    data_merge = data_list[0]
    for data_add in data_list[1:]:
        if clean:
            intersection,remainder,remainder_list1,remainder_list2 = compare_lists(data_merge.columns.to_list(),data_add.columns.to_list())
            intersection,remainder,remainder_list1,remainder_list2 = compare_lists(intersection,on)
            data_add = data_add.drop(labels = remainder,axis = 1)
        data_merge = pd.merge(data_merge,data_add, how=how, on=on,**kwargs) # complete data set, where values of porosity are added (otherwise nan)

    return data_merge

def extract_data(data,
                 name_list, 
                 keep_setting_data = True,
                 inplace = True,
                 ):

    """Function extracting data from dataframe for specified variables.

    Args:
    -------
        data: pandas.DataFrames
            dataframe with the measurements
        name_list: list of strings
            list of column names to extract from dataframes
        inplace: bool, default True
            If False, return a copy. Otherwise, do operation in place.

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
    
    if keep_setting_data:
        name_list = setting_data + name_list

    intersection,remainder,remainder_list1,remainder_list2 = compare_lists(data.columns.to_list(),name_list)  

    if len(intersection)<len(name_list):
        print("Warning: Not all variables in name_list are identified in the data frame columns: ",remainder_list2)

    data_new = data.drop(labels = remainder_list1,axis = 1,inplace=inplace)

    return data_new