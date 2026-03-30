my_dict = {
    "one": 1,
    "two": 2,
    "three": 3
}
keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()

print(keys)
print(values)
print(items)

#get values with get function
print(my_dict.get("one"))

#get values by []
print(my_dict["one"])

#updating values with the update method
print(type(my_dict["three"]))
my_dict.update({"three": '3'})
print(type(my_dict["three"]))

#updating with []
my_dict["three"] = [3]
print(type(my_dict["three"]))