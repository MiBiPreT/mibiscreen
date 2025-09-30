#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Functions for data I/O handling.

@author: Alraune Zech
"""
import os.path
import re
import numpy as np
import pandas as pd


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
            read_excel(), e.g. sep = ',' or sep = ';'

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

        >>> from mibiscreen.data import load_excel
        >>> load_excel(example_data.xlsx)

    """
    if verbose:
        print('===================================')
        print(" Running function 'load_excel()'")
        print('===================================')

    if file_path is None:
        raise ValueError('Specify file path and file name!')
    if not os.path.isfile(file_path):
        raise OSError('Cannot access file at : ',file_path)

    data = pd.read_excel(file_path,
                         sheet_name = sheet_name,
                         **kwargs)

    if verbose:
        print("Reading data from file: {}".format(file_path))
        print('------------------------------------------------------------------')

    _check_duplicates(data)

    units = data.drop(labels = np.arange(1,data.shape[0]))

    if verbose:
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

        >>> from mibiscreen.data import load_excel
        >>> load_excel(example_data.csv)

    """
    if verbose:
        print('==================================')
        print(" Running function 'load_csv()'")
        print('==================================')

    if file_path is None:
        raise ValueError('Specify file path and file name!')
    if not os.path.isfile(file_path):
        raise OSError('Cannot access file at : ',file_path)

    if verbose:
        print("Reading data from file: {}".format(file_path))
        print('------------------------------------------------------------------')

    data = pd.read_csv(file_path, encoding="unicode_escape")
    if ";" in data.iloc[1].iloc[0]:
        data = pd.read_csv(file_path, sep=";", encoding="unicode_escape")

    _check_duplicates(data)

    units = data.drop(labels = np.arange(1,data.shape[0]))

    if verbose:
        print("Units of quantities:")
        print('-------------------')
        print(units)
        print('________________________________________________________________')
        print("Loaded data as pandas DataFrame:")
        print('--------------------------------')
        print(data)
        print('================================================================')

    return data, units

def _check_duplicates(data):
    """Detects duplicate column names in a pandas DataFrame.

    When a DataFrame contains identical column names they are automatically
    renamed by pandas (e.g., 'Column', 'Column.1', 'Column.2'). This function
    identifies if such column names exists and prints a warning message.

    This function checks for column names that match the pandas auto-renaming pattern (`.1`, `.2`, etc.)
    indicating that duplicate column names were present in the original data source (e.g., an Excel file).

    Args:
    -----
        data (pd.DataFrame): The DataFrame to check for renamed duplicate columns.

    Returns:
    --------
        None
    """
    # Check for duplicated column names
    renamed_pattern = re.compile(r"^(.*)\.(\d+)$")   # Pattern to match renamed columns
    duplicate_columns = {}
    for col in data.columns:
        if (match := renamed_pattern.match(col)):
            base = match.group(1)
            duplicate_columns.setdefault(base, []).append(col)
    if duplicate_columns:
        print("WARNING: Duplicate column names detected. \n        They were automatically renamed by pandas into:")
        for base, renamed_list in duplicate_columns.items():
            for renamed in renamed_list:
                print(f" - '{renamed}'")
        print("Duplicate column names will not be identified as standard names.")
        print("Consider renaming them.")
        print('------------------------------------------------------------------')
