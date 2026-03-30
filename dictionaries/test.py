# -*- coding: utf-8 -*-

numbers = {"one": 1, "two": 2, "three": 3}

if 1 in numbers:
    print(True)
else:
    print(False)

if "one" in numbers.values():
    print(True)
else:
    print(False)

if "one" in numbers.items():
    print(True)
else:
    print(False)

txt = "hello"

reader = open('words.txt')

# for line in reader.readlines():
#   print(line.strip())
