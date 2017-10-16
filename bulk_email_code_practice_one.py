# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 16:26:00 2017

@author: mwaugh
"""

import smtplib
import pandas as pd

#%%
###############################################################################
# This part sets up the connection
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

smtpObj.ehlo()
# This thing says hello to the server...

smtpObj.starttls()


#mypassword = password.get_value(0,0)
# This reads in my password...

myemail = "mwaugh@stern.nyu.edu" # email goes here

smtpObj.login(myemail, "") # this then logs you into the gmail account
# Note that gmail will typically reject this upon the first attempt and probably
# send you an email saying that a unauthorized attempte was made, but if it was 
# you then approve requests from less secure apps such as this...

#%%
sender = myemail
subject = "Subject: Grade Code Practice # 1\n" # this last line seperates the subject from the body
intro =  "\nHi "
main_message = '''\n \nHow are you doing? I hope you are having a great weekend!
I'm emailing to let you know your grade on Code Practice #1. This assignment was
graded on a check plus, check, check minus scale. What's the difference? None...
other than professionalisim issues, everyone did great, so full credit. 
\n'''
grade_message_one = "On Code Practice 1 you recived a "

if_low_grade  = '''This probably means that everything was correct, but that it 
was not professionally executed.'''

no_grade = '''I do not seem to have a grade for you. This could be a clarical issue.
If you did turn somthing in, please let me 
know as soon as possible. '''
 
mikes_closing = "\n\nIf you have any questions, please let me know.\n\nMike" 

#smtpObj.sendmail(sender, reciver, subject+intro+main_message)
#%%
#%%

folder = "C:\\Users\\mwaugh\\Dropbox\\NYU TEACHING\\Data Boot Camp Fall 2017\\Roster"

# Note double backslash for windows, then the add sign on strings simply puts 
# the two things togetehr.

csv_file = folder + "\\grade_book.csv"

roster = pd.read_csv(csv_file)
#flist.columns = ["first_name", "email"]

#%%

for index, row in roster.iterrows():
    firstname = row["Name"]
    firstname = firstname[firstname.find(" ")+1:]+":"
    
    if row["CodePractice#1"] == 3:
        grade_message = grade_message_one + "check plus! Awesome!"
    
    elif row["CodePractice#1"] == 2:
            grade_message = grade_message_one + "check."
    
    elif row["CodePractice#1"] == 1:
            grade_message = grade_message_one + "check minus." + "\n" + if_low_grade 
       
    else:
            grade_message = no_grade
        
    message = subject + intro + firstname + main_message + grade_message 
    message = message + mikes_closing 
    
    print(message)
    
    #smtpObj.sendmail(sender, row["email"],message)
    
    print("I'm sending and email to", row["Email_Address"])
    
#smtpObj.sendmail(sender, row["Email_Address"],message)  
    
  
smtpObj.quit()

#%%

