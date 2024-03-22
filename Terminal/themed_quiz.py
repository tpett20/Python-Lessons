print("⚾️ Welcome to the Baseball Quiz! 🧢")
# \n is the new line character in Python
# Here it is used to create an empty line
print("Let's find out how much you know about baseball.\n")

# Set a variable to track the number of correct answers
points = 0

print("Question 1")
print("What is it called when you hit a fair ball out of the park?")
# Store the multiple choice answers in a list
options = ["a. Home Run", "b. Double", "c. Triple", "d. Pop Fly"]
# Use a for loop to print each one
for option in options:
    print(option)
# Use an input statement to store the player's answer in a variable
answer = input("Type 'a', 'b', 'c', or 'd'\n")
# Increase the points variable if the answer is correct
if answer == "a":
    points += 1

print("\nQuestion 2")
print("How many innings are in a normal game?")
options = ["a. 5", "b. 7", "c. 9", "d. 10"]
for option in options:
    print(option)
answer = input("Type 'a', 'b', 'c', or 'd'\n")
if answer == "c":
    points += 1

print("\nQuestion 3")
print("What is the first batter called?")
options = ["a. Leadoff", "b. Hitoff", "c. Startoff", "d. Slugger"]
for option in options:
    print(option)
answer = input("Type 'a', 'b', 'c', or 'd'\n")
if answer == "a":
    points += 1

print("\nQuestion 4")
print("What is a team's best starting pitcher called?")
options = ["a. Slugger", "b. Ace", "c. Closer", "d. Jack"]
for option in options:
    print(option)
answer = input("Type 'a', 'b', 'c', or 'd'\n")
if answer == "b":
    points += 1

print("\nQuestion 5")
print("What is a home run called when the bases are loaded?")
options = ["a. Big Fly", "b. Sandwich", "c. Grand Run", "d. Grand Slam"]
for option in options:
    print(option)
answer = input("Type 'a', 'b', 'c', or 'd'\n")
if answer == "d":
    points += 1

# Use an f-string to print the points variable's value within the string
print(f"\nYou got {points} out of 5 questions correct!")
if points == 5:
    print("PERFECT GAME!")