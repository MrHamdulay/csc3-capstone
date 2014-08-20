import math

fName = input("Enter first name:\n")
lName = input("Enter last name:\n")
money = input("Enter sum of money in USD:\n")
country = input("Enter country name:\n")
payment = round(eval(money)/100*30, 2)

print("")

print("Dearest", fName)
print("It is with a heavy heart that I inform you of the death of my father,")
print("General Fayk " + lName + ", your long lost relative from Mapsfostol.")
print("My father left the sum of " + money + "USD for us, your distant cousins.")
print("Unfortunately, we cannot access the money as it is in a bank in", country + ".")
print("I desperately need your assistance to access this money.")
print("I will even pay you generously, 30% of the amount - ",  payment, "USD,", sep="")
print("for your help.  Please get in touch with me at this email address asap.")
print("Yours sincerely")
print("Frank", lName)