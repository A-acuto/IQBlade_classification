import numpy as np
import pandas as pd
from pandas.core.common import flatten

from datasets import *
from usefull_tools import *

def score_intro_sic_codes(tokens):

    # loaded datasets of common words #

    # table of pool of words from the different company types divided by SIC codes too, see in DATASETS the differences and the references
    table_of_pool_words=[pool_recruitment_0, pool_recruitment_1, pool_isv_0, pool_isv_1, pool_isv_2, pool_isv_3,
                      pool_vendor_0, pool_vendor_1, pool_vendor_2, pool_cloud_0, pool_cloud_1, pool_cloud_2,
                      pool_msp_0, pool_msp_1, pool_ms_0, pool_ms_1, pool_ms_2, pool_telco_0, pool_telco_1,
                      pool_da_0, pool_da_1, pool_da_2, pool_da_3, pool_distributor_0, pool_distributor_1,
                      pool_reseller_0, pool_reseller_1, pool_reseller_2, pool_reseller_3, pool_outsourcer_0,
                      pool_outsourcer_1, pool_outsourcer_2, pool_outsourcer_3]

    # transfrom the words in to dataframe
    words_dataframe = pd.DataFrame(table_of_pool_words)

    pool_set = list(flatten(table_of_pool_words))

    # same procedure as done in the score_name_url
    # counts and finds unique words, then scores given the recurrencies
    unique_words = set()
    for x in pool_set:
        unique_words.add(x)

    gen_weights = np.zeros(len(unique_words))

    counter = 0
    for x in unique_words:
        id = np.where(words_dataframe == x)[0]
        gen_weights[counter] = len(id)
        counter += 1

    list_words = list(unique_words)
    points = np.asarray(list_words)

    # now here is the actual scoring of each datasets
    table_of_dataframes = []

    # loop over each pool words
    for iweight in range(len(table_of_pool_words)):
        id_pool = return_indices_of_a(list_words, table_of_pool_words[iweight])
        # here I created the pool and the weight for each word for each company type
        weight = 1. / gen_weights[id_pool]
        new_pool = points[id_pool]

        pool = pd.DataFrame([new_pool, weight])
        table_of_dataframes.append(pool)


    # actual sum of all the weights in each pool-words
    value_total = np.zeros(len(table_of_pool_words))

    for itotal in range(len(table_of_pool_words)):
        dataf = table_of_dataframes[itotal]
        value_total[itotal] = np.sum(dataf.iloc[1])

    n_str = len(tokens)
    flag_check = []
    if n_str == 0:
        print('!raised awareness! zero element in the analyzed text')
        flags_checks = np.zeros(len(table_of_pool_words))
    elif n_str > 0:

        if n_str == 1:
            print('!raised awareness! Only 1 element in the analyzed text')

        for ipool in range(len(table_of_pool_words)):
            dataf =  table_of_dataframes[ipool]
            id_0 = return_indices_of_a(dataf.iloc[0], tokens)
            values = np.sum(dataf.iloc[1][id_0])
            flag_check.append(values/value_total[ipool])

        flags_checks = 100 * np.asarray(flag_check)

    return flags_checks
