#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 21:11:52 2026

@author: aimmee
"""

# list comprehensions with if and else
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
fruits = ["apples", "peaches", "pears", "banana"]
even_sqrs = [number**2 for number in numbers if number % 2 == 0]
negative_odd_nums = [num if num < 0 else num*-
                     1 for num in numbers if num % 2 != 0]

# multiple ifs and fors
chosen = [(num, fruit) if fruit != "apple" else "orange"
          for num in numbers if num < 5
          for fruit in fruits if fruit != "banana" if fruit != "pears"
          and num % 2 == 0]

# just know your conditioning

print(chosen)
