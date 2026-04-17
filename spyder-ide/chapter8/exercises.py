
from doctest import run_docstring_examples

def run_doctest(func):
    run_docstring_examples(func, globals(), name=func.__name__)

def uses_none(word, restricted):
    for letter in restricted.lower():
        if letter in word.lower():
            return True
    return False

def used_only(word, available):
    for letter in word.lower():
        if letter not in available.lower():
            return False
    return True

def uses_all(word, required):
    for letter in required.lower():
        if required in word.lower:
            return True
    return False

def check_word(word, available, required):
    count = 0
    cnd = False
    for letter in word.lower():
        count += 1
        if letter in available.lower():
            cnd = True
        else:
            cnd = False
    if cnd and count >= 4:
        if required in word:
            return True
        else:
            return False
        
    return False