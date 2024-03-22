import random
import turtle

# Set up the canvas
screen = turtle.Screen()
# 400 x 400 pixels
screen.setup(400, 400)
screen.bgcolor('light green')

colors = ['red', 'blue', 'green']
# Make variables for each color and set them all to 0
red = blue = green = 0

t = turtle.Turtle()
t.hideturtle()
t.speed(2)
t.shape('turtle')
t.penup()
# Make the turtle larger
t.shapesize(3, 3)
# Go to the far left, so the turtle is off screen
t.goto(-500, 0)
t.showturtle()

# Have 10 clone turtles glide across the screen one after another, 
# each in a random color from the 3 options
for _ in range(10):
    sprite = t.clone()
    color = random.choice(colors)
    sprite.color(color)
    if color == 'red':
        red += 1
    elif color == 'blue':
        blue += 1
    else:
        green += 1
    sprite.fd(1000)
    sprite.hideturtle()

# Ask the player how many turtles of each color there were
response = int(input("How many red turtles were there? "))
if response == red:
    print("Correct!")
else:
    print("Whoops! That's not right.")

response = int(input("How many blue turtles? "))
if response == blue:
    print("Correct!")
else:
    print("Whoops! That's not right.")

response = int(input("How many green turtles? "))
if response == green:
    print("Correct!")
else:
    print("Whoops! That's not right.")

print('Red:', red, 'Blue:', blue, 'Green:', green)

screen.mainloop()