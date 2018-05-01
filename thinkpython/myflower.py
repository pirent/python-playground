from polygon import square, arc
import turtle

"""Draw a pental using two arc
   
   t: Turtle
   r: radius
"""
def petal(t, r):
  for i in range(2):
    arc(t, r, 60)
    t.lt(180 - 60)

bob = turtle.Turtle()
petal(bob, 100)
turtle.mainloop()
