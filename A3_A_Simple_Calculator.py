# Welcome the user
print("#" * 60)
print("Welcome to a simple compound intrest calculator".center(60))
print("#" * 60)
print("\n")

# Get user input
flPrinciple = float(input("What is the principle amount: "))
flRate = float(input("What is the intrest rate: "))
flTime = float(input("What is the time taken: "))
flCompound = float(input("How many times is it compounded: "))

# Calculating the intrest
flAmount = flPrinciple * (1 + (flRate / 100) / flCompound) ** (flCompound * flTime)

# Final answer
print(f"The compounded intrest rate for a principal of {flPrinciple} and a time of {flTime} with an intrest rate of {flRate} "
      f"compounded at {flCompound} gives a total amount of {flAmount}")