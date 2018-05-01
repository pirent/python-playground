"""
  enhance exercise 10-7 with dictionary
"""
def has_duplicate(t):
  s = set(t)
  return len(s) < len(t)

# Smoke test
if __name__ == "__main__":
  t = [1,3,5,1,3,7,8]
  print("Is {} has duplicated elements? {}".format(t, has_duplicate(t)))
