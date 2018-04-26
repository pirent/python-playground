def gcd(a, b):
  if b == 0:
    return a
  elif a > b:
    remainder = a % b
    return gcd(b, remainder)
  else:
    remainder = b % a
    return gcd(a, remainder)

a = int(input('Enter a: '))
b = int(input('Enter b: '))
print("GCD is {}".format(gcd(a, b)))
