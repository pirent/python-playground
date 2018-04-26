def is_palindrome(s):
  return s == s[::-1]

text = input('Enter your word: ')
print('Is {} palindrome: {}'.format(text, is_palindrome(text)))
