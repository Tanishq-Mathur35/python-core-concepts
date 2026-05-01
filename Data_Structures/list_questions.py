'''Question 1'''
# l = [-45, 67, 12, -68, -69, 34]

# print("Positive numbers in the list are:")
# for i in l:
#     if i >= 0:
#         print(i, end=" ")

# print("\nNegative numbers in the list are:")
# for i in l:
#     if i < 0:
#         print(i, end=" ")



'''Question 2 (Average of the list)'''
# l = [12, 435, 67, 89, 23, 25, 69, 90]

# sum = 0

# for i in l:
#     sum += i

# print(f"The Average of the list is {sum/len(l)}.")



'''Question 3 (Greatest number in the list)'''
# l = [12, 67, 89, 23, 25, 435, 69, 90]

# max = l[0]
# idx = 0

# for i in range(len(l)):
#     if l[i] > max:
#         max = l[i]
#         idx = i

# print(f"The greatest number in the list is {max} and its index is {idx}.")



'''Question 4 (2nd largest number in the list)'''
# l = [12, 67, 89, 23, 25, 435, 69, 90]

# sec_max = l[0]

# max = l[0]

# for i in range(len(l)):
#     if l[i] > max:
#         sec_max = max
#         max = l[i]
#     elif l[i] > sec_max:
#         sec_max = l[i]

# print(f"The second largest number in the list is {sec_max}.")



'''Question 5 (check if list is sorted or not)'''
# l = [12, 67, 89, 435, 678, 1000]

# flag = True

# for i in range(len(l)-1):
#     if l[i] > l[i+1]:
#         flag = False
#         break

# if flag:
#     print("The list is sorted.")
# else:
#     print("The list is not sorted.")
