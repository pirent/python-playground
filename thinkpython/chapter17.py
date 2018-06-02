import copy

class Time:
  """Represents the time of day.

  attribute: hour, minute, second
  """
  def __init__(self, hour=0, minute=0, seoncd=0):
    self.hour = hour
    self.minute = minute
    self.second = seoncd

  def print_time(self):
    print("{:02.0f}:{:02.0f}:{:02.2f}".format(self.hour, self.minute, self.second))
  
  def time_to_int(self):
    minutes = self.hour * 60 + self.minute
    seconds = minutes * 60 + self.second
    return seconds
  
  def increment(self, seconds):
    seconds += self.time_to_int()
    return int_to_time(seconds)

  def is_after(self, other):
    """takes two Time objects, self and other , 
    and returns True if self follows other chronologically and False otherwise
    """
    return self.time_to_int() > other.time_to_int()
 
  def __str__(self):
    return "{:02.0f}:{:02.0f}:{:02.2f}".format(self.hour, self.minute, self.second)
  
  def __add__(self, other):
    if isinstance(other, Time):
      return self.add_time(other)
    else:
      return self.increment(other)

  def add_time(self, other):
    seconds = self.time_to_int() + other.time_to_int()
    return int_to_time(seconds)
  
  def __radd__(self, other):
    return self.__add__(other)

  def __lt__(self, other):
    t1 = self.hour, self.minute, self.second
    t2 = other.hour, other.minute, other.second
    return t1 < t2

class Point:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def  __str__(self):
    return "{}, {}".format(self.x, self.y)
 
  def __add__(self, other):
    if isinstance(other, Point):
      return Point(self.x + other.x, self.y + other.y)
    elif isinstance(other, tuple):
      return Point(self.x + other[0], self.y + other[1])

def int_to_time(seconds):
  time = Time()
  minutes, time.second = divmod(seconds, 60)
  time.hour, time.minute = divmod(minutes, 60)
  return time

if __name__ == "__main__":
  start = Time(9, 45, 0)
  start.print_time()

  end = start.increment(1337)
  end.print_time()
  print("End is after start >>", end.is_after(start))

  duration = Time(1, 35)
  print(start + duration)

  p1 = Point()
  print("P1 is ", p1)
  p2 = Point(2, 3)
  print("p1 plus p2 is", p1 + p2)
  print("p1 plus a tuple is", p1 + (2, 3))

  start = Time(9, 45)
  duration = Time(1, 35)
  print(start + duration)
  print(start + 1337)
  print(1337 + start)

  print("Is start lesser than end?", start < end)
