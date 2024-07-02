#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Testing analysis module on NA screening of mibipret.

@author: Alraune Zech
"""

import numpy as np
import pandas as pd
from mibipret.analysis.sample.screening_NA import reductors
from mibipret.data.data import example_data  #, check_values

#path_data = "./mibipret/d"

class TestNA:
    """Class for testing analysis module on NA screening of mibipret."""

    data = example_data()
    data = data.drop(0)

    # tot_reduct_example_data = pd.Series(
    #     data = [1.942974,0.009434, 0.092681, 0.749220],
    #     name = 'total_reductors',
    #     dtype=float)

    def test_reductors_01(self):
        """Testing correct calculation of total amount of reductors."""
        tot_reduct_test = np.array([1.942974,0.009434, 0.092681, 0.749220])
        tot_reduct = reductors(self.data)

        assert np.sum(tot_reduct.values - tot_reduct_test)<1e-5
        # assert np.sum(tot_reduct.values - tot_reduct_example_data.values)<1e-5

    def test_reductors_02(self):
        """Testing correct calculation of total amount of reductors."""
        data_empty = pd.Series(
                        data = np.arange(4),
                        name = 'empyt_data',
                        dtype=float)
        tot_reduct = reductors(data_empty)
        assert tot_reduct is False
