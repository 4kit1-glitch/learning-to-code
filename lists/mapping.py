#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 21:55:50 2026

@author: aimmee
"""
from timeit import timeit


numbers = [1, 2, 3, 4, 5]
names = ["john", "peter", "donald"]
empty = []

# the two does the same thing: but map is smelly
str_nums = list(map(str, numbers))
str_nums = [str(x) for x in numbers]


filtered_nums = list(filter(lambda x, y=3: x > y, map(int, numbers)))


def times_two(num):
    return num*2


# the two do the same thing
modified_nums = [times_two(x) for x in numbers]
modified_nums = list(map(times_two, numbers))

print(timeit("map(times_two, numbers)", "from __main__ import times_two, numbers"))
print(timeit("map(lambda x: x*2, numbers)",
      "from __main__ import times_two, numbers"))
