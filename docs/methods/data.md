# `mibiscreen` Data

## General Data Handling

We designed data handling for field sample data typical for biodegradation processes. This data includes

* sample specification data, 
* contaminant concentrations, focusing on petroleum hydrocarbons, 
* hydrogeochemical data and habitat conditions, e.g. redox potential, pH, electron acceptor concentrations, such as oxygen, nitrate, sulfate
* microbiome data (i.e. the occurrence of DNA and functional genes), 
* metabolite data (i.e. intermediate products of the degradation process)
* measurements on stable isotope fractions (particularly for hydrogen and carbon within the sample and/or of individual contaminant)

Data has to be provided in a **standardized form**. Data transformation is implemented in functions performing:

* loading data from csv or excel files
* check of input data on 
  * correct units provided
  * numerical values
* standardisation, e.g. of column names to standard names
* selection of data

A workflow of data handling is illustrated for the Griftpark data in a jupyter-notebook `\examples\ex01_Griftpark\example_01_grift_data.ipynb`. 

## Contaminant Data

*mibiscreen* recognizes the typical petroleum hydrocarbon contaminants. The following tables provide an overview of them sorted by contaminant subgroups, including:

* MAHs
* PAHs
* Alkylphenols
* Contaminant groups (e.g.  BTEX, PAH total 16, or hydrocarbon fraction of specific chain lengths)

The name in the first column of each talbe also provides the standard name used in *mibiscreen*. All contaminants have the canonical unit µg/L.

