import string

letter_map = {}
lower_case_list = list(string.ascii_lowercase)

def rotate_letter(letter, n):
  mini_map = letter_map.setdefault(letter, {})
  letter_index = lower_case_list.index(letter)
  return mini_map.setdefault(n, lower_case_list[(letter_index + n) % 26])

def rotate_word(word, n):
  result = ''
  for letter in word:
    result += rotate_letter(letter, n)
  return result

def rotate_pair(word, word_dicts):
  for i in range(1,14):
    rotated_word = rotate_word(word, i)
    if rotated_word in word_dicts:
      print(word, "-", rotated_word)

def make_words_dict():
  words_dict = {}
  fin = open('words.txt')
  for line in fin:
    word = line.strip()
    words_dict[word] = 0
  return words_dict

if __name__ == "__main__":
  words_dict = make_words_dict()
  for word in words_dict:
    rotate_pair(word, words_dict)
  #for i in range(1, 14):
  #  print("Rotate {} to {}".format("zoo", rotate_word("zoo", i)))
