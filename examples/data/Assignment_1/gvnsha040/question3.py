first = input("Enter first name:\n")

last = input("Enter last name:\n")

amount = input("Enter sum of money in USD:\n")

country = input("Enter country name:\n")

donate = eval(amount)*.3

print("\nDearest " + first)
print("It is with a heavy heart that I inform you of the death of my father,")
print("General Fayk " + last +", your long lost relative from Mapsfostol.")
print("My father left the sum of " + amount+"USD for us, your distant cousins.")
print("Unfortunately, we cannot access the money as it is in a bank in " + country+".")
print("I desperately need your assistance to access this money.")
print("I will even pay you generously, 30% of the amount -" ,str(donate)+ "USD,")
print("for your help.  Please get in touch with me at this email address asap.")
print("Yours sincerely")
print("Frank " + last ) 
