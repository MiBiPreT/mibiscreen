#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Routines for calculating biostimulation related quantities and information.

@author: Alraune Zech
"""

import mibiscreen.data.names_data as names
from mibiscreen.data.check_data import check_data_frame
from mibiscreen.data.set_data import determine_quantities


def available_NP(
        data_frame,
        nutrients = 'NP',
        include = False,
        verbose = False,
        ):
    """Calculating available nutrients.

    Approximating the amount of hydrocarbons that can be degraded based
    on the amount of nutrients (nitrogen and phosphate available)

    Input
    -----
        data_frame: pd.DataFrame
            nitrate, nitrite and phosphate concentrations in [mg/l]
        nutrients: str or list, dafault is 'NP'
            either short name for group of nutrients to use, such as:
            - 'NP': nitrogen and phosphorus containing molecules (nitrate, nitrite, phosphorus)
        include: bool, default False
            Whether to modify the DataFrame rather than creating a new one.
        verbose: Boolean
            verbose flag (default False)

        Output
        ------
        NP_avail: pd.Series
            The amount of nutrients for degrading contaminants

    """
    if verbose:
        print('==============================================================')
        print(" Running function 'available_NP()' on data")
        print('==============================================================')

    ### check on correct data input format and extracting column names as list
    data,cols= check_data_frame(data_frame,inplace = include)

    ### sorting out which columns in data to use for summation of electrons available
    quantities, remainder = determine_quantities(cols,name_list = nutrients, verbose = verbose)
    if len(remainder)>0:
        raise ValueError("Concentrations of nutrient(s) missing:", *remainder,sep='\n')

    CNs = (data[names.name_nitrate] + data[names.name_nitrite]) * (39. / 4.5)
    CPs = data[names.name_phosphate] * (39. / 1.)
    NP_avail =CNs.combine(CPs, min, 0)
    NP_avail.name = names.name_NP_avail

    if include:
        data[names.name_NP_avail] = NP_avail

    if verbose:
        print("Total nutrients available is:\n{}".format(NP_avail))
        print('----------------------')

    return NP_avail

# def available_NP(
#         data,
#         inplace = False,
#         verbose = False,
#         **kwargs,
#         ):
#     """Function calculating available nutrients.

#     Approximating the amount of hydrocarbons that can be degraded based
#     on the amount of nutrients (nitrogen and phosphate available)

#     Input
#     -----
#         data: pd.DataFrame
#             nitrate, nitrite and phosphate concentrations in [mg/l]
#         inplace: bool, default False
#             Whether to modify the DataFrame rather than creating a new one.
#         verbose: Boolean
#             verbose flag (default False)

#         Output
#         ------
#         NP_avail: pd.Series
#             The amount of nutrients for degrading contaminants

#     """
#     if verbose:
#         print('==============================================================')
#         print(" Running function 'available_NP()' on data")
#         print('==============================================================')

#     cols = check_data(data)

#     nutrient_list = [names.name_nitrate, names.name_nitrite, names.name_phosphate]
#     list_nut_miss = []

#     for nut in nutrient_list:
#         if nut not in cols:
#             list_nut_miss.append(nut)
#     if len(list_nut_miss)>0:
#         raise ValueError("Concentrations of nutrient(s) missing:", list_nut_miss)

#     CNs = (data[names.name_nitrate] + data[names.name_nitrite]) * (39. / 4.5)
#     CPs = data[names.name_phosphate] * (39. / 1.)
#     NP_avail =CNs.combine(CPs, min, 0)
#     NP_avail.name = names.name_NP_avail

#     if inplace:
#         data[names.name_NP_avail] = NP_avail

#     if verbose:
#         print("Total NP available is:\n{}".format(NP_avail))
#         print('----------------------')

#     return NP_avail

