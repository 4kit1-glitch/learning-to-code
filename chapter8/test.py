
import re

story = open('chapter8/read.txt')
info = open('chapter8/info.txt')

def user_info(file):
    pattern = r'mary|marie|'
    for line in file:
        if re.search(pattern, line) != None:
            info.write(line)
        