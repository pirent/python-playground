def age_reversible():
  for age_distance in range(18, 30):
    print("> age distance: ", age_distance)
    count = 0
    for child_age in range(0, 80):
      mom_age = child_age + age_distance
      if str(child_age).zfill(2)  == str(mom_age)[::-1]:
        count = count + 1
        print("child age passed is {}, mom age passed is {}".format(child_age, mom_age))
    if count == 8:
      print('Found age distance: ', age_distance)

if __name__ == "__main__":
  age_reversible()
