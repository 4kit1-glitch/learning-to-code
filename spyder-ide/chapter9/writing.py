
reader = open('chapter9/words.txt')
writer = open('chapter9/written.txt', 'w')

def special_lines(file_object):
    for line in file_object:
        if line.startswith('***'):
            writer.write(line)
    writer.close()
    reader.close()
    
def write(file_object):
    for i in range(3):
        word = input("enter your 3 friends names: ")
        writer.write(word + f"{len(word)}\n")
    writer.close()

def read(file_object):
    for line in file_object:
        if len(line) > 0:
            print(line.strip())
    file_object.close()


write(writer)
read(open('chapter9/written.txt'))