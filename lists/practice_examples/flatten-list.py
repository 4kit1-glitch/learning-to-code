#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 23:43:52 2026

@author: aimmee
"""

from functools import reduce
from operator import add
import itertools as it

# nested list list of list
numbers = [[1, 3, 5], [6], [2, 3, 5, 7]]
mixed = [["mummy", "daddy", "aunt", "uncle"], [1, 2, 3, 4]]
fruits = ["apple", "banana", "pear"]

# method 1 of flattening
# list comprehension using for loops
flat_numbers = [item for items in numbers for item in items]
print(flat_numbers)


# sum built in function -- very bad method not clear
new_list = sum(numbers, [])
print(new_list)

# using functools reduce with labda --good to use
flat_list = reduce(lambda x, y: x + y, numbers)
print(flat_list)

# ussing operator module with add func
flat_list = reduce(add, numbers)
print(flat_list)

# using itertools chain -- clean and consise nice method
print(list(it.chain(*numbers)))
# if you dont want the asterist use .from_iterable (magic operator)
print(list(it.chain.from_iterable(numbers)))
