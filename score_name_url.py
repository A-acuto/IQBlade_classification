import numpy as np
import pandas as pd
from usefull_tools import *
from pandas.core.common import flatten
from datasets import *


def score_url_name(url, name):

    ### Load name and encode it and lower it to match ###

    company_name = str(name.encode("utf8")).lower()

    ### 11 are the company types present analyzed ###
    score_name = np.zeros(11)
    score_url = np.zeros(11)

    table_of_title_words = [recruitment_title_words,isv_title_words, telco_title_words, vendor_title_words,
                             cloud_title_words,MS_title_words, MSP_title_words, DA_title_words, RS_title_words,
                             DS_title_words,OS_title_words]

    # all words loaded

    # transfrom the words in to dataframe
    words_dataframe = pd.DataFrame(table_of_title_words)

    pool_set = list(flatten(table_of_title_words))

    # identify unique words to help the scoring
    unique_words = set()
    for x in pool_set:
        unique_words.add(x)

    # create a weight on each unique word
    gen_weights = np.zeros(len(unique_words))

    counter = 0
    for x in unique_words:
        id = np.where(words_dataframe == x)[0]
        gen_weights[counter] = len(id)
        counter += 1

    # so now I have a list of words and points for each
    list_words = list(unique_words)
    points = np.asarray(list_words)

    # Now starts the scoring for each company type.
    # Firstly it gets the indeces of the words present in the recruitment title words
    # then scores them and create a new dataframe ordered with the words and relative weight.
    # this is done for all pool words

    table_of_dataframes = []

    for iweight in range(11):
        id_pool = return_indices_of_a(list_words, table_of_title_words[iweight])
        # here I created the pool and the weight for each word for each company type
        weight = 1. / gen_weights[id_pool]
        new_pool = points[id_pool]

        pool = pd.DataFrame([new_pool, weight])
        table_of_dataframes.append(pool)


    # URL evaluation
    if url != 0 :
        # cleaning the company url from https and domains
        company_url = clean_url_name(url)

        # score of the company url compared to each dataframes in a elegant loop
        for idataframe in range(len(score_url)):
            # related dataframes and np arrays
            dataf = table_of_dataframes[idataframe]
            idf = checkIfAny(company_url, dataf.iloc[0])
            id_0 = np.where(idf == dataf.iloc[0])[0]
            values_0 = np.sum(dataf.iloc[1][id_0])
            score_url[idataframe] = 1. + values_0

    # score of the company names compared to each dataframes in a elegant loop
    for idataframe in range(len(score_name)):

        dataf = table_of_dataframes[idataframe]
        idf = checkIfAny(company_name, dataf.iloc[0])
        id_0 = np.where(idf == dataf.iloc[0])[0]
        values_0 = np.sum(dataf.iloc[1][id_0])
        score_name[idataframe] = 1. + values_0


    return score_url, score_name
