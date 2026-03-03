
from doctest import run_docstring_examples

def run_docsrings(func):
    run_docstring_examples(func, globals(), name=func.__name__)

def has_e(word):
    """Checks if a word has the letter e
    >>> has_e('happy')
    False
    >>> has_e('help')
    True
    """
    return 'e' in word.lower()

file_object = open('chapter8/words.txt')
num = 0

for line in file_object:
    if has_e(line):
        print(line.strip())
        num = num + 1

# print(f"There are {num} lines that use e")
