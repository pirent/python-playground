def print_n(s, n):
  if n <= 0:
    return
  print(s)
  print_n(s, n - 1)

def say_hello():
  print('Hello world')

def do_n(f, n, arg):
  if n <= 0:
    return
  f(*arg)
  do_n(f, n -1, arg)

do_n(say_hello, 2, '')
