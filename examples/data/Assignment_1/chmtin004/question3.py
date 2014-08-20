#Program to create a personalised spam message
#Tinotenda Chemvura (CHMTIN004)
#02 March 2014

def spam_message():
    print("Enter first name:")
    name1=input()
    print("Enter last name:")
    name2=input()
    print("Enter sum of money in USD:")
    cash=eval(input())
    print("Enter country name:")
    country=input()
    print()
    print("Dearest",name1)
    print("It is with a heavy heart that I inform you of the death of my father,")
    print("General Fayk ",name2,", your long lost relative from Mapsfostol.",sep="")
    print("My father left the sum of ",cash,"USD for us, your distant cousins.",sep="")
    print("Unfortunately, we cannot access the money as it is in a bank in",country,end=".\n")
    print("I desperately need your assistance to access this money.")
    print("I will even pay you generously, 30% of the amount -",round(0.30*cash, 2),end="USD,\n")
    print("for your help.  Please get in touch with me at this email address asap.")
    print("Yours sincerely")
    print("Frank",name2)

spam_message()