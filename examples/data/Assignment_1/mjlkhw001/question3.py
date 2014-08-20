# Program to create a spam message
# Khwezi Majola
# MJLKHW001
# 25 February 2014

FirstName = input("Enter first name:\n")
LastName = input("Enter last name:\n")
Money = eval(input("Enter sum of money in USD:\n"))
Country = input("Enter country name:\n")

print("\nDearest ", FirstName, "\n", "It is with a heavy heart that I inform you of the death of my father,\n", "General Fayk ", LastName, ", your long lost relative from Mapsfostol.\n", "My father left the sum of ", Money, "USD for us, your distant cousins.\n", "Unfortunately, we cannot access the money as it is in a bank in ", Country, ".\nI desperately need your assistance to access this money.\nI will even pay you generously, 30% of the amount - ", (Money * (3/10)), "USD,\nfor your help.  Please get in touch with me at this email address asap.\nYours sincerely\nFrank ", LastName, sep="")