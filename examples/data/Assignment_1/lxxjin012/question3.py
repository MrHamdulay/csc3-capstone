#program that generates a personalised spam message based on the user's full name, country and a sum of money
#Jenny Luo
#03-Mar-2014

first_name=input("Enter first name:\n")
last_name=input("Enter last name:\n")
money=eval((input("Enter sum of money in USD:\n")))
country=input("Enter country name:\n")
print("")
print("Dearest", first_name, end="\n")
print("It is with a heavy heart that I inform you of the death of my father,")
print("General Fayk "+last_name+", your long lost relative from Mapsfostol.")
print("My father left the sum of "+str(money)+"USD for us, your distant cousins.")
money30=float((0.3*money))
print("Unfortunately, we cannot access the money as it is in a bank in "+country+".")
print("I desperately need your assistance to access this money.")
print("I will even pay you generously, 30% of the amount - "+str(money30)+"USD," )
print("for your help.  Please get in touch with me at this email address asap.")
print("Yours sincerely")
print("Frank", last_name)


