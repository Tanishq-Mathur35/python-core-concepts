'''
Core Properties of Dictionaries:
1. Dictionaries are mutable (can be modified after creation).
2. Dictionaries are unordered (do not maintain insertion order).
3. Dictionaries do not support indexing and slicing.
4. Dictionaries are dynamic (can grow or shrink in size).
5. Dictionaries can store heterogeneous data types.
6. Dictionaries do not allow duplicate keys.
7. Dictionaries can be nested.
8. Dictionaries use key-value pairs to store data.
'''


# d = {10:100, 20:200, 30:300, 40:400}

# print(d)

# print(d[10]


# print(d.keys())
# print(d.values())
# print(d.items())

# print(dir(dict))    # prints all the methods and attributes of the dict class

# d[50] = 500
# print(d)


# d.update({60:600, 70:700})
# print(d)

# del d[50]
# print(d)



'''Dictionary Traversing'''
# d = {10:100, 20:200, 30:300, 40:400}

# for i in d.keys():     # or d.values()  and  d.items()
#     print(i, end=" ")



'''Dictionary Methods'''

# d = {10:100, 20:200, 30:300, 40:400}

# d.clear()

# d2 = d.copy()

# d3 = d.get(20)

# d.pop(20)

# print(d)
