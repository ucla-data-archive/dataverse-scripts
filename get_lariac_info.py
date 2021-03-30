#!/usr/bin/env python
# coding: utf-8

# In[1]:


# from pyDataverse documentation: https://pydataverse.readthedocs.io/en/latest/

import pandas as pd
#from pyDataverse.api import Api
from pyDataverse.api import NativeApi
from pyDataverse.models import Dataverse
import os  # this is so you can grep the current directory
dirpath = os.getcwd()
print("current directory: " + dirpath)
os.chdir(dirpath)


# In[2]:


# establish connection
# class Api(base_url, api_token=None, api_version='v1')
base_url = 'https://dataverse.ucla.edu/'
dv_token = '4eae5f4a-1a86-42a1-9764-cbebc0479a31'
#api = Api(base_url, dv_token)
api = NativeApi(base_url, dv_token)
#api.status


# In[3]:


# get dataverse
#dv = 'ucla'
#resp = api.get_dataverse(dv)
#resp.json()['data']['creationDate']
dv = 'ucla'
resp = api.get_dataverse(dv)
resp.json()['data']['creationDate']


# In[4]:


# get dataset of the lariac4 dataset
identifier = 'doi:10.25346/S6/T4LHZF' 
print("identifier: ", identifier)
resp = api.get_dataset(identifier)
datasetID = resp.json()['data']['publisher']
print("publisher: ", datasetID)
ds_title = resp.json()['data']['latestVersion']['metadataBlocks']['citation']['fields'][0]['value']
print(ds_title)


# In[7]:


# get list of all datafiles in dataset
# The dataset id can be extracted from the response retrieved from the API 
#      which uses the persistent identifier (/api/datasets/:persistentId/?persistentId=$PERSISTENT_IDENTIFIER).
# curl https://dataverse.ucla.edu/api/datasets/21062/versions/3.0/files | jq
# check what version you are up to
# curl https://dataverse.ucla.edu/api/datasets/21062/versions | jq . > filename.json
# curl https://dataverse.ucla.edu/api/datasets/21062/versions | jq
# identifier = 'doi:10.25346/S6/T4LHZF'
# version = '11.0'
#resp = api.get_datafiles(identifier, version)
#print(version)
resp = api.get_dataset(identifier)
datasetID = resp.json()['data']['id']
fileOut = resp.json()['data']
dataset_name = resp.json()['data']['latestVersion']['files'][9]
print(dataset_name)
# print(fileOut['latestVersion']['files'])
print(len(fileOut))
print(type(fileOut))
#print(fileOut)
print(fileOut.keys()) 


# In[8]:


#print(fileOut)


# In[9]:


import json
# output json file
with open('fileout2dv.json', 'w') as outfile:
    json.dump(fileOut, outfile)


# In[10]:


import pandas as pd
# output csv file - read from the previous json file
df = pd.read_json(r'fileout2.json')
df.to_csv (r'fileout2.csv')


# In[11]:


# test downloading file 'bundle'
# /api/access/datafiles/$id1,$id2,...$idN
# pyDataverse:   get_datafile_bundle(identifier)
# identifier is Metadata Id
#fileList = 'doi:10.25346/S6/T4LHZF/C9IZ9T, doi:10.25346/S6/T4LHZF/X2XS2C, doi.org/10.25346/S6/T4LHZF/I2NO6V'
# get_datafile(identifier, is_pid=True)
#file_doi = 'doi:10.25346/S6/T4LHZF/HF0XYG'
#file_id = '22175'
#resp = api.get_datafile(file_id)
#resp.json()


# In[46]:


# use pprint.pprint to get the structure of the metadata output, then pull out what's necessary for a csv file
import pprint
dir(pprint)
print("Number of files: ", len('fileOut'))
print('file id:', fileOut['id'])
print('doi:',fileOut['persistentUrl'])
file_label = resp.json()['data']['latestVersion']['files'][1]['label']
print("file label: ", file_label)
file_id = resp.json()['data']['latestVersion']['files'][1]['dataFile']['id']
print(file_id)
file_URL = resp.json()['data']['latestVersion']['files'][1]['dataFile']["pidURL"]
file_doi = resp.json()['data']['latestVersion']['files'][1]['dataFile']["persistentId"]
print(file_label,", ",file_id, ", ", file_doi, ", ", file_URL)
#print("Individual file structure:")
#pprint.pprint(fileOut)


# In[52]:


total_files = (len(resp.json()['data']['latestVersion']['files']))
print(total_files, " files")
n = 0
#outF = open("myOutFile.txt", "w")
f = open("file-lst2.csv", 'w')
while  n <= (total_files-1):
    #print(n)
    file_label = resp.json()['data']['latestVersion']['files'][n]['label']
    #print("file label: ", file_label)
    file_id = resp.json()['data']['latestVersion']['files'][n]['dataFile']['id']
    #print(file_id)
    file_URL = resp.json()['data']['latestVersion']['files'][n]['dataFile']["pidURL"]
    #print(file_URL)
    file_doi = resp.json()['data']['latestVersion']['files'][n]['dataFile']["persistentId"]
    #print(file_doi)
    line=""
    line=n,file_label, file_id, file_doi ,file_URL
    ','.join(str(line))
    #line = str(n + file_label + file_id + file_doi + file_URL)
    print(line)
    f.write(str(line))
    f.write("\n")
    n = n+1
f.close()


# In[ ]:





# In[ ]:




