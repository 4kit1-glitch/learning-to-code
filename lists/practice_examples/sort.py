#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 07:14:48 2026

@author: aimmee
"""

numbers = [20, 35, 12, 80, 50]


def my_func(num):
    return num


numbers.sort(key=my_func)

fruits = ['apple', 'banana', 'cherry', "ple", 1, 0, 100]

fruits.reverse()

print(fruits)

print(numbers)
