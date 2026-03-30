#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 16:29:00 2026

@author: aimmee
"""

letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
alphabets = letters.split(" ")

letter_to_num = {}
num_to_letter = {}
for idx, letter in enumerate(alphabets):
    letter_to_num[letter] = idx
    num_to_letter[idx] = letter


def shift_letter(word):
    encrypted_word = ""
    for letter in word:
        letter_position = letter_to_num[letter]
        encrypted_word = encrypted_word + \
            num_to_letter[(letter_position + 1) % 23]
    return encrypted_word


word = shift_letter("helloz")


print(word)
