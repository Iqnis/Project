# add = lambda x, y: x + y
# result = add (5,6)
# print(result)

# def add (x,y):
#   return x + y
# result = add(5,6)
# print(result)

# Define a list of number
# numbers = [1,2,3,4,5]

# # Use map() function to square each number
# # square_numbers = list(map(lambda x: x**2, numbers))
# # square_numbers = list(map(lambda x: x+2, numbers))

# # Print the squared numbers
# print(square_numbers)

# words = ['apple', 'banana', 'cherry']
# uppercase_words = list(map(lambda word: word.upper(), words))
# print(uppercase_words)

# a = [1,2,3]
# b = [1,2,3]
# print (a is b)
# print (a == b)

# a = [1,2,3]
# b = [1,2,3]
# print (a is b)
# d = a
# print (a is d)

# class person:
#   name = 'Nazca'
#   occupation = 'Imperial Prestiged Hussars'
#   networth = 100000

#   # method to print information about a person
#   def info(self):
#       print(f"{self.name} is a {self.occupation} and his networth is {self.networth}")

# w = person()
# l = person()

# c = person()
# h = person()
# a = person()
# d = person()

# w.name = 'Nazca'
# w.occupation = 'Imperial Prestiged Hussars'
# w.networth = 100000
# w.info()

# l.name = 'Nieger'
# l.occupation = 'Cotton Picker'
# l.networth = 12
# l.info()

# c.name = 'Iqnis'
# c.occupation = 'Imperial Royal Cataphract'
# c.networth = 500000
# c.info()

# h.name = 'Rosevelt'
# h.occupation = 'Imperial High General'
# h.networth = 1000000
# h.info()

# a.name = 'Joseph'
# a.occupation = 'Imperial Trooper'
# a.networth = 10000
# a.info()

# d.name = 'Rusha'
# d.occupation = 'Imperial Trooper'
# d.networth = 10000
# d.info()

# # Define the Person class with a constructor
# class Person:
#     # Constructor method
#     def __init__(self, name, occupation, networth):
#         # Initialize instance attributes
#         self.name = name
#         self.occupation = occupation
#         self.networth = networth

#     # Method to display information about the person
#     def info(self):
#         print(f"Name: {self.name}")
#         print(f"Occupation: {self.occupation}")
#         print(f"Net Worth: ${self.networth}")

# # Create an instance of the Person class
# person1 = Person("Nazca", "Imperial Prestiged Hussars", 100000)
# person2 = Person("Nieger", "Cotton Picker", 12)
# person3 = Person("Iqnis", "Imperial Royal Cataphract", 500000)
# person4 = Person("Rosevelt", "Imperial High General", 1000000)
# person5 = Person("Joseph", "Imperial Trooper", 10000)
# person6 = Person("Rusha", "Imperial Trooper", 10000)

# person1.info()
# person2.info()
# person3.info()
# person4.info()
# person5.info()
# person6.info()

# Define a decorator function
# def my_decorator(func):
#   def wrapper():
#     print('Before function execution')
#     func()
#     print('After function execution')
#   return wrapper

# @my_decorator
# def Warcry():
#   print('PANTANG MAUT SEBELUM AJAL!!!')
# Warcry()

# Getter and setter
# class Pawn:

#   def __init__(self, name, age):
#       self._name = name 
#       self._age = age    

#   # Getter method for the name attribute.
#   def get_name(self):
#       return self._name
#   def set_name(self, name):
#       self._name = name

#   def get_age(self):
#       return self._age

# #   def set_age(self, age):
# #       self._age = age

# # # Create an instance of the Pawn class
# # p1 = Pawn('Nazca', 21)
# # print(p1.get_name())
# # print(p1.get_age())

# # p2 = Pawn('Iqnis', 19)
# # print(p2.get_name())
# # print(p2.get_age())

# # Define the Parent class
# class Parent:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         # This method can be used by the Child class if needed
#         print(f"Hello, my name is {self.name}.")

# # Define the Child class that inherits from Parent
# class Child(Parent):
#     def __init__(self, name, age):
#         super().__init__(name)  # Initialize Parent class
#         self.age = age

#     def greet(self):
#         # Overriding greet method to match the desired output format
#         print(f"Hello, my name is {self.name} and I am {self.age} years old.")

#     def display_age(self):
#         print(f"My age is {self.age}.")

# # Create an instance of Child
# c = Child("Nazca", 26)
# c.greet()
# c.display_age()