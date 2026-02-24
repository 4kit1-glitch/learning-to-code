# program counts stuff in a word

word = "python is an amazing programming language"


print(f"number of words = {len(word.split())}")
print(f"number of characters = {len(word)} including spaces")
print(f"a appears {len(word.split('a')) - 1} times")