import numpy as np
import pandas as pd
from pandas.core.common import flatten
import sys
import csv
import json

from webscraper import *
from score_name_url import *
from decision_matrix import *
from usefull_tools import *
from score_intro_sic_codes import *
from score_web_text import *

# MAIN CODE #

#### LOAD DATA ####
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


# load the data and clean in case there are not available or other issues
sic_codes = df.sic_text_1
company_url = df.companyurl
primary_type = df.primary_type_id
introduction = df.introduction
company_name = df.company_name
company_number = df.company_number

sic_codes = sic_codes.replace('', 0)
sic_codes = sic_codes.replace('None Supplied', 0)
sic_codes.fillna(value=0, inplace=True)

introduction = introduction.replace('', 'None')
introduction = introduction.replace('None Supplied', 0)
introduction.fillna(value='None', inplace=True)

company_url = company_url.replace('', 0)
company_url = company_url.replace('None Supplied', 0)
company_url.fillna(value=0, inplace=True)

primary_type = primary_type.replace('', 0)
primary_type = primary_type.replace('None Supplied', 0)
primary_type.fillna(value=0, inplace=True)

# LOOP over the companies
for i in range(len(sic_codes)):
    sic =np.int64(sic_codes[i])
    url = company_url[i]
    primary_type_0 = primary_type[i]
    intro = introduction[i]
    c_number = company_number[i]
    name = company_name[i]


    # score Sic code and evaluate in case of enduser
    score_sic, id, tag = check_sic_score(sic)


    # In case the sic score is -99 it is automatically classified as ENDUSER
    if score_sic != -99.:


        # Classify and evaluate the Url and NAME
        score_url_val, score_name_val = score_url_name(url, name)

        # check the results internal
        url_perc, url_tag, name_perc, name_tag = check_score(score_url_val, score_name_val)

        # check the introductions
        intro_tokens = clean_text(intro)

        tokens = list(flatten(intro_tokens))
        flags_intro = score_intro_sic_codes(tokens)

        # out the introduction flags divided by sic codes
        web_text = webscrape(url)

        wb_text = web_text.decode(encoding='UTF-8', errors='strict')
        wbs_tokens = clean_text(wb_text)

        tokens_web = list(flatten(wbs_tokens))
        flags_web = score_web_text(tokens_wev)

        #### CROSS validation ####

        flags_intro_cross = score_intro_sic_codes(tokens)

        flags_wbs_cross = score_web_text(tokens_2)

        perc_max_intro, max_rag_intro, perc_30_intro, tag_30_intro = check_score_intro(flags_intro)

        perc_max_wbs, max_rag_wbs, perc_30_wbs, tag_30_wbs = check_score_web_text(flags_wbs)

        perc_max_intro_co, max_rag_intro_co, perc_30_intro_co, tag_30_intro_co = check_score_intro(flags_wbs_cross)

        perc_max_wbs_co, max_rag_wbs_co, perc_30_wbs_co, tag_30_wbs_co = check_score_web_text(flags_intro_cross)

        feed_matrix = []
        feed_matrix = tag+ url_tag+name_tag+max_rag_intro+max_rag_wbs+max_rag_intro_co+max_rag_wbs_co

        output = decision_matrix_variable(feed_matrix)

    else:

        print('Enduser spotted')

