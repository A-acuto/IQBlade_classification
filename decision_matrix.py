import numpy as np
import sys
from collections import Counter
import pandas as pd
from pandas.core.common import flatten

def decision_matrix_variable(*args):

   # *args input is a Tuple, let's convert into List to make things work

    new_args = list(args)    # converts

    vals = []

    # loop for each arg I have provided, maybe not needed if the feed vector is already an ordered list
    for element in range(len(new_args)):

        # if the input is a list with more than one element I'll add each one singularly
        if len(new_args[element]) > 1:
            new_list = new_args[element]

            for j in range(len(new_list)):
                vals.append(new_list[j])
        else:

            vals.append(new_args[element])

    # this flattening avoid the insurgence of list of lists
    new_vals = list(flatten(vals))

    # convert the values in dictionary to help the counting
    results = dict(Counter(new_vals))

    # this part converts the results from the matrices and arrays and gets the highest value
    # in case it's empty then spits an empty file

    if new_vals != []:
        pd_val = pd.DataFrame.from_dict(results.items())
        indexes = pd_val[pd_val[1] == pd_val[1].max()].index.values
        output = list(pd_val[0].loc[indexes])
    else:
        output = ['']

    # output the result
    return output

def decision_matrix_count(sic_name, url, name, intro, wbs, intro_cross, wbs_cross, intro_30, wbs_30, intro_cross_30, wbs_cross_30):
    vals= []
    for i in range(len(sic_name)):
        vals.append(sic_name[i])

    for i in range(len(url)):
        vals.append(url[i])

    for i in range(len(name)):
        vals.append(name[i])

    for i in range(len(intro)):
        vals.append(intro[i])

    for i in range(len(wbs)):
        vals.append(wbs[i])

    for i in range(len(intro_cross)):
        vals.append(intro_cross[i])

    for i in range(len(wbs_cross)):
        vals.append(wbs_cross[i])

    for i in range(len(intro_30)):
        vals.append(intro_30[i])

    for i in range(len(wbs_30)):
          vals.append(wbs_30[i])

    for i in range(len(intro_cross_30)):
         vals.append(intro_cross_30[i])

    for i in range(len(wbs_cross_30)):
         vals.append(wbs_cross_30[i])

    res = dict(Counter(vals))

    if vals != []:
        pd_val = pd.DataFrame.from_dict(res.items())
        indexes = pd_val[pd_val[1] == pd_val[1].max()].index.values
        output= list(pd_val[0].loc[indexes])
    else :
        output =['']
    return output

#ut = decision_matrix_count(test0, test0, test0, test0, test0, test0, test0)
#print(ut)
#sys.exit()

#def decision_matrix(url, name, sic, intro_max, wbs_max,  test):

    # so the input are the various scores and evaluated
    # url and name are classified by a score
    # while the others are percentage

        ##### first issue how to identify then the result of the category ###
#    id0 = 'Recruitment'
#    id1 = 'ISV'
#    id2 = 'MSP'
#    id3 = 'Telco'
#    id4 = 'Vendor'
#    id5 = 'Reseller'
#    id6 = 'CloudConsultant'
#    id7 = 'DigitalAgency'
#    id8 = 'ManagedService'
#    id9 = 'Distributor'
#    id10 = 'Outsourcerer'



    #### check url
    #### with this it's normalized to 10, so if the score was 100 now it's 10. or 25, 33...
 #   if url == []:
 #       url_value = 0.

 #   if url != []:
 #       url_value = np.float(url[0])/10.

    ##### check name
 #   if name == []:
  #      name_value = 0.

 #   if name != []:
 #       name_value = np.float(name[0])/10.

 #   sic_value = np.float(sic)

    #### watch out on the type of the data in.

 #   if intro_max != []:
 #       intro_value = np.float(intro_max[0])/10.
 #   if intro_max == []:
 #       intro_value = 0.

 #   if wbs_max != []:
 #       wbs_value = np.float(wbs_max[0])/10.
 #   if wbs_max == []:
 #       wbs_value = 0.

#    print(url_value, name_value, sic_value, intro_value, wbs_value)

#name =[]
#intro_max = [58.65624918,58.65624918]
#wbs_max = [58.65624918, 58.65624918]
#sic = 5.0
#decision_matrix(url,name, sic,intro_max,wbs_max,   test)
#url=[25.0]
#name=[25.0]
#decision_matrix(url,name, sic, intro_max, wbs_max,  test)