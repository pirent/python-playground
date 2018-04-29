from exercise91 import dothing_with_word_that_satisfy
from exercise94 import uses_only
"""
  Write a function named uses_all that takes a word and a string of required letters,
  and that returns True if the word uses all the required letters at least once.
"""
def uses_all(word, letters):
  return uses_only(letters, word)

if __name__ == "__main__":
  word = input("Enter word: ")
  letters = input("Enter required letters: ")
  print("Is \"{}\" uses all the required letters in \"{}\"? {}".format(word, letters, uses_all(word, letters)))

  print("========= Other smoke test ===========")
  print("Words that use all the vowel: ")
  dothing_with_word_that_satisfy(uses_all, letters="aeiou")
  print('======================================')
  print("Words that use all the \"aeiouy\": ")
  dothing_with_word_that_satisfy(uses_all, letters="aeiouy")
