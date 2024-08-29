# class mathoperations:
#     @staticmethod
#     def add(x,y):
#         return x+y
#     @staticmethod
#     def subtract(x,y):
#         return x-y
#     @staticmethod
#     def multiplication(x,y):
#         return x-y
#     @staticmethod
#     def division(x,y):
#         return x/y

# result1 = mathoperations.add(5,2)
# result2 = mathoperations.subtract(5,2)
# result3 = mathoperations.multiplication(5,2)
# result4 = mathoperations.division(5,2)

# print(result1)
# print(result2)
# print(result3)
# print(result4)

# class Dawg:
#     species = 'Canis lupus familiaris'
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed

# dawg1 = Dawg('Rover', 'Golden Retriever')
# dawg2 = Dawg('Max', 'German Shepherd')
# dawg3 = Dawg('Buddy', 'Labrador Retriever')

# print(dawg1.species)
# print(dawg2.species)
# print(dawg3.species)

# Dawg.species = 'unknwon'

# class Vehicle:
#     wheels = 4  

#     def __init__(self, camo, model):
#         self.camo = camo  
#         self.model = model  

#     @classmethod
#     def change_wheels(cls, number):
#         cls.wheels = number  

#     @classmethod
#     def from_string(cls, vehicle_str):
#         camo, model = vehicle_str.split('-')
#         return cls(camo, model)  

# # Changing the number of wheels for all vehicles
# Vehicle.change_wheels(6)
# print(Vehicle.wheels)  

# # Creating a new vehicle using a string
# car = Vehicle.from_string('Tan - Tarantula')
# print(car.camo)  
# print(car.model)  
# print(car.wheels) 

# class Person:
#     def __init__(self, name, age):
#         self.name = name  
#         self.age = age    
#         self.version = 1  

# # Create an instance of the Person class
# p = Person("John", 30)

# # Print the __dict__ attribute of the instance
# print(p.__dict__)

# # Print the help documentation for the Person class
# print(help(Person))

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name}, {self.age} years old"

# p = Person("John", 30)
# print(p)  


import time

# current_time = time.time()
# print(current_time)

# print('start')
# time.sleep(2)
# print('End')

# local_time = time.localtime()
# print(local_time)

# local_time = time.localtime()
# formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', local_time)
# print(formatted_time)

# data = input ('Whats the magic word? ')
# while data != 'Axios!!!':
#     print(f'Lum brada de {data}')
#     data = input('Whats the magic word? ' )

# while (data := input ('Whats the magic word? ')) != 'Axios!!!':
#     print(f'Avada del lupo de {data}')

# some_list = [1,2,3,4,5,6,7,8,9,10]
# value = len(some_list)
# value = len(some_list)
# if value > 5:
#     print(f"List is too long ({value} elements)")
# if (value := len(some_list)) > 5:
#     print(f"List is too long ({value} elements)")


















