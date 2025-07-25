# app e: Merge Dictionaries

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict2 = {'key1': 'value1', 'a': 1,'key2': 'value2', 'c': 'x'}

dict3 = {**dict1, **dict2}
print(dict3)

dict4 = {}
dict4.update(dict1)
dict4.update(dict2)
print(dict4)

dict1.update(dict2)

print(dict1)

dict5 = {}
for keyw,value in dict4.items():
    dict5.update(dict([(keyw,value)]))

print(dict5)
