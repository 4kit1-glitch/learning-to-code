
def compare_word(word1, word2):
    if word1 < word2:
        print(f"{word1} comes before {word2}")
    elif word1 > word2:
        print(f"{word2} comes before {word1}")
    else:
        print("the same words")

compare_word("$help", "2hep")