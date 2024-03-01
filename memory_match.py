import os
import random
from word_lists import emojis

num_cards = 8
blank_card = "⬜️"
# Make a list of blank / face-down cards to keep track of later revealed emojis
revealed = [blank_card] * num_cards
cards = []

# Get random emojis for each game
random.shuffle(emojis)

# Add half the number of cards to our deck
for i in range(num_cards // 2):
    cards.append(emojis[i])
# Then duplicate the deck, so we have 2 of each emoji
cards = cards * 2

random.shuffle(cards)

print("Welcome to Emoji Memory Match!")
print(f"Flip two cards per round by typing their position (1 - {num_cards}). \n")

# The game continues as long as the revealed list has face-down cards
while blank_card in revealed:
    print(revealed)
    print("Where should we search? ")

    # We take and convert the player's response into an integer (whole number) 
    # and decrease it by 1 because list indexing starts at 0
    # So, the first card is actually index 0
    idx1 = int(input("Guess 1: ")) - 1
    # If the index is greater than or equal to the length of the deck, 
    # or if the card has already been revealed, it's invalid
    while idx1 >= len(cards) or revealed[idx1] != blank_card:
        idx1 = int(input("Invalid choice. Try again: ")) - 1
    # Update revealed to store the emoji from the cards list
    revealed[idx1] = cards[idx1]

    idx2 = int(input("Guess 2: ")) - 1
    while idx2 >= len(cards) or revealed[idx2] != blank_card:
        idx2 = int(input("Invalid choice. Try again: ")) - 1
    revealed[idx2] = cards[idx2]

    print(revealed)

    if cards[idx1] == cards[idx2]:
        print("✅ Match!")
    else:
        print("❌ No match.")
        # If there was no match, the cards have to be flipped back face down
        revealed[idx1] = blank_card
        revealed[idx2] = blank_card

    input("\nPress ENTER to continue ")
    # This clears the console so the player can't see the positions of previous, non-matching emojis
    os.system("clear")

print(revealed)
print("\nAll matches found! Great job!")