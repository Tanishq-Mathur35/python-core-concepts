'''
Core Properties of Sets:
1. Sets are mutable (can be modified after creation).
2. Sets are unordered (do not maintain insertion order).
3. Sets do not support indexing and slicing.
4. Sets are dynamic (can grow or shrink in size).
5. Sets can store heterogeneous data types.
6. Sets do not allow duplicate elements.
'''

# s = {1, 2, 3, 4, 5, 5}
# print(s)

# print(dir(set))    # prints all the methods and attributes of the set class



'''Hash Function'''
# b = hash("hello")
# print(b)

# c = hash((1, 2, 344))
# print(c)



'''Set Traversing'''
# a = {1, 8, 9, "Hello", 2, 3, 4, 5}

# for i in a:
#     print(i, end=" ")



'''Set Methods'''
# a = {1, 2, 3, 4, 5}

# a.add(6)

# a.remove(4)

# a.discard(4)

# a.pop()

# a.clear()

# print(a)


a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(a.union(b))                       # or we can do a|b
print(a.intersection(b))                # or we can do a&b
print(a.difference(b))                  # or we can do a-b
print(a.symmetric_difference(b))        # or we can do a^b
