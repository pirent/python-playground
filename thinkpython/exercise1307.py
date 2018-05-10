from list_exercise import cumsum
import random
import bisect
from exercise13_vanilla import build_histogram_from_file

def pick_a_random_word_from_histogram(hist):
  # step 1: use keys to get a list of words in the book
  words = list(hist.keys())

  # step 2: build a list of cumulative sum of the word frequencies
  # the last item in this list is the total number of words in book: n
  freq_list = list(hist.values())
  cumsum_freq_list = cumsum(freq_list)
  print(">>DEBUG, cumsum_freq_list", cumsum_freq_list)
  total_number_of_words = cumsum_freq_list[-1]

  # choose a random number from 1 to n
  # use bisection search to find index where random number
  # would be inserted in the cumulative sum
  random_num = random.randint(1, total_number_of_words)  
  index = bisect.bisect_left(cumsum_freq_list, random_num)

  # use the index to find corresonding word in word list
  return words[index]

if __name__ == "__main__":
  hist = build_histogram_from_file("short_one.txt")
  random_word = pick_a_random_word_from_histogram(hist)
  print("Random word is", random_word)
