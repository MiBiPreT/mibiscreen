"""Tests for the mibipret.data module."""

import numpy as np
import pandas as pd
import pytest
from mibipret.data.data import check_columns
from mibipret.data.data import check_units
from mibipret.data.data import check_values
from mibipret.data.data import example_data
from mibipret.data.data import load_csv
from mibipret.data.data import load_excel
from mibipret.data.data import standardize

path_data = "./mibipret/data"

class TestData:
    """Class for testing data module of mibipret."""

    data_01 = example_data(with_units = True)
    data_02 = example_data(data_type = 'contaminants',with_units = True)
    data_03 = example_data(data_type = 'setting',with_units = True)
    data_04 = example_data(data_type = 'environment',with_units = True)

    columns = ['sample_nr', 'obs_well', 'depth', 'pH', 'redoxpot', 'sulfate',\
               'methane', 'ironII', 'benzene', 'naphthalene']
    columns_mod = ["sample","well","Depth",'pH', 'redox' , 'Sulfate', 'CH4','iron','c6h6', 'Naphthalene']

    units = [' ',' ','m',' ','mV', 'mg/L', 'mg/L', 'mg/L', 'ug/L', 'ug/L']
    units_mod = [' ',' ','cm',' ','','ug/L', 'mg/L', 'ppm', 'mg/L',  'ug/L']

    s01 = ['2000-001', 'B-MLS1-3-12',-12, 7.23, -208, 23, 748, 3,263,2207]

    new_column = pd.Series(data = ['ug/L',27.0, 54.1, 38.8, 19.70], name = 'unknown_contaminant')
    data_05 = pd.concat([data_01,new_column],axis = 1)

    def test_example_data_01(self):
        """Testing correct loading of example data as pandas data frame."""
