# spam message
# Name: Hebert Tema
# Student Number: TMXTHA006
# 28 February 2014

first_name = input("Enter first name: \n")
last_name = input("Enter last name: \n")
money = eval(input("Enter sum of money in USD: \n"))
country = input("Enter country name: \n")

money30 = (30 / 100) * money

print("")
print("Dearest", first_name, end="\n")
print("It is with a heavy heart that I inform you of the death of my father,", "\nGeneral Fayk ", last_name, ", your long lost relative from Mapsfostol.", sep="", end="\n")
print("My father left the sum of ", money,"USD for us, your distant cousins.", sep="", end="\n")
print("Unfortunately, we cannot access the money as it is in a bank in", country, end=".\n")
print("I desperately need your assistance to access this money.")
print("I will even pay you generously, 30% of the amount - ", money30, "USD,\nfor your help.  Please get in touch with me at this email address asap.", sep="")
print("Yours sincerely")
print("Frank", last_name)