from chapter15 import Point, Rectangle, distance_between_points
import math

class Circle:
   """Represent a circle
   center: a Point
   radius: a float number
	   """
def point_in_circle(circle, point):
  """return true if the point lies in or on the boundary of the circle"""
  #distance = distance_between_two_points(circle.center, point)
  distance = distance_between_points(circle.center, point)
  #print(">> DEBUG: distance is", distance)
  return distance <= circle.radius

#def distance_between_two_points(p1, p2):
#  return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def rect_in_circle(circle, rect):
  """return true if the rectangle lies entirely in or on the boundary of the circle"""
  if not point_in_circle(circle, rect.corner):
    return False

  # now calculate the upper left corner
  upper_left_corner = Point()
  upper_left_corner.x = rect.corner.x
  upper_left_corner.y = rect.corner.y + rect.height
  if not point_in_circle(circle, upper_left_corner):
    return False
  
  # now calculate the upper right corner
  upper_right_corner = Point()
  upper_right_corner.x = upper_left_corner.x + rect.width
  upper_right_corner.y = upper_left_corner.y
  if not point_in_circle(circle, upper_right_corner):
    return False

  return True

def rect_circle_overlap(circle, rect):
  """akes a Circle and a Rectangle and returns True if any of the corners of the Rectangle fall inside the circle.
     Or as a more challenging version, return True if any part of the Rectangle falls inside the circle.
  """
  ## a good page explain algorith used here with demo: https://yal.cc/rectangle-circle-intersection-test/
  ## TLDR: find a point in rect closet to the circle' center
  ##       and check that point is in the circle
  nearest_x = max(rect.corner.x, min(circle.center.x, rect.corner.x + rect.width))
  nearest_y = max(rect.corner.y, min(circle.center.y, rect.corner.y + rect.height))
  b = Point()
  b.x = nearest_x
  b.y = nearest_y
  return point_in_circle(circle, b)
    
if __name__ == "__main__":
  circle = Circle()
  circle.center = Point()
  circle.center.x = 150.0
  circle.center.y = 100.0
  circle.radius = 75.0
  print("Circle's center is {},{} and radius is {}".format(circle.center.x, circle.center.y, circle.radius))

  # test point in circle
  p1 = Point()
  p1.x = 140
  p1.y = 110
  print("Point({}, {}) lies within circle? >> {}".format(p1.x, p1.y, point_in_circle(circle, p1)))

  p2 = Point()
  p2.x = 75
  p2.y = 100
  print("Point({}, {}) lies within circle? >> {}".format(p2.x, p2.y, point_in_circle(circle, p2)))

  # test rectangle in circle
  rect1 = Rectangle()
  rect1.width = 50
  rect1.height =25
  rect1.corner = Point()
  rect1.corner.x = 100
  rect1.corner.y = 120
 
  print("Rectangle with corner of ({}, {}) and w={}, h={}".format(rect1.corner.x, rect1.corner.y, rect1.width, rect1.height))
  print("Is rectangle inside circle? >>", rect_in_circle(circle, rect1))
  print("Does rectangle has collision with circle? >>", rect_circle_overlap(circle, rect1))
