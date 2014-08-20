#question3.py

firstName = input("Enter first name:\n")
lastName = input("Enter last name:\n")
sumUSD = eval(input("Enter sum of money in USD:\n"))
country = input("Enter country name:\n")

newMoney = sumUSD*30/100


print("\nDearest %s\nIt is with a heavy heart that I inform you of the death of my father,\nGeneral Fayk %s, your long lost relative from Mapsfostol.\nMy father left the sum of %dUSD for us, your distant cousins.\nUnfortunately, we cannot access the money as it is in a bank in %s.\nI desperately need your assistance to access this money.\nI will even pay you generously, 30%% of the amount - %sUSD,\nfor your help.  Please get in touch with me at this email address asap.\nYours sincerely\nFrank %s" % (firstName, lastName, sumUSD, country, newMoney, lastName))