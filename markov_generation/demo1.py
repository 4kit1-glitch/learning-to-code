#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 15:24:55 2026

@author: kit
"""

from unicodedata import category
from random import choice, choices

song = """
Half a bee, philosophically,
Must, ipso facto, half not be.
But half the bee has got to be
Vis a vis, its entity. D'you see?
"""

bigram_count = {}
successor_map = {}

word_list = [word.strip() for word in song.split()]

def clean_word(word):
    puntuations = ''.join([char for char in word if category(char).startswith('P')])
    cleaned_word = word.strip(puntuations).lower()
    return cleaned_word


def count_bigrams(words):
    key = tuple(words)
    if key not in bigram_count:
        bigram_count[key] = 1
    else:
        bigram_count[key] += 1

def add_bigrams(bigram_map):
    for first, second in bigram_map.keys():
        if first not in successor_map:
            successor_map[first] = [second]
        else:
            successor_map[first].append(second)
        
def process_word(word_list):
    window = []
    for word in word_list:
        window.append(clean_word(word))
        if len(window) == 2:
            count_bigrams(window)
            window.pop(0)

def generate_sequence():
    word = choice([key for key, values in successor_map.items()])
    for dummy in range(5):
        successors = successor_map[word]
        word = choice(successors)
        print(word, end=' ')


process_word(word_list)
add_bigrams(bigram_count)

generate_sequence()
print()