The routine `check_columns()` allows to standardize loaded data to these standard names making use of a list of optional other names for each quantity (to be found in `/mibiscreen/data/settings/contaminants.py`.

### MAHs: monoaromatic hydrocarbons

All MAHs have the canonical unit µg/L.

| Name (contaminant)      | Chemical formula | Short description / notes                               |
| ----------------------- | ---------------- | ------------------------------------------------------- |
| benzene                 | C₆H₆             | Simple aromatic hydrocarbon; volatile and toxic         |
| toluene                 | C₆H₅CH₃          | Monoaromatic hydrocarbon; common solvent                |
| ethylbenzene            | C₆H₅CH₂CH₃       | Monoaromatic hydrocarbon; industrial solvent            |
| xylene                  | C₆H₄CH₃CH₃       | Mixture of ortho-, meta-, para- isomers; common solvent |
| pm_xylene               | C₆H₄CH₃CH₃       | Para- and meta-xylene isomers                           |
| o_xylene                | C₆H₄CH₃CH₃       | Ortho-xylene isomer                                     |
| styrene                 | C₆H₅CH=CH₂       | Vinyl-substituted benzene; precursor for polystyrene    |
| isopropylbenzene        | C₆H₅C₃H₇         | Cumene; industrial intermediate                         |
| n_propylbenzene         | C₆H₅CH₂CH₂CH₃    | Straight-chain propyl-substituted benzene               |
| ethyltoluene            | C₆H₄CH₃C₂H₅      | Ethyl-substituted toluene                               |
| 2_ethyltoluene          | C₆H₄CH₃C₂H₅      | Ortho-ethyltoluene isomer                               |
| 3_ethyltoluene          | C₆H₄CH₃C₂H₅      | Meta-ethyltoluene isomer                                |
| 4_ethyltoluene          | C₆H₄CH₃C₂H₅      | Para-ethyltoluene isomer                                |
| trimethylbenzene        | C₆H₃CH₃CH₃CH₃    | Generic trimethylbenzene isomers                        |
| 123_trimethylbenzene    | C₆H₃CH₃CH₃CH₃    | 1,2,3-trimethylbenzene                                  |
| 124_trimethylbenzene    | C₆H₃CH₃CH₃CH₃    | 1,2,4-trimethylbenzene                                  |
| 135_trimethylbenzene    | C₆H₃CH₃CH₃CH₃    | 1,3,5-trimethylbenzene                                  |
| 4_isopropyltouene       | C₆H₄CH₃C₃H₇      | Para-cymene; isopropyl-substituted toluene              |
| diethylbenzene          | C₆H₄C₂H₅C₂H₅     | Generic diethylbenzene isomers                          |
| 12_diethylbenzene       | C₆H₄C₂H₅C₂H₅     | 1,2-diethylbenzene                                      |
| 13_diethylbenzene       | C₆H₄C₂H₅C₂H₅     | 1,3-diethylbenzene                                      |
| 14_diethylbenzene       | C₆H₄C₂H₅C₂H₅     | 1,4-diethylbenzene                                      |
| tetramethylbenzene      | C₆H₂CH₃CH₃CH₃CH₃ | Generic tetramethylbenzene isomers                      |
| 1234_tetramethylbenzene | C₆H₂CH₃CH₃CH₃CH₃ | 1,2,3,4-tetramethylbenzene (prehnitene)                 |
| 1245_tetramethylbenzene | C₆H₂CH₃CH₃CH₃CH₃ | 1,2,4,5-tetramethylbenzene (durene)                     |
| 1235_tetramethylbenzene | C₆H₂CH₃CH₃CH₃CH₃ | 1,2,3,5-tetramethylbenzene (isodurene)                  |

### PAHs: polyaromatic hydrocarbons

All PAHs have the canonical unit µg/L.

| Name (contaminant)     | Chemical formula | Short description / notes                                                                                              |
| ---------------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------- |
| indene                 | C₉H₈             | Bicyclic aromatic hydrocarbon; fused benzene and cyclopentene                                                          |
| indane                 | C₉H₁₀            | Hydrogenated indene; bicyclic hydrocarbon                                                                              |
| naphthalene            | C₁₀H₈            | Two fused benzene rings; common PAH                                                                                    |
| naphthalene_VOC        | C₁₀H₈            | Volatile naphthalene; common VOC                                                                                       |
| naphthalene_PAH        | C₁₀H₈            | Standard PAH form of naphthalene                                                                                       |
| acenaphthylene         | C₁₂H₈            | Tricyclic aromatic hydrocarbon                                                                                         |
| acenaphthene           | C₁₂H₁₀           | Hydrogenated acenaphthylene; tricyclic                                                                                 |
| fluorene               | C₁₃H₁₀           | Tricyclic aromatic hydrocarbon; two benzene rings and one cyclopentane                                                 |
| phenanthrene           | C₁₄H₁₀           | Linear tricyclic aromatic hydrocarbon                                                                                  |
| anthracene             | C₁₄H₁₀           | Linear tricyclic aromatic hydrocarbon; isomer of phenanthrene                                                          |
| fluoranthene           | C₁₆H₁₀           | Four fused rings; common environmental PAH                                                                             |
| pyrene                 | C₁₆H₁₀           | Four fused rings; planar aromatic hydrocarbon                                                                          |
| chrysene               | C₁₈H₁₂           | Four-ring PAH; common in combustion products                                                                           |
| benzo[a]anthracene     | C₁₈H₁₂           | Four-ring PAH; known carcinogen                                                                                        |
| benzo[b]fluoranthene   | C₂₀H₁₂           | Five-ring PAH; common in soot                                                                                          |
| benzo[k]fluoranthene   | C₂₀H₁₂           | Five-ring PAH; structural isomer of benzo[b]fluoranthene                                                               |
| benzo[a]pyrene         | C₂₀H₁₂           | Five-ring PAH; highly carcinogenic                                                                                     |
| dibenz[a,h]anthracene  | C₂₂H₁₄           | Six-ring PAH; potent carcinogen                                                                                        |
| benzo[ghi]perylene     | C₂₂H₁₂           | Six-ring PAH; environmental pollutant                                                                                  |
| indeno[1,2,3-cd]pyrene | C₂₂H₁₂           | Five-ring PAH; planar aromatic compound                                                                                |
| methylindene           | C₁₀H₁₀           | Methyl-substituted indene; includes 1- and 2-methylindene isomers                                                      |
| methylnaphthalene      | C₁₁H₁₀           | Single methyl substitution on naphthalene; includes 1- and 2-methylnaphthalene isomers                                 |
| ethylnaphthalene       | C₁₂H₁₂           | Single ethyl substitution on naphthalene; includes 1- and 2-ethylnaphthalene isomers                                   |
| dimethylnaphthalene    | C₁₂H₁₂           | Two methyl groups on naphthalene; includes 1,2- / 1,3- / 1,4- / 1,5- / 1,6- / 1,7- / 1,8- / 2,3- / 2,6- / 2,7- isomers |

### Alkylphenols

All alkylphenols have the canonical unit µg/L.

| Name (contaminant)      | Chemical formula | Short description / notes                                                                  |
| ----------------------- | ---------------- | ------------------------------------------------------------------------------------------ |
| phenol                  | C₆H₆O            | Hydroxybenzene; simplest phenol; also called benzenol                                      |
| cresols (methylphenols) | C₇H₈O            | Methyl-substituted phenols; includes o-, m-, and p-cresol isomers                          |
| ethylphenols            | C₈H₁₀O           | Ethyl-substituted phenols; includes 2-ethylphenol, 3-ethylphenol, 4-ethylphenol            |
| dimethylphenols         | C₈H₁₀O           | Two methyl groups on phenol ring; includes 2,3- / 2,4- / 2,5- / 2,6- / 3,4- / 3,5- isomers |
| trimethylphenols        | C₉H₁₂O           | Three methyl groups on phenol; includes 2,3,5- and 3,4,5-trimethylphenol isomers           |
| isopropylphenols        | C₉H₁₂O           | Includes 2-isopropylphenol (o-isopropylphenol) and thymol (2-isopropyl-5-methylphenol)     |
| tert-butylphenols       | C₁₀H₁₄O          | Para-substituted tert-butylphenol; also called p-tert-butylphenol                          |
| thymol                  | C₁₀H₁₄O          | 2-isopropyl-5-methylphenol; a naturally occurring alkylphenol                              |

### Contaminant Groups

| Contaminant group (Standard name) | Short description                                       | Contaminants included (group members)                                                                                                                                                                                                                            |
| --------------------------------- | ------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| all_cont                          | Total sum of all quantified contaminants                | all individual contaminants measured in dataset (and part of the standard set)                                                                                                                                                                                   |
| BTEX                              | Sum of common volatile aromatic hydrocarbons (BTEX)     | benzene, toluene, ethylbenzene, p‑xylene, o‑xylene, m‑xylene (often grouped as “xylene”)                                                                                                                                                                         |
| BTEXIIN                           | Sum of BTEX plus selected hydrocarbons                  | BTEX members plus indane, indene, naphthalene                                                                                                                                                                                                                    |
| PAH_total_16                      | Sum of 16 EPA priority polycyclic aromatic hydrocarbons | naphthalene, acenaphthylene, acenaphthene, fluorene, phenanthrene, anthracene, fluoranthene, pyrene, benzo[a]anthracene, chrysene, benzo[b]fluoranthene, benzo[k]fluoranthene, benzo[a]pyrene, indeno[1,2,3‑cd]pyrene, dibenz[a,h]anthracene, benzo[ghi]perylene |
| PAH_total_10                      | Subset of 10 PAHs used in some environmental standards  | naphthalene, anthracene, benzo[a]anthracene, benzo[a]pyrene, benzo[b]fluoranthene, benzo[k]fluoranthene, chrysene, dibenz[a,h]anthracene, fluoranthene, pyrene                                                                                                   |
| fraction_C10‑C12                  | Hydrocarbon fraction of C₁₀–C₁₂ chain lengths           | hydrocarbons with 10–12 carbon atoms (e.g., light petroleum fractions)                                                                                                                                                                                           |
| fraction_C12‑C22                  | Hydrocarbon fraction of C₁₂–C₂₂                         | hydrocarbons with 12–22 carbon atoms (e.g., mid‑range petroleum fractions)                                                                                                                                                                                       |
| fraction_C22‑C30                  | Hydrocarbon fraction of C₂₂–C₃₀                         | hydrocarbons with 22–30 carbon atoms (e.g., heavier petroleum fractions)                                                                                                                                                                                         |
| fraction_C30‑C40                  | Hydrocarbon fraction of C₃₀–C₄₀                         | hydrocarbons with 30–40 carbon atoms (e.g., very heavy petroleum fractions)                                                                                                                                                                                      |
| total_C10‑C40                     | Sum of all C₁₀–C₄₀ hydrocarbon fractions                | hydrocarbons with 10–40 carbon atoms (aggregated)                                                                                                                                                                                                                |
| c2_alkylphenols_total             | Sum of phenols with two‑carbon substituents             | o‑cresol, m‑cresol, p‑cresol, 2‑ethylphenol, 3‑ethylphenol                                                                                                                                                                                                       |
| c3_alkylphenols_total             | Sum of phenols with three‑carbon substituents           | methylindene phenol derivatives with C3 substituents                                                                                                                                                                                                             |
| c4_alkylphenols_total             | Sum of phenols with four‑carbon substituents            | 4‑ethylphenol, p‑tertbutylphenol, thymol (p‑isopropyl‑5‑methylphenol)                                                                                                                                                                                            |

## Geochemical Habitat Data

*mibiscreen* recognizes the typical chemical quantities present in the (hydro)geological environment. The first table provides an overview of chemical quantities, the second table contains typical (additional) environmental measures. The name in the first column of each talbe also provides the standard name used in *mibiscreen*. 

The routine `check_columns()` allows to standardize loaded data to these standard names making use of a list of optional other names for each quantity (to be found in `/mibiscreen/data/settings/environment.py`.  

### Chemical Quantities

All chemicals have the standard unit mg/L.

| Name (chemical quantity) | Chemical formula (short) | Short description of meaning                                      |
| ------------------------ | ------------------------ | ----------------------------------------------------------------- |
| oxygen                   | O₂                       | Molecular oxygen; common electron acceptor in aerobic respiration |
| nitrate                  | NO₃⁻                     | Nitrate ion; fully oxidized inorganic nitrogen species            |
| sulfate                  | SO₄²⁻                    | Sulfate ion; fully oxidized sulfur species                        |
| iron2                    | Fe²⁺                     | Ferrous iron; reduced, soluble form of iron                       |
| iron3                    | Fe³⁺                     | Ferric iron; oxidized form of iron                                |
| manganese2               | Mn²⁺                     | Reduced, soluble manganese form                                   |
| manganese4               | Mn⁴⁺                     | Oxidized manganese form (commonly solid oxides)                   |
| methane                  | CH₄                      | Fully reduced carbon species; common anaerobic end product        |
| nitrite                  | NO₂⁻                     | Nitrite ion; intermediate nitrogen species                        |
| sulfide                  | S²⁻                      | Reduced sulfur species (includes H₂S/HS⁻ depending on pH)         |
| ammonium                 | NH₄⁺                     | Reduced inorganic nitrogen species; bioavailable form             |
| phosphate                | PO₄³⁻                    | Orthophosphate ion; bioavailable phosphorus form                  |
| chloride                 | Cl⁻                      | Conservative anion; common dissolved salt component               |
| bromide                  | Br⁻                      | Conservative halide ion; trace seawater component                 |
| fluoride                 | F⁻                       | Fluoride ion; trace halide species                                |
| sodium                   | Na⁺                      | Major alkali metal cation in natural waters                       |
| magnesium                | Mg²⁺                     | Major divalent cation in natural waters                           |
| potassium                | K⁺                       | Alkali metal cation; essential nutrient                           |
| calcium                  | Ca²⁺                     | Major divalent cation; important for hardness                     |
| acetate                  | CH₃COO⁻                  | Organic carbon source; fermentation intermediate                  |

### Environmental Parameters and Measures

| Name (environmental parameter) | Standard unit | Symbol / short form | Short description of meaning                                                           |
| ------------------------------ | ------------- | ------------------- | -------------------------------------------------------------------------------------- |
| redoxpot                       | mV            | Eh                  | Redox potential; measure of oxidation–reduction conditions in water                    |
| pH                             | —             | pH                  | Negative logarithm of hydrogen ion activity; measure of acidity/alkalinity             |
| temperature                    | °C            | T                   | Physical temperature of the sample                                                     |
| EC                             | µS/cm         | EC                  | Electrical conductivity; proxy for total dissolved ions                                |
| pE                             | —             | pE                  | Dimensionless measure of electron activity; thermodynamic redox state                  |
| DOC                            | mg/L          | DOC                 | Dissolved Organic Carbon; organic carbon passing a standard filter (typically 0.45 µm) |
| NPOC                           | mg/L          | NPOC                | Non-Purgeable Organic Carbon; organic carbon after inorganic carbon removal            |
| TOC                            | mg/L          | TOC                 | Total Organic Carbon; sum of dissolved and particulate organic carbon                  |
| nitrate_N                      | mg N/L        | NO₃⁻–N              | Nitrogen mass within the nitrate ion only                                              |
| nitrite_N                      | mg N/L        | NO₂⁻–N              | Nitrogen mass within the nitrite ion only                                              |
| phosphorus_total               | mg P/L        | P (total)           | Total phosphorus; sum of all phosphorus compounds                                      |
| cyanide_total                  | mg/L          | CN⁻ (total)         | Sum of cyanide species capable of releasing free cyanide                               |

## Sample Settings

| Standard name | Unit | Aliases / other names                                                                                                                             |
| ------------- | ---- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| sample_nr     | -    | sample, sample number, sample-number, sample_number, sample nr, sample-nr, sample_name, sample-name, sample_name, sample id, sample-id, sample_id |
| obs_well      | -    | well, observation well, observation-well, observation_well, obs well, obs_well, obs-well                                                          |
| well_type     | -    | welltype, well type, well-type, well_type                                                                                                         |
| depth         | m    | depth, sample_depth                                                                                                                               |
| aquifer       | -    | aquifer                                                                                                                                           |
| date          | -    | date, time                                                                                                                                        |

## Units

Each quantities has a standard unit. Internally, *mibiscreen* uses a unit system and aliases during unit check. Find an overview of all units in the following table.

| Internal unit key  | Standard unit | Meaning / Usage                                 | Accepted aliases                                                |
| ------------------ | ------------- | ----------------------------------------------- | --------------------------------------------------------------- |
| unit_mgperl        | mg/L          | Mass concentration (compound mass)              | mg/l, ppm                                                       |
| unit_mgNperl       | mg N/L        | Nitrogen mass concentration (as N only)         | mg/l, ppm, mgN/l, ppm N, ppm-N, ppm_N, mg/l as N, ppm as N      |
| unit_mgPperl       | mg P/L        | Phosphorus mass concentration (as P only)       | mg/l, ppm, mgP/l, ppm P, ppm-P, ppm_P, mg/l as P, ppm as P      |
| unit_microgperl    | µg/L          | Trace-level mass concentration                  | ug/l, µg/l, μg/l, micro g/l, μ g/l                              |
| unit_millivolt     | mV            | Electrical potential (e.g., redox potential Eh) | mV, mv                                                          |
| unit_celsius       | °C            | Temperature                                     | C, c, Celsius, °C, ° C, °Celsius, ° Celsius                     |
| unit_meter         | m             | Length (e.g., depth)                            | m, meter                                                        |
| unit_microsimpercm | µS/cm         | Electrical conductivity                         | uS/cm, us/cm                                                    |
| unit_permil        | ‰             | Per mille (e.g., isotope ratios)                | permil, ‰, per mil, per mille, promille, permill, permille, mur |
| unit_count         | count         | Number-based measurement                        | nr, number, count                                               |
| unit_less          | —             | Dimensionless parameter (e.g., pH, pE)          |                                                                 |
