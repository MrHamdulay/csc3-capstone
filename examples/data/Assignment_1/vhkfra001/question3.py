# Program to generate personalised spam messages based on user input


first_name = input("Enter first name:\n")
last_name = input("Enter last name:\n")
money = int(input("Enter sum of money in USD:\n"))
country = input("Enter country name:\n")

thirty_percent = (money/100)*30
percent = "%"

# Had to set '%' as a variable since it was creating problems in the string
# Program thought it was a string substitution
# Also, turns out %s works for all types of variable
# Still need to figure out how to seperate this print string into lines...

print ("\nDearest %s\nIt is with a heavy heart that I inform you of the death of my father,\nGeneral Fayk %s, your long lost relative from Mapsfostol.\nMy father left the sum of %sUSD for us, your distant cousins.\nUnfortunately, we cannot access the money as it is in a bank in %s.\nI desperately need your assistance to access this money.\nI will even pay you generously, 30%s of the amount - %sUSD,\nfor your help.  Please get in touch with me at this email address asap.\nYours sincerely\nFrank %s" % (first_name, last_name, money, country, percent, thirty_percent, last_name,) )
