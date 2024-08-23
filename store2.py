# break and continue

# for i in range (1,11):
#   print(i)
#   if i == 5:
#     print('The loop is stopped')
#     break

# count = 0
# while True:
#   count += 1
#   print(count)
#   if count >= 7:
#     print ('The loop is breaking bad!')
#     break

# continue statement

# for i in range(1,11):
#   if i == 6:
#       continue
#   print ('The loop is skipped')

# word = 'Nazca'
# for i in word:
#   if i == 'z':
#     continue
#   print (i)

# number = [1,2,3,4,5,6,7,8,9,10]
# for i in number:
#   if i % 2 == 1:
#     continue
#   print (i)

# def greet():
#   print('Hello')
#   print('Isnt it nice to be a human?')
#   print('Entirely human!')
# greet()
# greet()
# greet()

# def greet(name):
#   print(f'Hello {name}')
# name = input ('Enter your name: ')
# greet(name)

# def greet (name = 'Nazca'):
#   print(f'Hello {name}')

# greet()
# greet('Iqnis')

# def multiply(x, y):
#   print(x * y)
# multiply(5, 6)
# print (multiply (5,6))
# result = multiply (5,6)
# print (result)

# def check_number(number):
#   if number > 0:
#     return 'Positive'
#   elif number < 0:
#     return 'Negative'
#   else:
#     return 'Zero'
# #test the function
# print (check_number(5))
# print (check_number(-5))
# print (check_number(0))

# positional arguments in function

# def greet(firstname, lastname):
#   print(f'Hello {firstname} {lastname}')
# greet ('Nazca', 'Alfred')

# keyword arguments in function
# def greet (firstname, lastname):
#   print(f'Hello {firstname} {lastname}')
# greet (lastname = 'Nazca', firstname = 'Alfred')

# def greet (firstname, lastname):
#   print(f'Hello {firstname} {lastname}')
# firstname = input ('Enter your firstname: ')
# lastname = input ('Enter your lastname: ')
# greet (firstname, lastname)

#arbitrary function

# def greet (*names):
#   for name in names:
#     print(f'Hello {name}')
# greet ('Nazca', 'Alfred', 'Iqnis','Musckrat', 'Zein')

# list method

# append

# guns = ['AK47', 'M4', 'M16', 'Glock']
# guns.append('M16')
# print(guns)

# insert

# guns = ['AK47', 'M4', 'M16', 'Glock']
# guns.insert(2,'MCX-SPEAR')
# print(guns)

# extend

# guns = ['AK47', 'M4', 'M16', 'Glock']
# guns.extend (['MCX-SPEAR', 'AAC', 'AS-VAL'])
# print(guns)

# pop
# guns = ['AK47', 'M4', 'M16']
# guns.pop(0)
# print(guns)

# clear
# guns = ['AK47', 'M4', 'M16']
# guns.clear()
# print(guns)