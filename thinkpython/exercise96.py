from exercise91 import dothing_with_word_that_satisfy
"""
Write a function called is_abecedarian that returns True if the letters in a word
appear in alphabetical order (double letters are ok). How many abecedarian words are there?
"""
def is_abecedarian(word):
  prev = 0
  for letter in word:
    current = ord(letter)
    if current < prev:
      return False
    prev = current
  return True

def is_abecedarian2(word):
  if len(word) <= 1:
    return True
  if word[1] < word[0]:
    return False
  return is_abecedarian(word[1:])

if __name__ == "__main__":
  print("How many abecedarian wors are there: ")
  dothing_with_word_that_satisfy(is_abecedarian) 
