def build_histogram(collection, process=None):
  res = {}
  for item in collection:
    if process is not None:
      item = process(item)
    res[item] = res.setdefault(item, 0) + 1
  return res

def swap_counter_and_value_histogram(histogram):
  res = {}
  for value, counter in histogram.items():
    value_list = res.setdefault(counter, [])
    value_list.append(value)
  return res

def sumall(collection):
  total = 0
  for item in collection:
    total += item
  return total
