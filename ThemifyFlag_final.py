# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 00:36:55 2017

@author: Amit
"""

import nltk, csv, pandas as pd

csv.field_size_limit(500 * 1024 * 1024)

def themify(DataFile, ThemeFile):
    themelists = {}
    for i in range(len(list(csv.reader(open('testTheme.csv', 'r'))))):
        themelists[str(i+1)] = []
    article_ID = []
    with open('testData.csv', 'r') as stem:
        stem_file = csv.reader(stem)                
        for st_row in stem_file:
            article_ID.append(st_row[0])
            with open('testTheme.csv', 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    #print themelists[row[0]]
                    tokens = nltk.word_tokenize(row[1])
                    for i in tokens:
                        if i in st_row[1]:
                                if tokens.index(i)+1 == len(tokens):
                                    #article_ID.append(st_row[0])
                                    themelists[row[0]].append("1")
                                    print "Found"
                                    print themelists[row[0]]
                        else:
        ##                            print "get the next tokens"
                            #article_ID.append(st_row[0])
                            themelists[row[0]].append("0")
                            break
    print article_ID
    print "----------------------------"
    print themelists
    dataFrame_mid = pd.DataFrame({'articleID': article_ID})
    dataFrame_Final = dataFrame_mid.assign(**themelists)
    dataFrame_Final.to_csv(DataFile[:-4]+"0831_themed.csv", encoding='utf-8')

themify("testData.csv", "testTheme.csv")