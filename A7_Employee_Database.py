# Initializing the employee dictionary
dEmployee = {}

def addEmployee(dData):
    # Getting user input for the database
    strId = input("What is the employee id? ").strip()
    strName = input("What is the name of the employee? ").strip().title()
    strPos = input("What is the position of the employee? ").strip()
    flSalary = float(input("What is the salary of the employee? "))

    dTemp = {"Name": strName, "Salary": flSalary, "Position": strPos}

    dData[strId] = dTemp

    return dData

def removeEmployee(dData):
    listEmployees(dData)

    strRem = input("What is the ID of the employee to be removed? ")

    if strRem in dData:
        dTemp = dData.pop(strRem)
        print(f"Employee {dTemp['Name']} was removed.")
    else:
        print("That employee ID was not found!")
    return dData

def listEmployees(dData):
    for key in dData:
        print(f"ID: {key}".ljust(10) + f"{dData[key]['Name']}")

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