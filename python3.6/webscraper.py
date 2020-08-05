import requests
from bs4 import BeautifulSoup
import re
import numpy as np

# 3.6 version compatible need to add a couple of details here

def webscrape_company_number(companynumber, pages=10):
    allText = ""
​
    try:
        response = requests.get(f'http://crawler.iqblade.com:6969/api/scrapesite/{companynumber}/{pages}')
        responseText = response.text
        responseDict = json.loads(responseText)['scrapeData']
​
        if 'metaData' in responseDict:
            meta = responseDict['metaData']
            allText = meta['discription']
​
            keywords = meta['keyWords']
​
            for k in keywords:
                allText = allText + f" {k}"
​
        if 'siteTesxt' in responseDict:
            siteText = responseDict['siteTesxt']
            for key in siteText:
                textBlock = siteText[key]
​
                if textBlock not in allText:
                    allText = allText + f" {textBlock}"
    except:
        print(f"Failed to retrieve site for {companynumber}")
​
    return allText
