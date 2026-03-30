#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 12:00:46 2026
different methods of reading files
@author: aimmee
"""

file_object = open('words.txt')
reader = file_object.read()
word_list = reader.split('\n')
print(word_list)
