#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Routines for performing linear regression on isotope data.

@author: Alraune Zech
"""
import numpy as np
import mibiscreen.data.settings.standard_names as names
from mibiscreen.data.check_data import _generate_dict_other_names
from mibiscreen.data.settings.contaminants import properties_contaminants
from mibiscreen.data.settings.isotopes import properties_isotopes


def Lambda_regression(delta_C,
                      delta_H,
                      validate_indices = True,
                      verbose = False,
                      **kwargs,
                      ):
    """Performing linear regression to achieve Lambda value.

    The Lambda values relates the δ13C versus δ2H signatures of a chemical
    compound. Relative changes in the ratio can indicate the occurrence of
    specific enzymatic degradation reactions.

    The analysis is based on a linear regression of the hydrogen versus
    carbon isotope signatures. The parameter of interest, the Lambda values
    is the slope of the the linear trend line.

    A plot of the results with data and linear trendline can be generate with the
    method Lambda_plot() [in the module visualize].

    Input
    -----
        delta_C : np.array, pd.series
            relative isotope ratio (delta-value) of carbon of target molecule
        delta_H : np.array, pd.series (same length as delta_C)
            relative isotope ratio (delta-value) of hydrogen of target molecule
        validate_indices: boolean, default True
            flag to run index validation (i.e. removal of nan and infinity values)
        verbose : Boolean, The default is False.
           Set to True to get messages in the Console about the status of the run code.
        **kwargs : dict
            keywordarguments dictionary, e.g. for passing forward keywords to
            valid_indices()

    Returns
    -------
        results : dict
            results of fitting, including:
                * coefficients : array/list of lenght 2, where coefficients[0]
                    is the slope of the linear fit, reflecting the lambda values
                    and coefficient[1] is the absolute value of the linear function
                * delta_C: np.array with isotope used for fitting - all samples
                    where non-zero values are available for delta_C and delta_H
                * delta_H: np.array with isotope used for fitting - all samples
                    where non-zero values are available for delta_C and delta_H
    """
    ### ---------------------------------------------------------------------------
    ### check length of data arrays and remove non-valid values (NaN, inf & zero)

    if verbose:
        print('==============================================================')
        print(" Running function 'Lambda_regression()' on data")
        print('==============================================================')

    if validate_indices:
        data1, data2 = valid_indices(delta_C,
                                     delta_H,
                                     remove_nan = True,
                                     remove_infinity = True,
                                     remove_zero=True,
                                     )
    else:
        data1, data2 = delta_C,delta_H

    ### ---------------------------------------------------------------------------
    ### perform linear regression

    coefficients = np.polyfit(data1, data2, 1)

    if verbose:
        print("Lambda value, being the slope of the linear fit is \n identified with {:.2f}".format(coefficients[0]))
        print('______________________________________________________________')

    results = dict(
        delta_C = data1,
        delta_H = data2,
        coefficients = coefficients,
        )

    return results

def Rayleigh_fractionation(concentration,
                           delta,
                           validate_indices = True,
                           verbose = False,
                           **kwargs,
                           ):
    """Performing Rayleigh fractionation analysis.

    Rayleigh fractionation is a common application to characterize the removal
    of a substance from a finite pool using stable isotopes. It is based on the
    change in the isotopic composition of the pool due to different kinetics of
    the change in lighter and heavier isotopes.

    We follow the most simple approach assuming that the substance removal follows
    first-order kinetics, where the rate coefficients for the lighter and heavier
    isotopes of the substance differ due to kinetic isotope fractionation effects.
    The isotopic composition of the remaining substance in the pool will change
    over time, leading to the so-called Rayleigh fractionation.

    The analysis is based on a linear regression of the log-transformed concentration
    data against the delta-values. The parameter of interest, the kinetic
    fractionation factor (epsilon or alpha -1) of the removal process is the slope
    of the the linear trend line.

    A plot of the results with data and linear trendline can be generate with the
    method Rayleigh_fractionation_plot() [in the module visualize].

    Input
    -----
        concentration : np.array, pd.dataframe
            total molecular mass/molar concentration of target substance
            at different locations (at a time) or at different times (at one location)
        delta : np.array, pd.dataframe (same length as concentration)
            relative isotope ratio (delta-value) of target substance
        validate_indices: boolean, default True
            flag to run index validation (i.e. removal of nan and infinity values)
        verbose : Boolean, The default is False.
           Set to True to get messages in the Console about the status of the run code.
        **kwargs : dict
            keywordarguments dictionary, e.g. for passing forward keywords to
            valid_indices()

    Returns
    -------
        results : dict
            results of fitting, including:
                * coefficients : array/list of lenght 2, where coefficients[0]
                    is the slope of the linear fit, reflecting the kinetic
                    fractionation factor (epsilon or alpha -1) of the removal process
                    and coefficient[1] is the absolute value of the linear function
                * delta_C: np.array with isotope used for fitting - all samples
                    where non-zero values are available for delta_C and delta_H
                * delta_H: np.array with isotope used for fitting - all samples
                    where non-zero values are available for delta_C and delta_H
    """
    ### ---------------------------------------------------------------------------
    ### check length of data arrays and remove non-valid values (NaN, inf & zero)
    if verbose:
        print('==============================================================')
        print(" Running function 'Rayleigh_fractionation()' on data")
        print('==============================================================')

    if validate_indices:
        data1, data2 = valid_indices(concentration,
                                 delta,
                                 remove_nan = True,
                                 remove_infinity = True,
                                 remove_zero = True,
                                 **kwargs,
                                 )
    else:
        data1, data2 = concentration,delta

    ### ---------------------------------------------------------------------------
    ### perform linear regression
    if np.any(data1<=0):
        raise ValueError("Concentration data provided is negative, but has to be positive.")

    coefficients = np.polyfit(np.log(data1), data2, 1)

    if verbose:
        print("The kinetic fractionation factor ('epsilon' or 'alpha-1') of")
        print("the removal process, being the slope of the linear fit, is ")
        print("identified with {:.2f}".format(coefficients[0]))
        print('______________________________________________________________')

    results = dict(
        concentration = data1,
        delta = data2,
        coefficients = coefficients,
        )

    return results

def Keeling_regression(concentration,
                       delta_mix = None,
                       relative_abundance = None,
                       validate_indices = True,
                       verbose = False,
                       **kwargs,
                       ):
    """Performing a linear regression linked to the Keeling plot.

    A Keeling fit/plot is an approach to identify the isotopic composition of a
    contaminating source from measured concentrations and isotopic composition
    (delta) of a target species in the mix of the source and a pool.

    It is based on the linear relationship of the given quantities (concentration)
    and delta-values (or alternatively the relative abundance x) which are measured
    over time or across a spatial interval according to

        delta_mix = delta_source + m * 1/c_mix

    where m is the slope relating the isotopic quantities of the pool (which mixes
    with the sourse) by m = (delta_pool + delta_source)*c_pool.

    The analysis is based on a linear regression of the inverse concentration
    data against the delta (or x)-values. The parameter of interest, the delta
    (or relative_abundance, respectively) of the source quantity is the
    intercept of linear fit with the y-axis, or in other words, the absolute
    value of the linear fit function.

    A plot of the results with data and linear trendline can be generate with the
    method Keeling_plot() [in the module visualize].

    Note that the approach is only applicable if
        (i)  the isotopic composition of the unknown source is constant
        (ii) the concentration and isotopic composition of the target compound
            is constant (over time or across space)
            (i.e. in absence of contamination from the unknown source)

    Input
    -----
        concentration : np.array, pd.dataframe
            total molecular mass/molar concentration of target substance
            at different locations (at a time) or at different times (at one location)
        delta_mix : np.array, pd.dataframe (same length as c_mix), default None
            relative isotope ratio (delta-value) of target substance
        relative_abundance : None or np.array, pd.dataframe (same length as c_mix), default None
            if not None it replaces delta_mix in the inverse estimation and plotting
            relative abundance of target substance
        validate_indices: boolean, default True
            flag to run index validation (i.e. removal of nan and infinity values)
        verbose : Boolean, The default is False.
           Set to True to get messages in the Console about the status of the run code.
        **kwargs : dict
            keywordarguments dictionary, e.g. for passing forward keywords to
            valid_indices()

    Returns
    -------
        results : dict
            results of fitting, including:
                * coefficients : array/list of lenght 2, where coefficients[0]
                    is the slope of the linear fit and coefficient[1] is the
                    intercept of linear fit with y-axis, reflecting delta
                    (or relative_abundance, respectively) of the source quantity
                * delta_C: np.array with isotope used for fitting - all samples
                    where non-zero values are available for delta_C and delta_H
                * delta_H: np.array with isotope used for fitting - all samples
                    where non-zero values are available for delta_C and delta_H
    """
    if verbose:
        print('==============================================================')
        print(" Running function 'Keeling_regression()' on data")
        print('==============================================================')

    if delta_mix is not None:
        y = delta_mix
        text = 'delta'
    elif relative_abundance is not None:
        y = relative_abundance
        text = 'relative abundance'
    else:
        raise ValueError("One of the quantities 'delta_mix' or 'relative_abundance' must be provided")

    ### ---------------------------------------------------------------------------
    ### check length of data arrays and remove non-valid values (NaN, inf & zero)

    if validate_indices:
        data1, data2 = valid_indices(concentration,
                                 y,
                                 remove_nan = True,
                                 remove_infinity = True,
                                 remove_zero = True,
                                 **kwargs,
                                 )
    else:
        data1, data2 = concentration,y

    ### ---------------------------------------------------------------------------
    ### perform linear regression

    coefficients = np.polyfit(1./data1, data2, 1)

    if verbose:
        print("The {} of the source quantity, being the intercept".format(text))
        print("of the linear fit, is identified with {:.2f}".format(coefficients[1]))
        print('______________________________________________________________')

    results = dict(
        concentration = data1,
        delta = data2,
        coefficients = coefficients,
        )

    return results
    # return tuple(coefficients)

def valid_indices(data1,
                  data2,
                  remove_nan = True,
                  remove_infinity = True,
                  remove_zero = False,
                  **kwargs,
                  ):
    """Identifies valid indices in two equaly long arrays and compresses both.

    Optional numerical to remove from array are: nan, infinity and zero values.

    Parameters
    ----------
    data1 : np.array or pd.series
        numeric data
    data2 : np.array or pd.series (same len/shape as data1)
        numeric data
    remove_nan : boolean, default True
        flag to remove nan-values
    remove_infinity : boolean, default True
        flag to remove infinity values
    remove_zero : boolean, default False
        flag to remove zero values
    **kwargs : dict
        keywordarguments dictionary

    Returns
    -------
    data1 : np.array or pd.series
        numeric data of reduced length where only data at valid indices is in
    data2 : np.array or pd.series
        numeric data of reduced length where only data at valid indices is in

    """
    if data1.shape != data2.shape:
        raise ValueError("Shape of provided data must be identical.")

    valid_indices = np.full(data1.shape, True, dtype=bool)

    if remove_nan:
        valid_indices *= ~np.isnan(data1) & ~np.isinf(data1)
    if remove_infinity:
        valid_indices *= ~np.isnan(data2) & ~np.isinf(data2)
    if remove_zero:
        valid_indices *= (data1 != 0) & (data2 != 0)

    return data1[valid_indices],data2[valid_indices]

def extract_isotope_data(df,
                         molecule,
                         name_13C = names.name_13C,
                         name_2H = names.name_2H,
                         ):
    """Extracts isotope data from standardised input-dataframe.

    Parameters
    ----------
    df : pd.dataframe
        numeric (observational) data
    molecule : str
        name of contaminant molecule to extract isotope data for
    name_13C : str, default 'delta_13C' (standard name)
        name of C13 isotope to extract data for
    name_2H : str, default 'delta_2H' (standard name)
        name of deuterium isotope to extract data for

    Returns
    -------
    C_data : np.array
        numeric isotope data
    H_data : np.array
        numeric isotope data

    """
    other_names_contaminants = _generate_dict_other_names(properties_contaminants)
    other_names_isotopes = _generate_dict_other_names(properties_isotopes)

    molecule_standard = other_names_contaminants.get(molecule.lower(), False)
    isotope_13C = other_names_isotopes.get(name_13C.lower(), False)
    isotope_2H = other_names_isotopes.get(name_2H.lower(), False)

    if molecule_standard is False:
        raise ValueError("Contaminant (name) unknown: {}".format(molecule))
    if isotope_13C is False:
        raise ValueError("Isotope (name) unknown: {}".format(name_13C))
    if isotope_2H is False:
        raise ValueError("Isotope (name) unknown: {}".format(name_2H))

    name_C = '{}-{}'.format(isotope_13C,molecule_standard)
    name_H = '{}-{}'.format(isotope_2H,molecule_standard)

    if name_C not in df.columns.to_list():
        raise ValueError("No isotope data available for : {}".format(name_C))
    if name_H not in df.columns.to_list():
        raise ValueError("No isotope data available for : {}".format(name_H))

    C_data = df[name_C].values
    H_data = df[name_H].values

    return C_data, H_data
