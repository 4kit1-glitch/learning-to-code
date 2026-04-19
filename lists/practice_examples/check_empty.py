#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 15:39:01 2026

@author: aimmee
"""

lst = [1, 3, 4, 5, 6]
lst2 = []
lst3 = [[], []]

x = 0  # zero is falsy

if not bool(x):
    print("falsy")

# method 1

if not lst:  # recommended way
    print("empty")

# method 2 - contains type verification

if isinstance(lst, list) and not lst:  # best method for validation
    print("empty")

if lst == []:
    print("empty")

if not any(lst3):
    print("empty")
