#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Functions for data I/O handling.

@author: Alraune Zech
"""
import os.path
import numpy as np
import pandas as pd
import logging
logger = logging.getLogger(__name__)

def load_excel(
        file_path = None,
        sheet_name = 0,
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

    logger.info('==============================================================')
    logger.info(" Running function 'load_excel()' on data file ", file_path)
    logger.info('==============================================================')
    logger.info("Unit of quantities:")
    logger.info('-------------------')
    logger.info(units)
    logger.info('________________________________________________________________')
    logger.info("Loaded data as pandas DataFrame:")
    logger.info('--------------------------------')
    logger.info(data)
    logger.info('================================================================')

    return data, units

def load_csv(
        file_path = None,
        store_provenance = False,
        ):
    """Function to load data from csv file.

    Args:
    -------
        file_path: str
            Name of the path to the file
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

    logger.info('================================================================')
    logger.info(" Running function 'load_csv()' on data file ", file_path)
    logger.info('================================================================')
    logger.info("Units of quantities:")
    logger.info('-------------------')
    logger.info(units)
    logger.info('________________________________________________________________')
    logger.info("Loaded data as pandas DataFrame:")
    logger.info('--------------------------------')
    logger.info(data)
    logger.info('================================================================')

    return data, units
