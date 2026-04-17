
file_object = open('chapter8/words.txt')

line = file_object.readline()
word = line.strip()
word2 = file_object.readline().strip()
print(word, word2)

# print(file_object.readline() + file_object.readline())