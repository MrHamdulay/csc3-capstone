# MKHNEL011
# Assignment 1
# Question 3

#requesting_personal_info

#import math

#def personal_info():
first_name=input("Enter first name:\n")
last_name=input("Enter last name:\n")
money=eval(input("Enter sum of money in USD:\n"))
country=input("Enter country name:\n")
amount_payable= round((30/100)*(money),2)
    
#spamletterl

def letter():
    print("")
    print("Dearest",first_name)
    print("It is with a heavy heart that I inform you of the death of my father,")
    print("General Fayk ", last_name, ", your long lost relative from Mapsfostol.", sep="")
    print("My father left the sum of ", money,"USD for us, your distant cousins.", sep="")
    print("Unfortunately, we cannot access the money as it is in a bank in",country,end=".\n") 
    print("I desperately need your assistance to access this money.")
    print("I will even pay you generously, 30% of the amount - ",amount_payable, "USD,", sep="")
    print("for your help.  Please get in touch with me at this email address asap.")
    print("Yours sincerely")
    print("Frank",last_name)
    
#personal_info()
letter()