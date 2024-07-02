"""Tests for the mibipret.data module."""

import pandas as pd
from mibipret.data.data import check_columns
from mibipret.data.data import check_units
from mibipret.data.data import example_data
from mibipret.data.data import load_csv
from mibipret.data.data import load_excel

path_data = "./mibipret/data"

class TestData:
    """Class for testing data module of mibipret."""

    data_01 = example_data()
    data_02 = example_data(data_type = 'contaminants')
    data_03 = example_data(data_type = 'setting')
    data_04 = example_data(data_type = 'environment')

    columns = ['sample_nr', 'obs_well', 'depth', 'pH', 'redoxpot', 'sulfate',\
               'methane', 'ironII', 'benzene', 'naphthalene']
    columns_mod = ["sample","well","Depth",'pH', 'redox' , 'Sulfate', 'CH4','iron','c6h6', 'Naphthalene']

    units = [' ',' ','m',' ','mV', 'mg/L', 'mg/L', 'mg/L', 'ug/L', 'ug/L']
    units_mod = [' ',' ','m',' ','','ug/L', 'mg/L', 'ppm', 'mg/L',  'ug/L']

    s01 = ['2000-001', 'B-MLS1-3-12',-12, 7.23, -208, 23, 748, 3,263,2207]

    def test_example_data_01(self):
        """Testing correct loading of example data as pandas data frame."""
#        assert isinstance(self.data_01, pd.DataFrame) == True
        assert self.data_01.shape == (5,19)

    def test_example_data_02(self):
        """Testing correct loading of example data as pandas data frame."""
        # assert isinstance(self.data_02, pd.DataFrame) == True
        assert self.data_02.shape == (5,11)

    def test_example_data_03(self):
        """Testing correct loading of example data as pandas data frame."""
        # assert isinstance(self.data_03, pd.DataFrame) == True
        assert self.data_03.shape == (5,3)

    def test_example_data_04(self):
        """Testing correct loading of example data as pandas data frame."""
        # assert isinstance(self.data_04, pd.DataFrame) == True
        assert self.data_04.shape == (5,11)

    def test_load_csv(self):
        """Testing correct loading of example data from csv file."""
        print("{}/example_data.csv".format(path_data))
        data_t1 = load_csv("{}/example_data.csv".format(path_data))[0]
        # y = pd.load_csv('{}/example_data.csv'.format(path_data))
        # check = np.all(y.columns == all_test_data.columns)
        assert data_t1.shape == self.data_01.shape

    def test_load_excel(self):
        """Testing correct loading of example data from excel file."""
        data_t2= load_excel("{}/example_data.xlsx".format(path_data),sheet_name= 'contaminants')[0]
        assert data_t2.shape == self.data_02.shape

    def test_check_columns(self):
        """Testing check and renaming of column names.

        Testing check and renaming of column names on sample information,
        environmental conditions, and contaminnants
        """
        data4check = pd.DataFrame([self.units,self.s01],columns = self.columns_mod)
        data_t3 = check_columns(data4check)
        assert data_t3.columns.tolist() == self.columns

    def test_check_units(self):
        """Testing check of units.

        Testing check of units of given sample information on environmental
        conditions and contaminnants

        """
        data4units = pd.DataFrame([self.units_mod,self.s01],columns = self.columns)
        col_check_list = check_units(data4units)
        check_list = ['sulfate', 'ironII', 'benzene', 'redoxpot']

        assert col_check_list == check_list
