#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Routines for calculating natural attenuation potential.

@author: alraune
"""

import pandas as pd
import mibipret.data.names as ean
from .properties import properties


def reductors(
    data,
    verbose = True,
    **kwargs,
    ):
    """Calculate the amount of electron reductors [mmol e-/l].

    making use of imported molecular mass values for quantities in [mg/mmol]

    Input
    -----
        electron_acceptors: dict
            concentration values of electron acceptors in [mg/l]

    Output
    ------
        tot_reduct: float
        Total amount of electrons needed for reduction in [mmol e-/l]
    """
    tot_reduct = 0.
    if isinstance(data, pd.DataFrame):
        cols = data.columns.to_list()
    elif isinstance(data, pd.Series):
        cols = [data.name]
    else:
        raise ValueError("Calculation of total amount of electron reductors \
                          not possible with given data. Data has to be a \
                          panda-DataFrame or Series but is given as \
                          type {}".format(type(data)))

    for ea in [ean.name_oxygen,ean.name_nitrate, ean.name_sulfate, ean.name_ironII]:

        if ea in cols:
            tot_reduct += properties[ea]['factor_stoichiometry']* \
                pd.to_numeric(data[ea]) / properties[ea]['molecular_mass']

        else:
            print("WARNING: No data on {} given, zero concentration assumed.".format(ea))

    if isinstance(tot_reduct, float):
        print("\nWARNING: No data on electron acceptor concentrations given.")
        return False
    elif isinstance(tot_reduct, pd.Series):
        tot_reduct.rename("total_reductors",inplace = True)
        if verbose:
            print("Total amount of electron reductors per column in [mmol e-/l] is:\n{}".format(tot_reduct))
        return tot_reduct
