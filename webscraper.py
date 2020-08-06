import requests
from bs4 import BeautifulSoup
import re
import numpy as np

# webscraper provided by Sadie. Adapted to work on Python 3.5 -> main differences in the string format 

def webscrape(url):   # 3.6 version
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"

    endpoints = [
        "/solutions",
        "/services",
        "/solutions-services",
        "/what-we-do",
        "/about-us"
    ]
    allText = ""

    try:
        response = requests.get(url, timeout=120, headers={'User-Agent': user_agent})

        failed = (response.status_code != 200)
    except:
        failed = True

    if failed:
        #print('{}'.format("\tFailed to retrieve main page for {url}"))
        print(f'Failed to retrieve main page for {url}')
    else:
        rawText = response.text
        soup = BeautifulSoup(rawText, 'html.parser')
        links = list()

        text = soup.find_all(text=True)

        for t in text:
            #t = t.encode(encoding='UTF-8',errors='strict')
            if len(allText) == 0:
                allText = t
            else:
                #allText = allText + '{}'.format("\n"+t)
                allText = allText + f'{t}'
        for e in endpoints:
            #tmpLinkSoup = soup.find_all('a', {'href': re.compile('{}'.format(".{e}/*"))})
            tmpLinkSoup = soup.find_all('a', {'href': re.compile(f'.{e}/*')})
            for tmpLink in tmpLinkSoup:
                if '#' in tmpLink['href']:
                    toAppend = tmpLink['href']
                    toAppend = toAppend.split('#')[0]
                    links.append(toAppend)
                else:
                    links.append(tmpLink['href'])

        links = np.unique(links).tolist()

        if len(links) > 10:  # if more than 10 links pick the 10 shortest
            links = sorted(links, key=len)
            links = links[0:10]

        justDom = url.split('//')[1]

        usedList = list()
        for l in links:
            try:
                if not (l in usedList):
                    if justDom in l:
                        tmpUrl = l
                    else:
                        tmpUrl = url + l

                    tmpUrl = tmpUrl.replace(" ", "%20")

                    tmpResponse = requests.get(tmpUrl, timeout=60, headers={'User-Agent': user_agent})
                    tmpSoup = BeautifulSoup(tmpResponse.text, 'html.parser')
                    text = tmpSoup.find_all(text=True)
                    for t in text:
                        if t not in allText:  # Do not include repetitions of the same bits of site text
                            #allText = allText + '{}'.format("\n{t}")
                            allText = allText + f'{t}'
#                    print('{}'.format("\t Success - {tmpUrl}"))
                    #print(f'Success - {tmpUrl}')
            except:
                #print('{}'.format("\tError for - {tmpUrl}"))
                print(f'Error for - {tmpUrl}')
            usedList.append(l)

    return allText

# 2.7 version
#def webscrape(url):
#    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"#
#
#    endpoints = [
#        "/solutions",
#        "/services",
#        "/solutions-services",
#        "/what-we-do",
#        "/about-us"
#    ]
#    allText = ""#
#
#    try:
#        response = requests.get(url, timeout=120, headers={'User-Agent': user_agent})
#        failed = (response.status_code != 200)
#    except:
#        failed = True#
#
#    if failed:
#        print('{}'.format("\tFailed to retrieve main page for {url}"))
#    else:
#        rawText = response.text
#        soup = BeautifulSoup(rawText, 'html.parser')
#        links = list()
#
#        text = soup.find_all(text=True)
#
#        for t in text:
#            t = t.encode(encoding='UTF-8',errors='strict')
#            if len(allText) == 0:
#                allText = t
#            else:
#                allText = allText + '{}'.format("\n"+t)#
#
#        for e in endpoints:
#            tmpLinkSoup = soup.find_all('a', {'href': re.compile('{}'.format(".{e}/*"))})
#            for tmpLink in tmpLinkSoup:
#                if '#' in tmpLink['href']:
#                    toAppend = tmpLink['href']
#                    toAppend = toAppend.split('#')[0]
#                    links.append(toAppend)
#                else:
#                    links.append(tmpLink['href'])
#
#        links = np.unique(links).tolist()
#
#        if len(links) > 10:  # if more than 10 links pick the 10 shortest
#            links = sorted(links, key=len)
#            links = links[0:10]
#
#        justDom = url.split('//')[1]#
#
#        usedList = list()
#        for l in links:
#            try:
#                if not (l in usedList):
#                    if justDom in l:
#                        tmpUrl = l
#                    else:
#                        tmpUrl = url + l
#
#                    tmpUrl = tmpUrl.replace(" ", "%20")
#
#                    tmpResponse = requests.get(tmpUrl, timeout=60, headers={'User-Agent': user_agent})
#                    tmpSoup = BeautifulSoup(tmpResponse.text, 'html.parser')
#                    text = tmpSoup.find_all(text=True)
#                    for t in text:
#                        if t not in allText:  # Do not include repetitions of the same bits of site text
#                           allText = allText + '{}'.format("\n{t}")
#                    print('{}'.format("\t Success - {tmpUrl}"))
#            except
#                print('{}'.format("\tError for - {tmpUrl}"))#
#
#            usedList.append(l)
#
#    return allText
