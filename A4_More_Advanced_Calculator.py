# Welcome the user
print("#" * 90)
print("\n")
print("Welcome To My Advanced Calculator".center(90))
print("\n")
print("#" * 90)

# Provide menu choice for the user
print("Choose 1 for calculating simple intrest\nChoose 2 for calculating compounded intrest")
print("\n")

# Get user input on menu
intNum = input("What is your Choice? ")

# If option 1
if intNum == "1":
    # Ask user for variables
    flPrinciple = float(input("What is the principle amount: "))
    flRate = float(input("What is the intrest rate: "))
    flTime = float(input("What is the time taken: "))

    # Calculate from variables
    flIntrest = flPrinciple * (flRate/100) * flTime

    # Print results
    print(f"Your intrest rate for a principle of {flPrinciple} and an intrest rate of {flRate} and a time of {flTime} is"
          f" {flIntrest}")

# If option 2
elif intNum == "2":
    # Get user input
    flPrinciple = float(input("What is the principle amount: "))
    flRate = float(input("What is the intrest rate: "))
    flTime = float(input("What is the time taken: "))
    flCompound = float(input("How many times is it compounded: "))

    # Calculating the intrest
    flAmount = flPrinciple * (1 + (flRate / 100) / flCompound) ** (flCompound * flTime)

    # Print the results
    print(f"The compounded intrest rate for a principal of {flPrinciple} and a time of {flTime} with an intrest rate of {flRate} "
          f"compounded at {flCompound} gives a total amount of {flAmount}")

# If neither
else:
    # Print error and close
    print("You did not choose any of the given choices.")

# End the program
print("Thank you for using my calculator. Come again soon.")