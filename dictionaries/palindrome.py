#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 18:02:26 2026

@author: aimmee
"""

word_file = open('words.txt')
word_dict = {}

count = 0
for word in word_file:
    count += 1
    word_dict[word.strip()] = count


def reverse_word(word):
    return ''.join(reversed(word))


def is_palindrome(word):
    return reverse_word(word) == word


for word in word_dict:
    if is_palindrome(word):
        print(word)
