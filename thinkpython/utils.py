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

def print_attributes(obj):
  for attr in vars(obj):
    print(attr, getattr(obj, attr))

def find_defining_class(obj, method_name):
  """Takes an object, and a method name, then returns the class
  provides the definition of the method
  """
  for ty in type(obj).mro():
    if method_name in ty.__dict__:
      return ty
