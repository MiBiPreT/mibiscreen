#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Functions for data handling and standardization.

@author: Alraune Zech
"""
import numpy as np
import pandas as pd
import mibiscreen.data.settings.standard_names as names
from mibiscreen.data.settings.contaminants import contaminants_analysis
from mibiscreen.data.settings.contaminants import properties_contaminants
from mibiscreen.data.settings.environment import properties_geochemicals
from mibiscreen.data.settings.isotopes import properties_isotopes
from mibiscreen.data.settings.metabolites import properties_metabolites
from mibiscreen.data.settings.sample_settings import properties_sample_settings
from mibiscreen.data.settings.unit_settings import all_units
from mibiscreen.data.settings.unit_settings import properties_units


def standard_names(name_list,
                   standardize = True,
                   reduce = False,
                   verbose = False,
                   ):
    """Function transforming list of names to standard names.

    Function that looks at the names (of e.g. environmental variables, contaminants,
    metabolites, isotopes, etc) and provides the corresponding standard names.

    Args:
    -------
        name_list: string or list of strings
            names of quantities to be transformed to standard
        standardize: Boolean, default False
            Whether to standardize identified column names
        reduce: Boolean, default False
            Whether to reduce data to known quantities
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
    names_standard = []
    names_known = []
    names_unknown = []
    names_transform = {}


    if isinstance(name_list, str):
        name_list = [name_list]
    elif isinstance(name_list, list):
        for name in name_list:
            if not isinstance(name, str):
                raise ValueError("Entry in provided list of names is not a string:", name)

    properties_all = {**properties_sample_settings,
                      **properties_geochemicals,
                      **properties_contaminants,
                      **properties_metabolites,
                      **properties_isotopes,
                      **contaminants_analysis,
    }
    dict_names=_generate_dict_other_names(properties_all)

    other_names_contaminants = _generate_dict_other_names(properties_contaminants)
    other_names_isotopes = _generate_dict_other_names(properties_isotopes)

     # dict_names= other_names_all.copy()

    for x in name_list:
        y = dict_names.get(x, False)
        x_isotope = x.split('-')[0]
        y_isotopes = other_names_isotopes.get(x_isotope.lower(), False)

        if y_isotopes is not False:
            x_molecule = x.removeprefix(x_isotope+'-')
            y_molecule = other_names_contaminants.get(x_molecule.lower(), False)
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
        print("{} of {} quantities identified in name list.".format(len(names_known),len(name_list)))
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
        print("You can suggest missing quantities that could be added to the library here: <https://github.com/MiBiPreT/mibiscreen/issues/new/choose>")
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
        return (names_standard, names_known, names_unknown, names_transform)

def check_data_frame(data_frame,
                     sample_name_to_index = False,
                     inplace = False,
                     ):
    """Checking data on correct format.

    Tests if provided data is a pandas data frame and provides column names.
    Optionally it sets the sample name as index.

    Input
    -----
        data_frame: pd.DataFrame
            quantities for data analysis given per sample
        sample_name_to_index:  Boolean, default False
            Whether to set the sample name to the index of the DataFrame
        inplace: Boolean, default False
            Whether to modify the DataFrame rather than creating a new one.

    Output
    ------
        data: pd.DataFrame
            copy of given dataframe with index set to sample name
        cols: list
            List of column names
    """
    if not isinstance(data_frame, pd.DataFrame):
        raise ValueError("Data has to be a panda-DataFrame or Series \
                          but is given as type {}".format(type(data_frame)))

    if inplace is False:
        data = data_frame.copy()
    else:
        data = data_frame

    if sample_name_to_index:
        if names.name_sample not in data.columns:
            print("Warning: No sample name provided for making index. Consider standardizing data first")
        else:
            data.set_index(names.name_sample,inplace = True)

    if isinstance(data, pd.Series):
        cols = [data.name]
    else:
        cols = data.columns.to_list()

    return data, cols


