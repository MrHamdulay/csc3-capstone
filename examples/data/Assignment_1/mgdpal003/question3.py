#Program to generate a personalised spam message
#Palesa Magudulela
# 6 March 2014

def spam():
    firstname=input("Enter first name: \n")
    lastname=input("Enter last name: \n")
    money=eval(input("Enter sum of money in USD: \n"))
    country=input("Enter country name: \n")
    x=0.30*money
    print()
    print("Dearest",firstname,)
    print("It is with a heavy heart that I inform you of the death of my father,")
    print("General Fayk ",lastname, "your long lost relative from Mapsfostol.")
    print("My father left the sum of",money,"USD for us, your distant cousins.",sep="")
    print("Unfortunately, we cannot access the money as it is in a bank in",country,".")
    print("I desperately need your assistance to access this money.")
    print("I will even pay you generously, 30% the amount - ",x,"USD," "for your help.")
    print("Please get in touch with me at this email address asap.")
    print("Yours sincerely")
    print("Frank",lastname,)
spam()