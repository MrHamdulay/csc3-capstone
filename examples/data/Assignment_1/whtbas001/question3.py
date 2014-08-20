#ASSINGMENT 1
#QUESTION 3
#WHTBAS001
#BASIL T WHITEHEAD

def spam():
    
    FirstName = input("Enter first name: ")
    print()
    LastName = input("Enter last name: ")
    print()
    dollarz = eval(input("Enter sum of money in USD: "))
    print()
    newdollarz = dollarz * .3
    country = input("Enter country name: ")
    print()
    print()
    print("Dearest", FirstName, end="\n")
    print("It is with a heavy heart that I inform you of the death of my father", end=", \n")
    print("General Fayk ", LastName,", your long lost relative from Mapsfostol.", sep="", end="\n")
    print("My father left the sum of ", dollarz,"USD for us, your distant cousins.", sep="", end="\n")
    print("Unfortunately, we cannot access the money as it is in a bank in", country, end=". \n")
    print("I desperately need your assistance to access this money.", end="\n")
    print("I will even pay you generously, 30% of the amount -", newdollarz, end="USD, \n")
    print("for your help.  Please get in touch with me at this email address asap.", end="\n")
    print("Yours sincerely", end="\n")
    print("Frank", LastName)
spam()