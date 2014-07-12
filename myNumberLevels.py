# myNumber.py
# This game uses a home made function

import random

# Initilize computer_number is case of failure
computer_number = 101

# Create the function is_same()
def is_same(target, number):
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
print("Hello.")
level = input("What level would you like? Press e for easy, m for medium or h for hard\n")
while level != "e" and level != "m" and level != "h":
    print("Sorry. You must type in one of the letters 'e', 'm' or 'h'.")
    level = input("What level would you like? Press e for easy, m for medium or h for hard\n")

# Set upper_limit based on level
if level == "e":
    upper_limit = 10
elif level == "m":
    upper_limit = 20
elif level == "h":
    upper_limit = 100
else:
    computer_number = 102

# Set random number
computer_number = random.randint(1, upper_limit)
    
# Collect the user's guess as an integer
guess = int(input("I am thinking if a number between 1 and " + str(upper_limit) + ".\nCan you guess it? "))

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
input("Correct!\nWell Done\n\nPress RETURN to exit.")
