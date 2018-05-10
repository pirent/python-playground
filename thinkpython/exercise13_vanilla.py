import string

to_be_replaced_letter_list = string.whitespace + string.punctuation

def build_histogram_from_file(filename):
  res = {}
  end_of_header_pattern = "*** START"
  fin = open(filename)

  for line in fin:
    if end_of_header_pattern in line:
      break

  for line in fin:
    process_line(line, res)
  
  return res

def process_line(line, histogram):
  line.replace('-', ' ')
  
  for word in line.split():
    word = word.strip(to_be_replaced_letter_list)
    word = word.lower()
    histogram[word] = histogram.get(word, 0) + 1

def get_total_different_words(histogram):
  return len(histogram.keys())

def get_total_words_are_used(histogram):
  return sum(histogram.values())

def sort_histogram_by_frequency(histogram):
  res = []
  for word, freq in histogram.items():
    res.append((freq, word))
  res.sort(reverse=True)
  return res

def print_most_common_words(histogram, num=10):
  t = sort_histogram_by_frequency(histogram)
  print("The most common words are:")
  for freq,word in t[:num]:
    print(word, freq, sep='\t')
  
def compare_two_words_list(listA, listB):
  res = []
  for word in listA:
    if word not in listB:
      res.append(word)
  return res

if __name__ == "__main__":
  hist = build_histogram_from_file("the_invisible_man.txt")
  print("How many different words:", get_total_different_words(hist))
  print("How many words are used:", get_total_words_are_used(hist))
  print_most_common_words(hist)
  
  words_list = build_histogram_from_file("words.txt")
  diff = compare_two_words_list(hist, words_list)
  #print("Words that are not in words list:", diff)
