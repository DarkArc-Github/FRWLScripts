# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 00:36:55 2017

@author: Amit
"""

import nltk, csv, pandas as pd

csv.field_size_limit(500 * 1024 * 1024)

def themify(DataFile, ThemeFile):
    themelists = {}
    for i in range(len(list(csv.reader(open(ThemeFile, 'r'))))):
        print(str(i+1))
        themelists[str(i+1)] = []
    article_ID = []
    input()
    with open(DataFile, 'r', encoding='utf-8') as stem:
        stem_file = csv.reader(stem)
        for st_row in stem_file:
            article_ID.append(st_row[0])
            print(st_row[0])
            with open(ThemeFile, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    #print themelists[row[0]]
                    tokens = nltk.word_tokenize(row[2])
                    for i in tokens:
                        if i in st_row[3]:
                                if tokens.index(i)+1 == len(tokens):
                                    themelists[row[0]].append("1")
##                                    print "Found"
##                                    print themelists[row[0]]
                        else:
##                            print "get the next tokens"
                            themelists[row[0]].append("0")
                            break
##    print article_ID
##    print "----------------------------"
##    print themelists
    print(len(article_ID))
    for t in themelists:
        print(len(t))
    dataFrame_mid = pd.DataFrame({'articleID': article_ID})
    dataFrame_Final = dataFrame_mid.assign(**themelists)
    dataFrame_Final.to_csv(DataFile[:-4]+"0831_themed.csv", encoding='utf-8')

themify("Theme_4sources_08-31_utf8.csv", "Revised_Themes_Aug 29.csv")