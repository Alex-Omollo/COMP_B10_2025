dFruit = {
    "fr1":{"name":"Apples", "price":.69, "quant":10},
    "fr2":{"name":"Oranges", "price":.89, "quant":20}
}

def addFruit(dData):
    strId = input("What is the fruit id? ")
    strName = input("What is the fruit name? ")
    flPrice = float(input("What is the price? "))
    intQuant = int(input("How many are there? "))

    dTemp = {"name":strName, "price":flPrice, "quant":intQuant}

    dData[strId] = dTemp

    return dData

def listFruit(dData):
    for key in dData:
        print(f"ID: {key}".ljust(10)+ f"{dData[key]['name']}")

def removeFruit(dData):
    listFruit(dData)

    strRem = input("Enter the id of the fruit to remove: ")

    if strRem in dData:
        dTemp = dData.pop(strRem)
        print(f"{dTemp['name']} was removed")
    else:
        print("That id was not found.")
    return dData

while True:
    print("Welcome to the fruit stand")
    print("""
    1. List Fruit
    2. Add a Fruit
    3. Remove Fruit
    """)
    strMenu = input("Choose a number: ")

    if (strMenu == "1"):
        listFruit(dFruit)
    elif (strMenu == "2"):
        dFruit = addFruit(dFruit)
    elif (strMenu == "3"):
        dFruit = removeFruit(dFruit)
    else:
        print("That was not an option")

    print('\n\n')