from inlist import in_bisect2
from list_exercise import make_list_with_append

"""
  Two words "interlock" if taking alternative letters from each form a new word
  Write a program that find all pairs of words that interlock
  Hint: don't enumerate all pairs
"""
def find_interlock_pairs(word_list):
  res = []
  for word in word_list:
    word1 = word[::2]
    word2 = word[1::2]
    if in_bisect2(word1, word_list) and in_bisect2(word2, word_list):
      res.append(word)
      res.append(":")
      res.append(word1)
      res.append("-")
      res.append(word2)
  return res

def interlock(word, word_list, n):
  for i in range(n):
    split_word = word[i::n]
    if not in_bisect2(split_word, word_list):
      return False
  return True

if __name__ == "__main__":
  word_list = make_list_with_append()
  res = find_interlock_pairs(word_list)
  print("Interlock pairs are: ", ', '.join(res))

  print("Find three-way interlocked words")
  for word in word_list:
    if interlock(word, word_list, 3):
      print(word, word[0::3], word[1::3], word[2::3])
