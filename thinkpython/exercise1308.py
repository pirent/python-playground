import string
import random

to_be_replaced_letter_list = string.whitespace + string.punctuation
prefix = ()

def build_markov_analysis_from_file(filename, prefix_length=2):
  res = {}
  fin = open(filename)
  end_of_header_pattern = "*END*"
  
  for line in fin:
    if end_of_header_pattern in line:
      break
  
  for line in fin:
    #if line.startswith("#"):
    #  continue
    process_line(line, res, prefix_length)

  return res

def process_line(line, mapping, prefix_length=2):
  raw_words = line.split()
  processed_words = []
  for word in raw_words:
    word = word.strip(to_be_replaced_letter_list)
    word = word.lower()
    processed_words.append(word)
  
  #print(">> DEBUG: line = {}".format(line))
  #print(">> DEBUG: processed_words = {}".format(processed_words))
  
  for word in processed_words:
    global prefix
    if len(prefix) < prefix_length:
      prefix += (word,)
      continue
   
    suffixes = mapping.setdefault(prefix, [])
    suffixes.append(word)
  	
    prefix = shift(prefix, word)
    
    #print(">> DEBUG: prefix = {}, suffix = {}, suffixes after adding = {}".format(prefix, suffix, suffixes))

def shift(prefix, word):
  return prefix[1:] + (word,)

def build_randomly_text(mapping, txt_length=20):
  res = []
  prefixes = list(mapping.keys())
  random_prefix = random.choice(prefixes)
  #res.append(random_prefix)

  suffixes = mapping[random_prefix]
  random_suffix = random.choice(suffixes)
  res.append(random_suffix)

  print(">> DEBUG: first prefix = {}, first suffix = {}".format(random_prefix, random_suffix))

  previous_prefix = random_prefix
  previous_suffix = random_suffix
  for i in range(txt_length):
    # build next prefix
    prefix = shift(previous_prefix, previous_suffix)
    suffixes = mapping.get(prefix)
    if not suffixes:
      break
    suffix = random.choice(suffixes)
    res.append(suffix)

    previous_prefix = prefix
    previous_suffix = suffix

  return " ".join(res)

if __name__ == "__main__":
  filename = "emma.txt"
  mapping = build_markov_analysis_from_file(filename, 3)
  #print(mapping)
  random_txt = build_randomly_text(mapping)
  print("Random txt:", random_txt)
