first = input("Enter first name: \n")
last = input("Enter last name: \n")
money = eval(input("Enter sum of money in USD: \n"))
mon = money*0.3
country = input("Enter country name: \n")

print("\nDearest " + first + "\nIt is with a heavy heart that I inform you of the death of my father,\nGeneral Fayk " + last + ", your long lost relative from Mapsfostol.\nMy father left the sum of "+ str(money) + "USD for us, your distant cousins.\nUnfortunately, we cannot access the money as it is in a bank in " + country + ".\nI desperately need your assistance to access this money.\nI will even pay you generously, 30% of the amount - " + str(mon) + "USD,\n" + "for your help.  Please get in touch with me at this email address asap.\nYours sincerely\nFrank " + last)

