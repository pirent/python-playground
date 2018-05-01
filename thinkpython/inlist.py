from list_exercise import make_list_with_append
import time
import bisect

"""
  write a binary search and smoke test
"""
def in_bisect(element, t):
  if len(t) == 0:
    return False
  middle = len(t) // 2
  if element == t[middle]:
    return True
  elif element > t[middle]:
    return in_bisect(element, t[middle+1:])
  else:
    return in_bisect(element, t[:middle])

def in_bisect2(element, t):
  i = bisect.bisect_left(t, element)
  if i == len(t):
    return False
  return t[i] == element

"""
  Smoke test
"""
if __name__ == "__main__":
  word_list = make_list_with_append()
  print("Test list {}".format(word_list[:10]))
  
  print("=======================================")
  print("Search \"pizza\" with ordinary \"in\"")
  start_time = time.time()
  if "pizza" in word_list:
    print("--- take {} seconds ---".format(time.time() - start_time))
  
  print("Search \"pizza\"  with \"in bisect\"")
  start_time = time.time()
  if in_bisect("pizza", word_list):
    print("--- take {} seconds ---".format(time.time() - start_time))
 
  print("Search \"pizza\" with module \"bisect\"")
  start_time = time.time()
  if in_bisect2("pizza", word_list):
    print("--- take {} seconds ---".format(time.time() - start_time))
