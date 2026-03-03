
def has_e(word):
    return 'e' in word.lower()

file_object = open('chapter8/words.txt')
num = 0

for line in file_object:
    if has_e(line):
        print(line.strip())
        num = num + 1

print(f"There are {num} lines that use e")
        