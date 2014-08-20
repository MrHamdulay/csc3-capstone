def letter(First_name,Last_name,Money,Country):
    print("Dearest",First_name)
    print("It is with a heavy heart that I inform you of the death of my father,")
    print("General Fayk ",Last_name, ", your long lost relative from Mapsfostol.",sep="")
    print ("My father left the sum of ",Money,"USD for us, your distant cousins.",sep="")
    print("Unfortunately, we cannot access the money as it is in a bank in ",Country,".",sep="")
    print("I desperately need your assistance to access this money.")
    print("I will even pay you generously, 30% of the amount - ",Money*30/100,"USD,",sep="")
    print("for your help.  Please get in touch with me at this email address asap.")
    print("Yours sincerely")
    print("Frank", Last_name)
    
First_name = input("Enter first name:\n")
Last_name = input("Enter last name:\n")
Money= eval(input("Enter sum of money in USD:\n"))
Country =input("Enter country name:\n")

print()
letter(First_name,Last_name,Money,Country)