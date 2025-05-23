"""Name specifications of data!

File containing name specifications of quantities and parameters measured in
groundwater samples useful for biodegredation and bioremediation analysis

@author: A. Zech
"""
import mibiscreen.data.settings.standard_names as names

### Todo: adapt routine for running through list of names as dictionary keys
### use that to generate name dictionary for environmental settings

def _generate_dict_other_names(name_dict,
                               selection = False):

    """Function creating dictionary for mapping alternative names.

    Args:
    -------
        name_dict: dict
            dictionary of dictionaries with properties for each quantity (e.g. contaminant)
            each quantity-subdictionary needs to have one key called 'other_names' 
            providing a list of other/alternative names of the quantities

    Returns:
    -------
        other_names_dict: dictionary
            dictionary mapping alternative names to standard name

    """
    

    other_names_dict=dict()
    # if selection is False:
    #     name_list = name_dict.items()
    for key, value in name_dict.items():
        print(f"{key}: ")
        # print(value['other_names'])
        for other_name in value['other_names']:
            other_names_dict[other_name] = key

    return other_names_dict

from mibiscreen.data.settings.sample_settings import properties_sample_settings
from mibiscreen.data.settings.contaminants import properties_contaminants
# from mibiscreen.data.settings.geochemicals import properties_geochemicals,geochemicals
from mibiscreen.data.settings.metabolites import properties_metabolites
from mibiscreen.data.settings.isotopes import properties_isotopes

names_sample_settings = _generate_dict_other_names(properties_sample_settings)
names_contaminants = _generate_dict_other_names(properties_contaminants)
names_metabolites = _generate_dict_other_names(properties_metabolites)
names_isotopes = _generate_dict_other_names(properties_isotopes)

# names_chemicals = _generate_dict_other_names(properties_geochemicals)
# names_environment = _generate_dict_other_names(properties_geochemicals,selection = geochemicals['environmental_conditions'])

### -----------------------------------------------------------------------------
### Dictionary with potential names of quantities to be replaced by standard name

names_environment = {
    "redox": names.name_redox,
    "redoxpotential": names.name_redox,
    "redox potential": names.name_redox,
    "redox-potential": names.name_redox,
    "redox_potential": names.name_redox,
    "redoxpot": names.name_redox,
    "redox pot": names.name_redox,
    "redox-pot": names.name_redox,
    "redox_pot": names.name_redox,
    "ph": names.name_pH,
    "ec": names.name_EC,
    "pe": names.name_pE,
    "nopc": names.name_NOPC,
    "doc": names.name_DOC,
}

