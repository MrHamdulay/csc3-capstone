first = input("Enter first name:\n")
last = input("Enter last name:\n")
money= input("Enter sum of money in USD:\n")

country = input("Enter country name:\n")
money30 = str(round((eval(money)*0.3),2))
print()
print("Dearest "+ first+"\nIt is with a heavy heart that I inform you of the death of my father,\n\
General Fayk "+last+", your long lost relative from Mapsfostol.\n\
My father left the sum of "+money+"USD for us, your distant cousins.\n\
Unfortunately, we cannot access the money as it is in a bank in "+country+".\n\
I desperately need your assistance to access this money.\n\
I will even pay you generously, 30% of the amount - "+money30+"USD,\n\
for your help.  Please get in touch with me at this email address asap.\n\
Yours sincerely\n\
Frank "+last)