def check_columns(data_frame,
                  standardize = False,
                  reduce = False,
                  verbose = True):
    """Function checking names of columns of data frame.

    Function that looks at the column names and links it to standard names.
    Optionally, it renames identified column names to the standard names of the model.

    Args:
    -------
        data_frame: pd.DataFrame
            dataframe with the measurements
        standardize: Boolean, default False
            Whether to standardize identified column names
        reduce: Boolean, default False
            Whether to reduce data to known quantities
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
    if verbose:
        print('==============================================================')
        print(" Running function 'check_columns()' on data")
        print('==============================================================')

    data,cols= check_data_frame(data_frame,
                                sample_name_to_index = False,
                                inplace = True)

    results = standard_names(cols,
                             standardize = False,
                             reduce = False,
                             verbose = False,
                             )

    column_names_standard = results[0]
    column_names_known = results[1]
    column_names_unknown = results[2]
    column_names_transform = results[3]

    if standardize:
        data.columns = [column_names_transform.get(x, x) for x in data.columns]

    if reduce:
        data.drop(labels = column_names_unknown,axis = 1,inplace=True)

    if verbose:
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
                verbose = True):
    """Function to check the units of the measurements.

    Args:
    -------
        data: pandas.DataFrames
            dataframe with the measurements where first row contains
            the units or a dataframe with only the column names and units
        verbose: Boolean
            verbose statement (default True)

    Returns:
    -------
        col_check_list: list
            quantities whose units need checking/correction
        col_not_checked: list
            quantities not identified, thus not checked on units

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

    ### testing if provided data frame contains any units (at all)
    units_in_data = set(map(lambda x: str(x).lower(), units.iloc[0,:].values))
    test_unit = False
    for u in all_units:
        if u in units_in_data:
            test_unit = True
            break
    if not test_unit:
        raise ValueError("Error: The second line in the dataframe is supposed\
                         to specify the units. No units were detected in this\
                         line, check https://mibipret.github.io/mibiscreen/ Data\
                         documentation.")

    # standardize column names (as it might not has happened for data yet)
    # (column_names_known,column_names_unknown,column_names_standard) = check_columns(units,
    check_columns(units,
                  standardize = True,
                  verbose = False)
    col_check_list= []
    col_not_checked  = []

    properties_all = {**properties_sample_settings,
                      **properties_geochemicals,
                      **properties_contaminants,
                      **properties_metabolites,
                      **properties_isotopes,
    }

    ### run through all quantity columns and check their units
    for quantity in units.columns:
        #quantity = unit.encode("utf-8")

        ### identify standard unit for each column idenfied:
        if quantity in properties_all.keys():# test on standard column name
            standard_unit = properties_all[quantity]['standard_unit']
        elif quantity.split('-')[0] in properties_all.keys(): # test on isotopes
            standard_unit = properties_all[quantity.split('-')[0]]['standard_unit']
        else:
            col_not_checked.append(quantity)
            continue
        if standard_unit != names.unit_less:
            other_names_unit = properties_units[standard_unit]['other_names']
            if str(units[quantity][0]).lower() not in other_names_unit:
                col_check_list.append(quantity)
                if verbose:
                    print("Warning: Check unit of {}!\n Given in {}, but must be in {}."
                              .format(quantity,units[quantity][0],standard_unit))

    if verbose:
        print('________________________________________________________________')
        if len(col_check_list) == 0:
            print(" All identified quantities given in requested units.")
        else:
            print(" Quantities not in requested units:")
            print(*col_check_list, sep='\n')
        if len(col_not_checked) != 0:
            print(" Quantities not identified (and thus not checked on units):")
            print(*col_not_checked, sep='\n')
            print('================================================================')

    return col_check_list,col_not_checked


def check_values(data_frame,
                 dl_factor=None,
                 to_replace_list = ["-",'--','',' ','  '],
                 to_replace_value = np.nan,
                 inplace=False,
                 verbose = True,
                 ):
    """Function that cleans checks on values and cleans DataFrame.

    Cleaning includes:
            - fixing decimal commas
            - converting strings to floats
            - replacing empty strings with NaN
            - and optionally replacing detection limits.

    Args:
    -------
        data_frame: pandas.DataFrames
            dataframe with the measurements
        dl_factor: float or None, default None
            if set, values with '<' are replaced by (value * dl_factor)
        to_replace_list: list, default ["-",'--','',' ','  ']
            list of strings to replace before cleaning
        to_replace_value: float or np.nan, default: np.nan
            value to replace strings to_replace_list with
        inplace: Boolean, default False
            if True modifies df in place, else returns a cleaned copy
        verbose: Boolean
            verbose statement (default True)

    Returns:
    -------
        cleaned: pandas.DataFrame
            Cleaned dataframe without units

    """
    if verbose:
        print('================================================================')
        print(" Running function 'check_values()' on data")
        print('================================================================')

    df,cols= check_data_frame(data_frame, inplace = inplace)

    if dl_factor is not None and (dl_factor>1 or dl_factor<0):
        raise ValueError("Factor needs to be between 0 and 1 or 'nan'")

    ## testing if provided data frame contains first row with units
    for u in df.iloc[0].to_list():
        if u in all_units:
            print("WARNING: First row identified as units, has been removed for value check")
            print('________________________________________________________________')
            df.drop(labels = 0,inplace = True)
            break

    for sign in to_replace_list:
        df.iloc[:,:] = df.iloc[:,:].replace(to_replace=sign, value=to_replace_value)

    detection_limit_columns = []
    failed_conversion_columns = []

    def clean_quantity(quantity_series,quantity_name):
        found_dl = False
        found_failed = False

        def clean_value(val):
            nonlocal found_dl, found_failed
            if isinstance(val, str):
                val = val.strip().replace(',', '.')
                # if val == '':
                #     found_failed = True
                #     return np.nan
                if val.startswith('<'):
                    try:
                        number = float(val[1:])
                        if dl_factor is not None:
                            found_dl = True
                            return number * dl_factor
                        else:
                            return np.nan
                    except ValueError:
                        found_failed = True
                        return val
                try:
                    return float(val)
                except ValueError:
                    found_failed = True
                    return val
            return val

        cleaned = quantity_series.apply(clean_value)

        if found_dl:
            detection_limit_columns.append(quantity_name)
        if found_failed:
            failed_conversion_columns.append(quantity_name)

        return cleaned

    for quantity in cols:
        df[quantity] = clean_quantity(df[quantity], quantity)

    if verbose:
        if detection_limit_columns:
            print("Quantities with values given by detection limits:")
            print('-----------------------------------------------------------')
            for name in detection_limit_columns:
                print(name)
            print('-----------------------------------------------------------')
            print("All values with detection limit, given by '<X' have been replaced")
            print(" by the values multiuplied with the specified factor: {} * X ".format(dl_factor))
            print('================================================================')

        if failed_conversion_columns:
            print("Quantities where not all values could be transformed to numerical (int/float):")
            print('-----------------------------------------------------------')
            for name in failed_conversion_columns:
                print(name)
            print('================================================================')
    return df


