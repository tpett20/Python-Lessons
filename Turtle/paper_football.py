import time
import turtle

# Set up the screen to be narrow like a football field
screen = turtle.Screen()
screen.setup(200, 400)
screen.bgcolor("green")

# Make the turtle look like sheet of paper folded into a triangle
t = turtle.Turtle()
t.shape("triangle")
t.color("white")

# Draw the finish line
FINISH_Y = 150
t.penup()
t.goto(-500, FINISH_Y)
t.pendown()
t.goto(500, FINISH_Y)
t.penup()
# Start the turtle at the bottom of the screen, perfectly opposite the finish line
t.goto(0, -FINISH_Y)
# Point the turtle towards the finish line
t.left(90)

# The middle of the screen is at position 0 on the Y-axis.
# The finish line is FINISH_Y pixels above the middle of the screen.
# The turtle is FINISH_Y pixels below the middle of the screen.
# So the target distance is FINISH_Y * 2
TARGET_DIST = FINISH_Y * 2
total_dist = 0

print("You have 4 tries to reach the finish line.")
print("Your goal is to hit the finish line exactly!")
print("You'll travel 100 pixels for each second the clock runs.")
for i in range(4):
    # time.time() captures a time stamp.
    # By subtracting one time stamp from another, we can calculate the wait time in seconds.
    input("Press Enter to Start the Clock")
    start = time.time()
    input("Press Enter to Stop")
    end = time.time()
    elapsed = end - start
    # Multiply the time waited by 100 to convert seconds into pixels
    dist = elapsed * 100 # Pixels
    # Move the turtle foward and add that distance to the total distance variable
    t.fd(dist)
    total_dist += dist
    print("Total Distance:", total_dist)
    # If your total distance is beyond the target distance plus a buffer, you've lost
    # Otherwise, if your distance is beyond the target distance minus a buffer, you've won
    if total_dist > (TARGET_DIST + 5):
        print("You lost :(")
        break
    elif total_dist > (TARGET_DIST - 15):
        print("🎉 TOUCHDOWN! 🏈")
        screen.bgcolor("blue")
        break
    print()

# If you used up your 4 turns and the turtle still hasn't reached the finish line, you've lost
if total_dist < (TARGET_DIST - 15):
    print("You lost :(")

screen.mainloop()