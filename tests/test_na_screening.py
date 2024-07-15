#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Testing analysis module on NA screening of mibipret.

@author: Alraune Zech
"""

import numpy as np
import pandas as pd
import pytest
from mibipret.analysis.sample.screening_NA import NA_traffic
from mibipret.analysis.sample.screening_NA import available_NP
from mibipret.analysis.sample.screening_NA import check_data
from mibipret.analysis.sample.screening_NA import electron_balance
from mibipret.analysis.sample.screening_NA import oxidators
from mibipret.analysis.sample.screening_NA import reductors
from mibipret.analysis.sample.screening_NA import screening_NA
from mibipret.analysis.sample.screening_NA import thresholds_for_intervention
from mibipret.analysis.sample.screening_NA import total_contaminant_concentration
from mibipret.data.data import example_data  #, check_values

#path_data = "./mibipret/d"

class TestNA:
    """Class for testing analysis module on NA screening of mibipret."""

    # data, units = standardize(example_data(),verbose = False)
    data = example_data(with_units = False,standardize=True)
    cols = data.columns.to_list()
    data_empty = pd.Series(
                        data = np.arange(4),
                        name = 'empyt_data',
                        dtype=float)

    columns = ['sample_nr', 'sulfate', 'benzene']
    units = [' ','mg/L', 'ug/L']
    s01 = ['2000-001', 748, 263]
    s02 = ['2000-002', 548, ]
    data_nonstandard = pd.DataFrame([units,s01,s02],
                                columns = columns)


    tot_oxi = pd.Series(data = [1.5663,3.70051, 3.00658, 2.09641], name = 'total_oxidators')
    tot_reduct = pd.Series(data = [11.819184,0.525160, 0.347116, 15.265349], name = 'total_reductors')
    e_bal = pd.Series(data = [7.546422, 0.141929, 0.115486, 7.283465], name = 'e_balance')

    data_na = pd.concat([tot_reduct, tot_oxi,e_bal],axis =1)

    def test_check_data_01(self):
        """Testing routine check_data().

        Correct identification of data as dataframe returning list of column names
        """
        cols_check = check_data(self.data)

        assert np.all(self.cols == cols_check)

    def test_check_data_02(self):
        """Testing routine check_data().

        Correct identification of data as pd.Series returning list of column names
        """
        cols_check = check_data(self.data.iloc[:,0])

        assert len(cols_check) == 1

    def test_check_data_03(self):
        """Testing routine check_data().

        Check that routine returns Error when data is not provided as dataframe.
        """
        with pytest.raises(ValueError):
            # available_NP(test_data)
            available_NP(self.cols)

    def test_reductors_01(self):
        """Testing routine reductors().

        Correct calculation of total amount of reductors.
        """
        tot_reduct_test = 27.956808208823354
        tot_reduct = np.sum(reductors(self.data))

        assert (tot_reduct - tot_reduct_test)<1e-5
        # assert np.sum(tot_reduct.values - tot_reduct_example_data.values)<1e-5

    def test_reductors_02(self):
        """Testing routine reductors().

        Correct handling when no EA data is provided.
        """
        tot_reduct = reductors(self.data_empty)
        assert tot_reduct is False

    def test_reductors_03(self):
        """Testing routine reductors().

        Correct handling when unknown group of EA are provided.
        """
        tot_reduct = reductors(self.data,ea_group = 'test')
        assert tot_reduct is False

    def test_reductors_04(self):
        """Testing Error message that given data type not defined."""
        with pytest.raises(ValueError):  #, match = "Data not in standardized format. Run 'standardize()' first."):
            reductors(self.data_nonstandard)

    def test_reductors_05(self,capsys):
        """Testing routine reductors().

        Testing verbose flag.
        """
        reductors(self.data,verbose=True)
        out,err=capsys.readouterr()

        assert len(out)>0

    def test_oxidators_01(self):
        """Testing routine oxidators().

        Correct calculation of total amount of oxidators for standard contaminant
        group BTEXIIN.
        """
        tot_oxi_test = 10.369793079245106
        tot_oxi = np.sum(oxidators(self.data))

        assert (tot_oxi - tot_oxi_test)<1e-5

    def test_oxidators_02(self):
        """Testing routine oxidators().

        Correct calculation of total amount of oxidators for BTEX.
        """
        tot_oxi_test = 3.5295281756799395
        tot_oxi = np.sum(oxidators(self.data,contaminant_group='BTEX'))

        assert (tot_oxi - tot_oxi_test)<1e-5

    def test_oxidators_03(self):
        """Testing routine oxidators().

        Correct calculation of total amount of oxidators with option to
        include available nutrients.
        """
        tot_oxi_test = 6.669283330069978
        tot_oxi = np.sum(oxidators(self.data,nutrient = True))

        assert (tot_oxi - tot_oxi_test)<1e-5


    def test_oxidators_04(self):
        """Testing routine oxidators().

        Correct handling when no contaminant data is provided.
        """
        tot_oxi = oxidators(self.data_empty)
        assert tot_oxi is False

    def test_oxidators_05(self):
        """Testing Error message that given data type not defined."""
        with pytest.raises(ValueError):  #, match = "Data not in standardized format. Run 'standardize()' first."):
            oxidators(self.data_nonstandard)

    def test_oxidators_06(self):
        """Testing routine oxidators().

        Correct handling when unknown group of contaminants are provided.
        """
        tot_oxi = oxidators(self.data,contaminant_group = 'test')
        assert tot_oxi is False

    def test_oxidators_07(self,capsys):
        """Testing routine oxidators().

        Testing verbose flag.
        """
        oxidators(self.data,verbose=True)
        out,err=capsys.readouterr()

        assert len(out)>0

    def test_available_NP_01(self):
        """Testing routine available_NP().

        Correct calculation of total amount of nutrients.
        """
        NP_avail_test = 92.56
        NP_avail = np.sum(available_NP(self.data,nutrient = True))

        assert (NP_avail - NP_avail_test)<1e-5

    def test_available_NP_02(self):
        """Testing routine available_NP().

        Check that routine returns Error when nutrient data is not provided.
        """
        with pytest.raises(ValueError):
            # available_NP(test_data)
            available_NP(self.data_empty)

    def test_available_NP_03(self,capsys):
        """Testing routine available_NP().

        Testing verbose flag.
        """
        available_NP(self.data,verbose=True)
        out,err=capsys.readouterr()

        assert len(out)>0

    def test_electron_balance_01(self):
        """Testing routine electron_balance().

        Correct calculation of electron balance from data not containing
        amounts of reductors and oxidators (have to be calculated first).
        """
        e_bal_test = 15.087302683658793
        e_bal = np.sum(electron_balance(self.data))

        assert (e_bal - e_bal_test)<1e-5

    def test_electron_balance_02(self):
        """Testing routine electron_balance().

        Correct calculation of total amount of electron balance from
        dataframe containing amounts of reductors and oxidators.
        """
        e_bal_test = 15.087302683658793
        e_bal = np.sum(electron_balance(self.data_na))

        assert (e_bal - e_bal_test)<1e-5

    def test_electron_balance_03(self,capsys):
        """Testing routine electron_balance().

        Testing verbose flag.
        """
        electron_balance(self.data,verbose=True)
        out,err=capsys.readouterr()

        assert len(out)>0

    def test_NA_traffic_01(self):
        """Testing routine NA_traffic().

        Correct calculation of NA traffic light based on electron balance.
        When data does not contain electron balance (has to be calculated
        from reductors and oxidators).
        """
        na_traffic_test = ['green','red','red','green']
        na_traffic = NA_traffic(self.data)

        assert np.all(na_traffic.values == na_traffic_test)

    def test_NA_traffic_02(self):
        """Testing routine NA_traffic().

        Correct calculation of NA traffic light based on electron balance when
        dataframe contains values of electron_balance.
        """
        na_traffic_test = ['green','red','red','green']
        na_traffic = NA_traffic(self.data_na)

        assert np.all(na_traffic.values == na_traffic_test)

    def test_NA_traffic_03(self,capsys):
        """Testing routine NA_traffic().

        Testing verbose flag.
        """
        NA_traffic(self.data,verbose=True)
        out,err=capsys.readouterr()

        assert len(out)>0

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

        Correct handling when unknown group of contaminants are provided.
        """
        tot_conc = total_contaminant_concentration(self.data,contaminant_group = 'test')
        assert tot_conc is False

    def test_total_contaminant_concentration_04(self):
        """Testing Error message that given data type not defined."""
        with pytest.raises(ValueError):  #, match = "Data not in standardized format. Run 'standardize()' first."):
            total_contaminant_concentration(self.data_nonstandard)

    def test_total_contaminant_concentration_05(self):
        """Testing routine total_contaminant_concentration().

        Correct handling when no data is provided.
        """
        tot_conc = total_contaminant_concentration(self.data_empty)
        assert tot_conc is False

    def test_total_contaminant_concentration_06(self,capsys):
        """Testing routine total_contaminant_concentration().

        Testing verbose flag.
        """
        total_contaminant_concentration(self.data,verbose=True)
        out,err=capsys.readouterr()

        assert len(out)>0

    def test_thresholds_for_intervention_01(self):
        """Testing routine thresholds_for_intervention().

        Check that routine produced correct dataframe output.
        """
        na_intervention = thresholds_for_intervention(self.data)

        assert na_intervention.shape == (4,5)

    def test_thresholds_for_intervention_02(self):
        """Testing routine thresholds_for_intervention().

        Correct identification of list of contaminants exceeding
        intervention thresholds.
        """
        na_intervention = thresholds_for_intervention(self.data)
        intervention_contaminants_test = ['benzene', 'ethylbenzene', 'pm_xylene', 'o_xylene', 'indane', 'naphthalene']

        assert np.all(na_intervention['intervention_contaminants'].iloc[2] == intervention_contaminants_test)

    def test_thresholds_for_intervention_03(self):
        """Testing routine thresholds_for_intervention().

        Correct identification of number of contaminants exceeding
        intervention thresholds.
        """
        na_intervention = thresholds_for_intervention(self.data)
        na_intervention_number_test = 21
        assert (np.sum(na_intervention['intervention_number'].iloc[2]) - na_intervention_number_test)< 1e-5

    def test_thresholds_for_intervention_04(self):
        """Testing routine thresholds_for_intervention().

        Correct evaluation of traffic light on intervention value.
        """
        na_intervention = thresholds_for_intervention(self.data)
        na_intervention_test = ['red','red','red','red']

        assert np.all(na_intervention['intervention_traffic'].values == na_intervention_test)

    def test_thresholds_for_intervention_05(self):
        """Testing routine thresholds_for_intervention().

        Correct handling when unknown group of contaminants are provided.
        """
        na_intervention = thresholds_for_intervention(self.data,contaminant_group = 'test')
        assert na_intervention is False

    def test_thresholds_for_intervention_06(self):
        """Testing Error message that given data type not defined."""
        with pytest.raises(ValueError):  #, match = "Data not in standardized format. Run 'standardize()' first."):
            thresholds_for_intervention(self.data_nonstandard)

    def test_thresholds_for_intervention_07(self,capsys):
        """Testing routine thresholds_for_intervention().

        Testing verbose flag.
        """
        thresholds_for_intervention(self.data,verbose=True)
        out,err=capsys.readouterr()

        assert len(out)>0

    def test_screening_NA_01(self):
        """Testing routine screening_NA().

        Correct calculation of total amount of reductors.
        """
        na_data = screening_NA(self.data)

        assert na_data.shape == (4,10)

    def test_screening_NA_02(self):
        """Testing routine screening_NA().

        Correct calculation of total amount of reductors.
        """
        na_data = screening_NA(self.data,nutrient=True)

        assert na_data.shape == (4,11)

    def test_screening_NA_03(self,capsys):
        """Testing routine screening_NA().

        Testing verbose flag.
        """
        screening_NA(self.data,verbose=True)
        out,err=capsys.readouterr()

        assert len(out)>0
