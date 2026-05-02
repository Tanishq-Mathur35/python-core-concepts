# class Animal:
#     @property
#     def show(self):
#         print("hello How are you ?")

# obj = Animal()
# obj.show



'''BASIC DECORATOR'''
# def decorate(func):
#     def wrapper():
#         print("This is a basic decorator (before function call)")
#         func()
#         print("This is a basic decorator (after function call)")
#     return wrapper


# @decorate
# def hello():
#     print("Hi, I am Tanishq!!")

# hello()



'''*args'''
# def addition(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     print(f"The sum of {args} is {sum}.")


# addition(10, 20, 30, 40, 50)



'''**kwargs'''
# def information(**kwargs):
#     for i in kwargs:
#         print(f"{i} : {kwargs[i]}")

# information(name = "Tanishq", age = 20,  marks = 90)



'''DECORATOR WITH ARGUMENTS'''
# def decorate(func):
#     def wrapper(*args, **kwargs):
#         print("The addition of two numbers:-")
#         func(*args, **kwargs)
#         print("Thank you")
#     return wrapper


# @decorate
# def addition(a, b, c):
#     print(f"The sum of {a}, {b} and {c} is {a+b+c}.")

# addition(10, 40, 50)



'''List Comprehension'''
# l = [i for i in range(1, 21) if i%2==0]
# print(l)



'''Dictionary Comprehension'''
# d = {i : i**3 for i in range(1, 11)}
# print(d)



'''LAMBDA FUNCTIONS'''
# multiply = lambda a, b : a * b
# print(multiply(10, 20))

# even_or_odd = lambda a : "EVEN" if a%2==0 else "ODD"
# print(even_or_odd(11))



'''MAP FUNCTION'''
# a = [1,2,3,4,5]
# result = map(lambda x : x**2, a)
# print(list(result))



'''FILTER FUNCTION'''
# a = [1,2,3,4,5,6,7,8,9,10]
# result = filter(lambda x : x%2==0, a)
# print(list(result))



'''Modules and Packages'''
# from package import maths, hello

# maths.addition(10, 20)
# maths.multiplication(10, 20)
# hello.hello()



'''In Built Modules'''
# import math
# print(math.sqrt(2566))
