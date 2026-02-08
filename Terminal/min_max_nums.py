import random
import time

# Introduce the game to the user
print("Here are a bunch of numbers")
print("You have to find the greatest and smallest as fast as you can")

# Create variables for the highest and lowest numbers
# Make the hi variable really small, 
# so we're guaranteed to find a greater random number
hi = -1000000
# Make the lo variable really big, 
# so we're guaranteed to find a smaller random number
lo = 1000000

# Generate several random numbers
for i in range(10):
    num = random.randint(-10000, 10000)
    print(num)
    # If the random number is greater than the hi variable,
    if num > hi:
        # the random number is the new high
        hi = num
    # If the random number is less than the lo variable,
    if num < lo:
        # the random number is the new low
        lo = num

# Quiz the player on the greatest and smallest numbers
# And calculate how long it took them to answer
correct = 0
# Start Time Stamp
start = time.time()

response = int(input("Which number is the greatest? "))
if response == hi:
    print("Correct!")
    correct += 1
else:
    print(f"Incorrect. The hi was {hi}")

response = int(input("Which number is the smallest? "))
if response == lo:
    print("Correct!")
    correct += 1
else:
    print(f"Incorrect. The lo was {lo}")

# End Time Stamp
end = time.time()
elapsed = round(end - start, 2)
print(f"You took {elapsed} seconds")

# Check if the player got both questions correct in under 10 seconds
if elapsed < 10 and correct == 2:
    print("Excellent!")
else:
    print("01" * 1000)
    print("Incorrect... Program crashing.....")