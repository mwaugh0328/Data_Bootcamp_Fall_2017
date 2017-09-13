# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 11:21:00 2017

@author: mwaugh
"""

# Code to (i) import roster (ii) work through github names and pull .csv files 
# then interpert the results...

import pandas as pd
import requests

# Going to use pandas...

###############################################################################
# First, specify the correct folder we will work from:

folder = "C:\\data_bootcamp"
#folder = folder + "\\NYU TEACHING\\Data Boot Camp Fall 2017\\Roster"

# Note double backslash for windows, then the add sign on strings simply puts 
# the two things togetehr.

csv_file = folder + "\\new_roster.csv"

data_bootcamp_roster = pd.read_csv(csv_file)

# Now we have as a ``dataframe'' the data_bootcamp roster, then the following
# code will give a snap shoot of what it looks like

print(data_bootcamp_roster.head())
n_students = len(data_bootcamp_roster)


# Now I want to drop the guys who have not submited a git hub name... this should
#do it

data_bootcamp_roster  = data_bootcamp_roster.dropna(subset = ['GitHub_name'])
n_students_github = len(data_bootcamp_roster)

###############################################################################
# Now this is what I want to do (i) walk through the roster (ii) get their GitHub name
# pull the GitHub file and then append it to roster...

web_name_one = 'https://raw.githubusercontent.com/'
web_name_two = '/my_first_repository/master/my_first_file.csv'
count = 0


first_github_info = pd.DataFrame()


no_info = pd.DataFrame(['.']) 
# This creates an empy data frame to add to stuff, still need to understand, but it
# did the trick


for index, row in data_bootcamp_roster.iterrows():
    
    git_repository = web_name_one + row['GitHub_name'] + web_name_two
    
    request = requests.get(git_repository)
    
    # Check if the github repository is setup correctly...
    if request.status_code == 200:
        
        message = 'Your first repository exists...Great Job!!!  ' + row['Name']
        print(message,end = '\n \n')
        count = count + 1
        # Here is a counter to record if the github account was setup properly
    
        first_github_info = first_github_info.append(pd.read_csv(git_repository, header=None), ignore_index=True)
        # straight forward, first option tells that reading it in there is no header. then with the append command,
        # this says ignore the index, create its own. Same thing below.
                
    else:
        message = 'Something is wrong...' + row['Name']
        
        first_github_info = first_github_info.append(no_info, ignore_index=True)
        
        print(message,end = '\n \n')
    
       
# Notice the indentation here...I think this is the feature of python, the key
# is that it is signialling what is associated witht eh for loop.    

###############################################################################
# Lets organize some stuff so I can merge the results....
#print(first_github_info)

first_github_info.columns = ["first_message", "birth_year", "high_school_year", "college_year"]
# Rename the columns, NOTE don't leave a space, this will be convinent as you can see below when
# we call a column and compute some results from it....

get_index = data_bootcamp_roster.index
# Grab the index from the file (this is where the indexing in becomes a bit tricky)
# Then we want to reindex the github info which we know  (apriori) what it should be

first_github_info = first_github_info.set_index(get_index)

roster_github = data_bootcamp_roster.join(first_github_info)
# Then this will combine it. Again, given that both data sets have the same index
# this is the simpelest way to do...we will talk a lot about merging later.

###############################################################################
# Lets report some statistics
print('\n')
print('\n')
print('Number of Studens in Class', n_students, end = '\n \n')
print('Number of Studens for which I have a GitHub name',n_students_github, end = '\n \n')
print('Number of Students who have GitHub repository setup correctly',count, end = '\n \n')
print("Average Age",round(2017 - roster_github.birth_year.mean(),3), end = '\n \n')
print("Average Years Since High School",round(2017 - roster_github.high_school_year.mean(),3), end = '\n \n')
print("Average Years Till College Graduation",round(roster_github.college_year.mean()- 2017,3), end = '\n \n')






