import os
import random
import time

numbers = [
    '1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', 
    '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟'
]

emojis = [
    '🤖', '🎮', '👾', '👽', '🦄', '🐊', '🐲', '⭐️', 
    '🍕', '🍩', '⚽️', '🍎', '🐻', '😎', '🦖', '🐶', 
    '😻', '🍪', '🏀', '🛸', '🥋', '🎸', '🚕', '🗽'
]

print("🧠 MEMORY MATCH 🤔")
print("You'll see a row of emojis for a few seconds.")
print("Then you'll be asked to remember the position of a random one.")
print("Each time you're correct, you move on to the next round with one more emoji in the row.")
input("Press ENTER to start ")
os.system('clear')

# We start with Round 1
round = 1
# This variable controls how many seconds the player sees their hand
delay = 2

while True:
    # This list stores the random emojis for the round
    hand = []
    # This list stores the placeholder number emojis
    nums = []

    # By shuffling the emojis and then appending from the front of the list,
    # we can guarantee our hand will have random emojis without any repeated ones
    random.shuffle(emojis)
    # For Round 1, we start with 2 emojis, so our loop runs for the round variable + 1
    for i in range(round + 1):
        hand.append(emojis[i])
        # This conditional statement is in case the player makes it beyond the 10th number emoji
        if i < len(numbers):
            nums.append(numbers[i])
        else:
            nums.append("#️⃣")

    # This combines the items in our list into a string with a space between each item
    print(" ".join(hand))
    print(f"Round {round}")
    # time.sleep delays the program so the player can see their hand for a certain amout of time
    time.sleep(delay)
    # This clears the console after the delay
    os.system('clear')
    # This shows placeholder numbers where the emojis used to be
    print("  ".join(nums))

    # We need a random number to access a random emoji in our hand
    # Because list indexing starts at 0, our range is between 0 and one less than the length of our hand
    idx = random.randint(0, len(hand) - 1)
    emoji = hand[idx]
    # .strip removes any empty spaces before or after the player's response
    res = input(f"Where is {emoji}? ").strip()
    
    # When checking the player's response, we add 1 to the random index because list indexing starts at 0
    # By converting the number to a string, we match the default string data type of our input statement
    if str(idx + 1) == res:
        print("Correct!")
        # The player moves on to the next round
        round += 1
        # They get a little extra time because they have more emojis to remember
        delay += 0.25
    else:
        print("Incorrect...")
        # Show them the hand again, so they can check where the emoji actually was
        print(" ".join(hand))
        # break exits our while loop, ending the game
        break
    
    print(" ".join(hand))
    # Wait until the player is ready for the next round
    input("Press ENTER to continue")
    # Clear the console history from this round
    os.system('clear')

# When it's game over, the player's score is one less than their final round
# For example, if they lose on round 5, their score is 4
print(f"Game Over! Score: {round - 1}")