# class FactoryMumbai:     # parent class / superclass
#     a = "I am an attribute mentioned inside Factory Mumbai."

#     def hello(self):
#         print("hello I am a method mentioned inside Factory Mumbai.")


# class FactoryPune(FactoryMumbai):     # child class / sublcass
#     pass


# obj = FactoryPune()
# print(obj.a)
# obj.hello()



'''SINGLE INHERITANCE'''
# class Animal:
#     def __init__(self, name):
#         self.name = name
    
#     def show(self):
#         print(f"Your name is {self.name}.")

    
# class Dog(Animal):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age

#     def show(self):
#         print(f"Your name and age are {self.name} and {self.age} respectively.")


# janvaar = Dog("Tommy", 5)
# janvaar.show()



'''MULTIPLE INHERITANCE'''
# class Animal:
#     def __init__(self, name):
#         pass

# class Human:
#     def __init__(self, name, age):
#         pass

# class robots(Human, Animal):
#     name3 = "Chitty"


# obj = robots()



'''MULTILEVEL INHERITANCE'''
# class Factory:
#     def __init__(self, material, zips):
#         self.material = material
#         self.zips = zips


# class JodhpurFactory(Factory):
#     def __init__(self, material, zips, color):
#         super().__init__(material, zips)
#         self.color = color


# class MumbaiFactory(JodhpurFactory):
#     def __init__(self, material, zips, color, pockets):
#         super().__init__(material, zips, color)
#         self.pockets = pockets


# obj = MumbaiFactory("Leather", 3, "Black", 2)
