from exercise1202 import *

# ================================================================================
#  Two words form a “metathesis pair” if you can transform one into the other by
#  swapping two letters; for example, “converse” and “conserve”. Write a program that finds all of
#  the metathesis pairs in the dictionary.
# ================================================================================
def metathesis(dictionary):
  res = []
  for anagram_list in dictionary.values():
    # FIXME if this can be fixed by exercise1202, no need for this fitler
    if len(anagram_list) == 1:
      continue
    # for each element, compare with the remainder
    for i in range(len(anagram_list) - 1):
      current_word = anagram_list[i]
      next_word = anagram_list[i + 1]
      if compare_two_pairs(current_word, next_word):
        a_tuple = (current_word, next_word)
        res.append(a_tuple)
  return res

"""
  returns True when two words have two difference letter positions only
"""
def compare_two_pairs(word1, word2):
  different_letter_counter = 0
  for i in range(len(word1)):
    if word1[i] != word2[i]:
      different_letter_counter += 1
  return different_letter_counter == 2

if __name__ == "__main__":
  raw_anagram_map = build_anagram_list('words.txt')
  res = metathesis(raw_anagram_map)
  for i in range(20):
    print(res[i])
