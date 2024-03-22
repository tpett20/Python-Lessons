import random

print("Welcome to the Math Quiz!")

score = 0
operations = ["+", "-", "*", "/"]
# Get the number of questions and int() converts it from a string to a integer (whole number) data type
num_questions = int(input("How many questions would you like? "))

# Set the loop to run for however long the player decides
for i in range(num_questions):
    print(f"Question {i + 1}")

    # Get two random numbers between 1 and 12
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)

    # Get a random operation from the operations list
    operation = random.choice(operations)

    # Set the answer depending on the operation
    if operation == "+":
        answer = num1 + num2
    elif operation == "-":
        answer = num1 - num2
    elif operation == "*":
        answer = num1 * num2
    else:
        # To get a whole number answer in division, multiply the numbers to get the product
        product = num1 * num2
        # the divison answer becomes num1
        answer = num1
        # and the product becomes part of the equation as num1
        # For example, 5 * 6 == 30 becomes 30 / 6 == 5
        num1 = product
    
    # Use an f-string to combine our variables into a math equation to ask the player
    question = f"{num1} {operation} {num2} = "
    response = int(input(question))
    if response == answer:
        print("Correct!")
        # Increment the score variable if the player is correct
        score += 1 
    else:
        print(f"Incorrect. {question} {answer}")
    print()

# Calculate the player's grade
# round() is rounding division output to decimal to 2 places 
# After multiplying by 100, int() converts it from a float (decimal) to an integer (whole number)
grade = int(round(score / num_questions, 2) * 100)

print(f"You got {score} out of {num_questions} questions correct!")
print(f"Grade: {grade}%")