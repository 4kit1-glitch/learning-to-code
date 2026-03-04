
reader = open('chapter9/words.txt')

def special_lines(file):
    for line in file:
        if line.startswith('***'):
            print(line.strip())