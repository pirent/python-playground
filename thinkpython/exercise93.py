from exercise91 import dothing_with_word_that_satisfy

"""
 Return True if the word doesn't use any of forbidden letters

 Prompt the user to enter a string of forbidden letters
 and then print words (database taken from previous exercise)
 that don't contain any of them
"""
def avoid(word, forbidden_letters):
  # using any expression
  #return not any(letter in forbidden_letters for letter in word)
  # using set operation
  return not set(word).intersection(set(forbidden_letters))

if __name__ == "__main__":
  print('Smoke test')
  print("Does {} not contains {}? {}".format("police", "abd", avoid("police", "abd")))
  print("Does {} not contains {}? {}".format("police", "cef", avoid("police", "cef")))

  forbidden_letters = input('Enter your forbidden letters: ')
  print('Words that don\'t contain them are: ')
  dothing_with_word_that_satisfy(avoid, forbidden_letters=forbidden_letters)

