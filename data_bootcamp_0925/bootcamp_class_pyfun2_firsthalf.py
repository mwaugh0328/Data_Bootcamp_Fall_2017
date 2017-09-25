# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 09:27:45 2017

@author: mwaugh
"""

###############################################################################
# Code for first half of python fundelmentals 2, fall 2017....

# Recap, see old code but (i) calculations, variables, assignment, strings, lists
# (ii) built in functions like print, type, len, conversion of types like str, int,
# etc. (iii) objects and methods so .tab completion and and the exploration of this
# We should also be getting self sufficient at finding help....

#%%
###############################################################################
# Dictionary is another "data structure" that we may come accross, it is an
# unorderd, pair of items, enclosed by curley brackets {}

names = {"Dave":"Backus", "Chase": "Colman", "Spencer": "Lyon", "Glen": "Okun"}

print(names) # This will display the dictionary...
print(type(names)) # What if we did not know the type of names, this will tell us...

# Now the way a dictionary is setup is there is a "key" and a "value", so when
# you type names[key] it will return the assocated value... note that keys must 
# be unique, but values need not be. So for every key, it returns a specific value
# but for a given value there could be multiple keys that deliver it...

print(names["Dave"])
print(names["Glen"])

# can you go from a value back to a key? 
# print(names["Backus"])
'''
Exercise. Construct a dictionary whose keys are the integers 1, 2, and 3 and 
whose values are the same numbers as words: one, two, three. How would you get 
the word associated with the key 2?
'''
num_words = {1:"one", 2:"two", 3:"three"}
num_words[2]

# Does this workd num_words["2"], why or why not...



'''
Exercise. Enter the code
'''
d = {'Donald': 'Duck', 'Mickey': 'Mouse', 'Donald': 'Trump'}
print(d)
# What do you see? Why do you think this happened?
#
# Ok so this looks like a problem...there are multiple keys with the same value
# which is violating the rules above. I would expact an error message, but it 
# looks like python will still be ok with this but...that does not mean all is ok...
# When you print it notice that it overwrote the Donald: Duck example, so what is
# happening is that the last part of creating the dictionary did not create a new
# entry, (it can't) it just reassigned the value associated with Donald to be Trump
# rather than duck. 
# Note as well, spyder is warrning you that there is a potential issue...

'''
Exercise. Describe -- and explain if possible -- the output of these statements:
'''
list(names) # creates a list out of the KEYS in the dictionarl (why the KEYS)
names.keys() # this creates a type called dictionary keys and returns the keys
              # Googeling this is an iterable view(?)....
print(list(names.keys())) # This converts the dict_keys object to a list

names.values() # Same deal but with values...
print(list(names.values()))


'''
Exercise. Consider the dictionary
'''
data = {'Year': [1990, 2000, 2010], 'GDP':  [8.95, 12.56, 14.78]}

# What are the keys here? The values? What do you think this dictionary represents?

#%%
###############################################################################
# Boolean options, simple but very important and usefull...

test = 1 < 0 # This is a comparsition, value 1 versus zero....
print(test) # What does it return a True or False value...
print(type(test)) # Check out the type, its a bool or short for Boolean

# Side note, you CAN combine operations of bool with numbers, for example do this
print(2*test)

# Now what if we had 1 < 0 above, what would the command return... note that it will
# give a zero... so what is going on here is implicitly with a True is the value 1
# and associated with the value False is a zero (note how in the background there is
# probably a dictionary doing this....)

# Some more operations... == is equall, >= greater than or eaquals, <= less than
# or equals, != not equalls....

test1 = 0.666666666666666 # This is interesing, when are they equall...
test2 = 2/3
print(test1 == test2)


test = not 1 > 0 # this is not whatever 1 > 0 is, so not True which is FALSE
print(test)

#%%

x = 2*3
y = 2**3
print('x greater than y is', x > y)

'''
Exercise. What is 2 >= 1? 2 >= 2? not 2 >= 1? If you're not sure, 
try them in the IPython console and see what you get.
'''

'''
Exercise. What is
''' 
print(2 + 2 == 4) # Note that this is NOT assignment its comparing if the value
                    # associated with the calculation on the LHS equals the RHS
print(1 + 3 != 4) # Same thing...

# What is 
print("sarah" == 'Sarah')
# Can you explain why? First, note that the double or single quotation markrs don't
# matter here, this is just comparing the string Sarah with Sarah...they are equall
# this is amazing, a special feature built into python is string comparison, here
# it checks if the characters are the same, what if one was not capitalized???

'''
Exercise. What do these comparisons do? Are they true or false? Why?
'''
print(type('Sarah') == str) # IS it a string? YES!!! 
print(type('Sarah') == int) # IS it an integer??? NO!
print(len('Sarah') >= 3) # Is the length longer than three? YES!

'''
Exercise (challenging). What do you think this code produces?
'''
name1 = 'Chase'
name2 = 'Spencer'
check =  name1 > name2
print("Is Chase > Spencer ",check) #hmmmm....

'''
Run it and see if you're right. What type of variable is check? What is its value?
 Is Chase greater than Spencer?
'''
# https://stackoverflow.com/questions/4806911/string-comparison-technique-used-by-python

# Here is the quick run down, this does this thing in lexicographic ordering... this
# means:
# first the first two items are compared, and if they differ this determines the
# outcome of the comparison; if they are equal, the next two items are compared,
# and so on, until either sequence is exhausted.
# When comparing uppercase vs. lower case, uppercase come before lower case...
# The charecters like *& comebefore
# If your having a hard time with this play with stuff like this
# "z" > "a"
# "Z" > "z"
# "*z" > "a" # etc...

#%%
# Conditionals, if and else...now we are getting to programming essentials. This
# provides a key basic element to any program...
#
# Key issue, an if must always be followed by : and then the next line or lines
# associated with the if statment must be indeted by 4 spaces. ONLY 4 spaces...
# spyder will do this automatically....

if 1 > 0: # this statment checks the value, then IF TRUE it advances to the next line
    print("1 is greater than 0") # here where it prints the value
    print("test")
    
# A couple of things that you can do, change this where it is not true, see what happens
# what if the indentation is wrong
print("",end = "\n \n \n")
x = 7               # we can change this later and see what happens

if x > 6:
    print('x =', x)

print('Done!')


x = 7

condition = x > 6

if condition:
    print('if branch')             # do if true
    print(condition)
else:
    print('else branch')           # do if false
    print(condition)

# This should be intuitive, if one thing do it, if not do something else... 

'''
Exercise. Take the names name1 and name2, both of them strings. Write a program
 using if and else that prints the name that comes first in alphabetical order. 
 Test your program with name1 = 'Dave' and name2 = 'Glenn'.
'''

name1 = "Dave"
name2 = "Glenn"
message = "Names in alphabetical order "

name1 = name1.title()
name2 = name2.title() # this would fixe the capitalization...

if name1 > name2:
    name_list = [name2, name1] # Need to be mindfull name1 > name2 means name1 comes after...
    print(message, name_list)
else:
    name_list = [name1, name2]
    print(message, name_list)

# Here is an extension, what if the names had different punctuation...how some capital
# some not...how would you handle that...
    
    

