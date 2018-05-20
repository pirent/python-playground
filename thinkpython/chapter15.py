import math
import copy

class Point:
   """Represents a point in 2D-space"""

class Rectangle:
   """Represents a rectangle.
   
   attributes: width, height, corner
   with corner specifies the lower-left corner using Point
   """
def print_point(p):
  print("{} {}".format(p.x, p.y))

def distance_between_points(p1, p2):
   """Return distance between two points
      p1: first point
      p2: second point
   """
   distance = math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
   return distance

def find_center(rect):
  p = Point()
  p.x = rect.corner.x + rect.width/2
  p.y = rect.corner.y + rect.height/2
  return p

def grow_rectangle(rect, dwidth, dheight):
  rect.width += dwidth
  rect.height += dheight

def move_rectangle(rect, dx, dy):
  res = copy.deepcopy(rect)
  res.corner.x += res.corner.x + dx
  res.corner.y += res.corner.y + dy
  return res

if __name__ == "__main__":
  box = Rectangle()
  box.width = 100.0
  box.height = 200.0
  box.corner = Point()
  box.corner.x = 0.0
  box.corner.y = 0.0

  center = find_center(box)
  print_point(center)

  print("Before growing rectangle: {}, {}".format(box.width, box.height))
  grow_rectangle(box, 150.0, 300.0)
  print("After growing rectangle: {}, {}".format(box.width, box.height))
  
  moved_box = move_rectangle(box, 2, 3)
  print("After moving rectangle: ", end='')
  print_point(moved_box.corner)

  p1 = Point()
  p1.x = 3.0
  p1.y = 4.0

  p2 = copy.copy(p1)
  print("Is p2 p1?", p1 is p2)
  # expect false because with user-defined type, python has no way
  # to consider them equivalent
  print("Is p2 == p1?", p1 == p2)
 
  box2 = copy.copy(box)
  print("box2 is box?", box2 is box)
  print("box2.corner is box.corner", box2.corner is box.corner) 
