import os
import random

print("Welcome to Simon String!\n"
       "The game starts with an empty string.\n"
       "Each round the string gets a new addition, and\n"
       "you have type the entire string from the start.\n")

# Create empty string variables to store the sequence string and player's response
string = ""
response = ""
# Store the player's game type choice
game_type = input("Would you like to play with 'numbers', 'letters', or 'directions'? ")

# Continue the game as long as the player's response matches the sequence string
while string == response:
    if game_type == "numbers":
        # Get a random number from 0 to 9
        num = random.randint(0, 9)
        # We can use the addition symbol to concatenate (join) two strings together, but
        # our number has to be converted from an integer (whole number) into a string
        string = string + str(num)
        # Use an f-string to show the last number to the player
        print(f"New Number: {num}")

    elif game_type == "letters":
        # ASCII codes are the computer's way of storing characters as numbers
        # The ASCII codes 65 through 90 represent all the capital letters
        code = random.randint(65, 90)
        # chr() converts an ASCII code number into its corresponding character
        ltr = chr(code)
        # The following is an abbreviation of string = string + ltr
        string += ltr
        print(f"New Letter: {ltr}")
    
    else:
        # Get a random string that stores a direction from the options in the list
        dir = random.choice(["Up", "Down", "Left", "Right"])
        string += dir
        print(f"New Direction: {dir}")
        # Make sure to tell the player not to add any spaces when they type their response
        # because we are not adding any spaces when concatenating the string
        print("When you type the string, don't include any spaces.")
    
    response = input("Type the whole string: ")
    # This clears the console
    os.system('clear')

print("Game Over!") 
# For the numbers and letters game types,
# we can use the length of the string less 1 to count how rounds the player completed
# because each round added 1 character to the string.
if game_type == "numbers" or game_type == "letters":
    print(f"Score: {len(string) - 1}")
print(f"String: {string}")