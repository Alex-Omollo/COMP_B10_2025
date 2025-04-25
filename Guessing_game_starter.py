import random

# Create variables for min and max
intMin = 1
intMax = 10
intTotalTries = 3

# Welcome the user
print("@"*60)
print("Welcome to my guessing game".center(60))
print("@"*60)

while (True):
    # Generate the secret number
    intSecret = random.randint(intMin, intMax)

    intTry = 1

    while (intTry <= intTotalTries):
        print(f"\nThis is try number {intTry} of {intTotalTries}.")

        # Make sure the user gives the correct input
        while (True):
            # Get the user guess
            strGuess = input(f"Guess a number between {intMin} and {intMax}: ")

            if (strGuess.isnumeric()):
                intGuess = int(strGuess)
                break
            else:
                print("You need to enter a number!\n")

        # Compare to see if they guess right
        if (intGuess < intSecret):
            print("You guessed too low!")
        elif (intGuess > intSecret):
            print("You guessed too high!")
        else:
            print("You guessed the secret number!")
            break
        intTry += 1

    print(f"Secret number was {intSecret}.\n")
    strAgain = input("Would you like to play again? (y/n):")

    if (strAgain == "n"):
        break
    else:
        print("You have chossen to play again.\n")

print("Thanks for playing my game!")