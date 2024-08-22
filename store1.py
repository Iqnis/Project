# print("Hello to My Whole World")

# a = 35
# print("the type of this var is", type (a))

# b = 3.5
# print("the type of this var is", type (b))

# c = "Nazca"
# print("the type of this var is", type(c))

# d = True
# print("the type of this var is", type(d))

# list =[1,2,3,4,5,6,7,8,9,10]
# print(list)

# person = {
#   "Nazca",
#   "Melina",
#   "Karina",
#   "Dian"
# }

# print(person)

# # mathematical example

# # subtract
# print(5+6)
# # minus
# print(15-6)
# # division
# print(15/6)
# # flow division
# print(15//6)
# # dunno about this one
# print(5%3)
# # substraction
# print(5*3)
# print(6*3)
# print(5**3)

# a = "12"
# print(type(a))

# b = 15
# print(type(b))

# a = "12"
# i = int(a)
# print(type(i))

# a = "69"
# i = int(a)
# print(type(i))

# a = 3
# b = 2.5
# c = a + b
# print(c)

# c = 1.9
# d = 8
# print(c + d)

# print('Welcome to AskPython Quiz')
# answer=input('Are you ready to play the Quiz ? (yes/no) :')
# score=0
# total_questions=3

# if answer.lower()=='yes':
#     answer=input('Question 1: What is your Favourite programming language?')
#     if answer.lower()=='python':
#         score += 1
#         print('correct')
#     else:
#         print('Wrong Answer :(')

#     answer=input('Question 2: Do you follow any author on AskPython? ')
#     if answer.lower()=='yes':
#         score += 1
#         print('correct')
#     else:
#         print('Wrong Answer :(')

#     answer=input('Question 3: What is the name of your favourite website for learning Python?')
#     if answer.lower()=='askpython':
#         score += 1
#         print('correct')
#     else:
#         print('Wrong Answer :(')

# print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
# mark=(score/total_questions)*100
# print('Marks obtained:',mark)
# print('BYE!')

# a = input ('What is your Kamen Rider name?')
# print('I am a Kamen Rider', a)

# a = input('Enter your 1st Lucky number:')
# b = input('Enter your 2nd Lucky number:')

# print(int(a) + int(b))

# name = input("Enter your name: ")
# age = input("Enter your age: ")

# print("Hello, " + name + "!")
# print("You are " + str(age) + " years old.")

# single line string
# a = 'Nazca'
# print(a)

# # multi line string
# b = ''' Hello how are you
# i am fine
# thank you'''

# print(b)

# laught = '5'
# print(laught*10)

# # indexing string
# a = "python"
# print(a[0])
# print(a[5])

# # slicing string
# a = "empty is good"
# # print(a[1:6])
# # print (a[0:-3])
# print ('length of the string is', len(a))
# print ('uppercase string', a.lower())
# print ('lowercase string', a.upper())
# print ('remove trainling spaces', a.rstrip('y'))
# print ('replace string', a.replace('empty', 'Nazca'))

# a = 'introduce to pYthOn'
# # print('capitalize', a.capitalize())
# # print('center align', a.center(50, '*'))
# print('occurance', a.count('c'))

# a = 'The only reason these barbarian still alive and thriving is thanks to our mercy and'
# b = 'tolerance of their ignorance. However, it appear that a lot of them are forgetting'
# c = 'this fact. Perphaps we should remind them again with fire and steel'
# print(a,b,c)
# print ('find', a.find('barbarian'),b.find('ignorance'),c.find('fire'))

# str1 = "Welcome to the Console!!!"
# print("Ends with '!!!':", str1.endswith("!!!"))
# print("Ends with 'to' between indices 4 and 10:", str1.endswith('to', 4, 10))

# a = "Welcome to the python/n"
# print("Is printable", a.isprintable())

# str1 = '             '
# print('is space:', str1.isspace())

# str2 = "    "
# print('is space (with tab):', str2.isspace())

# str1 = 'Python is an Interpreted Language'
# print ('Start with Python:', str1.startswith('Python'))

# str2 = 'To kill a Mocking Bird'
# print('Is title case (example 2):', str2.istitle())

# str1 = "Python is a Interpreted Language"
# print ("Start with Python:", str1.startswith('Python'))

# str1 = "My name is Nazca. I am a honest man"
# print("Title case: ", str1.title())

# age = int(input("Enter your age: "))
# print('Your age is:', age)
# if age < 18:
#   print('You are young')
# else:
#   print('You are adult')
#   print('and sad one too')

# applePrice = 69
# budget = 50
# if (budget - applePrice > 50):
#   print ('Axios, add 1 kg Apples to the cart')
# else:
#   print('Axios, do not add Apples to the cart')

# number = int (input ('Enter a number:'))
# print ('You entered:', number)

# if number > 0:
#   print ('The number is positive!')
# if number % 2 == 0:
#   print('The number is even!')
# else:
#   print ('The number is odd!')
# else if number < 0:
# #    print ('The number is negative!')
#    if number % 2 == 0:
#       print ('The number is even!')
#    else:
#       print ('The number is odd!')

# day = input ('Enter a day of the week:').strip().lower()

# match day:
#   case 'Monday':
#     print ('Gotta Work')
#   case 'Tuesday':
#     print ('Get Money')
#   case 'Wednesday':
#     print ('Make a Money')
#   case 'Thursday':
#     print ('Make it Purr')
#   case 'Friday':
#     print ('Sugar Rush Ride')
#   case 'Saturday':
#     print ('Its Holiday')
#   case 'Sunday':
#     print ('Its Weekend')
#   case _:
#     print ('Its DOOMSDAY!!!')

# guns = ['AK47', 'M4', 'M16', 'Glock']
# for gun in guns:
#   print (guns)

# for u in range (69):
#   print(u)

# name = 'Auswitzer'
# for i in name:
#   print(i)
#   if i == 'w':
#    print ('This is something special')

# guns = ['AK47', 'M4', 'M16', 'Glock']
# for gun in guns:
#   print (gun)
#   for bullet in gun:
#     print (bullet)

# i = int(input('Enter a number:'))
# print('Your number is',i)
# while i <= 38:
#   i = int(input('Enter a number:'))
#   print('Your number is',i)
# print('Done with the loop')

# a = (input('Siapa Tuhan Kamu?'))
# while a != 'Allah':
#   a = (input('Siapa Tuhan Kamu?'))
# print ('Anda selamat')

# x = (input('Say My Name: '))
# while x != 'Heisenberg':
#   x = (input('Say It!: '))
# print ('You are DAMN right!')

# total_sum = 0
# print(
#     'Enter positive numbers to add to the sum. Enter a negative number to stop.'
# )

# while True:
#   number = float(input('Enter a number:'))
#   if number < 0:
#     break
#   total_sum += number

# print('The total sum of positive numbers is: ', total_sum)