names_chemicals = {
    "oxygen": names.name_oxygen,
    "o":names.name_oxygen,
    "o2":names.name_oxygen,
    "nitrite": names.name_nitrite,
    "no2": names.name_nitrite,
    "nitrate": names.name_nitrate,
    "no3": names.name_nitrate,
    "sulfate": names.name_sulfate,
    "so4": names.name_sulfate,
    "so42-": names.name_sulfate,
    "so4 2-": names.name_sulfate,
    "so4-2-": names.name_sulfate,
    "so4_2-": names.name_sulfate,
    "sulfide": names.name_sulfide,
    "s": names.name_sulfide,
    "s2": names.name_sulfide,
    "s 2": names.name_sulfide,
    "s-2": names.name_sulfide,
    "s_2": names.name_sulfide,
    "s2-": names.name_sulfide,
    "s 2-": names.name_sulfide,
    "s-2-": names.name_sulfide,
    "s_2-": names.name_sulfide,
    "s2min": names.name_sulfide,
    "s 2min": names.name_sulfide,
    "s-2min": names.name_sulfide,
    "s_2min": names.name_sulfide,
    "ammonium": names.name_ammonium,
    "nh4": names.name_ammonium,
    "nh4+": names.name_ammonium,
    "methane": names.name_methane,
    "ch4": names.name_methane,
    "manganese": names.name_manganese,
    "mn": names.name_manganese,
    "mn2": names.name_manganese,
    "mn 2": names.name_manganese,
    "mn-2": names.name_manganese,
    "mn_2": names.name_manganese,
    "mnii": names.name_manganese,
    "mn ii": names.name_manganese,
    "mn-ii": names.name_manganese,
    "mn_ii": names.name_manganese,
    "mn2+": names.name_manganese,
    "mn 2+": names.name_manganese,
    "mn-2+": names.name_manganese,
    "mn_2+": names.name_manganese,
    "mnii+": names.name_manganese,
    "mn ii+": names.name_manganese,
    "mn-ii+": names.name_manganese,
    "mn_ii+": names.name_manganese,
    "iron": names.name_ironII,
    "iron2": names.name_ironII,
    "iron 2": names.name_ironII,
    "iron-2": names.name_ironII,
    "iron_2": names.name_ironII,
    "iron2+": names.name_ironII,
    "iron 2+": names.name_ironII,
    "iron-2+": names.name_ironII,
    "iron_2+": names.name_ironII,
    "ironii": names.name_ironII,
    "iron ii": names.name_ironII,
    "iron-ii": names.name_ironII ,
    "iron_ii": names.name_ironII,
    "ironii+": names.name_ironII,
    "iron ii+": names.name_ironII ,
    "iron-ii+": names.name_ironII,
    "iron_ii+": names.name_ironII ,
    "fe": names.name_ironII,
    "fe2": names.name_ironII,
    "fe 2": names.name_ironII,
    "fe-2": names.name_ironII,
    "fe_2": names.name_ironII,
    "fe2+": names.name_ironII,
    "fe 2+": names.name_ironII,
    "fe-2+": names.name_ironII,
    "fe_2+": names.name_ironII,
    "feii": names.name_ironII,
    "fe ii": names.name_ironII,
    "fe-ii": names.name_ironII,
    "fe_ii": names.name_ironII,
    "feii+": names.name_ironII,
    "fe ii+": names.name_ironII,
    "fe-ii+": names.name_ironII,
    "fe_ii+": names.name_ironII,
    "phosphate": names.name_phosphate,
    "po4": names.name_phosphate,
    "po43-": names.name_phosphate,
    "po4 3-": names.name_phosphate,
    "po4-3-": names.name_phosphate,
    "po4_3-": names.name_phosphate,
    'chloride': names.name_chloride,
    'cl': names.name_chloride,
    'cl-': names.name_chloride,
    'bromide': names.name_bromide,
    'br': names.name_bromide,
    'br-': names.name_bromide,
    'fluoride': names.name_fluoride,
    'f': names.name_fluoride,
    'f-': names.name_fluoride,
    'sodium': names.name_sodium,
    'na': names.name_sodium,
    'na+': names.name_sodium,
    'magnesium': names.name_magnesium,
    'mg': names.name_magnesium,
    'mg2+': names.name_magnesium,
    'potassium': names.name_potassium,
    'k': names.name_potassium,
    'k+': names.name_potassium,
    'calcium': names.name_calcium,
    'ca': names.name_calcium,
    'ca2+': names.name_calcium,
    'acetate': names.name_acetate,
    'c2h3o2-': names.name_acetate,
}

names_contaminants_analysis = {
    "sum_contaminants": names.name_total_contaminants,
    "sum-contaminants": names.name_total_contaminants,
    "sum contaminants": names.name_total_contaminants,
    "sumcontaminants": names.name_total_contaminants,
    "total_contaminants": names.name_total_contaminants,
    "total-contaminants": names.name_total_contaminants,
    "total contaminants": names.name_total_contaminants,
    "totalcontaminants": names.name_total_contaminants,
    'Sum GC': names.name_total_contaminants,
    "total_oxidators": names.name_total_oxidators,
    "total_reductors": names.name_total_reductors,
    "NP_avail": names.name_NP_avail,
    'e_balance': names.name_e_balance,
    'na_traffic_light': names.name_na_traffic_light,
    'intervention_traffic': names.name_intervention_traffic,
    'intervention_number': names.name_intervention_number,
    'intervention_contaminants': names.name_intervention_contaminants,
}


names_metabolites_sum = {
    "metaboliteconcentration": names.name_metabolites_conc,
    "metabolite concentration": names.name_metabolites_conc,
    "metabolite_concentration": names.name_metabolites_conc,
    "Metabolite-concentration": names.name_metabolites_conc,
    'metabolitevariety': names.name_metabolites_variety,
    'metabolite variety': names.name_metabolites_variety,
    'metabolite-variety': names.name_metabolites_variety,
    'metabolite_variety': names.name_metabolites_variety,
    'metabolitesvariety': names.name_metabolites_variety,
    'metabolites variety': names.name_metabolites_variety,
    'metabolites-variety': names.name_metabolites_variety,
    'metabolites_variety': names.name_metabolites_variety,
    "number of detected metabolites":  names.name_metabolites_variety,
}


col_dict = {
    **names_sample_settings,
    **names_environment,
    **names_chemicals,
    **names_contaminants,
    **names_contaminants_analysis,
    **names_metabolites,
    **names_metabolites_sum,
}
