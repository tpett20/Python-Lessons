import math
import turtle

# Set up the canvas
screen = turtle.Screen()
screen.setup(1.0, 1.0)
screen.title("Concentric Circles")

# Create functions to calculate each circle's circumference and area
def get_circumference(r):
  return 2 * math.pi * r

def get_area(r):
  # ** is the exponent operator, so r ** 2 is r squared
  return math.pi * r ** 2

radius = 500
colors = ["purple", "light blue", "violet", "light green", "green"]
count = 0

t = turtle.Turtle()
# 0 is the fastest speed setting
t.speed(0)
t.hideturtle()

# To fill a large circle with increasingly smaller circles, 
# we use a while loop to draw new circles with a smaller radius each time
while radius > 0:
  # Print the values for each circle we draw, plus an empty line for spacing
  print('Radius:', radius)
  circumference = get_circumference(radius)
  print('Circumference:', circumference)
  area = get_area(radius)
  print('Area:', area)
  print()

  # By setting our Y-axis position to the negative value of the radius, 
  # we make the center of the screen the center of each circle
  t.goto(0, -radius)
  # The modulo operator (%) is used to iterate over the different colors in order no matter how many times the loop runs
  t.color(colors[count % len(colors)])
  t.begin_fill()
  t.circle(radius)
  t.end_fill()
  radius -= 10
  count += 1

print('Circles Drawn:', count)

screen.mainloop()