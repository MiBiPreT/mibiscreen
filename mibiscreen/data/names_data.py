"""Name specifications of data!

File containing name specifications of quantities and parameters measured in
groundwater samples useful for biodegredation and bioremediation analysis

@author: A. Zech
"""

import mibiscreen.data.settings.standard_names as names
from mibiscreen.data.settings.sample_settings import properties_sample_settings
from mibiscreen.data.settings.contaminants import properties_contaminants,contaminants_analysis
from mibiscreen.data.settings.environment import properties_geochemicals
from mibiscreen.data.settings.metabolites import properties_metabolites
from mibiscreen.data.settings.isotopes import properties_isotopes

def _generate_dict_other_names(name_dict,
                                selection = False):

    """Function creating dictionary for mapping alternative names.

    Args:
    -------
        name_dict: dict
            dictionary of dictionaries with properties for each quantity (e.g. contaminant)
            each quantity-subdictionary needs to have one key called 'other_names' 
            providing a list of other/alternative names of the quantities
        selectin: False or list
            if False, all keys in dictionary name_dict will be run through
            if a list: only keys which are also in list will be used

    Returns:
    -------
        other_names_dict: dictionary
            dictionary mapping alternative names to standard name

    """
    

    other_names_dict=dict()
    if selection is False:
        name_list = list(name_dict.keys())
    else:
        name_list = selection
    for key in name_list:
        for other_name in name_dict[key]['other_names']:
            other_names_dict[other_name] = key

    return other_names_dict

### -----------------------------------------------------------------------------
### List with all quantities of particular data type in standard names:
sample_settings = list(properties_sample_settings.keys())
contaminants = list(properties_contaminants.keys())
contaminants_analysis_quantities = list(contaminants_analysis.keys())
environment = list(properties_geochemicals.keys())
isotopes = list(properties_isotopes.keys())
metabolites = list(properties_metabolites.keys())

### -----------------------------------------------------------------------------
### combined dictionary of all properties
properties_all = {**properties_sample_settings,
                  **properties_geochemicals,
                  **properties_contaminants,
                  **properties_metabolites,
                  **properties_isotopes,
}

### -----------------------------------------------------------------------------
### dictionaries for mapping possible name to standard name for quantities of particular type

other_names_sample_settings = _generate_dict_other_names(properties_sample_settings)
other_names_contaminants = _generate_dict_other_names(properties_contaminants)
other_names_environment = _generate_dict_other_names(properties_geochemicals)
#               selection = environment['environmental_conditions']+environment['geochemicals'])
other_names_metabolites = _generate_dict_other_names(properties_metabolites)
other_names_isotopes = _generate_dict_other_names(properties_isotopes)
other_names_contaminants_analysis = _generate_dict_other_names(contaminants_analysis)

### -----------------------------------------------------------------------------
### Dictionary with all potentially identified names of quantities
other_names_all = {
        **other_names_sample_settings,
        **other_names_environment,
        **other_names_contaminants,
        **other_names_contaminants_analysis,
        **other_names_metabolites,
        **other_names_isotopes,
}

### -----------------------------------------------------------------------------
### dictionaries with specific selection lists of quantities of particular type

contaminant_groups = dict(
    BTEX = [names.name_benzene,
            names.name_toluene,
            names.name_ethylbenzene,
            names.name_pm_xylene,
            names.name_o_xylene,
            names.name_xylene],
    BTEXIIN = [names.name_benzene,
               names.name_toluene,
               names.name_ethylbenzene,
               names.name_pm_xylene,
               names.name_o_xylene,
               names.name_xylene,
               names.name_indane,
               names.name_indene,
               names.name_naphthalene],
    all_cont = list(properties_contaminants.keys())
)

environment_groups = dict(
    environmental_conditions = [names.name_redox,
                                names.name_pH,
                                names.name_EC,
                                names.name_pE,
                                ],
    geochemicals = [names.name_oxygen,
                            names.name_nitrate,
                            names.name_sulfate,
                            names.name_iron2,
                            names.name_iron3,
                            names.name_manganese2,
                            names.name_manganese4,
                            names.name_methane,
                            names.name_nitrite,
                            names.name_sulfide,
                            names.name_ammonium,
                            names.name_phosphate,
                            names.name_chloride,
                            names.name_bromide,
                            names.name_fluoride,
                            names.name_sodium,
                            names.name_magnesium,
                            names.name_potassium,
                            names.name_calcium,
                            names.name_acetate,
                            names.name_DOC,
                            names.name_NPOC,
                            names.name_TOC,
                            ],
    ONS = [names.name_oxygen,
           names.name_nitrate,
           names.name_sulfate
           ], # non reduced electron acceptors
    ONSFe = [names.name_oxygen,
             names.name_nitrate,
             names.name_sulfate,
             names.name_iron3,
             ], # selected electron acceptors
    all_ea = [names.name_oxygen,
              names.name_nitrate,
              names.name_sulfate,
              names.name_iron2,
              names.name_manganese2,
              names.name_methane], # all electron acceptors (unreduced/reduced form)
    NP = [names.name_nitrate,
          names.name_nitrite,
          names.name_phosphate], # nutrients
)
