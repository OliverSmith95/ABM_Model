# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 10:25:44 2018

@author: gy18os
"""
y0 = 50
x0 = 50
print (y0, x0)
print (y0, x0)

import random
int = random.randint(0, 100)
print (int)
#set up first set of vairables
if random.random () <0.5:
    y0 = y0 + 1 
else:
    y0 = y0 - 1

if random.random () <0.5:
    y0 = y0 + 1 
else:
    y0 = y0 - 1

print (y0, y0)
    
if random.random () <0.5:
    x0 = x0 + 1 
else:
    x0 = x0 - 1

if random.random () <0.5:
    x0 = x0 + 1 
else:
    x0 = x0 - 1

print (x0, x0)
#Set up second set
x1=50
y1=50
print (x1, x1)
print (y1, y1)
#set up y1
if random.random () <0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1
#set up y1 twice    
if random.random() <0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1
print (y1, y1) 
#set up x
if random.random () <0.5:
    x1 = x1 + 1
else:
    x1 = x1 - 1
#set up x twice
if random.random () <0.5:
    x1 = x1 + 1
else:
    x1 = x1 - 1
#print the outcome, reason for printing twice is a 2 step code.
print (x1,x1)

y_diff = (y0 - y1)
y_diffsq = y_diff * y_diff
x_diff = (x0 - x1)
x_diffsq = x_diff * x_diff
sum = y_diffsq + x_diffsq 
distance1 = sum**0.5
print(distance1) 