#        assert isinstance(self.data_01, pd.DataFrame) == True
        assert self.data_01.shape == (5,24)

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
        assert self.data_04.shape == (5,16)

    def test_load_csv_01(self):
        """Testing correct loading of example data from csv file."""
        data_t1 = load_csv("{}/example_data.csv".format(path_data))[0]
        # y = pd.load_csv('{}/example_data.csv'.format(path_data))
        # check = np.all(y.columns == all_test_data.columns)
        assert data_t1.shape == self.data_01.shape

    def test_load_csv_02(self):
        """Testing Error message that no path to csv file is given."""
        with pytest.raises(ValueError, match="Specify file path and file name!"):
            load_csv()

    def test_load_csv_03(self):
        """Testing Error message that given file path does not match."""
        with pytest.raises(OSError):
            load_csv("ThisFileDoesNotExist.csv")

    def test_load_excel_01(self):
        """Testing correct loading of example data from excel file."""
        data_t2= load_excel("{}/example_data.xlsx".format(path_data),sheet_name= 'contaminants')[0]
        assert data_t2.shape == self.data_02.shape

    def test_load_excel_02(self):
        """Testing Error message that no path to excel file is given."""
        with pytest.raises(ValueError, match="Specify file path and file name!"):
            load_excel()

    def test_load_excel_03(self):
        """Testing Error message that given file path does not match."""
        with pytest.raises(OSError):
            load_excel("ThisFileDoesNotExist.xlsx")

    def test_check_columns_01(self):
        """Testing check of column names.

        Testing that routine provides correct list of known quantities
        identified in the columns
        """
        data4check = pd.DataFrame([self.units,self.s01],columns = self.columns_mod)
        column_names_known,column_names_unknown,column_names_standard = check_columns(data4check)
        assert len(column_names_unknown) == 0 and column_names_standard == self.columns

    def test_check_columns_02(self):
        """Testing check of column names.

        Testing that routine provides correct list of unknown quantities
        identified in the columns
        """
        column_names_known,column_names_unknown,column_names_standard = check_columns(self.data_05)
        assert column_names_unknown[0] == 'unknown_contaminant'

    def test_check_columns_03(self,capsys):
        """Testing check of column names.

        Testing verbose flag.
        """
        check_columns(self.data_05,verbose=True)
        out,err=capsys.readouterr()

        assert len(out)>0

    def test_check_units_01(self):
        """Testing check of units.

        Testing that routine check_units() provides correct list of
        quantities where units are not in expected format when input is
        the entire data frame.

        """
        data4units = pd.DataFrame([self.units_mod,self.s01],columns = self.columns)
        col_check_list = check_units(data4units)
        check_list = ['sulfate', 'benzene','depth', 'redoxpot']

        assert col_check_list == check_list

    def test_check_units_02(self):
        """Testing check of units.

        Testing that routine check_units() provides correct list of
        quantities where units are not in expected format when input is
        the data frame with only the unit-row.
        """
        data4units = pd.DataFrame([self.units_mod],columns = self.columns)
        col_check_list = check_units(data4units)
        check_list = ['sulfate', 'benzene','depth', 'redoxpot']

        assert col_check_list == check_list

    def test_check_units_03(self):
        """Testing check of units.

        Testing Error message that provided input is not a data frame.
        """
        with pytest.raises(ValueError, match="Provided data is not a data frame."):
            check_units(self.s01)

    def test_check_units_04(self):
        """Testing check of units.

        Testing Error message that provided data frame does not contain units.
        """
        with pytest.raises(ValueError):
            data4units = pd.DataFrame([self.s01],columns = self.columns)
            check_units(data4units)

    def test_check_units_05(self,capsys):
        """Testing routine check of units.

        Testing verbose flag.
        """
        check_units(self.data_01,verbose=True)
        out,err=capsys.readouterr()

        assert len(out)>0

    def test_check_values_01(self):
        """Testing routine check_values().

        Testing that values in data frame have been transformed to numerics.
        """
        data_pure = check_values(self.data_01)

        # assert isinstance(data_pure.iloc[-1,-1], np.int64)
        assert isinstance(data_pure.iloc[-1,-1], np.float64)

    def test_check_values_02(self):
        """Testing routine check_values().

        Testing that data frame is cut clean from units row.
        """
        data_pure = check_values(self.data_01)

        assert data_pure.shape[0] == self.data_01.shape[0]-1

    def test_check_values_03(self):
        """Testing routine check_values().

        Testing Error message that provided input is not a data frame.
        """
        with pytest.raises(ValueError, match="Provided data is not a data frame."):
            check_values(self.s01)

    def test_check_values_04(self,capsys):
        """Testing routine check_values().

        Testing verbose flag.
        """
        check_values(self.data_01,verbose=True)
        out,err=capsys.readouterr()

        assert len(out)>0

    def test_standardize_01(self):
        """Testing routine standardize().

        Testing that data has been properly standardies,
        here that data frame is cut clean from units row.
        """
        data_standard,units = standardize(self.data_05,reduce = True, store_csv=False,  verbose=False)

        assert data_standard.shape[1] == self.data_01.shape[1]

    def test_standardize_02(self):
        """Testing routine standardize().

        Testing that data has been properly standardies,
        here without reducing to know quantities.
        """
        data_standard,units = standardize(self.data_05,reduce = False, store_csv=False,  verbose=False)

        assert data_standard.shape == (4,25)

    def test_standardize_03(self,capsys):
        """Testing routine standardize().

        Testing verbose flag.
        """
        standardize(self.data_05,reduce = True, store_csv=False,  verbose=True)
        out,err=capsys.readouterr()

        assert len(out)>0

    def test_standardize_04(self,capsys):
        """Testing routine standardize().

        Testing Error message that given file path does not match for writing
        standarized data to file.
        """
        file_name = '../dir_does_not_exist/file.csv'
        out_text = "WARNING: data could not be saved. Check provided file path and name: {}\n".format(file_name)
        standardize(self.data_05,reduce = True, store_csv=file_name,  verbose=False)
        out,err=capsys.readouterr()

        assert out==out_text
