# Ask for the player's dog's name with an input statement and
# store their response in a variable
dog = input("🐶 What's your dog's name? 🐕 \n")
# Use an f-string to print the dog's name within the sentence
print(f"Let's Find {dog}!\n")

search = input("Where should we look first? \n").lower()
# Store several possible variations of the correct answer in a list
hiding_place = ["park", "the park", "dog park", "the dog park"]

# Use a while loop to keep the game going until the player is correct
while search not in hiding_place:
    # Check whether the player needs a hint
    if search == "hint":
        print(f"{dog} loves going to the park, the grocery store, \n the bakery, and the living room.")
    else:
        print(f"Nope. {dog} isn't at the {search}.")
    search = input('Where should we look next? (or type "hint") \n')

# This code will only run after the player is correct and the while loop is exited
print("Hoooooray!")
print(f"We found {dog}! Thanks for your help!")