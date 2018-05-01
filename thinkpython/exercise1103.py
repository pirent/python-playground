import time

known = {}

def cache_it(m, n, value):
  mini_map = known.setdefault(m, {})
  mini_map[n] = value

def get_from_known(m, n):
  mini_map = known.setdefault(m, {})
  return mini_map.get(n)

def ack(m, n):
  space=(' '*(m+n))

  result = get_from_known(m, n)
  if result:
    return result

  if m == 0:
    result = n + 1
    cache_it(m, n, result)
    return result

  if n == 0:
    result = get_from_known(m - 1, 1)
    if not result: 
      result =  ack(m - 1, 1)
    cache_it(m, n, result)
    return result

  # the remain cases
  tmp = get_from_known(m, n - 1)
  if not tmp:
    tmp = ack(m, n - 1)

  result = get_from_known(m - 1, tmp)
  if not result:
    result = ack(m - 1, tmp)

  cache_it(m, n, result)
  return result

if __name__ == "__main__":
  m = int(input('Input for m: '))
  n = int(input('Input for n: '))
  start = time.time()
  print('Ackerman result is:', ack(m, n))
  print('Ackerman with cache takes', time.time() - start)
