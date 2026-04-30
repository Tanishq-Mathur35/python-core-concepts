# def hello():
#     print("Hello World")

# hello()



'''PARAMETERS AND ARGUMENTS'''

'''Positional Arguments'''
# def sum(a,b):
#     print(f"The sum of {a} and {b} is {a+b}")

# sum(10,20)
# sum(100,200)


'''Keyword Arguments'''
# def greet(name, age):
#     print(f"My name is {name} and I am {age} years old.")

# greet(name="Tanishq", age=20)
# greet(age=20, name="Tanishq")


'''Default Arguments'''
# def greet(name, age=19):
#     print(f"{name} is {age} years old.")

# greet("Tanishq")        # uses default age → 19
# greet("Tanishq", 20)



'''Palindrone Question'''
# def isPalindrome(a):
#     rev = ""

#     for i in range(len(a)-1, -1, -1):
#         rev += a[i]

#     if a == rev:
#         print(f"{a} is Palindrome.")
#     else:
#         print(f"{a} is not Palindrome.")


# isPalindrome("racecar")
# isPalindrome("TANISHQ")



'''Retrun Statement'''
# def hello():
#     return "Hello World"

# print(hello())
