"""Specifications of sample settings.

List of all quantities and parameters characterizing sample specifics for
measurements in groundwater samples useful for biodegredation and bioremediation analysis

@author: A. Zech
"""

import mibiscreen.data.settings.standard_names as names

properties_sample_settings = dict()
properties_sample_settings[names.name_sample]=dict(
    other_names = ["sample",
                   "sample",
                   "sample number",
                   "sample-number",
                   "sample_number",
                   "sample nr",
                   "sample-nr",
                   "sample_nr",
                   "sample name",
                   "sample-name",
                   "sample_name",
                   "sample id",
                   "sample-id",
                   "sample_id"],
    standard_unit = names.unit_less,
)

properties_sample_settings[names.name_observation_well]=dict(
    other_names = ["well",
                   "observation well",
                   "observation-well",
                   "observation_well",
                   "obs well",
                   "obs_well",
                   "obs-well"],
    standard_unit = names.unit_less,
)

properties_sample_settings[names.name_well_type]=dict(
    other_names = [ "welltype",
                    "well type",
                    "well-type" ,
                    "well_type"],
    standard_unit = names.unit_less,
)

properties_sample_settings[names.name_sample_depth]=dict(
    other_names = ["depth",
                   "sample_depth"],
    standard_unit = names.unit_meter,
)

properties_sample_settings[names.name_aquifer]=dict(
    other_names = ["aquifer"],
    standard_unit = names.unit_less,
)

### List with all quantities of particular data type in standard names:
sample_settings = list(properties_sample_settings.keys())
