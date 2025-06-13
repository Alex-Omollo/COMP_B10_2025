strText1 = """In publishing and graphic design, Lorem george.smith@google.com ipsum is a placeholder text commonly used 
to demonstrate the visual form of a document or a typeface without relying on george.smith@google.com meaningful content. 
Lorem henry@yahoo.com ipsum may be used as a placeholder before final copy is available. It is also used to temporarily 
(test@gmail.com) replace text in a process called greeking, which allows designers to consider the form of a webpage or 
newmail@hotmail.com. publication, without the meaning of the text influencing the design."""
strText2 = """The Internet (or internet)[a] is the global@gmail.com system of interconnected computer networks that uses 
the Internet protocol suite (TCP/IP)[dave@hotmail.com] to communicate between networks and devices. It is a network of 
networks that consists of private, public, academic, business, and government networks of local to global scope, linked 
by a broad array of electronic, wireless, and optical networking technologies. The Internet carries a vast range of 
bill@network.us information resources and services, such as the inter-linked hypertext@linkedin.org documents and 
applications of the World Wide Web (WWW), electronic mail, telephony, and file sharing."""
listEmail = ["bill@network.us","george.smith@google.com", "test@gmail.com"]

# Do this assignment WITHOUT the global keyword
# Function that takes in a string, and returns a list of emails found.
def returnEmails(strText):
    # filter and collect all that look like emails
    liText = strText.split()
    # print(liText)
    liMail = []

    # Get all that look like emails
    for word in liText:
        if "@" in word and "." in word:
            # print(word)
            word = word.strip("(),.{}[]/ ")
            liMail.append(word)
            # print(liMail)
    # Check that all are formated correctly as emails
    liNewMail = []
    for mail in liMail:
        parts = mail.split("@")
        if len(parts) != 2:
            continue

        # clean user-name
        rev = parts[0][::-1]
        user = ""
        for char in rev:
            if char.isalnum() or char == "_" or char == "." or char == "-":
                user += char
            else:
                break

        # clean domain name
        Drev = parts[1][::-1]
        domain = ""
        for char in Drev:
            if char.isalnum() or char == "_" or char == "." or char == "-":
                domain += char
            else:
                break

        # combine both parts together
        NewUser = user[::-1]
        print(type(NewUser))
        NewDomain = domain[::-1]
        cleanMail = NewUser + "@" + NewDomain
        liNewMail.append(cleanMail)
    return liNewMail

# Function that removes duplicates in a list, taking a list as input and returning the list without duplicates.
def removeDups(liEmail):
    liDups = returnEmails(liEmail)
    x = set(liDups)
    email = list(x)
    return email

# Function that takes a string and a list as input and returns a True or False depending on whether the string value is in the list or not.
def findCommon(strText, liText):
    results = []
    for item in strText:
        if item in liText:
            print(f"{item} is in listEmails")
            results.append(True)
        else:
            print(f"{item} is not in lisEmails")
            results.append(False)
    return results

print(returnEmails(strText2))
print(removeDups(strText2))
unique = removeDups(strText1)
print(findCommon(unique, listEmail))