# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 10:25:44 2018

@author: gy18os
"""
import random
#y0 = 50
#x0 = 50
x0 = random.randint(0,99)
y0 = random.randint(0,99)
print (y0, x0)
print (y0, x0)

#set up first set of vairables
if random.random () <0.5:
    y0 = y0 + 1 
else:
    y0 = y0 - 1

if random.random () <0.5:
    x0 = x0 + 1 
else:
    x0 = x0 - 1

print (y0, x0)
    
if random.random () <0.5:
    y0 = y0 + 1 
else:
    y0 = y0 - 1

if random.random () <0.5:
    x0 = x0 + 1 
else:
    x0 = x0 - 1

print (y0, x0)
#Set up second set
#x1=50
x1 = random.randint(0,99)
y1=50
y1 = random.randint(0,99)
print (y1, x1)

#set up y1 and x1 - step 1
if random.random () <0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1  
    
if random.random() <0.5:
    x1 = x1 + 1
else:
    x1 = x1 - 1
print (y1, x1) 
#set up y1 and x1 twice - step 2 
if random.random () <0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1

if random.random () <0.5:
    x1 = x1 + 1
else:
    x1 = x1 - 1
#print the outcome, reason for printing twice is a 2 step code.
print (y1,x1)

y_diff = (y0 - y1)
y_diffsq = y_diff * y_diff
x_diff = (x0 - x1)
x_diffsq = x_diff * x_diff
sum = y_diffsq + x_diffsq 
distance1 = sum**0.5
print(distance1) 