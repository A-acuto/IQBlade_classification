# IQBlade_classification
IQBlade classification tools 

Python version 3.5, should be compatible with 3.6+ versions. Should also work properly in non-windows environment.


The codes available are the text analizer code from introduction (from IQBlade database) and the URL scraped text.
Then the classification and scoring by SIC codes, names, url, introduction and url.

# Required packages:
* Numpy
* Pandas
* Matplotlib
* re
* NLTK (natural language toolkit)
* beatifoul soup
* requests

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
 
# CODES DESCRIPTION Details

* Tools: here are the quick functions that might be useful in many other different codes: as finding the index of unique elements in arrays or dataframes, verify the presence of sbstrings in strings for classification of names and urls. In general it is called in every other main codes for reference.

* Webscraper from URL: code that pulls requests to get text directly from websites. It is an adapted version of Sadie's webscraper to match the Python version.

* sic_code_score : sic code scorer that identifies if a sic code belongs to an enduser or to a classified company. The sic codes provided are at least the 5% of the classified companies in the database. It provides the associated tag and it is used for the Main and Decision Matrix. It needs the file Datasets (for the enduser sic codes)

* url_name_score: the first part of the code creates the way to score the name and url of companies and then provides a scoring for each category for those. The second part instead matches the score with the company tag.

* cleaning_text: function that cleans the introduction and text scraped from website it is used in the cleaning process of the main and for URL scoring. It needs dataset because there are loaded the stopwords used to clean.

* score_intro_sic_code : this is the scoring system for introduction (and later in the cross validation for webscraped text) divided by company types and sic codes. This need the datasets present in the file to create the matches. The logic behind is very close to the url_name_score.

* score_web_text : as the score intro, but it uses the text scraped form websites for calibration. 

* Main code code included

* datasets: code where are stored all the list or sets of words used in the classification, enduser sic code identification. 

# Code efficiency tests
- No 20% most likely in the analysis. 29/48 right, timing on windows pc 6/7 minutes [single core]
- with 20% same results with the same 6 minutes timing
