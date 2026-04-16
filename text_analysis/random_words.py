import random
from unicodedata import category

text = open('text.txt')
word_freq = {}
words = []
random_words = []


def coun_words(text):
    for line in text:
        for word in line.split():
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1


def is_punc(char):
    return category(char).startswith('P')

def clean_word(word):
    punctuations = ''.join([char for char in word if is_punc(char)])
    return word.strip(punctuations)

coun_words(text)
words = [clean_word(key) for key in word_freq]

# selecting a random word
random_word = random.choice(words)
print(random_word)

#selecting 10 random choices 
random_words = random.choices(words, k= 5)
print(random_words)

#controlling selection with a weight 
weight = word_freq.values()
random_words = random.choices(words, weights=weight, k= 5)
            
            


