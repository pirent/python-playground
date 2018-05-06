import time
from exercise1101 import store_as_dict

cache = {}
# the trickiest part is here
# without this shit, reducible on empty string will never work
cache[''] = [''] 

"""
  return a list of children which are also reducible
  empty if this word is not reducible
"""
def reducible(word, words_map):
  if word in cache:
    return cache[word]

  res = []
  for child in get_children(word, words_map):
    #print("word is {}, child is {}".format(word, child))
    child_red = reducible(child, words_map)
    #print("child red of {} is {}".format(child, child_red))
    if child_red:
      res.append(child)
  
  cache[word] = res
  return res
  
"""
  returns a list of words that are meaningful and reduced one letter from the provided input
"""
def get_children(word, words_map):
  res = []
  for i in range(len(word)):
    reduced_word = word[:i] + word[i+1:]
    if reduced_word in words_map:
      res.append(reduced_word)
  return res

def get_all_reducible(words_map):
  res = []
  for word in words_map:
    if reducible(word, words_map):
      res.append(word)
  return res

def build_word_dict():
  res = store_as_dict("words.txt")
  for i in ['a', 'i', '']:
    res[i] = None
  return res

"""
  prints the sequence of this word after reduced by one letter until empty
"""
def print_trail(word):
  if not word:
    return
  
  print(word, end=' ') 
  reducible_list = reducible(word, {})
  print_trail(reducible_list[0])

if __name__ == "__main__":
  words_map = build_word_dict()
  reducible_list = get_all_reducible(words_map)

  # print the longest
  reducible_list.sort(key=len, reverse=True)
#  print("reducible list is:", reducible_list)
  
  for i in range(10):
    print_trail(reducible_list[i])
    print("\n")
