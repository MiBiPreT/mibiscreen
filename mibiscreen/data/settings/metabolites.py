"""Specifications of metabolies.

List of basic metabolites measured in groundwater samples useful
for biodegredation and bioremediation analysis

@author: A. Zech
"""

import mibiscreen.data.settings.standard_names as names

properties_metabolites = dict()

properties_metabolites[names.name_metabolites_conc]=dict(
    other_names = ["metabolites","metabolites all","metabolites-all","metabolites_all",
                   "metabolitesall", "metaboliteconcentration","metabolite concentration",
                   "metabolite_concentration","metabolite-concentration"],
    standard_unit = names.unit_microgperl,
)

properties_metabolites[names.name_metabolites_count]=dict(
    other_names = ['metabolitevariety','metabolite variety','metabolite-variety',
                   'metabolite_variety','metabolitesvariety','metabolites variety',
                   'metabolites-variety','metabolites_variety',"number of detected metabolites"],
    standard_unit = names.unit_count,
)

properties_metabolites[names.name_phenol]=dict(
    # chemical_formula = "",
    # molecular_mass = ,
    other_names = ["phenol"],
    standard_unit = names.unit_microgperl,
)

properties_metabolites[names.name_cinnamic_acid]=dict(
    # chemical_formula = "",
    # molecular_mass = ,
    other_names = ["cinnamic_acid"],
    standard_unit = names.unit_microgperl,
)

properties_metabolites[names.name_benzoic_acid]=dict(
    # chemical_formula = "",
    # molecular_mass = ,
    other_names = ["benzoic_acid"],
    standard_unit = names.unit_microgperl,
)

properties_metabolites[names.name_dimethyl_benzoic_acid]=dict(
    # chemical_formula = "",
    # molecular_mass = ,
    other_names = ['dimethyl_benzoic_acid'],
    standard_unit = names.unit_microgperl,
)

properties_metabolites[names.name_benzylacetate]=dict(
    # chemical_formula = "",
    # molecular_mass = ,
    other_names = ['benzylacetate'],
    standard_unit = names.unit_microgperl,
)

properties_metabolites[names.name_benzoylacetic_acid]=dict(
    # chemical_formula = "",
    # molecular_mass = ,
    other_names = ["benzoylacetic_acid"],
    standard_unit = names.unit_microgperl,
)

properties_metabolites[names.name_p_coumaric_acid]=dict(
    # chemical_formula = "",
    # molecular_mass = ,
    other_names = ["p-coumaric_acid"],
    standard_unit = names.unit_microgperl,
)
properties_metabolites[names.name_hydroxycinnamate]=dict(
    # chemical_formula = "",
    # molecular_mass = ,
    other_names = ["hydroxycinnamate"],
    standard_unit = names.unit_microgperl,
)

properties_metabolites[names.name_acetylphenol]=dict(
    # chemical_formula = "",
    # molecular_mass = ,
    other_names = ["acetylphenol"],
    standard_unit = names.unit_microgperl,
)
properties_metabolites[names.name_methyl_benzoic_acid]=dict(
    # chemical_formula = "",
    # molecular_mass = ,
    other_names = ['methyl_benzoic_acid'],
    standard_unit = names.unit_microgperl,
)

properties_metabolites[names.name_benzylsuccinic_acid]=dict(
    # chemical_formula = "",
    # molecular_mass = ,
    other_names = ["benzylsuccinic_acid"],
    standard_unit = names.unit_microgperl,
)

properties_metabolites[names.name_3o_toluoyl_propionic_acid]=dict(
    # chemical_formula = "",
    # molecular_mass = ,
    other_names = ["3o_toluoyl_propionic_acid"],
    standard_unit = names.unit_microgperl,
)

### List with all quantities of particular data type in standard names:
metabolites = list(properties_metabolites.keys())
