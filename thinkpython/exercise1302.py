# ======================================================================
# Modify your program from the previous exercise to read the book you downloaded, skip over the
# header information at the beginning of the file, and process the rest of the words as before.
# 
# Then modify the program to count the total number of words in the book, and the number of times
# each word is used.
#
# Print the number of different words used in the book. Compare different books by different authors,
#written in different eras. Which author uses the most extensive vocabulary?
# ======================================================================
from exercise1301 import *

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

def process(filename):
  f = open(filename)

  start_line_number = find_line_number_of_start_line(filename)
  lines = f.readlines()[start_line_number:]
  histogram = build_histogram(lines)

  print("The total number of words in book:", count_total_words(histogram))
  print("The number of different words in book", len(histogram.keys()))
  print("Number of times each word is used")
  print(histogram)

  f.close 

if __name__ == "__main__":
  process("short_one.txt")
