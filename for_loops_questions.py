'''Question 1'''
# n = int(input("Enter a number: "))

# for i in range(n):
#     print("Hello World")


'''Question 2 (Sum of first n natural numbers)'''
# n = int(input("Enter a number: "))

# sum = 0
# for i in range(1, n+1):
#     sum += i

# print(f"Sum of first {n} natural numbers is {sum}.")


'''Question 3 (Factorial of a number)'''
# n = int(input("Enter a number: "))

# fact = 1
# for i in range(1, n+1):
#     fact *= i

# print(f"Factorial of {n} is {fact}.")


'''Question 4 (Sum of even and odd numbers in a range)'''
# n = int(input("Enter a number: "))

# even_sum = 0
# odd_sum = 0

# for i in range(1, n+1):
#     if i%2==0:
#         even_sum += i
#     else:
#         odd_sum += i

# print(f"Sum of even numbers in range 1 to {n} is {even_sum}.")
# print(f"Sum of odd numbers in range 1 to {n} is {odd_sum}.")


'''Question 5 (factors of a number)'''
# n = int(input("Enter a number: "))

# for i in range(1, n+1):
#     if n%i==0:
#         print(i, end=" ")


'''Question 6 (Perfect Number)'''
# n = int(input("Enter a number: "))

# sum_of_factors = 0

# for i in range(1, n):
#     if n%i==0:
#         sum_of_factors += i

# if sum_of_factors == n:
#     print(f"{n} is a perfect number.")
# else:
#     print(f"{n} is not a perfect number.")


'''Question 7 (Prime Number)'''
# n = int(input("Enter a number: "))

# for i in range(2, n):
#     if n%i==0:
#         print(f"{n} is not a prime number.")
#         break
# else:
#     print(f"{n} is a prime number.")


'''Question 8 (Reverse a String)'''
# a = "TANISHQ"

# for i in range(len(a)-1, -1, -1):
#     print(a[i], end=" ")


'''Question 9 (Palindrome)'''
# a = "racecar"

# b = ""

# for i in range(len(a)-1, -1, -1):
#     b += a[i]

# if a == b:
#     print(f"{a} is a palindrome.")
# else:
#     print(f"{a} is not a palindrome.")


'''Question 10 (Count all letters, digits and special characters in a string)'''
# a = "TANISHQ123!@#$%"

# char = 0
# digit = 0
# special = 0

# for i in a:
#     if i.isdigit():
#         digit += 1
#     elif i.isalpha():
#         char += 1
#     else:
#         special += 1

# print(f"Number of characters: {char}")
# print(f"Number of digits: {digit}")
# print(f"Number of special characters: {special}")
