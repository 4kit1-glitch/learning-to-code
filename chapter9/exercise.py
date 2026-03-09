
import random
import re


def head(file_path, num=5, condition=None):
    reader = open(file=file_path)
    count = 0
    for line in reader:
        if count >= num:
            break
        elif condition == None:
            print(line.strip())
        else:
            writer = open('chapter9/new-file.txt', '+a')
            writer.write(line)
        count += 1


def selection():
    word_list = open('word_list.txt')
    selected = random.choice(word_list.readlines()).strip()
    return selected


def comparing(word, selected):
    if word == selected:
        print("You win")
        return (True)
    else:
        position_verification(word, selected)


def position_verification(word, selected):
    for i in range(5):
        if word[i] in selected and word[i] == selected[i]:
            print(word[i] + " in correct position")
        elif word[i] in selected and word[i] != selected[i]:
            print(word[i] + " in but wrong position")
        elif word[i] not in selected:
            print(word[i] + " not there at all")


def play_wordle():
    chosen_word = selection()
    print("******wordle game********")
    while True:
        users_word = input("enter a five letter word: ")
        if comparing(users_word, chosen_word):
            return 0


if play_wordle() == 0:
    print("successful run")
else:
    print("unsuccessful run")
