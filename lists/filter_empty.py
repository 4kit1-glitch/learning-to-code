#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 15:49:20 2026

@author: aimmee
"""

# to filter empty list from a list

lst = [1, 3, 5, [], [1], {}, ""]

# method 1
filtered1 = [x for x in lst if x != []]  # do this
print(filtered1)

# method 2 - using filtered function


def remove_empty(val):
    if val != []:
        return val


filtered2 = list(filter(lambda x: x != [], lst))    # best method
print(filtered2)
