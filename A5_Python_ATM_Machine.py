# Initialize the main balance
flSavBal = 500.99
flChkBal = 100.31

# Welcome the user
print("#" * 80)
print("Welcome to THE ATM".center(80))
print("#" * 80)

# Start the atm
while True :
    # Ask the user what they want to do
    print("What would you like to do?")
    print("1 - Deposit\n2 - Withdraw\n3 - Check Balance")
    strOption = input(": ")

    # Initialize the Deposit account
    if strOption == "1":
        # Ask for account
        strAcc1 = input("Which account would you like to deposit to?\n1 - Savings account\n2 - Checking account\n: ")

        if strAcc1 == "1":
            flDep = float(input("How much would you like to deposit? "))
            flSavBal += flDep
            print(f"Your current saving account balance is $ {flSavBal}.".rjust(5))

        elif strAcc1 == "2":
            flDep = float(input("How much would you like to deposit? "))
            flChkBal += flDep
            print(f"Your current check account balance is $ {flChkBal}.".rjust(5))

        else:
            print("Invalid account option")

    # Initialize the Withdrawal account
    elif strOption == "2":
        # Ask for account
        strAcc2 = input("Which account would you like to withdraw from?\n1 - Savings account\n2 - Checking account\n: ")
        if strAcc2 == "1":
            flWidth = float(input("How much would you like to withdraw? "))
            # Check if the user can withdraw more than their balance
            if flWidth > flSavBal:
                print("You do not have enough money in your account!")
                print(f"Your current account balance is $ {flSavBal}")
            else:
                flSavBal -= flWidth
                print(f"Your current saving account balance is $ {flSavBal}.")

        elif strAcc2 == "2":
            flWidth = float(input("How much would you like to withdraw? "))
            # Check if the user can withdraw more than their balance
            if flWidth > flChkBal:
                print("You do not have enough money in your account!")
                print(f"Your current account balance is $ {flChkBal}")

            else:
                flChkBal -= flWidth
                print(f"Your current checking account balance is $ {flChkBal}.")

        else:
            print("Invalid option")

    # Initialize the check balance
    elif strOption == "3":
        # Get user input on what account to check and give balance
        strAcc = input("Which account would you like to check?\n1 - Savings account\n2 - Check account\n: ")
        if strAcc == "1":
            print(f"Your savings account balance is $ {flSavBal}".rjust(5))
        elif strAcc == "2":
            print(f"Your Check account balance is $ {flChkBal}".rjust(5))
        else:
            print("Invalid option!")

    # Invalid options
    else:
        print("That is not a valid option")

    # Ask if the user would like to continue
    strAgain = input("Would you like to do another transaction?(y/n) ")
    if strAgain != "y":
        break

# Exit the user
print("Thank you for your patronage. \nHave a good day.")