def standardize(data_frame,
                reduce = True,
                store_csv = False,
                verbose=True,
                **kwargs,
                ):
    """Function providing condensed data frame with standardized names.

    Function is checking names of columns and renames columns,
    condenses data to identified column names, checks units and  names
    sof data frame.

    Function that looks at the column names and renames the columns to
    the standard names of the model.

    Args:
    -------
        data_frame: pandas.DataFrames
            dataframe with the measurements
        reduce: Boolean, default True
            whether to reduce data to known quantities (default True),
            otherwise full dataframe with renamed columns (for those identifyable) is returned
        store_csv: Boolean, default False
            whether to save dataframe in standard format to csv-file
        verbose: Boolean, default True
            verbose statement
        **kwargs: Optional keyword arguments.
            dl_factor (float, optional): scaling factor for value given at detection limit.
               Default is None, so detection limit values are replaced by nan.

    Returns:
    -------
        data_numeric, units: pandas.DataFrames
            Tabular data with standardized column names, values in numerics etc
            and table with units for standardized column names

    """
    if verbose:
        print('================================================================')
        print(" Running function 'standardize()' on data")
        print('================================================================')
        print(' Function performing check of data including:')
        print('  * check of column names and standardizing them.')
        print('  * check of units and outlining which to adapt.')
        print('  * check and cleaning of values')

    data,cols= check_data_frame(data_frame,
                                sample_name_to_index = False,
                                inplace = False)

    # general column check & standardize column names
    check_columns(data,
                  standardize = True,
                  reduce = reduce,
                  verbose = verbose)

    # general unit check
    units = data.drop(labels = np.arange(1,data.shape[0]))
    col_check_list,_ = check_units(units,
                                 verbose = verbose)

    # transform data to numeric values
    data_numeric = check_values(data.drop(labels = 0),
                                inplace = False,
                                verbose = verbose,
                                **kwargs,
                                )

    # store standard data to file
    if store_csv:
        if len(col_check_list) != 0:
            print('________________________________________________________________')
            print("Data not saved because not all identified \n quantities are given in requested units.")
        else:
            try:
                data.to_csv(store_csv,index=False)
                if verbose:
                    print('________________________________________________________________')
                    print("Save standardized dataframe to file:\n", store_csv)
            except OSError:
                print("WARNING: data could not be saved. Check provided file path and name: {}".format(store_csv))
    if verbose:
        print('================================================================')

    return data_numeric, units

def _generate_dict_other_names(name_dict,
                               selection = False):
    """Function creating dictionary for mapping alternative names.

    Args:
    -------
        name_dict: dict
            dictionary of dictionaries with properties for each quantity (e.g. contaminant)
            each quantity-subdictionary needs to have one key called 'other_names'
            providing a list of other/alternative names of the quantities
        selection: False or list
            if False, all keys in dictionary name_dict will be run through
            if a list: only keys which are also in list will be used

    Returns:
    -------
        other_names_dict: dictionary
            dictionary mapping alternative names to standard name

    """
    other_names_dict=dict()
    if selection is False:
        name_list = list(name_dict.keys())
    else:
        name_list = selection
    for key in name_list:
        for other_name in name_dict[key]['other_names']:
            other_names_dict[other_name] = key

    return other_names_dict
