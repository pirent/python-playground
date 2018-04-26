import turtle
import math

def square(t, length):
  for i in range(4):
    t.fd(length)
    t.lt(90)

def polyline(t, n, length, angle):
  """Draw n line segments with the given length and angle (in degress).
     t is a turtle
  """
  for i in range(n):
    t.fd(length)
    t.lt(angle)

def polygon(t, length, n):
  """Draw a polygon with n side
  
  t: Turtle
  lenght: length of each side
  n: number of sides
  """
  angle = 360 / n
  polyline(t, n, length, angle)

def circle(t, r):
  act(t, r, 360)

def act(t, r, angle):
  act_length = 2 * math.pi * r * angle / 360
  n = int(act_length / 3) + 1
  step_length = act_length / n
  step_angle = angle / n
  polyline(t, n, step_length, step_angle)

bob = turtle.Turtle()
#polygon(bob, length=100, n=8)
circle(bob, r=100)
#act(bob, r=100, angle=90)
turtle.mainloop()
