# `mibiscreen` Concentrations


## General

`concentration` provides tools for analysis of concentrations values of:
* contaminants
* electron acceptors/geochemical quantities
* metabolites 

## Total concentration

The routine `total_concentration()` provides the option to calculate, per sample, the sum of concentrations for a selection of quantities, e.g. the total concentration of all contaminants, all BTEX contaminants, all metabolites (if they are provided as single data frame), etc.. 

## Threshold values

The routine `total_count()` provides the option to calculate, per sample, the number of quantities exceeding a self-defined threshold value (by default zero) for a list of quantities provided, e.g. for all contaminants, all BTEX contaminants, all metabolites (if they are provided as single data frame), etc.. Note that the same threshold values is applied to all quantities. 

The routine `thresholds_for_intervention()` provides the option to determine which contaminants exceed regulatory threshold values. Here, threshold values differ per contaminant. At the moment, only the regulatory threshold values for The Netherlands are implemented, and only for the group of contaminants: BTEXIIN (benzene, toluene, ethylbenzene, xylene, indene, indane, naphtalen). 

## Concentration plots

To be added: visualization of results of concentration analysis.
