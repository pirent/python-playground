def is_divisible(a, b):
  return a % b == 0

def is_power(a, b):
  if a == b or (a == 1 and b != 0):
    return True
  elif b == 0 or a == 0 or a < 0:
    return False
  elif is_divisible(a, b):
    quotient = a / b
    return is_power(quotient, b)
  else:
    return False

a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("Is {} power of {}? {}".format(a, b, is_power(a, b))) 
