#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 16:15:21 2026

@author: kit
"""

from unicodedata import category

reader = open('text.txt')
word_dict = {}
unique_words = []
punctuations = {}

def count_words(text):
    count = 0
    for line in text:
        words = line.split()
        for word in words:
            count += 1
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
    return count

def select_unique(word_dict):
    for word, freq in word_dict.items():
        if freq == 1:
            unique_words.append(word)
    return unique_words


def count_punctuations(words):
    
    count = 0
    for word in words:
        for char in word:
            if category(char).startswith('P'):
                count += 1
                punctuations[char] = count
    return count

count_words(reader)
select_unique(word_dict)

print(count_punctuations(unique_words))
print(punctuations)
        






















