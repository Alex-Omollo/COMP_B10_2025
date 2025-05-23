from rpsModule import *

print("#" * 90)
print("Welcome to my game!".center(90))
print("#" * 90)

# Game Logic
while True:

    # Initializing the score variables
    intU = 0
    intC = 0

    # Checking if the score has been achieved
    while intU < 2 and intC < 2:
        result = judge(strUser(), strComputer())
        if result == "u":
            intU += 1
        elif result == "c":
            intC += 1
        print(f"Your score is {intU} points\nComputer score is {intC} points")

        if intU == 2:
            print("You win.\n")
        elif intC == 2:
            print("Computer wins.\n")

    strPlay = input("Would you like to play again(y/n)? ").strip().lower()
    if strPlay == "n":
        break

print("Thank you for playing")