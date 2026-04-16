#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 14:46:06 2026

@author: kit
"""

sentence = "hello mr Kit i want to be your friend"
word_list = sentence.split()
bigram_count = {}


def count_bigrams(words):
    key = tuple(words)
    if key not in bigram_count:
        bigram_count[key] = 1
    else:
        bigram_count[key] += 1


def process_word(word_list):
    window = []
    for word in word_list:
        window.append(word)
        if len(window) == 2:
            count_bigrams(window)
            window.pop(0)

process_word(word_list)
print(bigram_count)