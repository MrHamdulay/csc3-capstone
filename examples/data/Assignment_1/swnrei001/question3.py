def spam():
    firstname = input("Enter first name:\n")
    lastname = input("Enter last name:\n")
    money = eval(input("Enter sum of money in USD:\n"))
    country = input("Enter country name:\n")
    
    letter = """Dearest """ + firstname + """\nIt is with a heavy heart that I inform you of the death of my father,
General Fayk """ + lastname + """, your long lost relative from Mapsfostol.
My father left the sum of """ + str(money) + """USD for us, your distant cousins.
Unfortunately, we cannot access the money as it is in a bank in """ + country + """.
I desperately need your assistance to access this money.
I will even pay you generously, 30% of the amount - """ + str(money * 0.3) + """USD,
for your help.  Please get in touch with me at this email address asap.
Yours sincerely
Frank """ + lastname
    print()
    print(letter)

spam()