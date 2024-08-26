# my_tuple = (1, 2, 3)
# # Tuples are immutable, so you cannot modify them.
# # If you need to modify elements, use a list instead.
# print(my_tuple)

# countries = ('Malaysia', 'Japan', 'Armenia', 'Brazil', 'Australia')
# temp = list(countries)
# temp.append ('Russia')
# countries = tuple(temp)
# print(countries)
# temp.pop(2)
# temp[0] = "Indianesia"
# countries = tuple(temp)
# print(countries)

# mytuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# index = mytuple.index(4)
# print(index)

# f strings
# name = 'Niegerl'
# age = '21'
# print(f'Hello, my name is {name} and I am {age} years old.')

# a = 5
# b = 10
# print(f'The sum of {a} and {b} is {a+b}')

# Formatting numbers
# pi = 3.14159
# formatted = f'the value of pi with 2 decimal is {pi:.3f}'
# print(formatted)

# name = 'Niegel'
# age = 25
# print (f'Hello, my name is {name} and I am {age*365} years old.')
# message = f"user:{f'name: {name}, Age: {age}'}"
# print(message)

# name = 'Muscrat'
# age = 29
# message = f"""
# Hello
# My name is {name}
# I am {age} years old
# """
# print(message)

# def factiorial(n):
#   if n == 0 or n == 1:
#     return 1
#   else:
#     return n * factiorial(n - 1)
# print(factiorial(5))

# my_set = {3,4,5,3,2,1,3,4}
# print(my_set)
# A set with the mixed data types
# mixed_set = {1, 'apple', 3.14, (2,3)}
# print(mixed_set)

# myset = set([1, 3.14, 'M4A1',(2,3)])
# print(myset)

# emptyset = set()
# print(f'this is the output of the string: {emptyset}')

# set method
# myset = {1,2,3,4,5,6,7,8,9,10}
# myset.add (11)
# print(myset)

# myset= {1,2,3,4}
# myset.update({3,4,5,6})
# print(myset)

# myset = {1,2,3,4,5,6,7,8,9,10}
# myset.remove(5)
# print(myset)

# myset = {1,2,3,4,5,6,7,8,9,10}
# myset.discard(12)
# print(myset)

# my_set = {1,2,3}
# removed_item = my_set.pop()
# print(removed_item)
# print(my_set)

# guns = {'M4', 'M16', 'M16A4', 'M16A1', 'M16A2', 'M16A'}
# guns.pop()
# print(guns)

# my_set = {1,2,3}
# my_set.clear()
# print(my_set)

#. intersection

# my_set = {1,2,3,4,5}
# another_set = (4,5,6,7,8)
# print(my_set.intersection(another_set))

# intersection_set = {1,2,3,4,5}
# print(intersection_set)

# set2 = {2,3,4}
# set1 = {1,2,3}
# sym_diff = set1.symmetric_difference(set2)
# print(sym_diff)
# sym_diff_set = set1 ^ set2
# print(sym_diff_set)
# difference_set = set2.difference(set2)
# print(difference_set)

# set1 = {1,2,3}
# set2 = {1,2}
# print(set1.issubset(set2))
# print(set1.issuperset(set2))
# print(set1.isdisjoint(set2))

# my_dict = {
#   'name': 'Nazca',
#   'age': 21,
# }
# print(my_dict)

# using the dict() function
# my_dict = dict(name = 'Nazca', age = 21, city = 'Kuantania')
# print(my_dict['age'])
# print(my_dict['name'])
# print(my_dict.get('citys','not found'))

# my_dict = {'name': 'Nazca', 'age': 21, 'city': 'Kuantania'}
# item = my_dict.pop('city')
# print(item)
# print(my_dict)

# my_dict = {'name': 'Nazca', 'age': 21}
# my_dict.update({'city': 'Kuantania'})
# print(my_dict)
