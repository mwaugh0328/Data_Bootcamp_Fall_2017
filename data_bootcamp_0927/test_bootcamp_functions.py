# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 13:16:28 2017

@author: mwaugh
"""

import pyfun2_functions as bootfun

# This is our first intro to modules, these are just a colleciton of functions...
# Now what I'm doing is saying import the python script that has are functions in it
# the the 'as' just gives things a shorter name. 

###############################################################################

square = bootfun.squareme(7)        # assign the "return" to variable on left
print('The square is', square)

bootfun.combine("michael", "waugh")

print(bootfun.nextyear("2016"))

print(bootfun.power2(2.56))

# So do teh .[TAB] and notice that there are the functions squareme and 
# combine associated with the module bootfun


