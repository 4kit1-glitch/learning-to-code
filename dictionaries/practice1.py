#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 15:41:57 2026

@author: aimmee
"""

point = {
    'x': 3,
    'y': 5,
    'z': 10
}

# Use .get() so it avoids program crashing if var not present
# print(point.get('x'))

# looping over a dictionary
# by keys
for key in point.keys():
    print(key)

# by values
for value in point.values():
    print(value)

# by items(key- value pair) key + value = item
for item in point.items():
    print(item)
