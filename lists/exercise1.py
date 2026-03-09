#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 17:50:47 2026

anagrams solutions

@author: aimmee
"""


def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    for char in word1:
        if char not in word2:
            return False
    return True

def is_anagram2(word1, word2):
    if sorted(word1) == sorted(word2):
        print("anagram")
    else:
        print("not anagram")

