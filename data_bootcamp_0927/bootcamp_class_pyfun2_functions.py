# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 11:41:00 2017

@author: mwaugh
"""

#print(squareme(9)) In a black console, this won't work as python reads line by
# line. Don't be fooled though, if you run this, later it will work, why the funciton
# will be defined in the enviornment/console.

def squareme(number):
    """
    Takes numerical input and returns its square 
    """
    return number**2        # this is what the function sends back

###############################################################################

square = squareme(7)        # assign the "return" to variable on left
print('The square is', square)

# Also type squareme? 
# This should return the comment under the function, this is like your self written
# help file...

#%%
###############################################################################

def combine(first, last):
    """
    This will take strings "first" and "last" then combine them to make a string
    of first + last name
    """
    newname = first.capitalize() + " " + last.capitalize()
    print(newname)
    return newname
    


combine("michael", "waugh")

'''
Exercise. Create and test a function that returns an arbitrary power of 2: the
input n (an integer) returns the output 2**n. Use n=2 and n=5 as test cases.
'''
#%%
def power2(number):
    if type(number) != int and type(number) !=float:
        print("Error power2 function: number is not proper type")
        return
    else:    
        return 2**number


print(power2(2))

power2('2')

'''
Exercise. Create and test a function nextyear that takes an integer year 
(say 2015) and returns the following year (2016).
'''
#%%
def nextyear(number):
    if type(number) == str:
        number = int(number)
    
    return number + 1


'''
Exercise (challenging). Create and test a function that takes a string year (say,
 '2015') and returns a string of the next year (say, '2016').
'''