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

password = pd.read_csv("mypassword.csv", header=None)
mypassword = password.get_value(0,0)
# This reads in my password...

myemail = "mwaugh@stern.nyu.edu" # email goes here

smtpObj.login(myemail, mypassword) # this then logs you into the gmail account
# Note that gmail will typically reject this upon the first attempt and probably
# send you an email saying that a unauthorized attempte was made, but if it was 
# you then approve requests from less secure apps such as this...

sender = myemail
subject = "Subject: I'm testing... \n" # this last line seperates the subject from the body
intro =  "Hi "
main_message = "\nHow are you doing?\nSorry to bug you, but I'm testing my bulk"
main_message = main_message + " email system.\nMike" 

#smtpObj.sendmail(sender, reciver, subject+intro+main_message)

#%%

folder = "C:\\data_bootcamp\\Data_Bootcamp_Fall_2017"
#folder = folder + "\\NYU TEACHING\\Data Boot Camp Fall 2017\\Roster"

# Note double backslash for windows, then the add sign on strings simply puts 
# the two things togetehr.

csv_file = folder + "\\friend_list.csv"

flist = pd.read_csv(csv_file, header = None)
flist.columns = ["first_name", "email"]

#%%

for index, row in flist.iterrows():
    message = subject + intro + row["first_name"]+main_message
    
    print(message)
    smtpObj.sendmail(sender, row["email"],message)
    
    print("I'm sending and email to", row["email"])
    
    
smtpObj.quit()

#%%
###############################################################################
# This part then will log in to my email account. Note that gmail will typically
# reject this upon the first attempt and probably send you an email saying that 
# a unauthorized attempte was made, but if it was you then approve requests from
# less secure apps such as this...

