#program to generate personalised spam
#runako muzwidzwa
#27 february 2014
def spam():
    first=input("Enter first name: "'\n')
    last=input("Enter last name: "'\n')
    total=eval(input("Enter sum of money in USD: "'\n'))
    country=input("Enter country name: "'\n')
    percent=(total*30/100)
    print()
    print("Dearest",first,)
    print("It is with a heavy heart that I inform you of the death of my father,")
    print("General Fayk ",last,", your long lost relative from Mapsfostol.",sep="") 
    print("My father left the sum of ",total,"USD for us, your distant cousins.",sep="") 
    print("Unfortunately, we cannot access the money as it is in a bank in ",country,".",sep="")
    print("I desperately need your assistance to access this money.") 
    print("I will even pay you generously, 30% of the amount - ",percent,"USD,",sep="") 
    print("for your help.  Please get in touch with me at this email address asap.")
    print("Yours sincerely")
    print("Frank",last)
spam()