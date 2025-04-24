import random

# Initialize the variables
intMin = 1
intMax = 100
intNum = random.randint(intMin, intMax)

# Get user input
print("Welcome to my guessing game.".center(60))
intGuess = int(input(f"Guess a number between {intMin} and {intMax} "))

# Generating the number
if intGuess == intNum:
    print("You have guessed it correctly!")
elif intGuess > intNum:
    print("You have guessed too high")
elif intGuess < intNum:
    print("You have guessed it too low")
print(f"The number was {intNum}")