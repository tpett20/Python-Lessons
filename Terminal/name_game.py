from word_lists import names, faces_and_animals as emojis

import os
import random

# A Python dictionary stores key-value pairs
name_lookup = {
    "🐢": "Chester",
    "🐼": "Daisy"
}

# How to access the panda's name
# name = name_lookup["🐼"]

# Add random emojis with random names to the dictionary
for i in range(3):
    new_emoji = random.choice(emojis)
    new_name = random.choice(names)
    name_lookup[new_emoji] = new_name 

# Make a list with all the emojis in our dictionary
keys = list(name_lookup.keys())

# Print each emoji and their name
for emoji in keys:
    name = name_lookup[emoji]
    print(f"{emoji} 's name is {name}")

# Once the player is ready, clear the console
input("Press Enter once you've memorized the names")
os.system("clear")

# Shuffle the emojis
random.shuffle(keys)

# Quiz the player on each emoji's name
for emoji in keys:
    name = name_lookup[emoji]
    answer = input(f"What is {emoji} 's name? ").capitalize()
    if name == answer:
        print("Correct!")
    else:
        print(f"No, {emoji} 's name is {name}")