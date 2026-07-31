dict1 = {'apple': 7, 'orange': 2, 'peach': 5}
dict2 = {'kiwi': 1, 'apple': 6, 'orange': 2}

keys = set(dict1.keys()) | set(dict2.keys())
result = {}

for key in keys:
    result[key] = dict1.get(key, 0) + dict2.get(key, 0)

print(result)
