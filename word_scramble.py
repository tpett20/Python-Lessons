import random
from word_lists import animals

score = 0
num_questions = 5

# Mix up the order of words
random.shuffle(animals)

print("Welcome to the Word Scramble!")
print("For each word, you can type 'hint' or 'shuffle'. \n")

# Create a function for converting a list of letters into a string
def list_to_str(ltr_list):
    string = ""
    for ltr in ltr_list:
        string += ltr
    return string

for i in range(num_questions):
    answer = animals[i]

    # Shuffle the Letters of Each Word
    # convert the word to a list, so we can use random.shuffle
    letters = list(answer)
    random.shuffle(letters)
    # use our function to put the scrambled letters back to a string
    clue = list_to_str(letters)
    response = input(f"{clue}: ")

    # allow the player to ask for both a hint and a new shuffle in the same round
    while response == "hint" or response == "shuffle":
        if response == "hint":
            first_ltr = answer[0]
            print(f"The first letter is {first_ltr}")
            # after giving a hint, we need to ask the question again.
            response = input(f"{clue}: ")
        elif response == "shuffle":
            # reshuffle the letters and convert them to a string
            random.shuffle(letters)
            clue = list_to_str(letters)
            response = input(f"{clue}: ")
    
    if response == answer:
        print("Correct!")
        score += 1
    else:
        print(f"Nope. It was {answer}.")
    print()

print(f"Score: {score} out of {num_questions}.")