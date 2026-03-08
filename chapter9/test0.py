#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 23:00:15 2026

@author: aimmee
"""
from re import search
text = 'hello'
pattern = 'h'

for i, char in enumerate('le'):
    if char not in 'el':
        print(False)
    if 'le'[i] == 'el'[i]:
        print("correct position")
    else:
        print("wrong position")
    print(True, i)
