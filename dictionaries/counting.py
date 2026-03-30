#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 16:52:36 2026

@author: aimmee
"""

# to show the number of times a letter or word appears in an iterable
# a dictionary is a good fast and efficient way to do it

word = "brontosaurus"
counter = {}
count = 0

for letter in word:
    if letter not in counter:
        counter[letter] = 1
    else:
        counter[letter] += 1


def find_count(letter):
    if letter in counter:
        return counter[letter]


print(find_count('o'))
