# `mibipret` Data handling

## General

We designed data handling for field sample data typical for biodegradation processes. This data includes sample specification data, contaminant concentrations (we focus on petroleum hydrocarbons), habitat conditions (e.g. redox potential, pH, electron acceptor concentrations, such as oxygen concentration), microbiome data (i.e. the occurrence of DNA and functional genes), metabolite data (i.e. intermediate products of the degradation process) and measurements on stable isotope fractions (particularly for hydrogen and carbon within the sample and/or of individual contaminant).
The type of input data here is in line with data gathered in WP1 during the first sampling round. Some of the field sample data from the MIBIREM project is also used for code testing and demonstration. 
Data handling is implemented in functions in the folder mibirpret/data. Routines handle data input, like reading in from spreadsheets; check of input data, such as correct units provided; validation of input data, standardisation, selection of data etc. Routines have been designed in accordance with the design of standard data formats for field sampling data as part of the data management, WP1, task  T1.4, milestone 3.
The workflow of data handling is illustrated for the Griftpark data (folder ex01_Griftpark) in the jupyter-notebook “example_01_grift_data.ipynb”. A pdf-version of the notebook is attached as annex. 



