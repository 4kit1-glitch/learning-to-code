# program prints the current working dir

import os

print(os.getcwd())
print(os.path.abspath("memo.txt")) # gets the absolute path
print(os.listdir("/home/")) #listing individual paths 
print(os.path.exists("memo.txt")) 
print(os.path.isfile("words.txt"))
print(os.path.isdir("/home"))

# problem arises from defining absolute path 
# try relative path to be relative
print(os.path.join("/home", "kit", "Documents"))
print(os.path.exists(os.path.join("/home", "kit", "Documents")))


#writing files
with open("memo.txt", "w") as file:
    file.write("hello")

with open("memo.txt") as file:
    print(file.readline())



