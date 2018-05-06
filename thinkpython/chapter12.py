"""
  Takes any number of arguments and return their sum
"""
def sumall(*args):
  return sum(args)

def has_match(t1, t2):
  for x,y in zip(t1, t2):
    if x = y:
      return True
  return False
