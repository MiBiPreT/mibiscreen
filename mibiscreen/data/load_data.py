#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Functions for data I/O handling.

@author: Alraune Zech
"""
import os.path
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

        >>> from mibiscreen.data import load_excel
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

        >>> from mibiscreen.data import load_excel
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
