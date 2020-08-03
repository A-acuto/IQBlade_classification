import numpy as np
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

   # OLD Decision matrix with fixed input
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

