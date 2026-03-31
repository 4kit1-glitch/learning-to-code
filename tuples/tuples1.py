#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 15:00:11 2026

@author: aimmee
"""


def do_arithmetic(x, y):
    plus = x + y
    diff = x - y
    mult = x * y
    div = x / y

    return (plus, diff, mult, div)


def min_max(sequence):
    return min(sequence), max(sequence)


numbers = [3, 2, 1, 5]


print(min_max(numbers))
