name = input("Enter first name:\n")
lastname = input("Enter last name:\n")
moneysum = eval(input("Enter sum of money in USD:\n"))
country = input("Enter country name:\n")
fraction = ((moneysum*30)/100)

print("")
print("Dearest", name)
print("It is with a heavy heart that I inform you of the death of my father,")
print("General Fayk ",lastname,", your long lost relative from Mapsfostol.", sep=(""))
print("My father left the sum of ", moneysum, "USD for us, your distant cousins.", sep=(""))
print("Unfortunately, we cannot access the money as it is in a bank in ", country,".", sep=(""))
print("I desperately need your assistance to access this money.")
print("I will even pay you generously, 30% of the amount - ", fraction ,"USD,",sep=(""))
print("for your help.  Please get in touch with me at this email address asap.")
print("Yours sincerely")
print("Frank", lastname)



