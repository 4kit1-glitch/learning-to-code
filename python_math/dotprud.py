#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 16:18:56 2026

@author: kit
"""

l1 = [1, 2, 3]
l2 = [6, 8, 4]

def compute_prod(list1, list2):
    sum = 0
    for x, y in zip(list1, list2):
        sum += x * y
    return sum

print("the total sum is:", compute_prod(l1, l2))