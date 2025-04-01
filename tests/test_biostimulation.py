#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Testing analysis module on biostimulation analysis of mibiscreen.

@author: Alraune Zech
"""

import numpy as np
import pandas as pd
import pytest
from mibiscreen.analysis.sample.biostimulation import available_NP
from mibiscreen.data.example_data import example_data


class TestAvailableNP:
    """Class for testing available_NP analysis module on NA screening of mibipret."""

    data = example_data(with_units = False)
    data_empty = pd.Series(
                        data = np.arange(4),
                        name = 'empyt_data',
                        dtype=float)

    def test_available_NP_01(self):
        """Testing routine available_NP().

        Correct calculation of total amount of nutrients.
        """
        NP_avail_test = 92.56
        NP_avail = np.sum(available_NP(self.data))

        assert (NP_avail - NP_avail_test)<1e-5

    def test_available_NP_02(self):
        """Testing routine available_NP().

        Check that routine returns Error when nutrient data is not provided.
        """
        with pytest.raises(ValueError):
            available_NP(self.data_empty)

    def test_available_NP_03(self):
        """Testing routine available_NP().

        Testing inplace option adding calculated values as column to data.
        """
        data_test = self.data.copy()
        available_NP(data_test,include = True)
        assert data_test.shape[1] == self.data.shape[1]+1

    def test_available_NP_04(self,capsys):
        """Testing routine available_NP().

        Testing verbose flag.
        """
        available_NP(self.data,verbose=True)
        out,err=capsys.readouterr()

        assert len(out)>0
