def have_more_than_20chars(word):
  return len(word) > 20

def dothing_with_word_that_satisfy(condition_check, **kwargs):
  fin = open('words.txt')
  total = 0
  hit = 0
  for line in fin:
    total = total + 1
    word = line.strip()
    kwargs['word'] = line.strip()
    if condition_check(**kwargs):
      print(word, end=' ')
      hit = hit + 1
  print('\nStatistic: {}/{} = {:.6f} %'.format(hit, total, hit/total))

if __name__ == "__main__":
  print('Words that have more than 20 characters')
  dothing_with_word_that_satisfy(have_more_than_20chars)
