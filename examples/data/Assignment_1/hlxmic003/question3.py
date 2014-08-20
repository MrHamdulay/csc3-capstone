# Michaela Heale
# CSC1015F Assignement 1
# Question 3

name = input("Enter first name:\n")
sname = input("Enter last name:\n")
moneyUSD = eval(input("Enter sum of money in USD:\n"))
country = input("Enter country name:\n")

money30 = moneyUSD*0.3

print("\nDearest ",name,"\nIt is with a heavy heart that I inform you of the death of my father,\nGeneral Fayk ",sname,", your long lost relative from Mapsfostol.\nMy father left the sum of ",moneyUSD,"USD for us, your distant cousins.\nUnfortunately, we cannot access the money as it is in a bank in ",country,".\nI desperately need your assistance to access this money.\nI will even pay you generously, 30% of the amount - ",money30,"USD,\nfor your help.  Please get in touch with me at this email address asap.\nYours sincerely\nFrank ",sname, sep='')