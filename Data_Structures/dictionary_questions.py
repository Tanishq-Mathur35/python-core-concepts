'''Question 1 (Merge two dictionaries)'''
# d1 = {10:100, 20:200, 30:300, 40:400}
# d2 = {50:500, 60:600, 70:700, 80:800}

# for i in d2:
#     d1[i] = d2[i]

# # print(d1)


# d3 = {**d1, **d2}
# print(d3)



'''Question 2 (Sum all the values in a dictionary)'''
# d = {10:100, 20:200, 30:300, 40:400}

# sum = 0

# for i in d.values():
#     sum += i

# print(f"The sum of all the values in the dictionary is {sum}.")



'''Question 3 (Count the frequency of elements in a list)'''
# a = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 7, 8]
# dict = {}

# for i in a:
#     if i in dict.keys():
#         dict[i] += 1
#     else:
#         dict[i] = 1

# print(dict)



'''Question 4 (Adding values for common keys)'''
# d1 = {10:100, 20:200, 40:300}
# d2 = {40: 400, 50: 500, 60: 600}

# for i in d2:
#     if i in d1.keys():
#         d1[i] += d2[i]
#     else:
#         d1[i] = d2[i]

# print(d1)