
reader = open('chapter9/words.txt')
writer = open('chapter9/written.txt', 'w')

def special_lines(file):
    for line in file:
        if line.startswith('***'):
            print(line.strip())