# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 10:19:01 2017

@author: mwaugh
"""

# Intro to pandas "pan"nel "da"ta "s"tructures. Powerfull, intuitive, data analysis
# tool. This package convinced me to learn and start to use python as a research tool
# Developed at AQR (a quantative hedgfund) by Wes Mckinney. They made it open source
# and quickly expanded developed and became widely used. 

#%%
# First we need to import the pandas package...very simmilar to when we imported
# our functions, but this is a MUCH larger. Further more, this is what makes pandas
# a higher-level addon to python. That is at a lower level the objects, methods, functions...
# are already created for us, then when we import pandas they are ready to go.

import pandas as pd

# This says import the package pandas then the "as pd" says call it pd (our alias)
# this just simplifys our life without having to always be typing pandas, we jsut
# type pd

#%%
# LEts first create some data...we have worked iwth this beofor...

data = {"GDP": [5974.7, 10031.0, 14681.1],
                   "CPI": [127.5, 169.3, 217.488],
                   "Year": [1990, 2000, 2010],
                   "Country": ["US", "US", "US"]}
# what kind of data structure is this

print(type(data))

# It should tells us that it is a dictionary, with keys and values (which are lists)

#%%
# Now we are going to convert the type of data to a "DataFrame" this is the key
# oject within pandas. (If familir with R this is simmialr to their dataframe)

df = pd.DataFrame(data)

# now lets check the type of df which should say somethign to the effect of being
# a dataframe
print("\n", type(df))

# Now lets see how cool this is, return to the original data and lets look at it
print(data)

# OK, while fine, we can mentally visulize that there are some keys then vaules 
# and how they line up, but it is not NATURAL. Its is not like looking at an excel
# file...
# lets contrast this with the dataframe of the same exact data...

print(df)

# This lays out the data in a very intuitive way, colums defined by the keys...
# values as rows...literally like an excell file. Amazing. You may be thinking...
# so what, well there is a reason why excell is popular, it is natural for people
# do think about data in a table like formate, a dataframe is always going to 
# present this in this intuitive, natural way. This is also important because it
# helps us visualize and then implement calcuations, operations, on the table. 
# Where as this could be very hard to do in the data variable above.

# 

#%%
# In python remember the datafame is an object and with that object comes methods
# and attributes (we have seen less attributes, but lots of methods)

# so lets find the shape of this...

print(df.shape) # Note that this is an attribute not a method as the method 
# takes in arguments through () where as this just asks what is the shape of df

# And then we can learn about the columns...

print(df.columns) # which returns an object...but we can get it to a list.
print(df.columns.tolist())
# A couple of things about the command above, .columns is an attribute, .tolist()
# is a method. AND note how we can combine multilpe operations....

# So what about the rows....one of the powerful, features of a dataframe is that
# implicity there is a natural index created for the dataframe... so to see this
print(df)
print(df.index) # which is like a range type, but within pandas...
print(df.index.tolist())

# Now what kind of data do we have, strings, numbers, etc.... the dataframe can
# tell us...

print(df.dtypes) # this is an attribute on the dataframe, simmilar to type

# So this is interesting, for the numerical values it says that they are flaoting
# point vlaues, that is great. For the names, strings, it says that they are objects
# NOT stings? Pandas does this (i) if all the data in a column is a number, then 
# it is recognized as a number (ii) if not, then it is just going to be an object

#%%
# Excercises....
pwt_data = {'countrycode': ['CHN', 'CHN', 'CHN', 'FRA', 'FRA', 'FRA'],
        'pop': [1124.8, 1246.8, 1318.2, 58.2, 60.8, 64.7],
        'rgdpe': [2.611, 4.951, 11.106, 1.294, 1.753, 2.032],
        'year': [1990, 2000, 2010, 1990, 2000, 2010]}
pwt = pd.DataFrame(pwt_data)

print("\n", pwt)

# Note that this is the definition of a pannel data set, that is it has a 
# "cross-section" that is several countries, France and China in this case, that 
# are followed over time. So we see the same cross-section over and over again.

"""
What are the dimensions of pwt?
"""
print("\n","Rows", pwt.shape[0], "Columns", pwt.shape[1])

"""
What dtypes are the variables? What do they mean?
"""
pwt.dtypes

"""
What does pwt.columns.tolist() do? How does it compare to list(pwt)?
Its the same, not sure why???
"""
"""
Challenging. What is list(pwt)[0]? Why? What type is it?
"""
list(pwt)[0]

"""
Challenging. What would you say is the natural index? How would you set it?
"""
pwt.set_index(['year']) 

#If you said year, this will do it.
 
###############################################################################
#%% Calculations on a dataframe...

# One thing to note is that a column is of a different data type, its called a 
# Series

print(type(df["GDP"]))

# then it is easy to do optionation on a series...


print(df["GDP"] + df["GDP"])

print(df["GDP"] / df["CPI"]) # This would be real gdp

print(100*df["GDP"] / df["GDP"][0]) # what is this doing...if you remeber from EGB
# This is a way to index GDP by the first entry...

# Then it is super easy to create a new column based on an operation or existing
# columns, almost excel like...

df['RGDP'] = df['GDP']/df['CPI']

df['GDP_div_1000'] = df['GDP'] / 1000

print("\n",df) # so there is a new column called real gdp now...

# See the digressioini n the book....I don't mind doing this...

print("\n",df.RGDP)
#%%
###############################################################################
# HEre are some more things we can do...

df.columns = ["cpi", "country", "gdp", "year", "rgdp", "gdp_div_1000"]
# What if the elelments here were less than the number of columns?

df.columns = [var.upper() for var in df.columns]
# HEre we can use list comprehension to change the neames in columns in the way
# we want...

df = df.rename(columns = {"GDP":"NGDP"})
# Another way to rename specific instances... not that if we did not have the df
# in front, nothing would fundementally change, it would just copy and print out
# the new one, but the saved df is the same...

namelist = ["NGDP","CPI"]

print("\n",df[namelist])

numlist = [2,0]

print("\n",df[numlist])
# So here is another way to pull this out, note also that it changed the ordering
# of the columns, now NGDP is fist, the CPI...very nice...

# Here are some ways to drop stuff, its worth doing df.drop?

df.drop("CPI", axis = 1)

# The key thing to recognize is the axis, this is saying drop a column named "CPI"
# if you did this with out the axis it would give an error, why the defalut is 
# axis = 0 which are rows...and there is no index named "CPI"

df.drop(2, axis = 0)
# This will drop the index 2, row number 3 from the dataframe...
# Here is another way to see this...

pwt = pwt.set_index(['year'])
pwt.drop(2000) # set theindex to the year, then drop all the observations for 2000

"""
Exercise. For the DataFrame df, create a variable diff equal to the difference
 of ngdp and rgdp. Verify that diff is now in df.
"""
df["diff_gdp"] = df["NGDP"] - df["RGDP"]


"""
Exercise. How would you extract the variables ngdp and year?
"""
new_df = df[["NGDP","YEAR"]]

"""
Exercise. How would you drop the variable diff? 
If you print your dataframe again, is it gone? 
If not, why do you think it is still there?
"""

df = df.drop("diff_gdp",axis = 1)

"""
Exercise (very challenging). Use a list comprehension to change the variable
 names
 from ['ngdp', 'rgdp', 'gdp_div_1000'] to ['nGDP', 'rGDP', 'GDP_div_1000']. 
"""

df.columns = [var.lower().replace("gdp","GDP") for var in df.columns]

