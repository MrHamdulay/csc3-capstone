def secure_message():
    A = input("Enter first name:""\n")
    B = input("Enter last name:""\n")
    C = eval(input("Enter sum of money in USD:""\n"))
    D = input("Enter country name:""\n")
    
    print()
    print("Dearest", A)
    print("It is with a heavy heart that I inform you of the death of my father,")
    print("General Fayk ",B,", your long lost relative from Mapsfostol.", sep=(""))
    print("My father left the sum of ", C,"USD for us, your distant cousins.", sep=(""))
    print("Unfortunately, we cannot access the money as it is in a bank in ",D,".",sep=(""))
    print("I desperately need your assistance to access this money.")
    print("I will even pay you generously, 30% of the amount - ", (C*30/100),"USD,",sep=(""))
    print("for your help.  Please get in touch with me at this email address asap.")
    print("Yours sincerely")
    print("Frank", B)

secure_message()