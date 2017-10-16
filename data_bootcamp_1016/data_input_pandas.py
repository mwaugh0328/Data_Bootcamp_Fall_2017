# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 10:15:27 2017

@author: mwaugh

We've been rolling a long, now lets get data into the computer and start to 
work with it...

"""


#%%
import pandas as pd # as ususall we need to read in the pandas package...
import os 

#%%
# Lets first test this out, we are going to read in a .csv file from the internet
# so this will use the command ``pd.read_csv() where we put in either the local
# location in the brackets or a url...

url1 = "https://raw.githubusercontent.com/NYUDataBootcamp"
url2 = "/Materials/master/Data/test.csv"
url = url1 + url2 # I love this feature...

df = pd.read_csv(url)

print(df.head())
print(df.shape)
print("\n", df)

#Why not just type in the url and look at it...what is it show us.... 
#NOTE, remember those other .csv files you posted, can you read those in as well

df_only2 = pd.read_csv(url, nrows = 2)
print("\n", df_only2)

# Then this is cool too, set certain values to be read in as NaN (not a number)

df_noone = pd.read_csv(url, na_values = 1)
print("\n", df_noone)


#%%
# Now lets read in an excel file....

url3 = "/Materials/master/Data/test.xls"
url = url1 + url3

df_excel = pd.read_excel(url, na_values = 1) # Simmilar funcitonality!
print("\n", df_excel)



#%% Excercises...

#url4 = "Materials/master/Data/test0.csv"
url = url1+ url2

df_test = pd.read_csv(url, index_col = 0) # This tells it what the index should be

print("\n", df_test)

df_excel2 = pd.read_excel(url1+url3+"x")
print("\n", df_excel2)

df_noonesix = pd.read_csv(url, na_values = [1,6]) # Just create a list!
print("\n", df_noonesix)

#%%

path = "C:\\data_bootcamp\\test.csv"
# ON PCS...NEED TO CHANGE THE SLASHES!!!!!!!!!!!
# IF you just cut and past from the file explorer window...it would look like
# this...
# C:\data_bootcamp\test.csv

dfnew = pd.read_csv(path)

# Then here is a way jsut to work within your current directory...

file = "test.csv"
print("Current working directory is", os.getcwd())
print("Is our file here", os.path.isfile(file))

df = pd.read_csv(file)
print("\n",df)

#%%
###############################################################################
# Now lets practice reading in some real data and doing some stuff with it...
# We are going to skip the penn world table example, why, we will come back to 
# it later in a week...

url1 = 'https://www.imf.org/external/pubs/ft/weo/'
url2 = '2017/02/weodata/WEOOct2017all.xls'

url = url1 + url2

weo = pd.read_csv(url1+url2,
                  sep='\t',                 # \t = tab
                  thousands=',',            # kill commas
                  na_values=['n/a', '--'])  # missing values

# This data set is mess, and think, its the IMF's job to make this stuff readable
# but this is the world that we live in... this from the book...
'''
Keep in mind that it took us an hour or two to figure all this out.
You can get a sense of where we started by running the read_csv 
statement without the last two arguments and listing its dtypes. 
You'll notice that variables you might expect to be floats are 
objects instead.
'''

'''
Exercise. Download the WEO file. What happens when you open it in Excel? 
(You can use the link in the code. Or Google "imf weo data", 
look for the most recent link, and choose Entire Dataset.)
'''
'''
Exercise. Why were we able to spread the read_csv() statement over 
several lines?
'''

'''
Exercise. Google "python pandas weo" to see if someone else has figured out 
how to read this file.
'''

'''
Exercise. How big is the DataFrame weo? What variables does it include?
'''

''' 
Use the statement weo[[0, 1, 2, 3, 4]].head() to see what the first five 
columns contain.
'''

just_gdp_weo = weo[weo["WEO Subject Code"] == "NGDP"]

#%%
###############################################################################

url = 'http://dx.doi.org/10.1787/888932937035'
pisa = pd.read_excel(url,
                     skiprows=18,             # skip the first 18 rows
                     skipfooter=7,            # skip the last 7
                     parse_cols=[0,1,9,13],   # select columns of interest
                     index_col=0,             # set the index as the first column
                     header=[0,1]             # set the variable names
                     )

# Note that the columns thing is intersting, if you look at the excel file,
# this looks odd, but as is the excel file is hiding certain columns...

pisa = pisa.dropna()

pisa.columns = ['Math', 'Reading', 'Science']  

pisa.Math.describe()

pisa.corr()

#pisa['Math'].plot(kind='barh')

pisa[pisa.index == "United States"] / pisa.mean()

pisa[pisa.index == "Singapore"] / pisa.mean()