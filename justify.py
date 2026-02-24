#This program alligns a text into the center of the screen

def print_right(text):
    lenght = len(text)
    spacing  = 40 - lenght  #this calculates the remaining spaces to make it 40
    print(" "*spacing , text)


word1 = "a"
word2  = "hi"
word3 = "anthropic"

print_right(word1)
