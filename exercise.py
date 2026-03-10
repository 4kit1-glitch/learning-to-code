#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 18:07:43 2026

@author: aimmee
"""


def is_anacram(word1, word2):
    for letter in list(word1):
        if letter not in list(word2):
            return False
    return True


word1 = "hello"
word2 = "lleoh"

if is_anacram(word1, word2):
    print("anacrams")
else:
    print("not anacrams")
