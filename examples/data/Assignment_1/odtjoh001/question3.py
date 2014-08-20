

firstname = input("Enter first name:\n")
lastname = input("Enter last name:\n")
money = eval(input("Enter sum of money in USD:\n"))
countryname = input("Enter country name:\n")
print()

def spamMessage(fname, lname, mon, cname):
    print("Dearest ",fname, "\nIt is with a heavy heart that I inform you of the death of my father,\nGeneral Fayk ", lname , ", your long lost relative from Mapsfostol.\nMy father left the sum of ", mon, "USD for us, your distant cousins.\nUnfortunately, we cannot access the money as it is in a bank in ", cname, ".\nI desperately need your assistance to access this money.\nI will even pay you generously, 30% of the amount - ", (0.3*mon), "USD,\nfor your help.  Please get in touch with me at this email address asap.\nYours sincerely\nFrank ",  lname, sep ="")
    
spamMessage(firstname, lastname, money, countryname)