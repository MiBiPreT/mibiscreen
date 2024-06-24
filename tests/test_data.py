"""Tests for the mibipret.data module."""

# importing module
path_package = '/home/alraune/GitHub/MiBiPreT/mibipret'
path_data = "{}/mibipret/data".format(path_package)

import pandas as pd
import pytest
import sys

sys.path.append(path_package) # appending a path
from mibipret.data.data import example_data, load_csv, load_excel,check_columns , check_units #, check_values 


class TestData:
    data_01 = example_data()   
    data_02 = example_data(data_type = 'contaminants')   

    columns = ['sample_nr', 'obs_well', 'depth', 'pH', 'redoxpot', 'sulfate', 'methane', 'ironII', 'benzene', 'naphthalene']
    columns_mod = ["sample","well","Depth",'pH', 'redox' , 'Sulfate', 'CH4','iron','c6h6', 'Naphthalene']
    
    units = [' ',' ','m',' ','mV', 'mg/L', 'mg/L', 'mg/L', 'ug/L', 'ug/L']
    units_mod = [' ',' ','m',' ','','ug/L', 'mg/L', 'ppm', 'mg/L',  'ug/L']
    
    s01 = ['2000-001', 'B-MLS1-3-12',-12, 7.23, -208, 23, 748, 3,263,2207]

    def test_example_data(self):
        """Testing correct loading of example data as pandas data frame."""
        assert isinstance(self.data_01, pd.DataFrame) == True

    def test_load_csv(self):

        """Testing correct loading of example data from csv file."""
        data_t1 = load_csv("{}/example_data.csv".format(path_data))[0]
        # y = pd.load_csv('{}/example_data.csv'.format(path_data))
        # check = np.all(y.columns == all_test_data.columns)
        assert data_t1.shape == self.data_01.shape

    def test_load_excel(self):

        """Testing correct loading of example data from excel file."""
        data_t2= load_excel("{}/example_data.xlsx".format(path_data),sheet_name= 'contaminants')[0]
        assert data_t2.shape == self.data_02.shape

    def test_check_columns(self):

        """Testing check and renaming of column names on sample information, environmental conditions, and contaminnants """

        data4check = pd.DataFrame([self.units,self.s01],columns = self.columns_mod)
        data_t3 = check_columns(data4check)
        assert data_t3.columns.tolist() == self.columns
        
    def test_check_units(self):

        """Testing check of units of given sample information on environmental conditions and contaminnants"""

        data4units = pd.DataFrame([self.units_mod,self.s01],columns = self.columns)
        col_check_list = check_units(data4units)
        check_list = ['sulfate', 'ironII', 'benzene', 'redoxpot']
    
        assert col_check_list == check_list
        
        
