from exercise91 import dothing_with_word_that_satisfy
"""
  Give me a word with three consecutive double letter
"""
def three_consecutive_letter(word):
  pairs = 0
  i = 0
  while i < len(word) - 1:
    if word[i] == word[i+1]:
      pairs = pairs + 1
      if pairs == 3:
        return True
      i = i + 2
    else:
      pairs = 0 # reset
      i = i + 1
  return False


if __name__ == "__main__":
  print("Give me a word with three consecutive double letter")
  dothing_with_word_that_satisfy(three_consecutive_letter)
   
    
  
