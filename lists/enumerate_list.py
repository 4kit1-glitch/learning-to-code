#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 16:24:30 2026

@author: aimmee
"""
txt = "hello"
lst = dict(enumerate(txt))
print(lst)

for i, j in enumerate(txt):
    print(i, type(i))

# if you use one value you get a tuple bu default
for i in enumerate(txt):
    print(i)

# dictionary comprehension
print({i: j for i, j in enumerate("hello")})

# you can control the index it mus'nt be 0 by modifcations
