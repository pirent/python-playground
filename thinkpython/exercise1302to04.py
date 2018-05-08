# ======================================================================
# Exercise 13.02
# Modify your program from the previous exercise to read the book you downloaded, skip over the
# header information at the beginning of the file, and process the rest of the words as before.
# 
# Then modify the program to count the total number of words in the book, and the number of times
# each word is used.
#
# Print the number of different words used in the book. 
#
# Exercise 13.03
# Modify the program from the previous exercise to print the 20 most frequently used words
#
# Exercise 13.04
# Modify the previous program to read a word list (see Section 9.1) and then print all
# the words in the book that are not in the word list. How many of them are typos? How many of
# them are common words that should be in the word list, and how many of them are really obscure?
# ======================================================================
from exercise1301 import *
from list_exercise import make_list_with_append

def find_line_number_of_start_line(filename):
  start_line_pattern = "*** START"
  with open(filename) as infile:
    for num, line in enumerate(infile, 1):
      if start_line_pattern in line:
        return num
  infile.close()
  return None

def build_histogram(lines):
  histogram = {}
  translation_table = create_translation_table()

  for line in lines:
    word_list = line.strip()
    if not word_list:
      continue
    for raw_word in word_list.split(' '):
      word = turn_to_pure_word(raw_word, translation_table)
      histogram[word] = histogram.setdefault(word, 0) + 1
  return histogram

def count_total_words(histogram):
  total = 0
  for count in list(histogram.values()):
    total += count
  return total

def find_most_frequently_used_words(histogram, number_of_words=10):
  tuple_list = []
  for word, count in histogram.items():
    t = (count, word)
    tuple_list.append(t)
  tuple_list.sort(reverse=True)
  
  res = []
  for i in range(number_of_words):
    res.append(tuple_list[i][1])
  return res

def process(filename):
  f = open(filename)

  start_line_number = find_line_number_of_start_line(filename)
  lines = f.readlines()[start_line_number:]
  histogram = build_histogram(lines)

  f.close 

  print("The total number of words in book:", count_total_words(histogram))
  print("The number of different words in book", len(histogram.keys()))
  print("Number of times each word is used")
  for item in histogram.items():
     print(item)
  print("================================")
  print("Most 20 frequenly used words")
  print(find_most_frequently_used_words(histogram, 20))
  
  word_list = set(make_list_with_append())
  words_from_book = set(histogram.keys())
  print("Words from book that are not in word list:", words_from_book - word_list)


# ===========================

if __name__ == "__main__":
  process("short_one.txt")
