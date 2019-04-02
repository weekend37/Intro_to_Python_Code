#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
multiple inputs and outputs
@author: helgi
"""

def swap(x, y): 
    myTemp = x 
    x = y
    y = myTemp
    return x, y
  
def ástuSwap(x,y):
    return y,x
    
# __main__
x = 2
y = 3
print("í byrjun er x =", x) 
print("og y =", y)
x, y = ástuSwap(x, y) 
print("en svo verður x =", x) 
print("og y =", y)


