import random

# Create a function that receives the user input
def strUser():
    while True:
        strUser = input("Choose between (r)ock, (p)aper or (s)cissors: ").strip().lower()
        if strUser == "r":
            strReturn =  "r"
            print("You chose rock.")
            break
        elif strUser == "p":
            strReturn =  "p"
            print("You chose paper.")
            break
        elif strUser == "s":
            strReturn = "s"
            print("You chose scissors.")
            break
        else:
            print("Invalid option! Choose among the ones given.\n")
    return strReturn

# Creates the computer input
def strComputer():
    strChoice = ["r", "p", "s"]
    strComp = random.choice(strChoice)

    if strComp == "r":
        print("The computer chooses rock.")
    elif strComp == "p":
        print("The computer chooses paper.")
    else:
        print("The computer chooses scissors.")
    return strComp

# Gives a winner
def judge(strU, strC):
    if strU == strC:
        print("Its a tie.\n")
        return "t"
    else:
        if strU == "r":
            if strC == "p":
                print("Computer wins.\n")
                return "c"
            else:
                print("You win.\n")
                return "u"
        elif strU == "p":
            if strC == "r":
                print("You win.\n")
                return "u"
            else:
                print("Computer wins.\n")
                return "c"
        else:
            if strC == "r":
                print("Computer wins.\n")
                return "c"
            else:
                print("You win.\n")
                return "u"