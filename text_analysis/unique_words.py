#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 15:14:58 2026

@author: kit
"""

text = open('text.txt')
word_dict = {}
unique_words = []

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


count_words(text)
select_unique(word_dict)

#sorting by lenght use the len keyword
sorted_words = sorted(unique_words, key= len)

#using the :: operator to select last five words
print(sorted_words[-5::])

# spliting words with punctuations
for word in sorted_words[-5::]:
    if '-' in word:
        print(word.replace('-', ' ').split())