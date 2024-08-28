def check_positive_number(num):
  if num < 0:
    raise ValueError("Thats is NOT a positive number!")
  return num


try:
  user_input = float(input("Would you kindly enter a positive number: "))
  check_positive_number(user_input)
  print("Success! The number is real positive.")
except ValueError as e:
  print(e)
