# IQBlade_classification
IQBlade classification tools 

The code requires python 3.6 

The codes available are the text analizer code from introduction (from IQBlade database) and the URL scraped text.
The classification and scoring by SIC codes, names, url, introduction and url (webscraped).

# Updates
multiprocessing for url text available

Compatible with Linux, windows and MacOS (not Tested)

Working in python 3.6, with possibilty to switch back to 2.7 if wanted (please note that the webscraper do fail in retrieving the links in the python2.7 version, so the classification it's worst)

Cleaned the issue with empty url or introduction and the creation of list of list items for the decision matrix and classification

# Required packages:
Added a requirement.txt from pip with packages versions.
* os 
* Numpy
* Pandas
* Matplotlib
* re
* NLTK (natural language toolkit) + words databases as PUNKT, wordnet Added in the code - VERSION == 3.4.5 to work on python 2.7 
* beatifoul soup
* requests
* glob (for most common words analyzer)
* multiprocessing

# Data handler
* CSV
* pickle
* JSON
* numpy

# CODES AVAILABLE UPDATED
* Decision Matrix
* Tools  # Common tools used in different codes
* most_frequent_words_analyzer # introduction based most frequent words analyzer
* Webscraper from URL # Adapted from Sadie's code to work in Python 3.5 (only the f-string changed)
* most_frequent_words_analyzer_url  
* sic_code_score 
* url_name_score # URL and NAME scorer and flag tag checker
* cleaning_text # code that cleans the introduction and webscraped text
* score_intro_sic_codes 
* score_web_text
* classification_main
* datasets
* most_frequent_words_analyzer_url (multiprocess version)
* most_frequent_words_analyzer_intro (multiprocess version)
* requirement.txt available with pip packages required
* json document to test
 
# CODES DESCRIPTION Details

* Tools: here are the quick functions that might be useful in many other different codes: as finding the index of unique elements in arrays or dataframes, verify the presence of sbstrings in strings for classification of names and urls. In general it is called in every other main codes for reference.

* Webscraper from URL: code that pulls requests to get text directly from websites. It is an adapted version of Sadie's webscraper to match the Python version.

* sic_code_score : sic code scorer that identifies if a sic code belongs to an enduser or to a classified company. The sic codes provided are at least the 5% of the classified companies in the database. It provides the associated tag and it is used for the Main and Decision Matrix. It needs the file Datasets (for the enduser sic codes)

* url_name_score: the first part of the code creates the way to score the name and url of companies and then provides a scoring for each category for those. The second part instead matches the score with the company tag.

* cleaning_text: function that cleans the introduction and text scraped from website it is used in the cleaning process of the main and for URL scoring. It needs dataset because there are loaded the stopwords used to clean.

* score_intro_sic_code : this is the scoring system for introduction (and later in the cross validation for webscraped text) divided by company types and sic codes. This need the datasets present in the file to create the matches. The logic behind is very close to the url_name_score.

* score_web_text : as the score intro, but it uses the text scraped form websites for calibration. 

* Main code code included, added version to avoid linux-windows-MAC directory issues

* datasets: code where are stored all the list or sets of words used in the classification, enduser sic code identification. 

# Code efficiency tests
_Python 3.6_
- Efficiency up to 83% (40/48 - after fixing empty classification (recruitment). Working on the recalibration of outsourcer and reseller), timing on single core up to 10-11 minutes (due to retrieving links)

_Python 2.7_
- No 20% most likely in the analysis. 29/48 right, timing on windows pc 6/7 minutes [single core]
- with 20% same results with the same 6 minutes timing
- in cluster linux : same results, but ~9 minutes in working time. single core
