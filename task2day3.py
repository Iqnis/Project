# Q1
# fruits = ('apple', 'banana', 'cherry', 'date')
# print(fruits[0])
# print(fruits[-1])

# Q2
# my_tupel = {1, 2, 3, 4, 5}
# a, b, *rest = my_tupel
# print(a, b, rest)

# Q3
# fruits = {'apple', 'banana', 'cherry', 'date'}
# fruits_list = list(fruits)
# fruits_list[1] = ('blueberry')
# fruits = tuple(fruits_list)
# print(fruits)

# Q4
# set_color = {'red', 'green', 'blue', 'yellow'}
# set_color.add('purple')
# print(set_color)

# Q5
# primary_colors = {'red', 'blue', 'yellow'}
# intersection_colors = set_color.intersection(primary_colors)
# print(intersection_colors)
# union_colors = set_color.union(primary_colors)
# print(union_colors)
# difference_colors = set_color.difference(primary_colors)
# print(difference_colors)

# Q6
# colors = {'red', 'green', 'blue', 'yellow'}
# primary_colors = {'red', 'blue', 'yellow'}
# print('green' in primary_colors)
# print('orange' not in colors)

# TASK 3: DICT

# Q1
# student_grades = {"Ace": 85, "Blob": 90, "Chalice": 78, "Diend": 92}
# print(student_grades["Blob"])

# Q2
# student_grades = {'Ace': 85, 'Blob': 90, 'Chalice': 78, 'Diend': 92}
# student_grades['Exe'] = 88
# student_grades['Ace'] = 95
# student_grades.pop('Chalice')
# print(student_grades)

# Q3
student_grades = {'Ace': 85, 'Blob': 90, 'Chalice': 78, 'Diend': 92, 'Exe': 88}
for name, grade in student_grades.items():
  print(f"Student: {name}, Grade: {grade}")
