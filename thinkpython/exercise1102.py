from chapter11 import *

"""
  invert_dict with "setdefault" enhancement
"""
def invert_dict(d):
  inverse = dict()
  for key in d:
    val = d[key]
    inverse.setdefault(val, []).append(key)
  return inverse

# Smoke test
h = histogram('banana')
print('Inverse of \"banana\" dict:', invert_dict(h))
