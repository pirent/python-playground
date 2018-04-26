def first(word):
  return word[0]

def last(word):
  return word[-1]

def middle(word):
  return word[1:-1]

def is_palindrome(word):
  print('Word is {}'.format(word))
  if len(word) == 1:
    return True
  elif first(word) != last(word):
    return False
  else:
    return is_palindrome(middle(word))
    

text_word = input('Enter your word: ')
print('First', first(text_word))
print('Last', last(text_word))
print('Middle', middle(text_word))
#print(middle('ab'), middle('a'), middle(''))
print("Is {} palindrome? {}".format(text_word, is_palindrome(text_word)))
