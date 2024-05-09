import random
import turtle

# Set up the canvas
screen = turtle.Screen()
# 800 x 800 pixels
screen.setup(800, 800)
screen.bgcolor("light blue")
screen.title("Guess the Magic Turtle!")

# We'll make 100 turtles, but the first one will be number 0
# So, grab a random number between 0 and 99
magic_idx = random.randint(0, 99)
sprites = []

for row in range(10):
    for col in range(10):
        t = turtle.Turtle()
        t.speed(0)
        t.shape("turtle")
        t.left(90)
        t.penup()
        # We use the variables col and row to set up consistently-spaced positions for the turtles
        # -300 is our starting position for the X-axis
        # 300 is our starting position for the Y-axis
        # Each turtle has 60 pixels of space from its closest neighbors
        x = -300 + (col * 60)
        y = 300 - (row * 60)
        t.goto(x, y)
        # Because our sprites array (or list) is indexed starting at 0, 
        # the length of the array before we add each turtle is that turtle's index
        t.write(f"     {len(sprites)}")
        sprites.append(t)

def hide_turtles(low, high, dir):
    # Depending on the specified direction, 
    # we can either hide our turtles from low to high or high to low
    if dir == "R":
        # For low to high, we'll use a standard loop
        # For the range, we must add 1 to the high value for it to be included
        for i in range(low, high + 1):
            sprites[i].clear()
            sprites[i].hideturtle()
    else:
        # For high to low, we'll use a backwards loop
        # For the range, we must deduct 1 from the low value for it to be included
        for i in range(high, low - 1, -1):
            sprites[i].clear()
            sprites[i].hideturtle()

floor = 0
ceil = len(sprites) - 1
# Ask the player to make a guess 
# Convert their response from a string to an integer
guess = int(input(f"Guess the magic turtle ({floor}-{ceil}):\n"))

while guess != magic_idx:
    if guess < magic_idx:
        # If our guess is too low, we can rule out any turtle from the floor up to our guess
        hide_turtles(floor, guess, "R")
        # Then the guess + 1 becomes our new floor
        floor = guess + 1
        guess = int(input(f"Guess Higher ({floor}-{ceil}): \n"))
    else:
        # If our guess is too high, we can rule out any turtle between the guess and our ceiling
        hide_turtles(guess, ceil, "L")
        # Then the guess - 1 becomes our new ceiling
        ceil = guess - 1
        guess = int(input(f"Guess Lower ({floor}-{ceil}): \n"))

# Once we exit our loop, we've found the magic turtle!
# So we can hide all the others
hide_turtles(floor, guess - 1, "R")
hide_turtles(guess + 1, ceil, "L")

print(f"Correct! Turtle {magic_idx} is the Magic Turtle")
screen.bgcolor("light green")
magic_turtle = sprites[magic_idx]
magic_turtle.speed(3)
magic_turtle.color("blue")
magic_turtle.right(90)
magic_turtle.circle(100)
magic_turtle.left(90)

screen.mainloop()