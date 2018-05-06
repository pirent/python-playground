"""
  takes a string and prints the letters in decreasing order of frequency
"""
def most_frequent(s):
  histogram = {}
  for letter in s:
    histogram[letter] = histogram.get(letter, 0) + 1
  
  #print("> debug: histogram is", histogram)
  res = []
  for k,v in histogram.items():
    res.append((v, k))
  #print("> debug: rest is", res)
  res.sort(reverse=True)
  #print("> debug: rest after sort", res)

  final_res = []
  for k,v in res:
    final_res.append(v) 
  return final_res

if __name__ == "__main__":
  s = input('Input a string: ')
  print("The letters in decreasing order of frequency:", most_frequent(s))
  

  
