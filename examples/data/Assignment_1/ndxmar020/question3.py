def Spam():
    Name = input("Enter first name:\n")
    LastName = input("Enter last name:\n")
    Money = input("Enter sum of money in USD:\n")
    Money = eval(Money)
    Country = input("Enter country name:\n")
    print("")
    print("Dearest",Name)
    print("It is with a heavy heart that I inform you of the death of my father,")
    print("General Fayk ",LastName,", your long lost relative from Mapsfostol.",sep="")
    print("My father left the sum of ",Money,"USD for us, your distant cousins.",sep="")
    print("Unfortunately, we cannot access the money as it is in a bank in ",Country,".",sep="")
    print("I desperately need your assistance to access this money.")
    print("I will even pay you generously, 30% of the amount - ",0.3*Money,"USD,",sep="")
    print("for your help.  Please get in touch with me at this email address asap.")
    print("Yours sincerely")
    print("Frank",LastName)
    
Spam()




