#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 14:41:56 2026

@author: kit
"""


#computing the results
def g(x):
    result = x**2
    return result

# geting the derivative
def g_derivative(x):
    h = -0.00000001 # accuracy of answer increases as h -> 0
    result = (g(x + h) - g(x)) / h
    return result

output = g_derivative(9)
print(output)
