# =============================================================
# Write a function takes a histogram, returns a random value from the it,
# chosen with probability in proportion
# =============================================================
import random
import utils

def choose_from_hist(histogram):
  swap_map = utils.swap_counter_and_value_histogram(histogram)
  counter_list = list(swap_map.keys())
  max_counter = max(counter_list)
  min_counter = min(counter_list)

  res = None
  rand = random.randint(min_counter, max_counter)
  while not res:
    res = swap_map[rand]
    rand = random.randint(min_counter, max_counter)

  return (res, rand, utils.sumall(counter_list))

if __name__ == "__main__":
  t = ['a', 'a', 'b']
  histogram = utils.build_histogram(t)
  res = choose_from_hist(histogram)
  print("The choosen one is {} with probability of {}/{}".format(res[0], res[1], res[2]))

  # OR using built-in function
  rand_word = random.choice(list(histogram.keys()))
  print("Random word using built-in function:", rand_word)
