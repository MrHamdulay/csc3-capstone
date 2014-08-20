first_name = str(input("Enter first name:\n"))
last_name = str(input("Enter last name:\n"))
money = round(int(input("Enter sum of money in USD:\n")), 2)
money30 = round(money * 0.3, 2)
country = str(input("Enter country name:\n"))
string = """
Dearest {0}
It is with a heavy heart that I inform you of the death of my father,
General Fayk {1}, your long lost relative from Mapsfostol.
My father left the sum of {2}USD for us, your distant cousins.
Unfortunately, we cannot access the money as it is in a bank in {4}.
I desperately need your assistance to access this money.
I will even pay you generously, 30% of the amount - {3}USD,
for your help.  Please get in touch with me at this email address asap.
Yours sincerely
Frank {1}""".format(first_name, last_name, money, money30, country)
print(string)
