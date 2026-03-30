#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 15:15:31 2026

@author: aimmee
"""

names = ["john paul", "james smith"]
Names = []

# list comprehension

Names = [name.title() for name in names]

print(names, Names)
