#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 16:36:39 2026

@author: kit
"""

from unicodedata import category
word = "!.()Behold-me!"

def clean_word1(word):
    cleaned_word = ""
    for char in word:
        if 'P' not in category(char):
            cleaned_word += char
    return cleaned_word.lower()


def clean_word2(word):
    punctuations = ''.join([char for char in word if category(char).startswith('P')])
    return word.strip(punctuations)

print(clean_word2(word))
    