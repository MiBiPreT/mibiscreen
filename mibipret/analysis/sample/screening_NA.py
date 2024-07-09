#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Routines for calculating natural attenuation potential.

@author: alraune
"""

import numpy as np
import pandas as pd
import mibipret.data.names as ean
from .properties import properties


def reductors(
    data,
    ea_group = 'ONSFe',
    verbose = False,
    **kwargs,
    ):
    """Calculate the amount of electron reductors [mmol e-/l].

    making use of imported molecular mass values for quantities in [mg/mmol]

    Input
    -----
        data: pd.DataFrame
            concentration values of electron acceptors in [mg/l]
        ea_group: str
            Short name for group of electron acceptors to use
            default is 'ONSFe' (for oxygen, nitrate, sulfate and ironII)
        verbose: Boolean
            verbose flag (default False)

    Output
    ------
        tot_reduct: pd.Series
        Total amount of electrons needed for reduction in [mmol e-/l]
    """
    tot_reduct = 0.
    cols= check_data(data)

    try:
        for ea in ean.electron_acceptors[ea_group]:
            if ea in cols:
                tot_reduct += properties[ea]['factor_stoichiometry']* \
                    data[ea] / properties[ea]['molecular_mass']
                #     pd.to_numeric(data[ea]) / properties[ea]['molecular_mass']
            else:
                print("WARNING: No data on {} given, zero concentration assumed.".format(ea))
    except KeyError:
        print("WARNING: group of electron acceptors ('ea_group') not defined: '{}'".format(ea_group))
        tot_reduct = False


    if isinstance(tot_reduct, float):
        print("\nWARNING: No data on electron acceptor concentrations given.")
        tot_reduct = False
    elif isinstance(tot_reduct, pd.Series):
        tot_reduct.rename("total_reductors",inplace = True)
        if verbose:
            print("Total amount of electron reductors per column in [mmol e-/l] is:\n{}".format(tot_reduct))
    return tot_reduct

def oxidators(
    data,
    contaminant_group = "BTEXIIN",
    nutrient = False,
    verbose = False,
    **kwargs,
    ):
    """Calculate the amount of electron oxidators [mmol e-/l].

    Calculate the amount of electron oxidators in [mmol e-/l]
    based on concentrations of contaminants, stiochiometric ratios of reactions,
    contaminant properties (e.g. molecular masses in [mg/mmol])

    alternatively: based on nitrogen and phosphate availability

    Input
    -----
        data: pd.DataFrame
            Contaminant contentrations in [ug/l], i.e. microgram per liter
            if nutrient is True, data also needs to contain concentrations
            of Nitrate, Nitrite and Phosphate
        contaminant_group: str
            Short name for group of contaminants to use
            default is 'BTEXIIN' (for benzene, toluene, ethylbenzene, xylene,
                                  indene, indane and naphthaline)
        nutrient: Boolean
            flag to include oxidator availability based on nutrient supply
            calls internally routine "available_NP()" with data
        verbose: Boolean
            verbose flag (default False)

    Output
    ------
        tot_oxi: pd.Series
            Total amount of electrons oxidators in [mmol e-/l]
    """
    tot_oxi = 0.
    cols = check_data(data)


    if nutrient:
        NP_avail = available_NP(data)

    try:
        eas = ean.contaminants[contaminant_group].copy()
        if (ean.name_o_xylene in cols) and (ean.name_pm_xylene in cols): # and (ean.name_xylene in cols):
            eas.remove(ean.name_xylene)

        for cont in eas:
            if cont in cols:
                # tot_oxi += data[cont]*0.001/properties[cont]['molecular_mass']*
                    #properties[cont]['factor_stoichiometry']
                if nutrient:
                    nut_avail = 1000.*NP_avail*properties[cont]['molecular_mass']/(properties[cont]['cs']*12.)
                    c_min = nut_avail.combine(data[cont], min, 0) # mass concentration in ug/l
                else:
                    c_min = data[cont]

                cm_cont = c_min* 0.001/properties[cont]['molecular_mass'] # molar concentration in mmol/l

                tot_oxi += cm_cont *  properties[cont]['factor_stoichiometry']
            else:
                print("WARNING: No data on {} given, zero concentration assumed.".format(cont))
    except KeyError:
        print("WARNING: group of contaminant ('contaminant_group') not defined: '{}'".format(contaminant_group))
        tot_oxi = False

    if isinstance(tot_oxi, float):
        print("\nWARNING: No data on contaminant concentrations given.")
        tot_oxi = False
    elif isinstance(tot_oxi, pd.Series):
        tot_oxi.rename("total_oxidators",inplace = True)
        if verbose:
            print("Total amount of oxidators per column in [mmol e-/l] is:\n{}".format(tot_oxi))

    return tot_oxi

def available_NP(
        data,
        verbose = False,
        **kwargs,
        ):
    """Function calculating available nutrients.

    Approximating the amount of hydrocarbons that can be degraded based
    on the amount of nutrients (nitrogen and phosphate available)

    Input
    -----
        data: pd.DataFrame
            nitrate, nitrite and phosphate concentrations in [mg/l]
        verbose: Boolean
            verbose flag (default False)

        Output
        ------
        NP_avail: pd.Series
            The amount of nutrients for degrading contaminants

    """
    cols = check_data(data)

    nutrient_list = [ean.name_nitrate, ean.name_nitrite, ean.name_phosphate]
    list_nut_miss = []

    for nut in nutrient_list:
        if nut not in cols:
            list_nut_miss.append(nut)
    if len(list_nut_miss)>0:
        raise ValueError("Concentrations of nutrient(s) missing:", list_nut_miss)

    CNs = (data[ean.name_nitrate] + data[ean.name_nitrite]) * (39. / 4.5)
    CPs = data[ean.name_phosphate] * (39. / 1.)
    NP_avail =CNs.combine(CPs, min, 0)
    NP_avail.name = "NP_avail"

    if verbose:
        print("Total NP available is:\n{}".format(NP_avail))

    return NP_avail


def electron_balance(
        data,
        verbose = False,
        **kwargs,
        ):
    """Decision if natural attenuation is taking place.

    Function to calculate electron balance, based on electron availability
    calculated from concentrations of contaminant and electron acceptors

    Input
    -----
        data: pd.DataFrame
            tabular data containinng "total_reductors" and "total_oxidators"
                -total amount of electrons available for reduction [mmol e-/l]
                -total amount of electrons needed for oxidation [mmol e-/l]
        verbose: Boolean
            verbose flag (default False)

    Output
    ------
        e_bal : pd.Series
            Ratio of electron availability: electrons available for reduction
            devided by electrons needed for oxidation

    """
    cols = check_data(data)

    if 'total_reductors' in cols:
        tot_reduct = data['total_reductors']
    else:
        tot_reduct = reductors(data,**kwargs)
        # raise ValueError("Total amount of oxidators not given in data.")

    if 'total_oxidators' in cols:
        tot_oxi = data['total_oxidators']
    else:
        tot_oxi = oxidators(data,**kwargs)
        # raise ValueError("Total amount of reductors not given in data.")

    e_bal = tot_reduct.div(tot_oxi, axis=0)
    e_bal.name = "e_balance"

    if verbose:
        print("Electron balance e_red/e_cont is:\n{}".format(e_bal))

    return e_bal #,decision

def NA_traffic(
        data,
        verbose = False,
        **kwargs,
        ):
    """Function evaluating if natural attenuation (NA) is ongoing.

    Function to calculate electron balance, based on electron availability
    calculated from concentrations of contaminant and electron acceptors.

    Input
    -----
        data: pd.DataFrame
            Ratio of electron availability
        verbose: Boolean
            verbose flag (default False)

    Output
    ------
        traffic : pd.Series
            Traffic light (decision) based on ratio of electron availability

    """
    cols = check_data(data)

    if 'e_balance' in cols:
        e_balance = data['e_balance']
    else:
        e_balance = electron_balance(data,**kwargs)
        # raise ValueError("Electron balance not given in data.")

    e_bal = e_balance.values
    traffic = np.where(e_bal<1,"red","green")
    traffic[np.isnan(e_bal)] = 'yellow'

    NA_traffic = pd.Series(name ='na_traffic_light',data = traffic,index = e_balance.index)

    if verbose:
        print("===============================================================")
        print("Evaluation if natural attenuation (NA) is ongoing:\n")#" for {}".format(contaminant_group))
        print("Red light: Reduction is limited at {} out of {} locations".format(
            np.sum(traffic == "red"),len(e_bal)))
        print("Green light: Reduction is limited at {} out of {} locations".format(
            np.sum(traffic == "green"),len(e_bal)))
        print("Yellow light: No decision possible at {} out of {} locations".format(
            np.sum(np.isnan(e_bal)),len(e_bal)))

    return NA_traffic

def total_contaminant_concentration(
        data,
        contaminant_group = "BTEXIIN",
        verbose = False,
        **kwargs,
        ):
    """Function to calculate total concentration of contaminants.

    Input
    -----
        data: pd.DataFrame
            Contaminant contentrations in [ug/l], i.e. microgram per liter
        contaminant_group: str
            Short name for group of contaminants to use
            default is 'BTEXIIN' (for benzene, toluene, ethylbenzene, xylene,
                                  indene, indane and naphthaline)
        verbose: Boolean
            verbose flag (default False)

    Output
    ------
        tot_conc: pd.Series
            Total concentration of contaminants in [ug/l]

    """
    tot_conc = 0.
    cols = check_data(data)
    try:
        eas = ean.contaminants[contaminant_group].copy()
        if (ean.name_o_xylene in cols) and (ean.name_pm_xylene in cols): # and (ean.name_xylene in cols):
            eas.remove(ean.name_xylene)
        for cont in eas:
            if cont in cols:
                tot_conc += data[cont] # mass concentration in ug/l
            else:
                print("WARNING: No data on {} given, zero concentration assumed.".format(cont))
    except KeyError:
        print("WARNING: group of contaminant ('contaminant_group') not defined: '{}'".format(contaminant_group))
        tot_conc = False

    if isinstance(tot_conc, float):
        print("\nWARNING: No data on contaminant concentrations given.")
        tot_conc = False
    elif isinstance(tot_conc, pd.Series):
        tot_conc.rename("total_contaminants",inplace = True)
        if verbose:
            print("Total concentration of {} in [ug/l] is:\n{}".format(contaminant_group,tot_conc))

    return tot_conc

def thresholds_for_intervention(
        data,
        contaminant_group = "BTEXIIN",
        verbose = False,
        **kwargs,
        ):
    """Function to evalute the threshold set by the Dutch government.

    Input
    -----
        data: pd.DataFrame
            Contaminant contentrations in [ug/l], i.e. microgram per liter
            if nutrient is True, data also needs to contain concentrations
            of Nitrate, Nitrite and Phosphate
        contaminant_group: str
            Short name for group of contaminants to use
            default is 'BTEXIIN' (for benzene, toluene, ethylbenzene, xylene,
                                  indene, indane and naphthaline)
        verbose: Boolean
            verbose flag (default False)

    Output
    ------
        intervention: list
        List of contaminants above the threshold of intervention, including
        ratio of exceeding the threshold

    """
    cols= check_data(data)
    na_intervention= pd.DataFrame(data, columns=[ean.name_sample,ean.name_observation_well])
    traffic = np.zeros(data.shape[0])
    intervention = [[] for i in range(data.shape[0])]

    try:
        eas = ean.contaminants[contaminant_group].copy()
        if (ean.name_o_xylene in cols) and (ean.name_pm_xylene in cols): # and (ean.name_xylene in cols):
            eas.remove(ean.name_xylene)
        for cont in eas:
            if cont in cols:
                th_value = properties[cont]['thresholds_for_intervention_NL']
                traffic += (data[cont].values > th_value)
                for i in range(data.shape[0]):
                    if data[cont].values[i] > th_value:
                        intervention[i].append(cont)
            else:
                print("WARNING: No data on {} given, zero concentration assumed.".format(cont))

        traffic_light = np.where(traffic>0,"red","green")
        traffic_light[np.isnan(traffic)] = 'yellow'
        na_intervention['intervention_traffic'] = traffic_light

        na_intervention['intervention_number'] = traffic
        na_intervention['intervention_contaminants'] = intervention

        if verbose:
            print("===============================================================")
            print("Evaluation of contaminant concentrations exceeding intervention values for {}:\n".format(
                contaminant_group))
            print("Red light: Intervention values exceeded for {} out of {} locations".format(
                np.sum(traffic >0),data.shape[0]))
            print("green light: Concentrations below intervention values at {} out of {} locations".format(
                np.sum(traffic == 0),data.shape[0]))
            print("Yellow light: No decision possible at {} out of {} locations".format(
                np.sum(np.isnan(traffic)),data.shape[0]))
    except KeyError:
        print("WARNING: group of contaminant ('contaminant_group') not defined: '{}'".format(contaminant_group))
        na_intervention = False

    return na_intervention

def screening_NA(
    data,
    ea_group = 'ONSFe',
    contaminant_group = "BTEXIIN",
    nutrient = False,
    verbose = False,
    **kwargs,
    ):
    """Calculate the amount of electron reductors [mmol e-/l].

    making use of imported molecular mass values for quantities in [mg/mmol]

    Input
    -----
        data: pd.DataFrame
            Concentration values of
                - electron acceptors in [mg/l]
                - contaminant in [ug/l]
                - nutrients (Nitrate, Nitrite and Phosphate) if nutrient is True
        ea_group: str
            Short name for group of electron acceptors to use
            default is 'ONSFe' (for oxygen, nitrate, sulfate and ironII)
        contaminant_group: str
            Short name for group of contaminants to use
            default is 'BTEXIIN' (for benzene, toluene, ethylbenzene, xylene,
                                   indene, indane and naphthaline)
        nutrient: Boolean
            flag to include oxidator availability based on nutrient supply
            calls internally routine "available_NP()" with data
        verbose: Boolean
            verbose flag (default False)

    Output
    ------
        na_data: pd.DataFrame
            Tabular data with all quantities of NA screening listed per sample
    """
    check_data(data)

    na_data = thresholds_for_intervention(data,
                                          contaminant_group = contaminant_group,
                                          verbose = verbose)
    tot_cont = total_contaminant_concentration(data,
                                               contaminant_group = contaminant_group,
                                               verbose = verbose)
    tot_reduct = reductors(data,
                            ea_group = ea_group,
                            verbose = verbose)
    tot_oxi = oxidators(data,
                        contaminant_group = contaminant_group,
                        nutrient = nutrient,
                        verbose = verbose)
    e_bal = electron_balance(data,
                              verbose = verbose)
    na_traffic = NA_traffic(data,
                            contaminant_group = contaminant_group,
                            verbose = verbose)

    for add in [tot_cont,na_traffic,e_bal,tot_oxi,tot_reduct]:
        na_data.insert(2, add.name, add)

    if nutrient:
        NP_avail = available_NP(data,verbose = verbose)
        na_data.insert(4, NP_avail.name, NP_avail)

    return na_data

def check_data(data):
    """Checking data on correct format.

    Input
    -----
        data: pd.DataFrame
            concentration values of quantities

    Output
    ------
        cols: list
        List of column names
    """
    if isinstance(data, pd.DataFrame):
        cols = data.columns.to_list()
    elif isinstance(data, pd.Series):
        cols = [data.name]
    else:
        raise ValueError("Calculation of not possible with given data. \
                          Data has to be a panda-DataFrame or Series \
                          but is given as type {}".format(type(data)))

    return cols
