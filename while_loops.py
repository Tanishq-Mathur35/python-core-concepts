'''WHILE LOOPS'''
# i = 1
# while(i <= 30):
#     print(i, end=" ")
#     i += 1



'''While Loops Questions'''

'''Ques 1 (Seperation of digits in a number)'''
# n = int(input("Enter a number: "))

# while n > 0:
#     digit = n % 10
#     print(digit)
#     n = n // 10


'''Ques 2 (Reverse of a number)'''
# n = int(input("Enter a number: "))

# rev = 0

# while n > 0:
#     rev = rev * 10 + n % 10
#     n = n // 10

# print(rev)


'''Ques 3 (Palindrome Number)'''
n = int(input("Enter a number: "))

rev = 0
copy = n

while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10

if rev == copy:
    print(f"{copy} is a palindrome number.")
else:
    print(f"{copy} is not a palindrome number.")
