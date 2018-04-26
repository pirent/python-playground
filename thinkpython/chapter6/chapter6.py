def factorial(n):
  space = ' ' * (2 * n)
  print(space, 'fibonacci of', n)
  if not isinstance(n, int):
    print('Apply for integer only: {:d}'.format(n))
    return None
  elif n < 0:
    print('Only for positive number: {:d}'.format(n))
    return None
  elif n == 0:
    print(space, 'return 1')
    return 1
  else:
    recurse = factorial(n - 1)
    result = n * recurse
    print(space, 'return', result)
    return result

def b(z):
  prod = a(z, z)
  print(z, prod)
  return prod

def a(x, y):
  x = x + 1
  return x * y

def c(x, y, z):
  total = x + y + z
  square = b(total)**2
  return square


# ==============================
# MAIN
# =============================
#n = int(input('Enter your number to calculate its factorial: '))
#result = factorial(n)
#print('Result is {:d}'.format(result))

x = 1
y = x + 1
print('Exercise 6.1:', c(x, y + 3, x + y))
