# program to generate a personalised spam message



first_name = input("Enter first name:\n")
last_name = input("Enter last name:\n")
money = eval(input("Enter sum of money in USD:\n"))
country = input("Enter country name:\n")
print()
print("Dearest", first_name)
print("It is with a heavy heart that I inform you of the death of my father,")
print("General Fayk", last_name, end="")
print(", your long lost relative from Mapsfostol.")
print("My father left the sum of", money, end="")
print("USD for us, your distant cousins.")
print("Unfortunately, we cannot access the money as it is in a bank in", country, end="")
print(".")
print("I desperately need your assistance to access this money.")
money_30 = money * (30 / 100) # 30% willing to pay for help
print("I will even pay you generously, 30% of the amount -", money_30, end="")
print("USD,")
print("for your help.  Please get in touch with me at this email address asap.")
print("Yours sincerely")
print("Frank", last_name)