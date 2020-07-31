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

def type_comp_max(id):
    # Code that associates the tag at the maximum value from URL and NAME scoring
    id = np.asarray(id)

    # must keep this order or change also the order of the loaded companies in the scoring code
    company_type = ['Recruitment', 'ISV', 'Telco', 'Vendor', 'CloudConsultant',
                    'ManagedServices', 'MSP', 'DigitalAgency', 'Reseller',
                    'Distributor', 'Outsourcer']
    ctype =[]

    for icompany in range(11):
        if any(id == icompany):
            ctype.append(company_type[icompany])

    # output company score flag
    return ctype

# For introduction scoring
def type_comp_max_intro(id):
    id = np.asarray(id)
    ### this is matched with intro score that's why we have so many company repetitions
    company_type =['Recruitment', 'Recruitment', 'ISV', 'ISV', 'ISV','ISV',
                   'Vendor', 'Vendor', 'Vendor', 'CloudConsultant',
                   'CloudConsultant', 'CloudConsultant', 'MSP', 'MSP',
                   'ManagedServices', 'ManagedServices', 'ManagedServices',
                   'Telco', 'Telco', 'DigitalAgency', 'DigitalAgency', 'DigitalAgency',
                   'DigitalAgency', 'Distributor', 'Distributor', 'Reseller', 'Reseller',
                   'Reseller', 'Reseller', 'Outsourcer', 'Outsourcer', 'Outsourcer']
    ctype =[]

    for icompany in range(len(company_type)):
        if any(id == icompany):
            ctype.append(company_type[icompany])
#
    return ctype

def check_score_intro(flags):

    score_max_per = []
    score_max_tag = []
    score_30_per = []
    score_30_tag = []

    max_val = np.max(flags)

    if max_val > 0.:
        count = np.where(flags == max_val)[0]

        if len(count) < 20 :

            id_max = np.where(flags == max_val)[0]

            # this is for getting the least likely result
            min_30 = max_val- max_val*0.25

            id_most_l = np.where(flags >= min_30)[0]
            id_most_m = np.where(flags < max_val)[0]
            id_most = np.intersect1d(id_most_l, id_most_m)

            score_max_per.append(flags[id_max])
            score_30_per.append(flags[id_most])
            # here I have added the maximum percentage
            score_max_tag.append(type_comp_max_intro(np.asarray(id_max)))
            score_30_tag.append(type_comp_max_intro(np.asarray(id_most)))
            # here I have instead added the flags

        else :
            score_max_per.append(' ')
            score_30_per.append(' ')
            score_max_tag.append('0')
            score_30_tag.append('2')

    else:

        score_max_per.append(' ')
        score_30_per.append(' ')
        score_max_tag.append('x')
        score_30_tag.append('2')

    return score_max_per, score_max_tag, score_30_per, score_30_tag

def check_score_web_text(flags):

    score_max_per = []
    score_max_tag = []
    score_30_per = []
    score_30_tag = []

    max_val = np.max(flags)

    if max_val > 0. :
        count = np.where(flags == max_val)[0]

        if len(count) < 8:

            id_max = np.where(flags == max_val)[0]

            min_30 = max_val - max_val * 0.25
            id_most_l = np.where(flags >= min_30)[0]
            id_most_m = np.where(flags < max_val)[0]
            id_most = np.intersect1d(id_most_l, id_most_m)

            score_max_per.append(flags[id_max])
            score_30_per.append(flags[id_most])
            score_max_tag.append(type_comp_max_web_text(np.asarray(id_max)))
            score_30_tag.append(type_comp_max_web_text(np.asarray(id_most)))

        else :
            score_max_per.append(' ')
            score_30_per.append(' ')
            score_max_tag.append('0')
            score_30_tag.append('1')

    else :
        score_max_per.append(' ')
        score_30_per.append(' ')
        score_max_tag.append('Y')
        score_30_tag.append('1')

    return score_max_per, score_max_tag, score_30_per, score_30_tag
