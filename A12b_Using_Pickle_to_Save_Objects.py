# The Challenge
#
# You may choose one of the two following challenges to complete this assignment:
#
# Enhance the employee database assignment so that the database data is stored in a file,
# and that file is loaded when the program starts, and updated each time there is a change to the data.
# I would suggest using the Pickle module to save your database (your dictionary) to a file,
# and calling that function whenever a change is made to the data.
# Another function should load the data using Pickle and return the dictionary.

# Constraints / Success Criteria
#
#     Must save data to a text file.
#     Must load data from the text file upon startup.
#     All code must be commented.
#     Use only what we have covered in this class up to this point

import pickle

dEmployee = {}

def saveData(dObj):
    fPickle = open("a12pickle.txt", "wb")
    pickle.dump(dObj, fPickle)
    fPickle.close()
    print("\nData Saved.\n")

def loadData():
    fPickle = open("a12pickle.txt", 'rb')
    dObj = pickle.load(fPickle)
    print("\nData Loaded.\n")
    return dObj

def addEmployee(dData):
    print("Here is the format of employee data: ")
    print("""
    employee ID = emp
    employee name = first-name second-name
    employee position = name of position in company
    employee salary = salary to the nearest decimal ie. 125.69
    """)
    # Getting user input for the database
    strId = input("What is the employee id? ").strip()
    strName = input("What is the name of the employee? ").strip().title()
    strPos = input("What is the position of the employee? ").strip().title()
    while True:
        try:
            strSalary = input("What is the salary of the employee? ")
            flSalary = float(strSalary)
            break
        except ValueError:
            print("You cant have a name as a number!")
        except:
            print("Enter a valid number")

    dTemp = {"Name": strName, "Salary": flSalary, "Position": strPos}

    dData[strId] = dTemp

    saveData(dData)

    return dData

def removeEmployee(dData):
    listEmployees(dData)

    strRem = input("What is the ID of the employee to be removed? ")

    if strRem in dData:
        dTemp = dData.pop(strRem)
        print(f"Employee {dTemp['Name']} was removed.")
    else:
        print("That employee ID was not found!")

    saveData(dData)

    return dData

def listEmployees(dData):
    for key in dData:
        print(f"ID: {key}".ljust(10, ".") + f"{dData[key]['Name']}")

while True:
    print("Welcome to the Employees Database")
    print("""
    1. Add Employee
    2. List Employees
    3. Remove Employee
    """)
    strMenu = input("Choose one option: ").strip()

    # Check the user input and call the appropriate function
    if strMenu == "1":
        addEmployee(dEmployee)
    elif strMenu == "2":
        listEmployees(dEmployee)
    elif strMenu == "3":
        removeEmployee(dEmployee)
    else:
        print("That option is not available!")

    # Ask if the user wants to continue
    strCont = input("Would you like to continue(y/n)?").strip().lower()
    if strCont == "n":
        break