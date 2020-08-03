import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
from numpy import inf
import pickle
from collections import Counter
import re
import glob
import os

# Natural language processing
import nltk
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk.corpus  import stopwords
from nltk.stem  import PorterStemmer
from nltk.stem  import WordNetLemmatizer
from nltk.util import ngrams

# local codes
from usefull_tools import *
from datasets import *   # here are all the sets of words used for cleaning

# load the data directory with your pathline
### data_dir ####

# loading the JSON file it's better because it keeps the shape and do not break as a CSV file for the introduction files
# let's load the data in case of a CSV or a JSON file
try :
    file = os.path.join(data_dir, 'file.csv')
    with open(file, 'r') as header_test:  # Maybe colliding of string versions with ->  encoding="utf8"
        csv_read = csv.reader(header_test)
        headers = next(csv_read)


    data = pd.read_csv(file, header=0,  na_values=['#VALUE!', '#DIV/0!'], error_bad_lines=False)

    # load the data
    df  = pd.DataFrame(data, columns=headers)
    print('CSV Loaded')
except:
    file = os.path.join(data_dir, 'file.json')
    df = pd.read_json(file)

    df.fillna(value=' ', inplace= True)

    print('JSON Loaded')


# whatever CSV or JSON used load the SIC-data

# This loads the SIC codes
# Don't know if the name could be changed from the download from the database, so I will keep it standard

SIC = df.sic_text_1
SIC = SIC.replace(' ', 0)
SIC = SIC.replace('None Supplied', 0)
SIC.fillna(value=0, inplace=True)

# SIC codes loaded and cleaned by "none supplied" or missing data

# UniqueIndexes find the indexes of unique SIC Codes, so it is easier to group them by SIC CODES
index_SIC = uniqueIndexes(SIC)

Unique_SIC_CODES =np.asarray(SIC[index_SIC])   # this are the Unique SIC codes present in the datafile

# This is the loading of the introduction
intro = df.introduction

# this is used to analyze the text properly, comes from the python package NLTK
lemmatizer = WordNetLemmatizer()


## loop over the SIC numbers to create a singular value for each category
for i in range(len(index_SIC)):

    id_sic = np.where(SIC == Unique_SIC_CODES[i])[0]

    if len(id_sic)>=10:     # so if the number of sic codes present is greater than 10 then proceed in the analysis

        #id_tk2 = []  # Bigrams
        #id_tk3 = []  # trigrams
        all_token =[]

        for element in range(len(id_sic)):
            intro_sel=  intro[id_sic[element]]

            if intro_sel:

                # cleaning process of the introduction
                intro_sel = cleanhtml(intro_sel)
                tokenlist = nltk.word_tokenize(intro_sel)

                tk_2 = list(filter(lambda token: nltk.tokenize.punkt.PunktToken(token).is_non_punct, tokenlist))
                tk_3 = [word.lower() for word in tk_2]
                tk_4 = list(filter(lambda token: token not in stopwords.words('english'), tk_3))
                tk_5 = list(filter(lambda token: token not in stopwords_nt, tk_4))
                tk_6 = list(filter(lambda token: token not in stopwords_year, tk_5))
                tk_65 = list(filter(lambda token: token not in stopwords_vebs, tk_6))
                tk_7 = [lemmatizer.lemmatize(word) for word in tk_65]

                # here all the singular token are stored
                all_token.append(tk_7)

                # in case someone needs to add N-Grams this should be the place

                #bigrams = ngrams(tk_7, 2)
                #trigrams = ngrams(tk_7, 3)

                #id_tk2.append(Counter(bigrams).most_common(5))
                #id_tk3.append(Counter(trigrams).most_common(5))

        token_dataframe = pd.DataFrame(all_token)

        # here you can create the dataframe for N-Grams
        #bigrams_dataframe = pd.DataFrame(bi_grams)

        counts_words = []

        for toks in range(len(token_dataframe.iloc[0])):
            value_token = token_dataframe[toks].value_counts()

            # count each singular words
            counts_words.append(value_token)

        Counted_words = pd.DataFrame(counts_words)

        Counted_words.fillna(value=0, inplace= True)

        dimension = Counted_words.shape[0]

        # Now I proceed in the matching between the words and the repetition found in the dataframe
        idx = Counted_words.columns

        # create a vector for the recurrencies
        word_value = np.zeros(len(idx))

        for icolumn in range(len(idx)):   # loop over the dataframe columns
            total = Counted_words[idx[icolumn]].sum()  # Sum over the same word

            id0 = np.where(Counted_words[idx[icolumn]] > 0)[0]
            word_value[icolumn] = total

        id_sorted = word_value.argsort()[::-1]   # this sorts the words by the most frequent to the least

        word_value =word_value[id_sorted]
        words_sorted = idx[id_sorted]

        # in case you want only the most frequent (max / 5)  let's use this bit of code
        #id_much = np.where(word_value >= np.max(word_value)/5.)[0]
        #most_frequent = words_sorted[id_much]

        # SAVING FILE in NPZ (easier to deal with in python environment,
        # please note that the order of the file might be different while you are recalling it) ##
        # you should substitute EXTRA with the name you want #
        title = 'SIC_'+str(Unique_SIC_CODES[i])+'_values_'+EXTRA+'.npz'

        np.savez(title, word_value, words_sorted, dimension)  ## add the most frequent and so on...

# out of the loop

# grep files to be loaded and analyzed
outfile =os.path.join(dir, 'SIC_*_values_'+EXTRA+'.npz')
files= glob.glob(outfile)  # * means that loads all the possible SIC CODES available


for x in files:
    # loop over the files loaded

    sic_code = str(x[-19:-14]) # in case you need to retrive back the sic code associated with the analysis

    with np.load(x, allow_pickle=True) as data:
        # load the data

        word_values = data['arr_0']     # in the saved file is word_values
        words = data['arr_1']           # is words_sorted
        dim = data['arr_2']             # dimension



        if len(word_values) > 0:
            threshold = np.max(word_values)/10.
        else :
            threshold =1

        max1 = np.where(word_values >= threshold)[0]

    max_val = word_values[max1]
    most_frequent_words = words[max1]

    for iwords in range(len(most_frequent_words)):
        print(max_val[iwords], most_frequent_words[iwords])


