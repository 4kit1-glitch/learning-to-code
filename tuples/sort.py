members = {
    "boys": 10,
    "girls": 2,
    "born":5
}
member_count = [(key, value) for key, value in members.items()]

def second_element(x):
    return x[1]

#before sort
print(member_count)

#after sort
member_count.sort(key = second_element)
print(member_count)

