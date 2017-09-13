# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 09:21:01 2017

@author: mwaugh
"""
#%%
###############################################################################
# This is my code walking through python fundementals 1 for the Fall 2017 data 
# boot camp course.

test = 2*3 # simple multiplication
print(test)

test = 2 * 3 # add some white space, nice feature of python is that it is not sensitve to this..
print(test)

test = 2  *  3 # add some more...
print(test)

# What about division...
test = 2/3
print(test)

# Now lets try powers...

test = 2^3 # This is what you would do in excel (matlab too)
print(test)
print("is this a 8???")

test = 2**3 # Now what happens...
print(test)
print("is this a 8???")

"""
test = log(3) # what do you think will happen here...note in spyder it is given
              # a alert, this is telling you that there is a problem...log is not defined
print(test)

# Note the quotation markes like this is good for multiline comments...
# Note as well, the code will not go any further than this...python, the computer
# is DUMB! You gave it an instruction that it did not know what to do, so it stoped,
# and did not proceed. A couple of points about this:
# 1. The top to bottom, simply following instructions/commands nature of a program
# 2. When you run this is spyder, note how (after some stuff) it is telling you where
# the problem is: Line 36, then this name log is not defined.

""" 

test = 4**2 # Now what happens...
print(test)
print("is this a 8???")

#%%
###############################################################################
# Above I've been assigning variables... but lets look at this more closely...

x = 2 # nice so the thing on the left is the "variable" named "x", then the thing
        # on the right is the value that this variable is assigned... then the 
        # = sign is the operator that assings that value.

print(x)

y = 3 # lets do it again...
print(y)

z = x/y # now we are getting somewhere, we take these variables and perform an operation
        # notice that (like excell) the value assigned to z will change as we change the values
        # assigned to x or y
print(z)

# Here is a place where you might want to look at spyder and the variable explorere
# your should see the name of the variable, x  (the type and size ignore for now)
# and then the value... this is a nice feature of spyder to trackdown bugs and have
# an understanding what variables are in your enviornment at any point in time.

# Now lets do some excercises...
'''
Exercise. Type w = 7 in the IPython console. What does the code w = w + 2 do? 
Why is this not a violation of basic mathematics?
'''
w = 7
w = w +2
print(w)
# Note what is goint on here, this says w is 7, then the next line says take w and 
# add 2 then reassign the value w to be this new number. Nice right...

'''
Exercise. Suppose we borrow 200 for one year at an interest rate of 5 percent. 
If we pay interest plus principal at the end of the year, what is our total payment? 
Compute this using the variables principal = 200 and i = 0.05.
'''
loan = 200 # Note, I like to make variable names, short, but informative
interest = 0.05 # Same thing, be mindfull not to name your varible the same as an operation(?)

total_payment = 200*(1+interest)

print(total_payment) 

'''
Exercise. Real GDP in the US (the total value of things produced) was 15.58 trillion
 in 2013 and 15.96 trillion in 2014. What was the growth rate? Express it as an annual percentage.
'''
gdp_2013 = 15.58
gdp_2014 = 15.96

gdp_growth = 100*((gdp_2014/gdp_2013) - 1)
print(gdp_growth)
# Very nice, again note the naming convention, things are short, but informative so
# if your friend looked at the code he would understand what you are doing.

'''
Exercise (challenging). Suppose we have two variables, x and y.
How would you switch their values, so that x takes on y's value and y takes on x's?
'''
# Naive approach...
# Fist record what you have..
print(x,y)
temp = x
x = y
y = temp
print(x,y)

# Now this is a great place to practice ``google fu'' so I typed into google
# how to switch values in python
# And the first entry was this thing called stack overflow which is a place one
# can post questions and recive answers. Sure enough was this question asking about
# standard ways to do this and the answer was this

# first reset things...
x = 2
y = 3

x,y = y,x
print(x,y)
# This is cool...the stackoverflow explains this that Python creates a tuple out of
# the stuff on the righthand side (y,x) and then will take this tuple and assign it
# to a new tuple (x,y) all in the background. 
#
# Another point that this brings up is the evaluation order so as the documentation says
# (1) When assigning something (=) it starts on the left (2) where ever it starts, it works left to right
#
# Interesting note, the answer also corrects the language, x is not a varible but
# an object (this is correct) but we will stick with variable...

'''
Exercise (challenging). Type x = 6 in the IPython console. We've reassigned x 
so that its value is now 6, not 2. If we type and submit z, we see its still 0.666
whats up...

The bottom line is that z will not change unless evalueated again (this is unlike 
excell where connected cells atomatically update). This gives us a lot of explict control
over the operations on variables...this has benefits but must also be mindfull of 
what is goint on, like quote from spider man ``with great powers, come great responsibility"
'''
#%%
###############################################################################
# Printing stuff, you've seen a lot of this 
# This is a place to see how spyder provide help 
# Here are some things to do
# What happens if you do this...
# print(x y) # note in spyder a red x is showing up, it knows there is a problem...

print(x, y, sep='---')


print(x,y, end='\n \n \n \n \n')

# Other ways to understand this in the iphython consol type print? (which will tell
# you what is up) or check out the object consol
# Return to quesiton about why quotation marks...

#%%
###############################################################################
# Strings...this is where I think python is VERY POWERFULL...lots of enviornments
# can do numerical calculations, plotting well, but handeling and manipulating 
# strings is less common...

# Lesson 1: A string is a collection of characters between quotation marks
# Lesson 2: A string may look like a number, but it is not.

# '12'/3 this is not going to work as "12" is a string, python does not see it 
# as a number, and then it is being asked to perform a numerical computation on
# something that is not a number, thus an error message.

a = "some"
b = "thing"
c = a + b # this is awesome....so natural and intuitive... suppose you tried
            # this in excel?? what would happen.
print(c)

# Back to print, we can do some cool things with this...
print("the value of z is", z)

# or even do something like this
message = "the value of z is"
print(message, z)

'''
Exercise. What is a string? How would you explain it to a friend?
'''

'''
Exercise. What happens if we run the statement: 'Chase'/2? Why?
'''

'''
Exercise. This one's a little harder. Assign your first name as a string to the
variable firstname and your last name to the variable lastname. 
Use them to construct a new variable equal to your first name, a space, 
then your last name. Hint: Think about how you would express a space as a string.
'''
first_name = "Michael"
last_name = "Waugh"
space = " "

full_name = first_name + space + last_name
print(full_name)
# Note how python interperts this space in " " it is implicitly a character, just
# and empty space...

'''
Exercise. Set s = 'string'. What is s + s? 2*s? s*2? What is the logic here?
'''
s = 'string'
print(s+s)
print(2*s)
print(s*2)
print(s + full_name*2)











