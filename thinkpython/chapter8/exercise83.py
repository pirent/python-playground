def is_palindrome(s):
  return s == s[::-1]

if __name__ == "__main__":
  text = input('Enter your word: ')
  print('Is {} palindrome: {}'.format(text, is_palindrome(text)))
