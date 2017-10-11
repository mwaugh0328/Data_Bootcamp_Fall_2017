# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 15:12:12 2017

@author: mwaugh
"""

new_list = []
def notsix(xx):

    for x in xx:
        if str(x)[0] != '6':
            new_list.append(x)
    return new_list

x1 = [12,6,32,666]
x2 = [66,34,5,666]

print(notsix(x1))
print(notsix(x2))

#%%
# note that both change the new_list.

def notsix2(xx):
    new_list = []
    for x in xx:
        if str(x)[0] != '6':
            new_list.append(x)
    return new_list

x1 = [12,6,32,666]
x2 = [66,34,5,666]

new_x1 = notsix2(x1);
new_x2 = notsix2(x2)