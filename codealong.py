arQuote = ["in", "rather", "someone", "a", "change", "be", "else's", "powerful", "cloud", "rainbow"]
# The above array contains a scrambled quote. Follow the steps below to unscramble it.
# Start with the array above(you can copy this code to PyChar as a template)

# 1.Sort the list alphabetically
arQuote.sort()
print(arQuote)
# 2.Use pop() to remove the third element
arQuote.pop(2)
print(arQuote)
# 3.User remove() to remove the element containing "powerful"
arQuote.remove("powerful")
print(arQuote)
# 4.Make a copy of the array called arQuote2
arQuote2 = arQuote.copy()
# 5.Copy from the 2nd element of arQuote2 to the 1st element of arQuote
arQuote[0] = arQuote2[1]
# 6.Copy from the 1st element of arQuote2 to the 2nd element of arQuote
arQuote[1] = arQuote2[0]
# 7.Use pop() to remove the 8th element of the array and store in a variable
strTemp = arQuote.pop(7)
# 8.Use pop() to remove the 7th element of the array
strTemp = arQuote.pop(6)
# 9.Copy the current arQuote into arQuote again
arQuote2 = arQuote.copy()
# 10.Copy from the 6th element of arQuote2 to the 3rd element of arQuote
arQuote[2] = arQuote2[5]
# 11.Copy from the 3rd element of arQuote2 to the 6th element of arQuote
arQuote[5] = arQuote2[2]
# 12.Copy from the 5th element of arQuote2 to the 4th element of arQuote
arQuote[3] = arQuote2[4]
# 13.Copy from the 4th element of arQuote2 to the 5th element of arQuote
arQuote[4] = arQuote2[3]
# 14.Insert the value you stored in the variable into the 5th position in arQuote
arQuote.insert(4, strTemp)
print(arQuote)
# 15.Use a for loop to print each element of the array in order.
for x in arQuote:
    print(x)