import random
import turtle

# Set up the canvas for displaying the game
screen = turtle.Screen()
# This makes it fullscreen
screen.setup(1.0, 1.0)
screen.bgcolor('#F6D7B0')

# Draw the Pond
# Get a random distance for where the pond will be drawn on the Y-axis (between 50 and 150 pixels)
pond_dist = random.randint(50, 150)
pond_size = 50

pond = turtle.Turtle()
pond.speed(0)
pond.penup()
pond.goto(0, pond_dist)
pond.pendown()
# Make the pond a circle and fill it in blue
pond.color("blue")
pond.begin_fill()
# The input for .circle is the radius length (the distance between the center and edge),
# so to make the circle's diameter (width) the pond_size, we divide pond_size by 2
pond.circle(pond_size / 2)
pond.end_fill()
pond.hideturtle()

# Set Up the Turtle Jump
t = turtle.Turtle()
t.shape('turtle')
t.color('black', 'light green')
t.penup()
# Turn the turtle to the left, facing the pond
t.lt(90)

# Ask the player how far the turtle should jump
jump = screen.numinput("Distance", "How far should we jump?")
# This can also be done with an input statement,
# but you have to convert their answer to an integer (whole number)
# jump = int(input("How far should we jump? "))

t.fd(jump)

# pond_dist stores the Y-axis position of the bottom of the circle
# pond_dist + pond_size calculates the Y-axis position of the top of the circle
if jump >= pond_dist and jump <= (pond_dist + pond_size):
    print('SCORE')
    t.write(("    Success!"), font = ('Arial', 12, 'normal'))
else:
    print('MISS')
    t.write(("    Miss!"), font = ('Arial', 12, 'normal'))

# This keeps the screen from closing automatically
screen.mainloop()