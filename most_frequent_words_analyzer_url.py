import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from usefull_tools import *
import csv
import JSON
from pandas.core.common import flatten
from webscraper import *
from cleaning_text import *

# the basic idea is the same as the INTRO analizer cfr. most_frequent_words_analyzer.py
# but here we use the webscraper to call from the website URL and then use it to analyze it

### LOAD DATA ####
# data_dir #
data_dir = r'C:\Users\User\Desktop\Placement\iqbladecompanydata'
# data = pd.read_csv(data_dir+r'\EXT_C_URL_TEST_UNKNOWN.csv', header=0,  na_values=['#VALUE!', '#DIV/0!'], error_bad_lines=False)#,  na_values=['#VALUE!', '#DIV/0!'])
#df = pd.DataFrame(data, columns=headerx)


try :
    with open(data_dir+r'\file.csv', 'r') as header_test:  # Maybe colliding of string versions with ->  encoding="utf8"
        csv_read = csv.reader(header_test)
        headers = next(csv_read)


    data = pd.read_csv(data_dir+r'\file.csv', header=0,  na_values=['#VALUE!', '#DIV/0!'], error_bad_lines=False)

    # load the data
    df  = pd.DataFrame(data, columns=headers)
    print('CSV Loaded')
except:

    df = pd.read_json(data_dir+r'\file.json')

    df.fillna(value=' ', inplace= True)

    print('JSON Loaded')


# whatever CSV or JSON used load the SIC-data

df = pd.read_json(data_dir+r'\BIG_Telco_URL_WBS.json')

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

for i in range(len(Company_url)):
    Curl = Company_url[i]

    # now calling the webscraper to retreive data from the website
    text = webscrape(Curl)

    # due to unicode transformations to make it work fine with the rest of the cleaning process we need
    # to convert it into a UTF-8 decent format, that's why we do this process

    text_decoded = text.decode(encoding='UTF-8',errors='strict')

    # Cleaning process
    tokens = cleaning_text(text_decoded)

    # add the tokens in a list
    all_tks.append(list(flatten(tokens)))


# transform as before the list into dataframe for counting the words in an easier way
all_tokens = pd.DataFrame(all_tks)

counts_words = []

# as done for the introduction now it loops over the singular elements and count them
for toks in range(len(all_tokens.iloc[0])):
    value_token = all_token[toks].value_counts()

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

title = 'website_most_frequent_words_values_' + EXTRA + '.npz'
np.savez(title, word_value, words_sorted, dimension)

# grep files to be loaded and analyzed
files= glob.glob(dir+r'\website_most_frequent_words_values_' + EXTRA + '.npz')  # * means that loads all the possible SIC CODES available


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

