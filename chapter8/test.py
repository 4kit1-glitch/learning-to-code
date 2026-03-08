
import re

story = open('chapter8/read.txt')
info = open('chapter8/info.txt','w')

def user_info(file):
    pattern = r'Mary|Marie'
    for line in file:
        result = re.search(pattern, line)
        if result != None:
            info.write(result.string)
            print(result.span())

user_info(story)
        