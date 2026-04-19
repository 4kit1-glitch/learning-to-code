#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 15:20:49 2026

@author: kit
"""

bad_words = ["bandit", "voleur", "imbecil", "bad"]
good_words = ["intelligent", "friendly", "generous", "kind"]
weight = [0.9, -0.77]

good_count = 0
bad_count = 0

user_message = input("Enter your message: ")
words = user_message.lower().split()

def dot(x, y):
    sum = 0
    for i, j in zip(x, y):
        sum += i * j
    return sum

def check_words(message):
    seen_bad = set()
    seen_good = set()
    for word in words:
        if word in bad_words:
            seen_bad.add(word)
            bad_count += 1
        elif word in good_words:
            seen_good.add(word)
            good_count += 1
    good_bad = (good_count, bad_count)
    sum = dot(weight, good_count)
    predict(sum)

def predict(value):
    if value < 0:
        print("bad message")
    else:
        print("good message")
    

def punish_user(words):
    print("Your message contains bad words")
    print(words)
def praise_user(words):
    print("you used good words the good words you used is are:")
    print(" ".join(words))

check_words(user_message)