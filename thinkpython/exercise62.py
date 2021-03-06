import time

def ack(m, n):
  space=(' '*(m+n))
#  print(space, 'ack with {:d} {:d}'.format(m, n))

  if m == 0:
    result = n + 1
#    print(space, 'returning', result)
    return result
  elif m > 0 and n == 0:
    result =  ack(m - 1, 1)
#    print(space, 'returning', result)
    return result
  elif m > 0 and n > 0:
    tmp = ack(m, n -1)
    result = ack(m - 1, tmp)
#    print(space, 'returning', result)
    return result

if __name__ == "__main__":
  m = int(input('Input for m: '))
  n = int(input('Input for n: '))
  start = time.time()
  print('Ackerman result is:', ack(m, n))
  print('Ackerman without cache takes', time.time() - start)
