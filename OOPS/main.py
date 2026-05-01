# class Factory:
#     a = 12   # attribute : variable that is defined inside a class

#     def hello(self):    # method : function that is defined inside a class
#         print("Hello World!")


# obj = Factory()

# print(obj.a)
# obj.hello()



'''CONSTRUCTOR'''
# class Bag_Factory:
#     def __init__(self, material, zips, pockets):
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets

#     def show(self):
#         print(f"Your Object details are: {self.material}, {self.zips}, {self.pockets}")



# reebok = Bag_Factory("Leather", 3, 2)
# # print(reebok.pockets)
# reebok.show()


# campus = Bag_Factory("Cotten", 2, 4)
# # print(campus.material)
# campus.show()



'''ATTRIBUTES'''
# class Animal:
#     name = "Lion"    # class attribute

#     def __init__(self, age):
#         self.age = age    # instance attribute



'''METHODS'''
# class Animal:
#     name = "Lion"

#     def __init__(self, age):
#         self.age = age

#     def show(self):       # instance method
#         print(f"Your age is {self.age}")

#     @classmethod
#     def hello(cls):
#         print("How are you ?")

#     @staticmethod
#     def info():
#         print("This is a static method")


# obj = Animal(12)
# obj.show()
# obj.hello()
# obj.info()
