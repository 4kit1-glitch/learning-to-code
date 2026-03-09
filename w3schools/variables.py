x, y, z = 1, "hello", 9.7

print(x, y, z)

x = y = z = "damn"
print(x, y, z)

#unpacking
fruits = ("apple", "banana", "cherry")
x, y, z = fruits
print(x)
print(y)
print(z)

#global variables and global keyword

def my_func():
    global name
    name = "harry"
    print(name)

def other_func():
    print(name) #name appears here cause it has been made global with the global keyword