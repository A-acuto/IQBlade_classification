import numpy as np
import pandas as pd
import sys
import os
import csv
import json
import glob
from pandas.core.common import flatten
from multiprocessing.pool import ThreadPool as Pool

from webscraper import *
from cleaning_text import *
from usefull_tools import *

# Same code as most_frequent_analyzer_url but with multiprocessing application for speed up
# the basic idea is the same as the INTRO analizer cfr. most_frequent_words_analyzer.py
# but here we use the webscraper to call from the website URL and then use it to analyze it

### LOAD DATA ####
# data_dir #


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


SIC = df.sic_text_1
SIC = SIC.replace(' ', 0)
SIC = SIC.replace('None Supplied', 0)
SIC.fillna(value=0, inplace=True)

Company_url = df.companyurl
Company_url = Company_url.replace('',0)
Company_url = Company_url.replace('None Supplied', 0)
Company_url.fillna(value=0, inplace=True)

# SIC codes and URL cleaned by none supplied and empty values

# Loop over the companies in the file. Here there is a different because I do not divide by sic CODE. I can do that too.

pool_size = 6 # number of processes opened to run the code. you can also use multiprocessing.cpu_count() or os.cpu_count() to use all the cps available 

# definition of the function that need to be looped
# this is just what happened in the previous code in the loop, so webscraping, cleaning and storing 
def worker(url_r, all_tks):
    text = webscrape(url_r)
    tokens = cleaning_text(text)
    all_tks.append(list(flatten(tokens)))
    return all_tks

pool = Pool(pool_size) # creation of the pool
all_tks= []

# multiprocess 
for i in range(len(SIC)):
    Curl = Company_url[i]
    pool.apply_async(worker, (Curl,all_tks,))

pool.close()
pool.join()

# transform as before the list into dataframe for counting the words in an easier way
all_tokens = pd.DataFrame(all_tks)

# from now on, just the same
counts_words = []

# as done for the introduction now it loops over the singular elements and count them
for toks in range(len(all_tokens.iloc[0])):
    value_token = all_tokens[toks].value_counts()

    # due to the huge number of elements involved I decided to slice it up.
    # to the 50% of all value token
    counts_words.append(value_token[0:int(len(value_token)/2.)])

# created a dataframe for easier handling
Counted_words = pd.DataFrame(counts_words)
Counted_words.fillna(value=0, inplace=True)

dimension = Counted_words.shape[0]

#
idx = Counted_words.columns

# create a vector for the recurrencies
word_value = np.zeros(len(idx))

for icolumn in range(len(idx)):
    total = Counted_words[idx[icolumn]].sum()

    id0 = np.where(Counted_words[idx[icolumn]]> 0)[0]   # always [0] to have an index

    word_value[icolumn] = total

id_sorted = word_value.argsort()[::-1]   # this sorts the words by the most frequent to the least

word_value =word_value[id_sorted]
words_sorted = idx[id_sorted]

title = 'website_most_frequent_words_values_MT_'+extra+'.npz'
np.savez(title, word_value, words_sorted, dimension)

# grep files to be loaded and analyzed
file = os.path.join('website_most_frequent_words_values_MT_'+extra+'.npz')
files= glob.glob(file)  # * means that loads all the possible SIC CODES available


# in case you want to analyze and see it
for x in files:
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

