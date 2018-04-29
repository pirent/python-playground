from exercise91 import dothing_with_word_that_satisfy

def palindromic_4_digits_number():
  for number in range(1000, 9999):
    as_string = str(number).zfill(4)
    for i in range(4):
      if is_palindrome(as_string[3:2 - i:-1]):
        print(as_string, end=' ')
        break
      

def is_palindrome(word):
  return len(word) > 1 and word == word[::-1]

if __name__ == "__main__":
  palindromic_4_digits_number()    
