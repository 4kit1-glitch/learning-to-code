#empty list 

empty = []

print(type(empty), bool(empty) == bool(None))
print(len(empty))

#list are mutable

greetings = ["hello", "hi", "wassup"]
print(greetings)

greetings[1] = "haw"
print(greetings)

#greetings[3] = "wassup"    list assignment index out of range

print(greetings[::])

#in operator

print("h" in "".join(greetings)) #works but with elements in list 