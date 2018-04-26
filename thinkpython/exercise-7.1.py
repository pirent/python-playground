import math

def mysqrt(a, x):
  while True:
    #print(x)
    y = (x + a/x) / 2
    if y == x:
      break;
    x = y
  return y

def test_square_root():
  a = 1
  print("{:3s} {:13s} {:13s} {:13}".format("a", "mysqrt(a)", "math.sqrt(a)", "diff"))   
  print("{:3s} {:13s} {:13s} {:13}".format("-", "--------", "-----------", "------"))   
  while a < 10:
    mysqrt_result = mysqrt(a, 3)
    sqrt_result = math.sqrt(a)
    diff = abs(mysqrt_result - sqrt_result)
    print("{:3.1f} {:13f} {:13f} {:13f}".format(a, mysqrt_result, sqrt_result, diff))   
    a = a + 1

test_square_root()
