#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 15:29:57 2026

@author: aimmee
"""
# the * operator in a function parameter
# packs all inputted arguements into a tuple

# function that calculates the mean of a range of numbers


def mean(*args):
    return sum(args) / len(args)


def median(*args):
    lenght = len(args)
    sorted_args = sorted(args)
    if lenght % 2 == 0:
        return sorted_args[lenght / 2]
    return sorted_args[lenght // 2]


def mode(*args):
    counter = {}

    def count_occurence(args):
        for var in args:
            if var not in counter:
                counter[var] = 1
            else:
                counter[var] += 1
    count_occurence(args)
    return max([value for key, value in counter.items()])
