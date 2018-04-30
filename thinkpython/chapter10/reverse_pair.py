from inlist import in_bisect2
from list_exercise import make_list_with_append

"""
  Two words are a reverse pair if each is the reverse of each other
  Write a program that finds all the reverse pairs in the word list
"""
def reverse_pair(word_list):
  #word_list = word_list[:10]
  print(word_list)
  res = []
  for index in range(len(word_list)):
    word = word_list[index]
    reverse_word = word[::-1]
    if in_bisect2(reverse_word, word_list):
      res.append(word)
      res.append(reverse_word)
  return ", ".join(res)

if __name__ == "__main__":
  word_list = make_list_with_append()
  print("Reverse pairs are: ", reverse_pair(word_list))
