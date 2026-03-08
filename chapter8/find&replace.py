reader = open('chapter8/words.txt')
writer = open('chapter8/story.txt', 'w')

def total_lines(file_object):
    total = 0
    for line in file_object:
        total += 1
    return total 
    
def portfolio(file_object):
    line_num = 0
    for line in file_object:
        if line_num > 13:
            writer.write(line)
        line_num += 1

def find(file_object , item):
    for line in file_object:
        if item in line:
            print(line)

def replace(file_object, old, new):
    for line in file_object:
        if old in line:
            line = line.replace(old, new)
            writer.write(line)
            
    pass

portfolio(reader)