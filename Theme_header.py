# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 21:11:08 2017

@author: Amit
"""

import nltk
import csv
import pandas as pd
csv.field_size_limit(500 * 1024 * 1024)

def themify(fileName):
    article_List = list()
    token_list = list()
    date_List = list()
    with open(fileName, 'r') as stem:
        stem_file = csv.reader(stem)
        i = next(stem_file)
        print(i)

themify("RT_Aug30.csv")