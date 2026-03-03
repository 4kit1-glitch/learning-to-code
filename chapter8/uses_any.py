
def uses_any(word, letters):
    for letter in letters:
        if letter in word:
            return True
        else:
            return False


print(uses_any("banana", "e"))