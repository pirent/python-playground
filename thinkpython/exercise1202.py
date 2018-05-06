# ============================================================================================
#  you might want to build a dictionary that maps from a collection of letters to a list
#of words that can be spelled with those letters. The question is, how can you represent the
#collection of letters in a way that can be used as a key?
#  > make them as a tube
# ============================================================================================

def convert_word_to_tuple_with_order(word):
  word_as_list = list(word)
  word_as_list.sort()
  return tuple(word_as_list)

def add_word_to_dict(word, dictionary):
  key = convert_word_to_tuple_with_order(word)
  #print('word is', word, ', key is', key)
  anagram_list = dictionary.setdefault(key, [])
  anagram_list.append(word)

"""
  Write a program that reads a word list from a file (see Section 9.1) and prints all the sets of
words that are anagrams.
"""
def build_anagram_list(input_file):
  res = {}
  fin = open(input_file)
  for line in fin:
    word = line.strip()
    convert_word_to_tuple_with_order(word)
    add_word_to_dict(word, res)
  return res

"""
  prints the longest list of anagrams first, followed by the second longest, and so on
"""
def index_anagram_list_by_length(anagram_list, number_to_filter=None, len_must_greater_than=1):
  res = {}
  for k,v in anagram_list.items():
    length = len(v)
    if len_must_greater_than > length:
      continue
    if number_to_filter and number_to_filter != length:
      continue 
    temp_list = res.setdefault(length, [])
    temp_list.append(v)
  return res

if __name__ == "__main__":
  raw_anagram_map = build_anagram_list('words.txt')
  #anagram_map = build_anagram_list('mini_sample.txt')
  #print('The anagram_map is:', anagram_map)
  #for value in anagram_map.values():
  #  if len(value) > 1:
  #    print(value)

  # Modify the previous program so that it prints the longest list of anagram first
  # followed by the second longest, and so on
  indexed_anagram_map = index_anagram_list_by_length(raw_anagram_map, len_must_greater_than=8)
  temp_list = list(indexed_anagram_map.keys())
  temp_list.sort(reverse=True) 
  #for item in temp_list:
  #  print(indexed_anagram_map[item])

  # What collection of 8 letters forms the most possible bingos?
  # Hint: there are seven.
  print("Scrabble list")
  eight_letters_anagram = index_anagram_list_by_length(raw_anagram_map, number_to_filter=8)
  print(eight_letters_anagram.values())
