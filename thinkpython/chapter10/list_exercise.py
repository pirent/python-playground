import time

"""
  Exercise 10-1:
  Take a list of list of integers and add up elements
  from the nested lists
"""
def nested_sum(t):
  total = 0
  for nested_list in t:
    total += sum(nested_list)
  return total


"""
  Exercise 10-2:
  Take a list of numbers and returns the cummulative sum;
  a new list where the ith element is the sum of the first i + 1 elements
  from the original list
"""
def cumsum(t):
  res = t[:]
  for i in range(len(res)):
    if i == 0:
      continue
    res[i] = res[i-1] + res[i]
  return res

"""
  Exercise 10-3:
  take a list and return a a new list that contains all but the first and last elements
"""
def middle_z(t):
  return t[1:len(t) - 1]

"""
  Exercise 10-4:
  take a list, modifies it by removing the first and last elements, return None
"""
def chop(t):
  del t[-1]
  del t[0]
  return None

"""
  Exercise 10-5:
  take a list, return True if the list is sorted in ascending order, otherwise False
"""
def is_sorted(t):
  t2 = sorted(t)
  return t2 == t

"""
  Exercise 10-6:
  Take two strings and return True if they are anagram
"""
def is_anagram(s1, s2):
  t1 = list(s1)
  t2 = list(s2)
  if len(t1) != len(t2):
    return False
  for letter in t1:
    t2.remove(letter)

  if not t2: #t2 is empty
    return True
  else:
    return False

"""
  Exercise 10-7:
  take a list and return True if there is any element that appears more than once;
  should not modify the original list
"""
def has_duplicated(t):
  for i in range(len(t)):
    element = t[i]
    if element in t[i + 1:]:
      return True
  return False

"""
  Exercise 10-9:
  Read the file words.txt and build a list with one element per word;
  Write two versions of this function;
  one using the append method
  and the other using the idiom t = t + [x]
  Which one takes longer to run? Why
"""
def make_list_with_append():
  res = []
  fin = open('words.txt')
  start_time = time.time()
  for line in fin:
    word = line.strip()
    res.append(word)
  print("--- {} seconds --".format(time.time() - start_time))
  return res

def make_list_with_concat():
  res = []
  fin = open('words.txt')
  start_time = time.time()
  for line in fin:
    word = line.strip()
    res = res + [word]
  print("--- {} seconds --".format(time.time() - start_time))
