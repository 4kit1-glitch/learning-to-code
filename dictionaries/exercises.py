# -*- coding: utf-8 -*-

word = "brontosaurus"
chr_freq = {}


def count_chars(word):
    for char in word:
        count = 1
        if char in chr_freq:
            count += 1
        chr_freq.update({char: count})


def display_count(letter):
    count_chars(word)
    return chr_freq.get(letter.lower(), 0)


def find_repeats(counter):
    return [key for key, value in counter.items() if value > 1]


count_chars(word)
print(find_repeats(chr_freq))
