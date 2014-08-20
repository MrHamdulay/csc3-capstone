#Hendrik Joosten
#JSTJOH004

firstname = input("Enter first name:\n")
lastname = input("Enter last name:\n")

strmoney = input("Enter sum of money in USD:\n")
money = float(strmoney)*0.30
moneyout = str(money)
country = input("Enter country name:\n")
print("")
print("Dearest " + firstname)
print("It is with a heavy heart that I inform you of the death of my father,")
print("General Fayk "+lastname+", your long lost relative from Mapsfostol.")
print("My father left the sum of "+strmoney+"USD for us, your distant cousins.")
print("Unfortunately, we cannot access the money as it is in a bank in "+country+".")
print("I desperately need your assistance to access this money.")
print("I will even pay you generously, 30% of the amount - "+moneyout+"USD,")
print("for your help.  Please get in touch with me at this email address asap.")
print("Yours sincerely")
print("Frank " + lastname)
