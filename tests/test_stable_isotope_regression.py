#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Testing analysis module on isotope regression of mibiscreen.

@author: Alraune Zech
"""

import numpy as np
import pytest
from mibiscreen.analysis.reduction.stable_isotope_regression import Keeling_regression
from mibiscreen.analysis.reduction.stable_isotope_regression import Lambda_regression
from mibiscreen.analysis.reduction.stable_isotope_regression import Rayleigh_fractionation
from mibiscreen.analysis.reduction.stable_isotope_regression import extract_isotope_data
from mibiscreen.analysis.reduction.stable_isotope_regression import valid_indices
from mibiscreen.data.example_data.example_data import example_data


class TestData:
    """Class for testing data module of mibiscreen."""

    delta_13C_01 = np.array([-26.5, -26.2, -25.2, -25.7])
    delta_2H_01 = np.array([-77., -75., -51., -61.])

    concentration_01 = np.linspace(2, 0.6,9)
    delta_01 = 0.001*np.linspace(9, 30,9)
    concentration_02 = np.array([0.05,0.075,0.11,0.13,0.15,0.04,0.04])
    delta_02 = np.array([35.,20.,10.,7.,5.,25.,35.])

    data = example_data(with_units = False)

    ### ---------------------------------------------------------------------------

    def test_Lambda_regression_01(self):
        """Testing routine Lambda_regression().

        Correct linear regression of provided data
        """
        results = Lambda_regression(self.delta_13C_01,
                                    self.delta_2H_01,
                                    validate_indices = False,
                                    )
        ceoff_fit = np.array([ 21.2244898 , 483.71428571])
        assert isinstance(results, dict) and np.all(np.abs(results['coefficients'] - ceoff_fit) <1e-5)

    def test_Lambda_regression_02(self):
        """Testing routine Lambda_regression().

        Correct linear regression of provided data with keyword validate_indices
        """
        delta_13C = np.array([np.nan, -26.2, -25.2, -25.7])

        results = Lambda_regression(delta_13C,
                                    self.delta_2H_01,
                                    validate_indices = True,
                                    )

        assert np.abs(results['coefficients'][0] - 24) <1e-5

    def test_Lambda_regression_03(self,capsys):
        """Testing routine Lambda_regression().

        Testing verbose flag.
        """
        Lambda_regression(self.delta_13C_01,
                                    self.delta_2H_01,
                                    validate_indices = False,
                                    verbose = True,
                                    )
        out,err=capsys.readouterr()

        assert len(out)>0

    def test_Rayleigh_fractionation_01(self):
        """Testing routine Rayleigh_fractionation().

        Correct linear regression of provided data
        """
        results = Rayleigh_fractionation(self.concentration_01,
                                         self.delta_01,
                                         validate_indices = False,
                                         )

        assert isinstance(results, dict) and np.abs(results['coefficients'][0] + 0.0174713) <1e-5

    def test_Rayleigh_fractionation_02(self):
        """Testing routine Rayleigh_fractionation().

        Correct linear regression of provided data with keyword validate_indices
        """
        delta = np.copy(self.delta_01)
        delta[:-4] = np.nan
        results = Rayleigh_fractionation(self.concentration_01,
                                         delta,
                                         )

        assert np.abs(results['coefficients'][0] + 0.01245475) <1e-5

    def test_Rayleigh_fractionation_03(self):
        """Testing routine Rayleigh_fractionation().

        Correct linear regression of provided data with keyword validate_indices
        """
        with pytest.raises(ValueError):
            Rayleigh_fractionation(-self.concentration_01,self.delta_01)

    def test_Rayleigh_fractionation_04(self,capsys):
        """Testing routine Rayleigh_fractionation().

        Testing verbose flag.
        """
        Rayleigh_fractionation(self.concentration_01,
                                 self.delta_01,
                                 validate_indices = False,
                                 verbose = True,
                                 )
        out,err=capsys.readouterr()

        assert len(out)>0

    def test_Keeling_regression_01(self):
        """Testing routine Keeling_regression().

        Correct linear regression of provided data
        """
        results = Keeling_regression(self.concentration_02,
                                     self.delta_02,
                                     validate_indices = False,
                                     )

        assert isinstance(results, dict) and np.abs(results['coefficients'][1] +2.40843306 ) <1e-5

    def test_Keeling_regression_02(self):
        """Testing routine Keeling_regression().

        Correct linear regression of provided data with keyword validate_indices
        """
        delta = np.copy(self.delta_02)
        delta[-1] = np.nan
        results = Keeling_regression(self.concentration_02,
                                     delta,
                                     )

        assert np.abs(results['coefficients'][1] + 1.85592) <1e-5

    def test_Keeling_regression_03(self):
        """Testing routine Keeling_regression().

        Correct linear regression of provided data with relative_abundance
        instead of delta value
        """
        delta = np.copy(self.delta_02)
        delta[-1] = np.nan
        results = Keeling_regression(self.concentration_02,
                                     relative_abundance = self.delta_02,
                                     )

        assert np.abs(results['coefficients'][1] +2.40843306 ) <1e-5

    def test_Keeling_regression_04(self):
        """Testing routine Keeling_regression().

        Check on error handling when not sufficient data is provided.
        """
        with pytest.raises(ValueError):
            Keeling_regression(self.concentration_01)

    def test_Keeling_regression_05(self,capsys):
        """Testing routine Keeling_regression().

        Testing verbose flag.
        """
        Keeling_regression(self.concentration_02,
                           self.delta_02,
                           validate_indices = False,
                           verbose = True,
                           )
        out,err=capsys.readouterr()

        assert len(out)>0

    def test_valid_indices_01(self):
        """Testing routine valid_indices().

        Correct identification of valid indices in both arrays
        """
        data1 , data2 = valid_indices(self.delta_13C_01,self.delta_2H_01)
        assert np.all(data1 == self.delta_13C_01) and np.all(data2 == self.delta_2H_01)

    def test_valid_indices_02(self):
        """Testing routine valid_indices().

        Correct identification of valid indices in both arrays - filtering out nan values
        """
        delta_13C = np.array([np.nan, -26.2, -25.2, -25.7])


        data1 , data2 = valid_indices(delta_13C,self.delta_2H_01)
        assert np.all(data1 == delta_13C[1:]) and np.all(data2 == self.delta_2H_01[1:])

    def test_valid_indices_03(self):
        """Testing routine valid_indices().

        Correct identification of valid indices in both arrays - filtering out infinity values
        """
        delta_13C = np.array([26.5, -26.2, -25.2,np.inf])


        data1 , data2 = valid_indices(delta_13C,self.delta_2H_01)
        assert np.all(data1 == delta_13C[:-1]) and np.all(data2 == self.delta_2H_01[:-1])

    def test_valid_indices_04(self):
        """Testing routine valid_indices().

        Correct identification of valid indices in both arrays - filtering out zero values
        """
        delta_13C = np.array([26.5, -26.2, -25.2,0])


        data1 , data2 = valid_indices(delta_13C,self.delta_2H_01,remove_zero=True)
        assert np.all(data1 == delta_13C[:-1]) and np.all(data2 == self.delta_2H_01[:-1])

    def test_valid_indices_05(self):
        """Testing routine valid_indices().

        Correct error message when data is not the same length
        """
        with pytest.raises(ValueError):
            valid_indices(self.delta_13C_01,self.delta_2H_01[:-1])

    def test_extract_isotope_data_01(self):
        """Testing routine extract_isotope_data().

        Test proper functionality
        """
        delta_C , delta_H = extract_isotope_data(self.data,'benzene')

        assert np.all(delta_C == self.data['delta_13C-benzene'].values) and \
            np.all(delta_H == self.data['delta_2H-benzene'].values)

    def test_extract_isotope_data_02(self):
        """Testing routine extract_isotope_data().

        Correct error message when data of unknown contaminant is requested
        """
        with pytest.raises(ValueError):
            extract_isotope_data(self.data,'test')

    def test_extract_isotope_data_03(self):
        """Testing routine extract_isotope_data().

        Correct error message when name of isotope is unknown
        """
        with pytest.raises(ValueError):
            extract_isotope_data(self.data,'benzene',name_13C = 'd13C')

    def test_extract_isotope_data_04(self):
        """Testing routine extract_isotope_data().

        Correct error message when name of isotope is unknown
        """
        with pytest.raises(ValueError):
            extract_isotope_data(self.data,'benzene',name_2H = 'd2H')

    def test_extract_isotope_data_05(self):
        """Testing routine extract_isotope_data().

        Correct error message when data is not available.
        """
        with pytest.raises(ValueError):
            extract_isotope_data(self.data,'toluene')

