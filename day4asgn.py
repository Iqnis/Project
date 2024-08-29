# Q1

counter = 0

def increment_counter():
    global counter
    counter += 1
    print(f'Global counter value: {counter}')

def reset_counter():
    counter = 0 
    print(f'Local counter value: {counter}')

increment_counter()  
increment_counter() 
increment_counter()  
reset_counter()  
print(f'Global counter after reset_counter: {counter}')  

# Q2

import os

print(f"Current working directory: {os.getcwd()}")

print("Files and directories in current working directory:")
print(os.listdir(os.getcwd()))

os.mkdir('test_dir')

os.chdir('test_dir')
print(f"New working directory: {os.getcwd()}")

with open('test_file.txt', 'w') as file:
    file.write("This is a test file.")

os.remove('test_file.txt')
os.chdir('..') 
os.rmdir('test_dir')

# Q3

def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print('Error: Cannot divide by zero.')
        return None
    else:
        return result
    finally:
        print('Division operation completed.')

try:
    a = float(input('Enter the first number: '))
    b = float(input('Enter the second number: '))
    result = divide_numbers(a, b)
    if result is not None:
        print(f'Result of division: {result}')
except ValueError:
    print('Invalid input: Please enter numeric values.')


