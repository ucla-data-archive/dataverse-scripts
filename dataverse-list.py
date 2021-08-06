#!/usr/bin/env python
# coding: utf-8

# # may have to install:   pip install pyDataverse
import pyDataverse


# In[2]:


# example runs but way too many,  just need DOIs and titles, maybe PI
from datetime import datetime
import sys, re, fileinput
import json
import requests  # http://docs.python-requests.org/en/master/
import pyDataverse
from pyDataverse.api import Api
# establish connection
# example runs but way too many,  just need DOIs and titles, maybe PI
import urllib
from urllib.parse import urlparse
# you need this just-in-case for non-english/latin charactersets
import unicodedata

#outfile = open('D:\work-related\pyDataverse\dvOut2.txt', 'w')
with open('D:\work-related\pyDataverse\dvOut.csv', "w", encoding="utf-8-sig") as outfile:

    #base = 'https://test.dataverse.ucla.edu'
    base = 'https://dataverse.ucla.edu/'
    #base = 'https://dataverse.harvard.edu/dataverse/ssda_ucla'
    print(base)
    rows = 10
    start = 0
    page = 1
    condition = True # emulate do-while
    outfile = open('D:\work-related\pyDataverse\dataverse-info.csv', 'w', encoding="utf-8-sig")
    while (condition):
        url = base + '/api/search?q=*' + "&start=" + str(start)
        print(url)
        data = json.load(urllib.request.urlopen(url))   
        print(data)
        total = data['data']['total_count']
        print ("=== Page", page, "===")
        print ("start:", start, " total:", total)
        for i in data['data']['items']:
            if (i['type']) == 'dataset' or (i['type']) == 'file' and 'doi' in i['url'] and 'handle' not in i['url']:
                print (i['url'])
                line=("\"" + i['name'] + "\"" + "*"   + "," + i['type'] + "*" + i['url'])
                #print(line)
                outfile.write(line)
                outfile.write("\n")
    
        start = start + rows
        page += 1
        condition = start < total

    outfile.close()



