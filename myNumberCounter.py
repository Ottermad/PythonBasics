# myNumber.py
# This game uses a home made function

import random

# Think of a number and create counter
computer_number = random.randint(1, 100)
counter = 0

# Create the function is_same()
def is_same(target, number):
    global counter
    counter += 1
    if target == number:
        result = "Win"
    elif target > number:
        result = "Low"
    elif target < number:
        result = "High"
    else:
        result = "Error"
    return result

# Start the game
print("Hello.\nI have thought of a number between 1 and 100.")


# Collect the user's guess as an integer
guess = int(input("Can you guess it? "))

# Use a function
higher_or_lower = is_same(computer_number, guess)

# Run the game until the user is correct
while higher_or_lower != "Win":
    if higher_or_lower == "Low":
        guess = int(input("Sorry, you are too low. Try again. "))
    else:
        guess = int(input("Sorry, you are too high. Try again. "))

    higher_or_lower = is_same(computer_number, guess)

# End the game
input("Correct!\nWell Done. It took you " + str(counter) + " guesses.\n\nPress RETURN to exit.")
