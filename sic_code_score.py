import numpy as np
import pandas as pd
import csv

from datasets import *

def check_sic_score(sic):

    # sic code scoring system

    ## load data ##
    ### from the datasets ###
    # convert from set to np array and into np.float_ (32 or 64)
    outer_SIC = np.asarray(list(enduser_sic_codes), dtype= np.float_)  #

    #### SIC CODES ####
    # here are considered the sic codes that have that code at least 5% of companies in the database from each type
    #  ISV + Reseller
    SIC0 = 58290.
    SIC1 = 62011.
    SIC2 = 62012.
    SIC3 = 62020.
    SIC4 = 62090.

    # Recruitment
    SIC5 = 78109.
    SIC6 = 78200.

    # MSP, Telco
    SIC7 = 61900.   # +Vendor + MS
    SIC8 = 63110.
    SIC9 = 61100.

    # Outsourcer
    SIC10 = 46510.   # + Vendor
    SIC11 = 63990.
    SIC12 = 70229.
    SIC13 = 82990.    #+ Vendor  + ManagedServices + ISV + Reseller
    SIC14 = 74909.  # + Vendor
    SIC15 = 70100.   # + Vendor

    # DigitalAgency
    SIC16 = 74100.
    SIC17 = 73110.
    SIC18 = 73120.
    SIC19 = 63120.

    # Distributor
    SIC20 = 46520.
    SIC21 = 46900.

    # Vendor
    SIC22 = 26200.

    # Managed Services
    SIC23 = 62030.

    # these are the most frequent sic codes up to 10% of the total number of the present

    most_freq_sics = np.asarray([SIC0, SIC1, SIC2, SIC3, SIC4, SIC5, SIC6,SIC7, SIC8, SIC9,
                                 SIC10, SIC11, SIC12,SIC13, SIC14, SIC15, SIC16, SIC17, SIC18,
                                 SIC19, SIC20, SIC21, SIC22, SIC23])

    tag = []

    # ENDUSER Skimming
    if any(sic == outer_SIC):
        score = -99.
        id = -99
        tag.append('Enduser')

    else :
        if any(sic== most_freq_sics):
            score = 10.    # score values in case there is the need of sort of statistical values

            # classification output
            id = np.where(sic == most_freq_sics)
            id = id[0]

            # please note that the IDs start at 0
            if (id < 5):
                tag.append('ISV')
            if (id > 1) and (id < 5): # exclude the 62011 and 58290
                tag.append('CloudConsultant')
                tag.append('Vendor')
                tag.append('Reseller')
                tag.append('ManagedServices')
                tag.append('Telco')
                tag.append('MSP')
                tag.append('DigitalAgency')
            if (id == 4 ):
                tag.append('Distributor')
            if (id == 5 ) or (id == 6):
                tag.append('Recruitment')
            if (id == 7) :
                tag.append('Telco')
                tag.append('MSP')
                tag.append('ManagedServices')
            if (id > 7 ) and (id <= 9):
                tag.append('Telco')
                tag.append('MSP')
            if (id > 9) and (id <= 15):
                tag.append('Outsourcer')
            if (id == 13) :   #82990
                tag.append('Vendor')
                tag.append('ManagedServices')
                tag.append('ISV')
                tag.append('Reseller')
            if  (id == 10) or (id == 15) :  # 46510
                tag.append('Vendor')
            if (id > 15  ) and (id  <= 19):
                tag.append('Digital Agency')
            if (id > 19) and (id <= 21):
                tag.append('Distributor')
            if (id == 22):
                tag.append('Vendor')
                tag.append('Reseller')
            if (id == 23):
                tag.append('ManagedServices')
                tag.append('DigitalAgency')
        else :  # if it's not a known enduser sic code and it is out of the most common sic codes provided
            score = 5.
            id = -99
            
    return score, id, tag

