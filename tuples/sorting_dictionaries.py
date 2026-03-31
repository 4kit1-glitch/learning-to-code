members = {
    "boys": 10,
    "girls": 2,
    "born": 5,
    "unborn": 3,
    "dead": 13
}

sorted = sorted(members.items(), key= lambda x : x[1])
print(sorted)

