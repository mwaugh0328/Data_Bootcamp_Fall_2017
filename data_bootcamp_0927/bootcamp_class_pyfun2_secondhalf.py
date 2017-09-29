# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 10:52:23 2017

@author: mwaugh
"""

###############################################################################
# Code for second half of python fundelmentals 2, fall 2017....

# So we talked about dictionaries, comparisions, boolean operations, and then if
# else statmetns... now for loops and more...

#%%
# Slicing... we did some of this already with lists, but we can do more...

a = "some"
print([a[0], a[1], a[2]])

# Note how it is treating the string just like a list (remember python starts from 0)
# so we are calling each individual character...

#a[1] = "*"  # can we re-assgin? # no...its like a tuple where the object is immutable.
#print(a)

# What is intersting too is that we can count different ways...

print(a[-3]) # this should give an o, so 0 is s, -1 is e, -2, is m...
#print(a[-400]) # But it will not do this infinitly, it will do this untill it returns
# back to s or -4,  

'''
ake the string firstname = 'Monty' and write below it the forward and backward 
counting conventions. What integer would you put in square brackets to extract 
the third letter (n) under each system?
'''

firstname = "Monty"
print(firstname[2])
print(firstname[-3])

'''
Exercise. Find the last letter of the string lastname = 'Python'. Find the second 
to last letter using both the forward and backward counting conventions.
'''
lastname = "Python"
print(lastname[len(lastname)-2]) # -1 for second to last letter, -1 as we start from zero
print(lastname[-2]) # I see this gives a sense why this might be helpfull, the last letter is -1
                    # the second do the last letter is -2, etc..

'''
Exercise. Take the list numberlist = [1, 5, -3]. Use slicing to set a variable 
first equal to the first item. Set another variable last equal to the last item.
 Set a third variable named middle equal to the middle item.
'''

numberlist = [1, 5, -3]

first = numberlist[0]
middle = numberlist[-2]
last = numberlist[-1]

print(first, middle, last)

#%% More slicing... but lets pull out a set of stuff...

c = 'something'
print('c[1] is', c[1]) # We know this...
print('c[1:2] is', c[1:2]) # This says take between 1 and 2 NOT including 2 (so same as above)
print('c[1:3] is', c[1:3]) # This says take between 1 and 3 NOT including 3
print('c[1:] is', c[1:]) # This says give from postion 1 onward so omething...if -1?
print('c[1:-1] is', c[1:-1]) # This works, again, from postion 1 and -1 NOT including -1, so oemthin

'''
Exercise. Set lastname = 'Python'. Extract the string 'thon'.
'''
print("this should be 'thon'", lastname[2:])

'''
Exercise. Set numlist = [1, 7, 4, 3]. Extract the middle two items and assign 
them to the variable middle. 
'''
numlist = [1,7,4,3]
middle = numlist[1:-1] # This is nice, it says don't take the first one, don't take the last one. 
print(middle)


'''
Extract all but the first item and assign them to the variable allbutfirst. 
Extract all but the last item and assign them to the variable allbutlast.
'''
allbutfirst = numlist[1:] # I guess the more you do this the convention works well..
allbutlast = numlist[0:-1]
print(allbutfirst, allbutlast)


'''
Exercise. Take the string c = 'something'. What is c[:3] + c[3:]?
'''

c = "something"

print(c[:3] + c[3:]) # this should be something....


#%% For loops one of the things I use all the time....

# Here is our first example...

namelist = ['Chase', 'Dave', 'Sarah', 'Spencer']    # creates the list "namelist"
                                                    # below, the word "item" is arbitrary. End the line with a colon.
for bannana in namelist:    # goes through the items in the list one at a time
    print(bannana)           # indent this line exactly 4 spaces
                            # if there is code after this, we'd typically leave a blank line in-between
                            # do print bannana what happens? why?
                            
                            
# Then lets do this...
count = 0
for num in numlist:
    count = count + num
    
print(count)

'''
Exercise. Adapt the example to compute the average of the elements of numlist.
'''

count = 0
n_items = len(numlist)
for num in numlist:
    count = count + num/n_items
    
print("The Average value is", count)

# Then we can do the same thing with a string... key thing is that the object is 
# itterable, next test can we do this with a floating point number...


word = "word"
for letter in word:
    print(letter)
    
#number = 12.3456
#for num in number:   # This won't work, why floating point numbers are not itterable...
#    print(num)

    
vowels = 'aeiouy'
word = "anything"

for letter in word: # Same deal work through each item in word
    
    if letter not in vowels: # this is new, but easyt to understand, if the letter is in vowles, 
        print(letter)    # it will do something, like print
        
print("",end = "\n \n")
        
'''
Exercise. Take the list stuff = ['cat', 3.7, 5, 'dog'].
Write a program that prints the elements of stuff.
'''
stuff = ["cat", 3.7, 5, "dog"]

for st in stuff:
    print(st)
    
print("",end = "\n \n")

'''
Write a program that tells us the type of each element of stuff.
'''


for st in stuff:
    print(type(st))
    
'''
Challenging. Write a program that goes through the elements of stuff and prints
only the elements that are strings; that is, the print the elements where function 
type returns the value str.
'''
    
for st in stuff:
    if type(st) == str:
        print(st)
    else:
        print(st, " is not a sring")
        
#%% For loops over counters, this is more natural to me, note above, python implicitly
# recognizes that the object can be itterated on, nice but simpliing doint something 
# for a fixed number of times is good too.

# First the range function type range? Basic idea goes from starting point to endingponint
# NOT including it, and then the final argument is the step size...
# Note also range command generates a type called range, obviously it must be itterable....

for banana in range(5): # again, the name here does not matter...
    print(banana)
    
    
for number in range(1, 11):
    square = number**2
    print('Number and its square:', number, square)
    
total = 0
for num in range(1, 11):
    total = total + num

print("Sum total from 1 to 10", total)

# Some more examples... this is a bond pricing one...
maturity = 10
coupon = 5
ytm = 0.05                 # yield to maturity

# This is how you would price a bond using a got loop...
price = 0
for year in range(1, maturity + 1):
    
    price = price + coupon/((1+ytm)**year)
    # https://en.wikipedia.org/wiki/Bond_valuation see the present value calculation...

price = price + 100/((1+ytm)**maturity) # Then this is the principal...

print('The price of the bond is', price) # Should be 100...which it is...

maxnum = 500
total = 0
for nm in range(1,maxnum):
    
    total = total + nm
    if total > 100:
        break # This says break the loop
        
print("At number", nm," The total was", total)

'''
Exercise. Consider the list namelist = ['Chase', 'Dave', 'Sarah', 'Spencer']. 
Write a loop that goes through the list until it reaches a name than begins with
 the letter S. At that point it prints the names and exits the loop.
'''

namelist = ["Chase", "Dave", "Sarah", "Spencer"]

for item in namelist:
    if item[0] == "S":
        print("First name with an S is ", item)
        break
    else:
        print("Names that did not begin with S ", item)



'''
fruit = ['apple', 'banana', 'clementine']
FRUIT = [item.upper() for item in fruit]
'''
'''
def squareme(number):
    """
    Takes numerical input and returns its square
    """
    return number**2        # this is what the function sends back

square = squareme(7)        # assign the "return" to variable on left
print('The square is', square)
'''
    

