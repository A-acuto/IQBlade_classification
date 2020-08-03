import numpy as np
import nltk
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk.corpus  import stopwords
from nltk.stem  import PorterStemmer
from nltk.stem  import WordNetLemmatizer

from usefull_tools import *
from datasets import *


def cleaning_text(intro):

    lemmatizer = WordNetLemmatizer()

    # stopwords list in datasets : nt, year, vebs, 'lore_ipsum, extra, JV_HTML

    char_list = ['-', '_', 'px', '.', '=', 'medium', '+']

    # clean the text from main html issues
    intro_clean = cleanhtml(intro)

    # this is the solution for websites with huge amount of characters. It passes a UNICODE file and
    # if exceeds some values on a single computer it can not process it decently.
    # in case in a better handling of UNICODE files you might reorder by longer
    # element and then keep only the most talkative (e.g. > 4 element)

    if len(intro_clean) > 200000:    # if words from website more than 100000
        intro_clean=intro_clean[0:200000]

    # process of cleaning and tokenization
    tokenlist = nltk.word_tokenize(intro_clean)
    step1 = list(filter(lambda token: nltk.tokenize.punkt.PunktToken(token).is_non_punct, tokenlist))  # take out punctuation
    step2 = [word.lower() for word in step1] # lower the words
    step3 = list(filter(lambda token: token not in stopwords.words('english'), step2)) # remove stopwords
    step4 = list(filter(lambda token: token not in stopwords_nt, step3)) # stopwords from the words -> see datasets
    step5 = list(filter(lambda token: token not in stopwords_year, step4)) # stopwords from year
    step6 = list(filter(lambda token: token not in stopwords_vebs, step5)) # stopwords from verbs and not useful words
    step7 = list(filter(lambda token: token not in stopwords_lore_ipsum, step6)) # stopwords in case there is a lore ipsum text -> not fully formatted website
    step8 = list(filter(lambda token: token not in stopwords_extra, step7)) # extra - HTML words
    step9 = list(filter(lambda token: token not in stopwords_JV_HTML, step8)) # HTML + Javascript words
    step10 = [element for element in step9 if all(ch not in element for ch in char_list)] # remove words that have one of the char in the list
    final_step = [lemmatizer.lemmatize(word) for word in step10]

    tokens = []
    tokens.append(final_step)
    return tokens
