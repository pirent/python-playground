def is_triangle(a, b, c):
  if a > b + c or b > a +c or c > a + b:
    print('No')
  else:
    print('Yes')

def test_triangle():
  print('Testing triangle')
  a = int(input('Input first stick length: '))
  b = int(input('Input second stick length: '))
  c = int(input('Input third stick length: '))
  is_triangle(a, c, c)

test_triangle()
