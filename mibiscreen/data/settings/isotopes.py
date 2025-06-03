"""Specifications of isotopes.

List of basic isotopes measured in groundwater samples useful
for biodegredation and bioremediation analysis

@author: A. Zech
"""

import mibiscreen.data.settings.standard_names as names

properties_isotopes = dict()

properties_isotopes[names.name_13C]=dict(
    other_names = ['delta_c',
                    'delta_13c',
                    'delta_c13',
                    'delta_carbon',
                    'delta_13carbon',
                    'delta_carbon13',
                    'deltac',
                    'delta13c',
                    'deltac13',
                    'deltacarbon',
                    'delta13carbon',
                    'deltacarbon13',
                    'delta c',
                    'delta 13c',
                    'delta c13',
                    'delta carbon',
                    'delta 13carbon',
                    'delta carbon13',
                    'δ_c',
                    'δ_13c',
                    'δ_c13',
                    'δ_carbon',
                    'δ_13carbon',
                    'δ_carbon13',
                    'δc',
                    'δ13c',
                    'δc13',
                    'δcarbon',
                    'δ13carbon',
                    'δcarbon13',
                    'δ c',
                    'δ 13c',
                    'δ c13',
                    'δ carbon',
                    'δ 13carbon',
                    'δ carbon13'],
    standard_unit = names.unit_permil,
    )

properties_isotopes[names.name_2H]=dict(
    other_names = ['delta_h',
                    'delta_2h',
                    'delta_h2',
                    'delta_hydrogen',
                    'delta_2hydrogen',
                    'delta_hydrogen2',
                    'deltah',
                    'delta2h',
                    'deltah2',
                    'deltahydrogen',
                    'delta2hydrogen',
                    'deltahydrogen2',
                    'delta-h',
                    'delta-2h',
                    'delta-h2',
                    'delta-hydrogen',
                    'delta-2hydrogen',
                    'delta-hydrogen2',
                    'delta h',
                    'delta 2h',
                    'delta h2',
                    'delta hydrogen',
                    'delta 2hydrogen',
                    'delta hydrogen2'],
    standard_unit = names.unit_permil,
    )

### List with all quantities of particular data type in standard names:
isotopes = list(properties_isotopes.keys())
