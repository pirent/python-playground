import time

"""
  write a function that reads words in words.txt
  and store them as keys in a dictionary;
  it doesn't matter what the values are
"""
def store_as_dict(input_file):
  res = {}
  fin = open(input_file)
  for line in fin:
    word = line.strip()
    res[word] = 0
  return res

if __name__ == "__main__":
  words_dict = store_as_dict("words.txt")
  start_time = time.time()
  if "pizza" in words_dict:
    print("--- take {} seconds ---".format(time.time() - start_time))
