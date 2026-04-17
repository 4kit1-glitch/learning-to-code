
def uses_any(word, letters):
    for letter in letters.lower():
        if letter in word.lower():
            return True
    return False


print(uses_any("banana", "o"))