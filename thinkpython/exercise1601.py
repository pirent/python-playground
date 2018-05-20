from chapter16 import *

def mul_time(time, num):
  """takes a Time object and a number and returns a new Time object 
  that contains the product of the original Time and the number.
  """
  assert valid_time(time)
  temp = time_to_int(time) * num
  return int_to_time(temp)

def get_pace(duration, distance):
  temp = mul_time(duration, 1/distance)
#  print(">> DEBUG: temp is {}:{}:{}".format(temp.hour, temp.minute, temp.second)) 
  return temp

if __name__ == "__main__":
  t1 = Time()
  t1.hour = 1
  t1.minute = 20
  t1.second = 10
  print("T1 is ", end='')
  print_time(t1)

  print("T1 multiply with 3 is ", end='')
  print_time(mul_time(t1, 3))

  distance = 3
  print("pace of {} km with {} seconds is ".format(distance, time_to_int(t1)), end='')  
  print_time(get_pace(t1, distance))
