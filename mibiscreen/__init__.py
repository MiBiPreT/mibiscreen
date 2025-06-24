"""Documentation about mibiscreen."""

__author__ = "Alraune Zech"
__email__ = "a.zech@uu.nl"
__version__ = "0.5.0"


# Add some commonly used functions as top-level imports
from mibiscreen.data.load_data import load_excel, load_csv
from mibiscreen.data.check_data import (
    standardize,
    standard_names,
    check_columns,
    check_units,
    check_values
)
from mibiscreen.data.set_data import merge_data, extract_data

from mibiscreen.analysis.reduction.stable_isotope_regression import Lambda_regression
from mibiscreen.analysis.reduction.stable_isotope_regression import extract_isotope_data
from mibiscreen.analysis.reduction.transformation import filter_values, transform_values
from mibiscreen.analysis.reduction.ordination import pca
from mibiscreen.analysis.sample.screening_NA import (
    reductors,
    oxidators,
    electron_balance,
    sample_NA_traffic,
    sample_NA_screening
)
from mibiscreen.analysis.sample.concentrations import (
    total_contaminant_concentration,
    thresholds_for_intervention
)

from mibiscreen.visualize.stable_isotope_plots import Lambda_plot
from mibiscreen.visualize.activity import activity
from mibiscreen.visualize.ordination_plot import ordination_plot
