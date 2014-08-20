#Spam Email
#Assignment 1, Question 3
#By Tejasvin Bagirathi BGRTEJ001

name = input("Enter first name:\n")
surname = input("Enter last name:\n")
money = eval(input("Enter sum of money in USD:\n"))
country = input("Enter country name:\n")

def email(a, b, c, d):
    print("\nDearest ", a, sep=(""))
    print("It is with a heavy heart that I inform you of the death of my father,\nGeneral Fayk ", b, ", your long lost relative from Mapsfostol.\n" "My father left the sum of ", c, "USD for us, your distant cousins.\nUnfortunately, we cannot access the money as it is in a bank in ", d, ".\nI desperately need your assistance to access this money.\nI will even pay you generously, 30% of the amount - ", (0.3*c), "USD,\nfor your help.  Please get in touch with me at this email address asap.\nYours sincerely\nFrank ", b, sep=(""))
    
email(name, surname, money, country)