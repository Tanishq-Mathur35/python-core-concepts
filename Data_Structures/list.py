'''
Core Properties of Lists:
1. Lists are mutable (can be modified after creation).
2. Lists are ordered (maintain insertion order).
3. Lists support indexing and slicing.
4. Lists are dynamic (can grow or shrink in size).
5. Lists can store heterogeneous data types.
6. Lists allow duplicate elements.
'''

a = [1, 2, 3, 4, 5, 6.7, False, "hello", print]

# print(a[1])
# print(a[-1])

# first way
# for i in range(len(a)):
#     print(a[i], end=" ")

# second way
# for i in a:
#     print(i, end=" ")


# print(dir(list))    # prints all the methods and attributes of the list class




'''List Functions'''

# l = [1, 2, 3, 4, 5]

# # 1. append(x) → Adds element x to the end of the list
# l.append(6)

# # 2. insert(i, x) → Inserts element x at index i
# l.insert(2, 10)

# # 3. extend(iterable) → Adds all elements from another iterable
# l.extend([7, 8])

# # 4. remove(x) → Removes first occurrence of x
# l.remove(10)

# # 5. pop([i]) → Removes and returns element at index i (last if not specified)
# l.pop()

# # 6. clear() → Removes all elements from the list
# # l.clear()

# # 7. index(x) → Returns index of first occurrence of x
# idx = l.index(3)

# # 8. count(x) → Returns number of times x appears
# cnt = l.count(2)

# # 9. sort() → Sorts the list in ascending order (in-place)
# l.sort()

# # 10. reverse() → Reverses the list (in-place)
# l.reverse()

# # 11. copy() → Returns a shallow copy of the list
# new_list = l.copy()

# print("List:", l)
# print("Index of 3:", idx)
# print("Count of 2:", cnt)
# print("Copied list:", new_list)
