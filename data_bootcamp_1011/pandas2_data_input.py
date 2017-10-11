# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 13:37:46 2017

@author: mwaugh
"""

import pandas as pd # we need to do this to get the pandas package...

url1 = 'https://raw.githubusercontent.com/NYUDataBootcamp'
url2 = '/Materials/master/Data/test.csv'
url  = url1 + url2        # location of file

# This is super cool, but we should understand this...we created a string, it
# just happens to bea url or web address... 


df = pd.read_csv(url)     # read file from the web and assign it to df

dfsmall = pd.read_csv(url, nrows = 2)     # read file from the web and assign it to df

dfna = pd.read_csv(url, na_values=[1, 2])

dfna.iloc[0,2]

# What does this do...
#%%
###############################################################################
# Now we can read in excell files...
urlx = '/Materials/master/Data/test.xls'

url = url1 + urlx # What am I doing here...

dfx = pd.read_excel(url) 

#%%
###############################################################################
# Here is some real data that we can jsut play around with and practice with...
'''
"https://raw.githubusercontent.com/fivethirtyeight/data/master
/college-majors/recent-grads.csv
'''

cm_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/"
cm_url = cm_url + "college-majors/recent-grads.csv"

df = pd.read_csv(cm_url) 

print(df.head)

print(df.columns)

df[["Unemployment_rate", "Major"]].sort(columns = "Unemployment_rate")