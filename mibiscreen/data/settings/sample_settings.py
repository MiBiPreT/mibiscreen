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
)

properties_sample_settings[names.name_observation_well]=dict(
    other_names = ["well",
                   "observation well",
                   "observation-well",
                   "observation_well",
                   "obs well",
                   "obs_well",
                   "obs-well"],
)

properties_sample_settings[names.name_well_type]=dict(
    other_names = [    "welltype",
        "well type",
        "well-type" ,
        "well_type"],
)

properties_sample_settings[names.name_sample_depth]=dict(
    other_names = ["depth",
                   "sample_depth"],
)

properties_sample_settings[names.name_aquifer]=dict(
    other_names = ["aquifer"],
)

sample_settings = list(properties_sample_settings.keys())
