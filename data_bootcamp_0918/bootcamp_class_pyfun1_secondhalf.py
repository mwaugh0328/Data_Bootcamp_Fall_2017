# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 21:25:10 2017

@author: mwaugh
"""
# This is the second half of python fundementals 1. It should corespond with class
# on 09/18

#%%
z = 2/3

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

#%%
# Comments. Very important. I use them all the time, mostly it was because I 
# found myself spending too much time on my old code trying to understand what 
# it was doing, thus I resoved to comment heavily to (i) supllement my understanding
# of what I'm currrently doing and (ii) talk to my futureself and save me some time
# Nuff said

#%%
# Here is the thing, you'll notice that sometimes I use single quotation, double 
# quotation markes... First, both are valid ways to define a string. The real 
# issue is my inconsistent use partly this is a problem with the NYU databoot camp
# team I actually prefer double

a = 'string'
b = "string"
print(a,b) # We should see the same thing....

# This is one instance where double helps...
message = "I don't know what I'm doing"
print(message)

# Note how we can use the aposterphy here...not possible with single quotation 
# marks...

# Finally, triple quotes allow you to handle a return, like this

longstring = """
Four score and seven years ago
Our fathers brought forth. """

print(longstring) 

# Intresting, play around with new lines before and after the message
# and see what comes out of it...

"""
Exercise. In the Four score etc code, replace the triple double quotes with 
triple single quotes. What happens?
"""

longstring = '''
Four score and seven years ago
Our fathers brought forth. '''

print(longstring) 

# IT WORKS...again, same issue here singel or double do the same thing....

"""
Exercise. Fix this code: bad_string = 'Sarah's code'
"""

bad_string = "sarah's code" # Do double quotation marks...
print(bad_string)

"""
Exercise. Which of these are strings? Which are not?
apple NOT
"orange" YES
'lemon84' YES
"1" YES
string NOT
4 NOT
15.6 NOT
'32.5' YES

Remember: A string is a collection of characters between quotation marks
"""

#%% LISTS
###############################################################################

# Key concept: A list is an ordered collection of items. 
# This will obviously be important as data will naturally come in a list or 
# list like form.

# Some examples of listis...
numberlist = [1, 5, -3] # Note also the use of square brackes...this is what
                        # defines a list, () are tuples, {} are sets...


stringlist = ['hi', 'hello', 'hey']

a = 'some'

b = 'thing'

c = a + b

variablelist = [a, b, c]
print("\n")
print(variablelist, end = "\n \n")

# Now what is really cool is that you can have a list with different types...

randomlist = [1, "hello", a]

# So notice that the first part of the list is an integer, then a string, then 
# the variable a (which currently is a string as well)

# Then there is the combining of litss... so here is this awsome example

big_list_one = randomlist + stringlist
print(big_list_one, end = "\n \n")
# So notice what this did here, it litterally took randomlist and then added it
# to the stringlist, so we have a new list that combines all of this

# What do you think this does...

big_list_two = [randomlist, stringlist]
print(big_list_two, end = "\n \n")
# VERY INTERESTING....This took the two litsts and the created another list 
# which is composed of two lists!!! A "List of Lists"

# Final point, the book does not talk about this yet, later it does, but its
# worth understanding the "orderd" part...this means for each item in the list
# we can call that item with its order in the list or number.
# Key: Python starts from the number 0, so the first item in a list is item number
# zero...

# Lets try some stuff

print(randomlist[0], "Should print the first value, a one", end = "\n \n")
print(randomlist[2], " Should print the last value, 'some'", end = "\n \n")

# Now lets do this with big_list_two, the "list of list"
print(big_list_two[1], " Should be the list 'hi', 'hello', 'hey'")



'''
Exercise. How would you explain a list to a classmate?
'''

'''
Exercise. Add print(numberlist) and print(variablelist) to your code and note 
the format of the output. What do the square brackets tell us? The single 
quotes around some entries?
'''
# Square brackets tell us its a LIST!!! then the quotes around it are indicating
# if its a string or not....

'''

Exercise. Run the statements
'''

mixedlist = [a, b, c, numberlist]
print(mixedlist)

'''
What is the output? How would you explain it to a classmates?
'''

'''
Exercise. Suppose x = [1, 2, 3] is a list. What is x + x? 2*x? Try them and see.
'''
x = [1,2,3]
print(x+x) # This is going to make another list that is just 1,2,3,1,2,3
print(2*x) # Same thing...amazing!!!


#%%
# Tuples...still not sure why this is here in the book, very simmilar to lists,
# but the key issue is once a tuple is set, then the entries in it cannot be changed
# in lists they can...let me show you

print(numberlist)
numberlist[0] = 328
print(numberlist) # Note how I changed the fist entry int he list!!!

test_tuple = (1,2,3) # Similar to a list, but round brackets...
#test_tuple[0] = 328 # UNCOMMENT THIS PART OF THE CODE TO UNDERSTAND 
# This won't run 
#"TypeError: 'tuple' object does not support item assignment" meaning, that once
# set you can not assignm new values... This is the immutability property of a tuple

#%% 
# Builtin functions. We've been using one a lot print, here are some more....note
# these are "buildin" meaning that they are ready to go when we boot up, this is
# unlike the log function which with out adding some package is not recognized.

print(len('hello world')) # note how len is "counting how many characters" 
                          # And it is including the white space...
print(len([1, 5, -3])) # How many times in the list
print(len((1, 5, -3))) # how many itesm in the tuple
print(len('1234')) # String, so how many characters
#len(1234) # This is interesting, you should get an error message, a number
            # does not have this "attribute" 
len('12.34') # Again, a string....
#len(12.34) # same issue wiht a floating point number...

print(type(2)) # Its saying an integer
print(type(2.5)) # A floating point number, or float
print(type('2.5')) # Looks like a number, but a string
print(type('something')) # String
print(type([1, 5, -3])) # Here it sees that this is a list...
print(type((1, 5, -3))) # A tuple

# Note spyder in the variable explorer is always reporting this as well...with 
# the type reported. What is a float anyways...
'''
Exercise. Try type(zoo). Why does it generate an error? What does the error mean?
It should tells us that zoo had not been defined. Big picture, when we create a 
variable, assigninging it a value, we are implicitly giving it a type that can 
be recognized...
'''
'''
Exercise. Set zoo = ['lions', 'bears'] and try type(zoo) again. 
What do you get this time?
# Now it works...it tells us a list. Why not a string???
'''

#%%
###############################################################################
# Changing types...super important for data work....





