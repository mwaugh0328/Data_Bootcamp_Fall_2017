# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 11:21:00 2017

@author: mwaugh
"""

# Code to (i) import roster (ii) work through github names and pull .csv files 
# then interpert the results...

import pandas as pd
import requests
from numbers import Number

# Going to use pandas...

###############################################################################
# First, specify the correct folder we will work from:

folder = "G:\\data_bootcamp\\Data_Bootcamp_Fall_2017"
#folder = folder + "\\NYU TEACHING\\Data Boot Camp Fall 2017\\Roster"

# Note double backslash for windows, then the add sign on strings simply puts 
# the two things togetehr.

csv_file = folder + "\\new_roster.csv"

data_bootcamp_roster = pd.read_csv(csv_file)

# Now we have as a ``dataframe'' the data_bootcamp roster, then the following
# code will give a snap shoot of what it looks like

print(data_bootcamp_roster.head(), end = '\n \n')
n_students = len(data_bootcamp_roster)


# Now I want to drop the guys who have not submited a git hub name... this should
#do it

data_bootcamp_roster  = data_bootcamp_roster.dropna(subset = ['GitHub_name'])
n_students_github = len(data_bootcamp_roster)

#%%
###############################################################################
# Now this is what I want to do (i) walk through the roster (ii) get their GitHub name
# pull the GitHub file and then append it to roster...

web_name_one = 'https://raw.githubusercontent.com/'
web_name_two = '/my_first_repository/master/time_for_practice1.csv'
count = 0


code_practice = pd.DataFrame()


no_info = pd.DataFrame(['.']) 
# This creates an empy data frame to add to stuff, still need to understand, but it
# did the trick


for index, row in data_bootcamp_roster.iterrows():
    
    git_repository = web_name_one + row['GitHub_name'] + web_name_two
    
    request = requests.get(git_repository)
    
    # Check if the github repository is setup correctly...
    if request.status_code == 200:
        
        count = count + 1
        # Here is a counter to record if the github account was setup properly
        # print(pd.read_csv(git_repository, header=None)) Show this, random stuff gets pulled in...
        
        grab = pd.read_csv(git_repository, header=None, nrows= 1)

        if isinstance(grab[0].iloc[0],Number) == False: #Check if the first element is a number...
            
            message = row['Name'] + " something is wrong with file 'time_for_practice1.csv'"
            
            print(message,end = '\n \n')
            
        else:
            #print(isinstance(grab[0],numbers.Number))
            message = row['Name'] + " great job! It took you" + " " + str(grab[0].iloc[0]) + " " + "minutes"
            
            print(message,end = '\n \n')
            
        
        code_practice = code_practice.append(grab, ignore_index=True)
        # straight forward, first option tells that reading it in there is no header. then with the append command,
        # this says ignore the index, create its own. Same thing below.
        # Now a new command is nrows = 1, I'm only going to pull in the very first row...
                     
    else:
        message = 'Something is wrong...' + row['Name'] + " with your repository"
        
        code_practice = code_practice.append(no_info, ignore_index=True)
        
        print(message,end = '\n \n')
    
       
# Notice the indentation here...I think this is the feature of python, the key
# is that it is signialling what is associated witht eh for loop.    
#%%
###############################################################################
# Lets organize some stuff so I can merge the results....
#print(first_github_info)

code_practice = code_practice.rename(columns = {0 :'time_to_complete'})
time_code_practice = pd.to_numeric(code_practice.time_to_complete, errors='coerce')

# Rename the column, one issue here is that some people have more complicated 
# setups, so I actually don't know (wihtout looking) know how many columns there
# are, assuming people did as I asked the number should be there. 

###############################################################################
# Lets report some statistics
print('\n')
print('\n')
print('Number of Studens in Class', n_students, end = '\n \n')
print('Number of Studens for which I have a GitHub name',n_students_github, end = '\n \n')
print("Number of Students for which I have a usable time", time_code_practice.count(), end = '\n \n')
print("Average time to complete", round(time_code_practice.mean(),2), end = '\n \n')
print("Median time to complete", round(time_code_practice.median(),2), end = '\n \n')






