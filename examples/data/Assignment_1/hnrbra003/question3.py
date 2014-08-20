# personalised spam message programme based on the user's full name, country and a sum of money.

def SpamMsg():
    firstname = input("Enter first name:\n")
    lastname = input("Enter last name:\n")
    money = eval(input("Enter sum of money in USD:\n"))
    country = input("Enter country name:\n")
    
    print("\nDearest",firstname)                                                          # To seperate a string and a input, use a comma ( strings use brackets, calling a input doesn't
    print("It is with a heavy heart that I inform you of the death of my father,")
    print("General Fayk ",lastname,", your long lost relative from Mapsfostol.",sep="")
    print("My father left the sum of ",money,"USD for us, your distant cousins.",sep="")
    print("Unfortunately, we cannot access the money as it is in a bank in ",country,".",sep="")
    print("I desperately need your assistance to access this money.")
    print("I will even pay you generously, 30% of the amount - ", str(0.3*money),"USD,",sep="")     # Cannot have a number in print statement, so use (Str) to make use of a number in print
    print("for your help.  Please get in touch with me at this email address asap.")
    print("Yours sincerely")
    print("Frank",lastname)                                                               # MUST seperate strings from imputs with a comma
    
SpamMsg()

    
