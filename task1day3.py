def fbonacci(l):
  if l == 0:
    return 0
  elif l == 1:
    return 1
  else:
    return fbonacci(l - 1) + fbonacci(l - 2)
print(fbonacci(10))