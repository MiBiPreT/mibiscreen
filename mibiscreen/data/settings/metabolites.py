"""Specifications of metabolies.

List of basic metabolites measured in groundwater samples useful
for biodegredation and bioremediation analysis

@author: A. Zech
"""

import mibiscreen.data.settings.standard_names as names

properties_metabolites = dict()
properties_metabolites[names.name_phenol]=dict(
    # chemical_formula = "",
    # molecular_mass = ,
    other_names = ["phenol"],
)

properties_metabolites[names.name_cinnamic_acid]=dict(
    # chemical_formula = "",
    # molecular_mass = ,
    other_names = ["cinnamic_acid"],
)

properties_metabolites[names.name_benzoic_acid]=dict(
    # chemical_formula = "",
    # molecular_mass = ,
    other_names = ["benzoic_acid"],
)

properties_metabolites[names.name_dimethyl_benzoic_acid]=dict(
    # chemical_formula = "",
    # molecular_mass = ,
    other_names = ['dimethyl_benzoic_acid'],
)

properties_metabolites[names.name_benzylacetate]=dict(
    # chemical_formula = "",
    # molecular_mass = ,
    other_names = ['benzylacetate'],
)

properties_metabolites[names.name_benzoylacetic_acid]=dict(
    # chemical_formula = "",
    # molecular_mass = ,
    other_names = ["benzoylacetic_acid"],
)

properties_metabolites[names.name_p_coumaric_acid]=dict(
    # chemical_formula = "",
    # molecular_mass = ,
    other_names = ["p-coumaric_acid"],
)
properties_metabolites[names.name_hydroxycinnamate]=dict(
    # chemical_formula = "",
    # molecular_mass = ,
    other_names = ["hydroxycinnamate"],
)

properties_metabolites[names.name_acetylphenol]=dict(
    # chemical_formula = "",
    # molecular_mass = ,
    other_names = ["acetylphenol"],
)
properties_metabolites[names.name_methyl_benzoic_acid]=dict(
    # chemical_formula = "",
    # molecular_mass = ,
    other_names = ['methyl_benzoic_acid'],
)

properties_metabolites[names.name_benzylsuccinic_acid]=dict(
    # chemical_formula = "",
    # molecular_mass = ,
    other_names = ["benzylsuccinic_acid"],
)

properties_metabolites[names.name_3o_toluoyl_propionic_acid]=dict(
    # chemical_formula = "",
    # molecular_mass = ,
    other_names = ["3o_toluoyl_propionic_acid"],
)

metabolites = list(properties_metabolites.keys())
