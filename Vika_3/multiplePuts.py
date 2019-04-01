#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
multiple inputs and outputs
@author: helgi
"""


def swap(x, y): 
    temp = x 
    x = y
    y = temp
    return x, y
  
# __main__
x = 2
y = 3
print("í byrjun er x =", x) 
print("og y =", y)
swap(x, y) 
print("en svo verður x =", x) 
print("og y =", y)


