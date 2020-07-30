import numpy as np
import re
# in this piece of code we have the most frequent and useful functions to do some technical things.

def uniqueIndexes(l):
    # This function find the Unique indexes of an array, It's useful if you are looking to divide the
    # array in same objects.
    # This gives the index of the values so if you want the actual values you need to array[res].
    seen = set()
    res = []
    for i, n in enumerate(l):
        if n not in seen:
            res.append(i)
            seen.add(n)
    return res


def find_nearest(array, value):
    # defines the nearest value in array. Pretty self explanatory
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]


def cleanhtml(raw_html):
    # procedure to clean the text from most HTML and JAVA scripts

  cleanr0 = re.compile('<.*?>')
  cleanr1 = re.compile('&nbsp;')
  cleanr2 = re.compile('{.*?}')
  cleanr3 = re.compile('({.*?})')
  cleanr4 = re.compile('(<.*?>)')

  # cleaning process
    # re.sub(compiled cleaning, subsitute, original raw string)
  cleanr = re.sub(cleanr0, ' ', raw_html)
  cleanr_1 = re.sub(cleanr1, ' ', cleanr)
  cleanr_2 = re.sub(cleanr2, ' ', cleanr_1)
  cleanr_3 = re.sub(cleanr3, ' ', cleanr_2)
  cleantext = re.sub(cleanr4, ' ', cleanr_3)

  return cleantext

def checkIfAny(mainStr, listOfStr):
    # procedure to find if s subsubstring is present in a string. It's useful to find a match for the Name and URL matching system.
   for subStr in listOfStr:
       if subStr in mainStr:
           return (subStr)
   return (" ")

def return_indices_of_a(a, b):
  # this returns the indeces of the matched lists
  # it is fundamental for the URL-NAMES scoring because it can provide the right weight for each word easily
    
  b_set = set(b)
  return [i for i, v in enumerate(a) if v in b_set]

def clean_url_name(url):
    #cleaning process to get only the url-core without https/ and domains.
    clean_0 = url.replace('http://www.', ' ')
    clean_05 = clean_0.replace('https://www.', ' ')
    clean_1 = clean_05.replace('.co.uk', ' ')
    clean_2 = clean_1.replace('.org.uk', ' ')
    clean_3 = clean_2.replace('.com', ' ')
    clean_4 = clean_3.replace('.it', ' ')
    clean_5 = clean_4.replace('.co', ' ')
    clean_6 = clean_5.replace('.org', ' ')
    clean_7 = clean_6.replace('.net', ' ')
    clean_8 = clean_7.replace('.uk', ' ')
    return clean_8
