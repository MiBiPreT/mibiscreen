"""Documentation about mibiscreen."""

__author__ = "Alraune Zech"
__email__ = "a.zech@uu.nl"
__version__ = "0.6.0"

# Add some commonly used functions as top-level imports
from mibiscreen.data.load_data import load_excel, load_csv
from mibiscreen.data.check_data import (
    standardize,
    standard_names,
    check_columns,
    check_units,
    check_values
)
from mibiscreen.data.set_data import  (
    determine_quantities,
    merge_data,
    extract_data
)
from mibiscreen.analysis.reduction.stable_isotope_regression import Lambda_regression
from mibiscreen.analysis.reduction.stable_isotope_regression import extract_isotope_data
from mibiscreen.analysis.reduction.transformation import filter_values, transform_values
from mibiscreen.analysis.reduction.ordination import (
    pca,
    cca,
    rda,
)
from mibiscreen.analysis.sample.screening_NA import (
    reductors,
    oxidators,
    electron_balance,
    sample_NA_traffic,
    sample_NA_screening
)
from mibiscreen.analysis.sample.concentrations import (
    total_concentration,
    total_contaminant_concentration,
    total_metabolites_concentration,
    total_count,
    total_contaminant_count,
    total_metabolites_count,
)
from mibiscreen.analysis.sample.intervention import (
    thresholds_for_intervention_traffic,
    thresholds_for_intervention_ratio,
)

from mibiscreen.visualize.stable_isotope_plots import (
    Lambda_plot,
    Rayleigh_fractionation_plot,
    Keeling_plot,
)
from mibiscreen.visualize.screening_plots import (
    contaminants_bar,
    electron_balance_bar_data_prep,
    electron_balance_bar,
    threshold_ratio_bar,
    activity_data_prep,
    activity_plot,
)

from mibiscreen.visualize.ordination_plots import ordination_plot
