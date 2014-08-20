# Personalised spam message
# Author: Nasreen
# Date: 26/02/14

print("Enter first name:")
first_name = input() # User's first name
print("Enter last name:")
last_name = input() # User's last name
print("Enter sum of money in USD:")
money = input() # Amount of money
print("Enter country name:")
country = input() # Country name
money30 = (eval(money)*30)/100
print() #Prints a blank line
print("Dearest", first_name, end='\n') # addressed; enter first name
print("It is with a heavy heart that I inform you of the death of my father", end=',\n'), print("General Fayk", last_name, end=','), print(" your long lost relative from Mapsfostol.") # Line 1; enter last name
print("My father left the sum of", money, end=''), print("USD for us, your distant cousins.") # line 2; enter amount of money
print("Unfortunately, we cannot access the money as it is in a bank in", country, end='.\n') # line 3; enter country
print("I desperately need your assistance to access this money.")
print("I will even pay you generously, 30% of the amount -", money30, end=''), print("USD", end=',\n'), print("for your help.  Please get in touch with me at this email address asap.")
print("Yours sincerely")
print("Frank", last_name) # line 8; enter last name