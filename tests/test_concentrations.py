#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Testing analysis module on concentration analysis of mibiscreen.

@author: Alraune Zech
"""

import numpy as np
import pandas as pd
import pytest
from mibiscreen.analysis.sample.concentrations import total_concentration
from mibiscreen.analysis.sample.concentrations import total_contaminant_concentration
from mibiscreen.analysis.sample.concentrations import total_contaminant_count
from mibiscreen.analysis.sample.concentrations import total_count
from mibiscreen.analysis.sample.concentrations import total_metabolites_concentration
from mibiscreen.analysis.sample.concentrations import total_metabolites_count
from mibiscreen.data.example_data.example_data import example_data


class TestTotalConcentration:
    """Class for testing analysis module on NA screening of mibiscreen."""

    columns = ['sample_nr', 'sulfate', 'benzene']
    units = [' ','mg/L', 'ug/L']
    s01 = ['2000-001', 748, 263]
    s02 = ['2000-002', 548, 103]
    s02b = ['2000-002', 548, ]

    data1 = pd.DataFrame([s01,s02],
                         columns = columns)

    data_nonstandard = pd.DataFrame([units,s01,s02b],
                                    columns = columns)


    def test_total_concentration_01(self):
        """Testing routine total_concentration().

        Correct calculation of total amount of contaminants (total concentration).
        """
        out = total_concentration(self.data1).values
        test = self.data1.iloc[:,1:].sum(axis = 1).values
        assert np.all(out == test)

    def test_total_concentration_02(self):
        """Testing routine total_concentration().

        Testing 'include' option adding calculated values as column to data.
        """
        data_test = self.data1.copy()
        total_concentration(data_test,
                            name_list=['benzene'],
                            include_as = 'test').values

        assert data_test.shape[1] == self.data1.shape[1]+1 and \
            np.all(data_test['test'] == self.data1['benzene'])

    def test_total_concentration_03(self):
        """Testing routine total_concentration().

        Correct handling when no overlap of specified list of quantities
        with column names in data frame.
        """
        with pytest.raises(ValueError):
            total_concentration(self.data1,name_list=['test1','test2'])


    def test_total_concentration_04(self):
        """Testing routine total_concentration().

        Correct handling when keyword 'include_as' is not correctly provided.
        """
        with pytest.raises(ValueError):
            total_concentration(self.data1,
                                include_as = 1,
                                )


    def test_total_concentration_05(self,capsys):
        """Testing routine total_concentration().

        Testing verbose flag.
        """
        total_concentration(self.data1,verbose=True)
        out,err=capsys.readouterr()

        assert len(out)>0


class TestTotalContaminantConcentration:
    """Class for testing total concentration of contaminants from module concentation of mibipret."""

    data = example_data(with_units = False)

    def test_total_contaminant_concentration_01(self):
        """Testing routine total_contaminant_concentration().

        Correct calculation of total amount of contaminants (total concentration).
        """
        tot_conc_test = 27046.0
        tot_conc = np.sum(total_contaminant_concentration(self.data))

        assert (tot_conc - tot_conc_test)<1e-5

    def test_total_contaminant_concentration_02(self):
        """Testing routine total_contaminant_concentration().

        Correct calculation of total amount of contaminants (total concentration)
        for BTEX.
        """
        tot_conc_test = 8983.0
        tot_conc = np.sum(total_contaminant_concentration(self.data,contaminant_group='BTEX'))

        assert (tot_conc - tot_conc_test)<1e-5

    def test_total_contaminant_concentration_03(self):
        """Testing routine total_contaminant_concentration().

        Correct calculation of total amount of contaminants (total concentration)
        for BTEX.
        """
        tot_conc_test = 27046.0
        tot_conc = np.sum(total_contaminant_concentration(self.data,contaminant_group='BTEXIIN'))

        assert (tot_conc - tot_conc_test)<1e-5

    def test_total_contaminant_concentration_04(self):
        """Testing routine total_contaminant_concentration().

        Correct handling when unknown group of contaminants are provided.
        """
        with pytest.raises(ValueError):
            total_contaminant_concentration(self.data,contaminant_group = 'test')

    def test_total_contaminant_concentration_05(self):
        """Testing routine total_contaminant_concentration().

        Testing 'include' option adding calculated values as column to data.
        """
        data_test = self.data.copy()
        total_contaminant_concentration(data_test,include = True)

        assert data_test.shape[1] == self.data.shape[1]+1
        assert 'concentration_contaminants' in data_test.columns


    def test_total_contaminant_concentration_06(self,capsys):
        """Testing routine total_contaminant_concentration().

        Testing verbose flag.
        """
        total_contaminant_concentration(self.data,verbose=True)
        out,err=capsys.readouterr()

        assert len(out)>0

class TestTotalMetaboliteConcentration:
    """Class for testing total concentration of metabolites from module concentation of mibipret."""

    data = example_data(with_units = False,
                        data_type = 'metabolites')

    def test_total_metabolites_concentration_01(self):
        """Testing routine total_metabolites_concentration().

        Correct calculation of total amount of metabolites (total concentration).
        """
        tot_conc_test = 27046.0
        tot_conc = np.sum(total_metabolites_concentration(self.data))

        assert (tot_conc - tot_conc_test)<1e-5


    def test_total_metabolites_concentration_02(self):
        """Testing routine total_metabolites_concentration().

        Testing 'include' option adding calculated values as column to data.
        """
        data_test = self.data.copy()
        total_metabolites_concentration(data_test,include = True)

        assert data_test.shape[1] == self.data.shape[1]+1
        assert "metabolites_concentration" in data_test.columns


    def test_total_metabolites_concentration_03(self,capsys):
        """Testing routine total_metabolites_concentration().

        Testing verbose flag.
        """
        total_metabolites_concentration(self.data,verbose=True)
        out,err=capsys.readouterr()

        assert len(out)>0


class TestTotalCount:
    """Class for testing analysis module on NA screening of mibiscreen."""

    columns = ['sample_nr', 'sulfate', 'benzene']
    units = [' ','mg/L', 'ug/L']
    s01 = ['2000-001', 748, 263]
    s02 = ['2000-002', 548, ]

    data1 = pd.DataFrame([s01,s02],
                         columns = columns)

    data_nonstandard = pd.DataFrame([units,s01,s02],
                                    columns = columns)


    def test_total_count_01(self):
        """Testing routine total_count().

        Correct calculation of total count of contaminants with concentration > 0.
        """
        out = total_count(self.data1).values

        assert np.all(out == [2,1])

    def test_total_count_02(self):
        """Testing routine total_count().

        Correct calculation of total count of contaminants with concentration > specific threshold.
        """
        out = total_count(self.data1,threshold = 300).values

        assert np.all(out == [1,1])

    def test_total_count_03(self):
        """Testing routine total_count().

        Correct handling when no overlap of specified list of quantities
        with column names in data frame.
        """
        with pytest.raises(ValueError):
            total_count(self.data1,threshold = -1)


    def test_total_count_04(self):
        """Testing routine total_count().

        Testing inplace option adding calculated values as column to data.
        """
        data_test = self.data1.copy()
        total_count(data_test,name_list=['sulfate'],include_as = 'test').values

        assert data_test.shape[1] == self.data1.shape[1]+1 and \
                np.all(data_test['test'] == [1,1])

    def test_total_count_05(self):
        """Testing routine total_count().

        Correct handling when no overlap of specified list of quantities
        with column names in data frame.
        """
        with pytest.raises(ValueError):
            total_count(self.data1,name_list=['test1','test2'])

    def test_total_count_06(self):
        """Testing Error message that given data type not defined."""
        with pytest.raises(ValueError):
            total_count(self.data_nonstandard)

    def test_total_count_07(self,capsys):
        """Testing routine total_count().

        Testing verbose flag.
        """
        total_count(self.data1,verbose=True)
        out,err=capsys.readouterr()

        assert len(out)>0

class TestTotalContaminantCount:
    """Class for testing total concentration of contaminants from module concentation of mibipret."""

    data = example_data(with_units = False)

    def test_total_contaminant_count_01(self):
        """Testing routine total_contaminant_count().

        Correct calculation of total amount of contaminants (total concentration).
        """
        tot_conc = np.sum(total_contaminant_count(self.data))

        assert tot_conc == 78

    def test_total_contaminant_count_02(self):
        """Testing routine total_contaminant_concentration().

        Correct calculation of total amount of contaminants (total concentration)
        for BTEX.
        """
        tot_conc = np.sum(total_contaminant_count(self.data,contaminant_group='BTEX'))

        assert tot_conc == 20

    def test_total_contaminant_count_03(self):
        """Testing routine total_contaminant_concentration().

        Correct calculation of total amount of contaminants (total concentration)
        for BTEX.
        """
        tot_conc = np.sum(total_contaminant_count(self.data,contaminant_group='BTEXIIN'))

        assert tot_conc == 32

    def test_total_contaminant_count_04(self):
        """Testing routine total_contaminant_concentration().

        Correct handling when unknown group of contaminants are provided.
        """
        with pytest.raises(ValueError):
            total_contaminant_count(self.data,contaminant_group = 'test')

    def test_total_contaminant_count_05(self):
        """Testing routine total_contaminant_concentration().

        Testing 'include' option adding calculated values as column to data.
        """
        data_test = self.data.copy()
        total_contaminant_count(data_test,include = True)

        assert data_test.shape[1] == self.data.shape[1]+1 and 'count_contaminants' in data_test.columns


    def test_total_contaminant_count_06(self,capsys):
        """Testing routine total_contaminant_count().

        Testing verbose flag.
        """
        total_contaminant_count(self.data,verbose=True)
        out,err=capsys.readouterr()

        assert len(out)>0

class TestTotalMetaboliteCount:
    """Class for testing total concentration of metabolites from module concentation of mibipret."""

    data = example_data(with_units = False,
                        data_type = 'metabolites')

    def test_total_metabolites_count_01(self):
        """Testing routine total_metabolites_count().

        Correct calculation of total amount of metabolites (total concentration).
        """
        tot_conc = np.sum(total_metabolites_count(self.data))

        assert tot_conc == 9


    def test_total_metabolites_count_02(self):
        """Testing routine total_metabolites_count().

        Testing 'include' option adding calculated values as column to data.
        """
        data_test = self.data.copy()
        total_metabolites_count(data_test,include = True)

        assert data_test.shape[1] == self.data.shape[1]+1 and "metabolites_count" in data_test.columns


    def test_total_metabolites_count_03(self,capsys):
        """Testing routine total_metabolites_count().

        Testing verbose flag.
        """
        total_metabolites_count(self.data,verbose=True)
        out,err=capsys.readouterr()

        assert len(out)>0
