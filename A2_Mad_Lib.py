# Write your code below this line:
# Getting user input
strAdj1 = input("Give me an adjective: ").strip().lower()
strInvention1 = input("Give me an invention: ").strip().lower()
strNoun1 = input("Give me a noun: ").strip().lower()
strAdj2 = input("Give me a second adjective: ").strip().lower()
strBodyPart1 = input("Give me a body part: ").strip().lower()
strAdj3 = input("Give me a third adjective: ").strip().lower()
strNoun2 = input("Give me a second noun: ").strip().lower()
strNoun3 = input("Give me a third noun: ").strip().lower()

# This first line is Bill's text.  Don't delete it, unless you are making up your own mad libs.
madlibstext = f"""I would like to say a few {strAdj1} words about the
most important invention of the twentieth century. I am not
referring to {strInvention1} or even the discovery of {strNoun1}.
The most {strAdj2} invention, in my opinion, is the sneaker.
If it were not for sneakers, our {strBodyPart1} would be dirty, cold,
and {strAdj3}. Sneakers keep me from skidding if the {strNoun2} are slippery,
and when I run, they keep me from stubbing my {strNoun3}."""

# Printing the full madlib text
print(madlibstext)