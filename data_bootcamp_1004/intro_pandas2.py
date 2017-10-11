# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 11:03:54 2017

@author: mwaugh
"""
#%%
###############################################################################
# Recap, pandas...very powerfull package to using, manipulating, analyzing data
# that was built for python....

import pandas as pd
# This imports pandas...


data = {"GDP": [5974.7, 10031.0, 14681.1],
                   "CPI": [127.5, 169.3, 217.488],
                   "Year": [1990, 2000, 2010],
                   "Country": ["US", "US", "US"]}
# what kind of data structure is this

df = pd.DataFrame(data)

#%%

###############################################################################

df.shape # Tells us the shape of the dataframe

df.columns # Tells us about the columns and their names

df.index # Tells us about the index, do list(df.index) to generate a list

df.dtypes # tells us about the types of data in each coloumn

# Then we can perform mathematical operations on the columns...

df['RGDP'] = df['GDP']/df['CPI']

df['GDP_div_1000'] = df['GDP'] / 1000

print("\n",df) # so there is a new column called real gdp now...

# See the digressioini n the book....I don't mind doing this...

print("\n",df.RGDP)


#%%
###############################################################################
# Now lets do some more stuff...this is new...


df.columns = ["cpi", "country", "gdp", "year", "rgdp", "gdp_div_1000"]
# What if the elelments here were less than the number of columns?

df.columns = [var.upper() for var in df.columns]
# HEre we can use list comprehension to change the neames in columns in the way
# we want...

df = df.rename(columns = {"GDP":"NGDP"})
# Another way to rename specific instances...
#  note that if we did not have the df in front, nothing would fundementally
# change, it would just copy and print outthe new one, but the saved df is the same...

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

# again, notice that nothing is fundementally changed to df, to really change df
# you could do two things...

#df = df.drop("CPI", axis = 1)
#df.drop("CPI", axis = 1, inplace = True) # look at df.drop? to see what this means

df.drop(2, axis = 0) # then this will drop a row (this the point of the axis)
                     # again, this does not change the df, unle

# I keep mentioning why the drop does not replace things, just creates a copy 
# with the df in place, why is this usefull, here is an example, I want the mean
# of stuff, but not the year...
                     
df.drop("YEAR", axis = 1).mean()

#%%
# Here is another way to see this...
pwt_data = {'countrycode': ['CHN', 'CHN', 'CHN', 'FRA', 'FRA', 'FRA'],
        'pop': [1124.8, 1246.8, 1318.2, 58.2, 60.8, 64.7],
        'rgdpe': [2.611, 4.951, 11.106, 1.294, 1.753, 2.032],
        'year': [1990, 2000, 2010, 1990, 2000, 2010]}
pwt = pd.DataFrame(pwt_data)


pwt = pwt.set_index(['year'])
pwt.drop(2000) # set theindex to the year, then drop all the observations for 2000

# Suppose I only wanted the year 2000 how would I do that...
drp = [var for var in pwt.index if var != 2000 ] # create a list of index that is not 2000

pwt.drop(drp)

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


###############################################################################
# Reading and writing data...
pwt.to_csv("pwt.csv") # not obvious where this is saving it!!!! 

#pwt.to_clipboard() # Does not seem to work for me... moreover it jams up my
# copy and save ability 

# we will do much more reading and writing later...

# One important feature of data analysis is looking at the data!!!! Pandas has 
# this feature 

print(pwt.head())

#### Then here are some basic statistics options...
print(df.mean()) # computes the mean
print(df.std()) # computes the standard deviation
print(df.describe()) # reports a lot of stuff about the data...

pwt.drop(drp).mean() # The pwt example is intersting, in teh sense that the pannel
# data aspect makes simply taking means, etc is not very informative, but here
# is how to get this for just one year....

# We are going to get into this much much more...but here is a quick way to 
# plot something

df.plot()
# This basically takes every column, then plots it agains the index sepecified
# hence note teh x-axis...

pwt[pwt.countrycode=="CHN"].plot()
# What does this do...note that the index was reset to the year, so now it is 
# by year...

#%%
pwt[pwt.countrycode=="CHN"]["rgdpe"].pct_change().plot()

'''
Set year as the index and assign the result to the DataFrame dfi. 
Use the index method to extract it and verify that year is, in fact, 
the index.
'''
dfi = df.set_index("year")
list(dfi.index)

'''
Exercise. Apply the reset_index() method to our new DataFrame dfi. 
What does it do? What is the index of the new DataFrame?
'''
dfi.reset_index()
'''
Exercise. What kind of object is df.mean()?
'''

'''
Exercise. Produce a bar chart of df with the statement 
(Hint: use the docstring for df.plot to see what kind argument does)
'''

df.plot(kind ="bar")







