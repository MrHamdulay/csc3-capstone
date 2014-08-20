# Student Number: FRDYON001
# Name: Yonela Ford
# Programme to generate a personalised spam message on user's full name, country and a sum of money.

def spam():
    x=input("Enter first name:\n")
    y=input("Enter last name:\n")
    z=input("Enter sum of money in USD:\n")
    w=input("Enter country name:\n")
    
    print("\nDearest",x)
    print("It is with a heavy heart that I inform you of the death of my father,")
    print("General Fayk",y+", your long lost relative from Mapsfostol.",)
    print("My father left the sum of",z+"USD for us, your distant cousins.")
    print("Unfortunately, we cannot access the money as it is in a bank in",w+".")
    print("I desperately need your assistance to access this money.")
    print("I will even pay you generously, 30% of the amount - ",round(30/100*eval(z),1),"USD,",sep="")
    print("for your help.  Please get in touch with me at this email address asap.")
    print("Yours sincerely")
    print("Frank",y)
spam()