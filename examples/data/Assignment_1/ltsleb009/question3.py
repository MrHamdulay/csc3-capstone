first_name = input("Enter first name:\n")
last_name = input("Enter last name:\n")
money = input("Enter sum of money in USD:\n")
money30 = int(money)*0.3
country = input("Enter country name:\n")

print("\nDearest {0}\nIt is with a heavy heart that I inform you of the death of my father,\nGeneral Fayk {1}, your long lost relative from Mapsfostol.\nMy father left the sum of {2}USD for us, your distant cousins.\nUnfortunately, we cannot access the money as it is in a bank in {4}.\nI desperately need your assistance to access this money.\nI will even pay you generously, 30% of the amount - {3}USD,\nfor your help.  Please get in touch with me at this email address asap.\nYours sincerely\nFrank {1}" .format(first_name, last_name, money, money30, country))