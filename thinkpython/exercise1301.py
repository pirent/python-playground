# =============================================================================
# Write a program that reads a file, breaks each line into words, strips whitespace and
# punctuation from the words, and converts them to lowercase.
# =============================================================================
import string

def turn_to_pure_word(word, translation_table):
  res = word.translate(translation_table)
  res = res.lower()
  return res

def create_translation_table():
  translation_table = {}
  list_to_replaced = string.whitespace + string.punctuation
  for letter in list_to_replaced:
    translation_table[letter] = None
  return translation_table

def turn_file_to_pure_words(file_input):
  res = []
  translation_table = create_translation_table()
  fin = open(file_input)
  for line in fin:
    word_list = line.strip()
    for raw_word in word_list.split(' '):
      word = turn_to_pure_word(raw_word, translation_table)
      res.append(word)
  return res

if __name__ == "__main__":
  res = turn_file_to_pure_words('chapter13.txt') 
  print("Words after purifying:", res)
