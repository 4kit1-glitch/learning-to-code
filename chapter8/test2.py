# testing the ^ and $ special characters

from re import search
reader = open('chapter8/words.txt')

def count_pattern(file_object):
    count = 0
    pattern = "^c"
    for line in file_object:
        result = search(pattern, line.lower())
        if result != None:
            count += 1
    reader.close()
    return count

pattern = 'colou?r'

print(search(pattern, 'colored baby'))