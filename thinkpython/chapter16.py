import copy

class Time:
  """Represents the time of day.

  attribute: hour, minute, second
  """

def print_time(time):
  print("{:02.0f}:{:02.0f}:{:02.2f}".format(time.hour, time.minute, time.second))

def is_after(t1, t2):
  """takes two Time objects, t1 and t2 , 
  and returns True if t1 follows t2 chronologically and False otherwise
  """
  return t1.hour > t2.hour or t1.minute > t2.minute or t1.second > t2.second

def add_time(t1, t2):
  assert valid_time(t1) and valid_time(t2)
  temp = time_to_int(t1) + time_to_int(t2)
  return int_to_time(temp)

def increment(t, seconds):
  temp = time_to_int(t) + seconds
  return int_to_time(temp)

def time_to_int(time):
  minutes = time.hour * 60 + time.minute
  seconds = minutes * 60 + time.second
  return seconds

def int_to_time(seconds):
  time = Time()
  minutes, time.second = divmod(seconds, 60)
  time.hour, time.minute = divmod(minutes, 60)
  return time

def valid_time(time):
  if time.hour < 0 or time.minute < 0 or time.second < 0:
    return False
  if time.minute >= 60 or time.second >= 60:
    return False
  return True

if __name__ == "__main__":
  t1 = Time()
  t1.hour = 2
  t1.minute = 50
  t1.second = 55
  print("T1 is:", end=' ')
  print_time(t1)

  t2 = Time()
  t2.hour = 3
  t2.minute = 10
  t2.second = 10
  print("T2 is:", end=' ')
  print_time(t2)
  print("Is t2 after t1? >>", is_after(t1, t2)) 

  print("T1 adds T2 is", end=' ')
  print_time(add_time(t1, t2))

  print("T1 after incrementing by {} seconds is".format(125), end = ' ')
  print_time(increment(t1, 125))

  print("verifying conversion of time to int and vice verse:", time_to_int(int_to_time(4500)) == 4500)
