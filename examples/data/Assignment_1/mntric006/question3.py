firstname = input("Enter first name:\n")
lastname = input("Enter last name:\n")
summoney = input("Enter sum of money in USD:\n")
country = input("Enter country name:\n")
percmoney = (eval(summoney))*0.3

print("")
print("Dearest "+firstname)
print("It is with a heavy heart that I inform you of the death of my father,")
print("General Fayk "+lastname+", your long lost relative from Mapsfostol.")
print("My father left the sum of "+summoney+"USD for us, your distant cousins.")
print("Unfortunately, we cannot access the money as it is in a bank in "+country+".")
print("I desperately need your assistance to access this money.")
print("I will even pay you generously, 30% of the amount - "+str(percmoney)+"USD,")
print("for your help.  Please get in touch with me at this email address asap.")
print("Yours sincerely")
print("Frank "+lastname)