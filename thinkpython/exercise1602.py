from datetime import *

def get_current_date():
  today = date.today()
  print("Day of the week:", today.isoweekday())
  print("Current date:", today.ctime())
  return today

def age_and_time_until_next_birthday(birthday):
  """takes a birthday as input and prints the user’s age and the number of
  days, hours, minutes and seconds until their next birthday
  
  parameters:
    birthday: a date object
  """
  today = get_current_date()
  age = (today - birthday).days // 365
  print("The user is {} years old".format(age))

  if birthday < today:
    birthday = birthday.replace(year=today.year + 1)
  
  time_to_bday = abs(birthday - today)
  temp_hours = divmod(time_to_bday.seconds, 3600)
  hours = temp_hours[0]
  temp_minutes = divmod(temp_hours[1], 60)
  minutes = temp_minutes[0]
  seconds = temp_minutes[1]
  res = (time_to_bday.days, hours, minutes, seconds)
  print("Time to birthday: {} days, {} hours, {} minutes, and {} seconds".format(res[0], res[1], res[2], res[3]))
  
  return res
  
if __name__ == "__main__":
  bday = date(1990, 2, 4)
  age_and_time_until_next_birthday(bday)
