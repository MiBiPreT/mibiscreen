"""Tests for the mibipret.analysis.reduction.ordination module.

@author: Alraune Zech
"""

import numpy as np

# import pandas as pd
import pytest
from mibipret.analysis.reduction.ordination import cca
from mibipret.analysis.reduction.ordination import check_data_frame
from mibipret.analysis.reduction.ordination import constrained_ordination
from mibipret.analysis.reduction.ordination import extract_variables
from mibipret.analysis.reduction.ordination import pca
from mibipret.analysis.reduction.ordination import rda
from mibipret.data.data import example_data


class TestOrdination:
    """Class for testing ordination module of mibipret."""

    data = example_data(with_units = False)
    cols = data.columns.to_list()
    environment_00 = ['oxygen','nitrate', 'Sulfate']
    environment_01 = ['nitrate', 'oxygen','sulfate']
    environment_02 = ['nitrate', 'oxygen','sulfate', 'ironII']

    species_01 = ['benzene', 'toluene']
    species_02 = ['benzene', 'toluene','naphthalene']
    # species_03 = ['benzene', 'toluene','benzoic_acid']
    species_03 = ['benzene', 'toluene','Phenol']


    # data_01 = example_data(data_type = 'set_env_cont',with_units = True)
    # data_02 = example_data(data_type = 'contaminants',with_units = True)
    # data_03 = example_data(data_type = 'setting',with_units = True)
    # data_04 = example_data(data_type = 'environment',with_units = True)
    # data_05 = example_data(data_type = 'metabolites',with_units = True)
    # data_05 = example_data(data_type = 'metabolites',with_units = True)
    # new_column = pd.Series(data = ['ug/L',27.0, 54.1, 38.8, 19.70], name = 'unknown_contaminant')

    def test_check_data_frame_01(self):
        """Testing routine check_data_frame().

        Correct identification of data as dataframe returning dataframe with
        modified indices (being sample names) and the list of column names
        """
        df, cols = check_data_frame(self.data)

        assert np.all(self.cols[1:] == cols)

    def test_check_data_frame_02(self):
        """Testing routine check_data_frame().

        Correct error message when data is not a pd.dataframe
        """
        with pytest.raises(ValueError):
            check_data_frame(self.data.iloc[:,3])

    def test_extract_variables_01(self):
        """Testing routine extract_variables().

        Correct identification overlap between the two provided lists
        """
        intersection = extract_variables(self.cols,self.environment_00)

        assert np.all(set(intersection) == set(self.environment_00[:-1]))

    def test_extract_variables_02(self,capsys):
        """Testing routine extract_variables().

        Testing Warning that not all variables in the variables list
        are detected in columns list
        """
        extract_variables(self.cols,self.environment_00)
        out,err=capsys.readouterr()

        assert len(out)>0

    def test_extract_variables_03(self):
        """Testing routine extract_variables().

        Correct error message when no overlap between list of variables
        and columns list
        """
        with pytest.raises(ValueError):
            extract_variables(self.cols,['Sulfate'])

    def test_extract_variables_04(self):
        """Testing routine extract_variables().

        Correct error message when argument 'variables' is not a list
        """
        with pytest.raises(ValueError):
            extract_variables(self.cols,np.array(self.environment_00))

    def test_constrained_ordination_01(self):
        """Testing routine constrained_ordination().

        Check that routine provides results dictionary with entries in correct
        shapes for standard ordination method 'cca'.
        """
        ordination_output = constrained_ordination(self.data,
                                                    independent_variables = self.environment_02,
                                                    dependent_variables = self.species_02,
                                                    )

        test = [ordination_output['method'] == 'cca',
                ordination_output['loadings_independent'].shape == (4,2),
                ordination_output['loadings_dependent'].shape == (3,2),
                ordination_output['scores'].shape == (4,2),
                len(ordination_output['names_independent']) == 4,
                len(ordination_output['names_dependent']) == 3,
                len(ordination_output['sample_index']) == 4
                ]

        assert np.all(test)

    def test_constrained_ordination_02(self):
        """Testing routine constrained_ordination().

        Check that routine provides results dictionary with entries in correct
        shapes for ordination method 'rda'.
        """
        ordination_output = constrained_ordination(self.data,
                                                   method =  'rda',
                                                    independent_variables = self.environment_02,
                                                    dependent_variables = self.species_02,
                                                    )

        test = [ordination_output['method'] == 'rda',
                ordination_output['loadings_independent'].shape == (4,2),
                ordination_output['loadings_dependent'].shape == (3,2),
                ordination_output['scores'].shape == (4,2),
                len(ordination_output['names_independent']) == 4,
                len(ordination_output['names_dependent']) == 3,
                len(ordination_output['sample_index']) == 4
                ]

        assert np.all(test)

    def test_constrained_ordination_03(self):
        """Testing routine constrained_ordination().

        Correct error message when number of samples is smaller then number
        of variables.
        """
        method = 'cca'
        data = self.data.drop(labels = 4).copy()
        with pytest.raises(ValueError,
            match="Ordination method {} not possible with more variables than samples.".format(method)):
            constrained_ordination(data,
                                   method = method,
                                   independent_variables = self.environment_02,
                                   dependent_variables = self.species_02,
                                   )

    def test_constrained_ordination_04(self):
        """Testing routine constrained_ordination().

        Correct error message when selected method is not implemented.
        """
        method = "test"
        with pytest.raises(ValueError,match="Ordination method {} not a valid option.".format(method)):
            constrained_ordination(self.data,
                                   method = method,
                                   independent_variables = self.environment_02,
                                   dependent_variables = self.species_02,
                                   )

    def test_constrained_ordination_05(self):
        """Testing routine constrained_ordination().

        Correct error message when number of dependent variables is too small.
        """
        with pytest.raises(ValueError,match="Number of dependent variables too small."):
            constrained_ordination(self.data,
                                   independent_variables = self.environment_02,
                                   dependent_variables = self.species_01,
                                   )

    def test_constrained_ordination_06(self):
        """Testing routine constrained_ordination().

        Correct error message when data is not in normalized form/i.e.
        values in data-frame columns are not numerics.
        """
        with pytest.raises(TypeError,
           match="Not all column values are numeric values. Consider standardizing data first."):
            constrained_ordination(self.data,
                                   independent_variables = self.environment_02,
                                   dependent_variables = self.species_03,
                                   )

    def test_rda_01(self):
        """Testing routine rda().

        Check that routine provides results dictionary with entries in correct
        shapes.
        """
        ordination_output = rda(self.data,
                                independent_variables = self.environment_02,
                                dependent_variables = self.species_02,
                                )

        test = [ordination_output['method'] == 'rda',
                ordination_output['loadings_independent'].shape == (4,2),
                ordination_output['loadings_dependent'].shape == (3,2),
                ordination_output['scores'].shape == (4,2),
                len(ordination_output['names_independent']) == 4,
                len(ordination_output['names_dependent']) == 3,
                len(ordination_output['sample_index']) == 4
                ]

        assert np.all(test)

    def test_rda_02(self,capsys):
        """Testing routine rda().

        Testing verbose flag.
        """
        rda(self.data,
            independent_variables = self.environment_02,
            dependent_variables = self.species_02,
            verbose = True,
            )
        out,err=capsys.readouterr()

        assert len(out)>0

    def test_cca_01(self):
        """Testing routine cca().

        Check that routine provides results dictionary with entries in correct
        shapes.
        """
        ordination_output = cca(self.data,
                                independent_variables = self.environment_02,
                                dependent_variables = self.species_02,
                                )

        test = [ordination_output['method'] == 'cca',
                ordination_output['loadings_independent'].shape == (4,2),
                ordination_output['loadings_dependent'].shape == (3,2),
                ordination_output['scores'].shape == (4,2),
                len(ordination_output['names_independent']) == 4,
                len(ordination_output['names_dependent']) == 3,
                len(ordination_output['sample_index']) == 4
                ]

        assert np.all(test)

    def test_cca_02(self,capsys):
        """Testing routine cca().

        Testing verbose flag.
        """
        cca(self.data,
            independent_variables = self.environment_02,
            dependent_variables = self.species_02,
            verbose = True,
            )
        out,err=capsys.readouterr()

        assert len(out)>0

    def test_pca_01(self):
        """Testing routine pca().

        Check that routine provides results dictionary with entries in correct
        shapes.
        """
        ordination_output = pca(self.data,
                                independent_variables = self.environment_01,
                                )

        test = [ordination_output['method'] == 'pca',
                ordination_output['loadings_independent'].shape == (3,2),
                ordination_output['loadings_dependent'].shape == (0,2),
                ordination_output['scores'].shape == (4,2),
                len(ordination_output['names_independent']) == 3,
                len(ordination_output['names_dependent']) == 0,
                len(ordination_output['sample_index']) == 4,
                len(ordination_output['percent_explained']) == 3,
                ordination_output['corr_PC1_PC2'] < 1e16,
                ]

        assert np.all(test)

    def test_pca_02(self):
        """Testing routine pca().

        Check that routine provides results dictionary with entries in correct
        shapes.
        """
        ordination_output = pca(self.data,
                                dependent_variables = self.environment_01,
                                )

        test = [ordination_output['method'] == 'pca',
                ordination_output['loadings_independent'].shape == (0,2),
                ordination_output['loadings_dependent'].shape == (3,2),
                ordination_output['scores'].shape == (4,2),
                len(ordination_output['names_independent']) == 0,
                len(ordination_output['names_dependent']) == 3,
                len(ordination_output['sample_index']) == 4,
                len(ordination_output['percent_explained']) == 3,
                ordination_output['corr_PC1_PC2'] < 1e16,
                ]

        assert np.all(test)

    def test_pca_03(self):
        """Testing routine pca().

        Check that routine provides results dictionary with entries in correct
        shapes.
        """
        ordination_output = pca(self.data,
                                independent_variables = self.environment_00,
                                dependent_variables = self.species_01
                                )

        test = [ordination_output['method'] == 'pca',
                ordination_output['loadings_independent'].shape == (2,2),
                ordination_output['loadings_dependent'].shape == (2,2),
                ordination_output['scores'].shape == (4,2),
                len(ordination_output['names_independent']) == 2,
                len(ordination_output['names_dependent']) == 2,
                len(ordination_output['sample_index']) == 4,
                len(ordination_output['percent_explained']) == 4,
                ordination_output['corr_PC1_PC2'] < 1e15,
                ]

        assert np.all(test)

    def test_pca_04(self):
        """Testing routine pca().

        Correct error message when number of samples is smaller then number
        of variables.
        """
        with pytest.raises(ValueError,match="PCA not possible with more variables than samples."):
            pca(self.data)

    def test_pca_05(self):
        """Testing routine pca().

        Correct error message when data is not in normalized form/i.e.
        values in data-frame columns are not numerics.
        """
        with pytest.raises(TypeError):
            pca(self.data,
                independent_variables = self.species_03,
                )

    def test_pca_06(self,capsys):
        """Testing routine pca().

        Testing verbose flag.
        """
        pca(self.data,
            independent_variables = self.environment_02,
            verbose = True,
            )

        out,err=capsys.readouterr()

        assert len(out)>0
