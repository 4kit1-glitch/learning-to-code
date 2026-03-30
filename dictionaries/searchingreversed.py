#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 23:27:37 2026

program prints the two words which one is the reverse of the other

@author: aimmee
"""

word_file = open('words.txt')
word_list = [word.strip() for word in word_file if word != '\n']

word_dict = {}
word_count = 0

for word in word_list:
    word_count += 1
    word_dict[word] = word_count


def reverse_word(word):
    new_word = ''.join(reversed(word))
    return new_word


def find_reversed(word_list):  # slow algorithm
    count = 0
    for word in word_list:
        if reverse_word(word) in word_list:
            count += 1
    return count


def find_reversed2(word_dict):  # Faster more efficient algorithms
    count = 0
    for word in word_dict.keys():
        if reverse_word(word) in word_dict:
            count += 1
    return count


print(find_reversed2(word_dict))
