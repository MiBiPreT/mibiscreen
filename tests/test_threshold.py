#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""Testing analysis module on threshhold exceedance analysis of mibiscreen.

@author: Alraune Zech
"""

import numpy as np
import pandas as pd
import pytest
from mibiscreen.analysis.sample.intervention import thresholds_for_intervention_traffic
from mibiscreen.data.example_data.example_data import example_data


class TestThresholdsForIntervention:
    """Class for testing thresholds_for_intervention_traffic() from module concentation of mibipret."""

    data = example_data(with_units = False)

    columns = ['sample_nr', 'sulfate', 'benzene']
    units = [' ','mg/L', 'ug/L']
    s01 = ['2000-001', 748, 263]
    s02b = ['2000-002', 548, ]

    data_nonstandard = pd.DataFrame([units,s01,s02b],
                                    columns = columns)


    def test_thresholds_for_intervention_traffic_01(self):
        """Testing routine thresholds_for_intervention_traffic().

        Check that routine produced correct dataframe output.
        """
        na_intervention = thresholds_for_intervention_traffic(self.data)
        intervention_contaminants_cols = ['sample_nr', 'obs_well', 'depth', 'intervention_traffic',
               'intervention_number', 'intervention_contaminants']

        assert na_intervention.shape == (4,6)
        assert set(na_intervention.columns) == set(intervention_contaminants_cols)

    def test_thresholds_for_intervention_traffic_02(self):
        """Testing routine thresholds_for_intervention_traffic().

        Correct identification of list of contaminants exceeding
        intervention thresholds.
        """
        na_intervention = thresholds_for_intervention_traffic(self.data)
        intervention_contaminants_test = ['benzene', 'ethylbenzene', 'pm_xylene', 'o_xylene', 'indane', 'naphthalene']

        assert set(na_intervention['intervention_contaminants'].iloc[2]) == set(intervention_contaminants_test)

    def test_thresholds_for_intervention_traffic_03(self):
        """Testing routine thresholds_for_intervention_traffic().

        Correct identification of number of contaminants exceeding
        intervention thresholds.
        """
        na_intervention = thresholds_for_intervention_traffic(self.data)
        na_intervention_number_test = 21
        assert (np.sum(na_intervention['intervention_number'].iloc[2]) - na_intervention_number_test)< 1e-5

    def test_thresholds_for_intervention_traffic_04(self):
        """Testing routine thresholds_for_intervention_traffic().

        Correct evaluation of traffic light on intervention value.
        """
        na_intervention = thresholds_for_intervention_traffic(self.data)
        na_intervention_test = ['red','red','red','red']

        assert np.all(na_intervention['intervention_traffic'].values == na_intervention_test)

    def test_thresholds_for_intervention_traffic_05(self):
        """Testing routine thresholds_for_intervention_traffic().

        Correct handling when unknown group of contaminants are provided.
        """
        with pytest.raises(ValueError):
            thresholds_for_intervention_traffic(self.data,contaminant_group = 'test')

    def test_thresholds_for_intervention_traffic_06(self):
        """Testing routine thresholds_for_intervention_traffic().

        Testing Error message that data is not in standard format.
        """
        with pytest.raises(ValueError):
            thresholds_for_intervention_traffic(self.data_nonstandard)

    def test_thresholds_for_intervention_traffic_07(self,capsys):
        """Testing routine thresholds_for_intervention_traffic().

        Testing Warning that some contaminant concentrations are missing.
        """
        data_test = self.data.drop(labels = 'benzene',axis = 1)
        thresholds_for_intervention_traffic(data_test,verbose = False, contaminant_group='BTEX')
        out,err=capsys.readouterr()
        assert len(out)>0

    def test_thresholds_for_intervention_traffic_08(self):
        """Testing routine thresholds_for_intervention_traffic().

        Testing inplace option adding calculated values as column to data.
        """
        data_test = self.data.copy()
        thresholds_for_intervention_traffic(data_test,include = True)
        assert data_test.shape[1] == self.data.shape[1]+3

    def test_thresholds_for_intervention_traffic_09(self,capsys):
        """Testing routine thresholds_for_intervention_traffic().

        Testing verbose flag.
        """
        thresholds_for_intervention_traffic(self.data,verbose=True)
        out,err=capsys.readouterr()

        assert len(out)>0
