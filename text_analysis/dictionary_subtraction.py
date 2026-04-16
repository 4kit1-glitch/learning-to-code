dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 2, "c": 3, "d": 4}

def subtract_dicts(dict1, dict2):
    result = {}
    for key in dict1:
        if key not in dict2:
            result[key] = dict1[key]
    return result

print(subtract_dicts(dict1, dict2))