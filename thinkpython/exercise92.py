from exercise91 import dothing_with_word_that_satisfy

def has_no_e(word):
  return word.count('e') == 0

print('Words that have no \'e\'')
dothing_with_word_that_satisfy(has_no_e)

