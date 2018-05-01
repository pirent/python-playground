# ------ Version 1 -----------------
def rotate_word_v1(s, shift):
  isUpper = False
  if s.isupper():
    s = s.lower()
    isUpper = True
  myList = []
  index = 0
  while (index < len(s)):
    myList.append(shift_it(s[index], shift)) 
    index = index + 1

  index = 0
  result = ''
  while index < len(s):
    result = result + chr(myList[index])
    index = index + 1

  if isUpper:
    result = result.upper()
  return result

def shift_it(letter, shift):
  z_index = ord('z')
  a_index = ord('a')
  shift_result = ord(letter) + shift
  if shift_result > z_index:
    return a_index + (shift_result - z_index - 1)
  elif shift_result < a_index:
    return z_index - (a_index - shift_result - 1)
  else:
    return shift_result

# ------ Version 2 -----------------
def rotate_letter(letter, n):
  if letter.isupper:
    start = ord('A')
  elif letter.islower:
    start = ord('a')
  else:
    return letter

  diff = ord(letter) - start
  index = (diff + n) % 26 + start
  return chr(index)

def rotate_word_v2(word, n):
  result = ''
  for letter in word:
    result = result + rotate_letter(letter, n)
  return result

# =======================================================
# MAIN
# =======================================================

if __name__ == "__main__":
  expected = 'jolly'
  actual = rotate_word_v1('cheer', 7)
  print('actual is {}'.format(actual))
  print('expected == actual? {}'.format(expected == actual))

  algorithm = rotate_word_v2

  text = input('Enter input: ')
  shift = int(input('Enter shift: '))
  print('Result is {}', algorithm(text, shift))
