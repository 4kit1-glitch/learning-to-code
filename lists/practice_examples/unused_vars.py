#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 16:04:04 2026

@author: aimmee

declaring unused variables in python with list comprehension
"""

["hello" for i in range(10)]  # dont do this
["hello" for _ in range(10)]  # do this instead
["hello" for dummy in range(10)]  # maybe

some_stuff = [("key", "value"), ("key1", "value1")]
keys = list(key for key, _ in some_stuff)  # key generator

for _, value in some_stuff:
    reversed_value = ''.join(reversed(value))
    print(reversed_value)
