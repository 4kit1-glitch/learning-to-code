
import re

def head(file_path, num = 5, condition = None):
    reader = open(file = file_path)
    count = 0
    for line in reader:
        if count >= num:
            break
        elif condition == None:
            print(line.strip())
        else:
            writer = open('chapter9/new-file.txt','+a')
            writer.write(line)
        count += 1


head('chapter9/words.txt', 4, 3)
    