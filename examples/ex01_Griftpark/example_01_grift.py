"""Example of data analysis of contaminant data from Griftpark, Utrecht.

@author: Alraune Zech
"""

import sys
path = '/home/alraune/GitHub/MiBiPreT/mibipret/mibipret/'
sys.path.append(path) # append the path to module
import data.data as md
import analysis.sample.screening_NA as na

# import mibipret.analysis.sample.screening_NA as na
# import mibipret.data.data as md
# import mibipret.data.names as ean

# from mibipret.data.data import check_columns
# from mibipret.data.data import check_units
# from mibipret.data.data import check_values
# from mibipret.data.data import load_csv
# from mibipret.data.data import standardize

###------------------------------------------------------------------------###
### Script settings 
verbose = True

###------------------------------------------------------------------------###
### Script settings 
file_path = './grift_BTEXIIN.csv'
file_standard = './grift_BTEXNII_standard.csv'

data,units = md.load_csv(file_path,verbose = verbose)

# column_names_known,column_names_unknown,column_names_standard = md.check_columns(data, verbose = verbose)
# # # print("\nQuantities to be checked on column names: \n",column_names_unknown)

# check_list = md.check_units(data,verbose = verbose)
# # # print("\nQuantities to be checked on units: \n",check_list)

# data_pure = md.check_values(data, verbose = verbose)

data_standard,units = md.standardize(data,reduce = True, store_csv=file_standard,  verbose=verbose)

tot_reduct = na.reductors(data_standard,verbose = verbose,ea_group = 'ONSFe')
#
 # tot_reduct2 = na.reductors(data,verbose = verbose,ea_group = 'all_ea')
# # tot_reduct3 = na.reductors(data,verbose = verbose,ea_group = 'test')

# # tot_reduct = na.reductors(data_empty)
# # # print(tot_reduct)
# # na_data[tot_reduct.name] = tot_reduct

# tot_oxi = na.oxidators(data,verbose = verbose)
# tot_oxi2 = na.oxidators(data,verbose = verbose,contaminant_group='BTEX')
# tot_oxi3 = na.oxidators(data,verbose = verbose,contaminant_group='all_cont')
# # tot_oxi4 = na.oxidators(data,verbose = verbose,contaminant_group='test')

# # # tot_oxi = na.oxidators(data,verbose = verbose,nutrient = True)
# na_data[tot_oxi.name] = tot_oxi

 
# na.check_data(cols)
# NP_avail = na.available_NP(data)
# na_data[NP_avail.name] = NP_avail
# 
# tot_cont = na.total_contaminant_concentration(data,verbose = verbose,contaminant_group='BTEX')
# # na_data[tot_cont.name] = tot_cont
# cols = na.check_data(data)#.iloc[:,0])
# if (ean.name_o_xylene in cols) and (ean.name_pm_xylene in cols) and (ean.name_xylene in cols):
#     eas = ean.contaminants["BTEX"].remove(ean.name_xylene)
#     print(1)
# else:
# eas = ean.contaminants["BTEX"].copy()
# eas.remove(ean.name_xylene)
#     print(2)

# print(eas)

# tot_oxi2 = pd.Series(data = [1.566197,3.700148, 3.005697, 2.095891],name = 'total_oxidators')
# tot_reduct2 = pd.Series(data = [11.819184,0.525160, 0.347116, 15.265349], name = 'total_reductors')

# na_data = pd.concat([tot_reduct2, tot_oxi2],axis =1)

# # e_bal = na.electron_balance(data,verbose = verbose)
# e_bal = na.electron_balance(na_data,verbose = verbose)
# na_data[e_bal.name] = e_bal

# na_traffic = na.NA_traffic(data,verbose = verbose)
# na_traffic = na.NA_traffic(na_data,verbose = verbose)
# print(np.all(na_traffic.values == ['green','red','red','green']))
# na_data[na_traffic.name] = na_traffic
  
# pd.DataFrame(data, columns=[ean.name_sample,ean.name_observation_well])

# na_intervention = na.thresholds_for_intervention(data,verbose = verbose,contaminant_group='test')
# intervention_contaminants_test = ['benzene', 'ethylbenzene', 'pm_xylene', 'o_xylene', 'indane', 'naphthalene']

# print(np.sum(na_intervention['intervention_number'].values))
# print(na_intervention.shape)
# na_intervention.insert(2, tot_oxi.name, tot_oxi)
#test = na_intervention[columns={'intervention_traffic','intervention_number','intervention_contaminants'}]
# na_data = pd.concat([na_data,],axis =1)

#data_na = na.screening_NA(data,verbose = False,nutrient = True)
# data_na = na.screening_NA(data,verbose = True,nutrient = False)

# #print(tot_reduct.values == tot_reduct_example_data)
# print(np.sum(tot_reduct.values - tot_reduct_example_data.values)<1e-5)

# data01 = data.benzene
# tot_reduct = na.reductors(data01)
# print(tot_reduct)

# quant = tot_cont
# print(np.sum(quant.values))

# # print(tot_reduct)

#data.rename(columns={'nitrite': 'nitrate'}, inplace=True)
# check_list = check_units(data_standard)
# print("quantities to be checked on units: \n",check_list)

#