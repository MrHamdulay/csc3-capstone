print("Enter first name:")
first = input()
print("Enter last name:")
last = input()
print("Enter sum of money in USD:")
money = eval(input())
print("Enter country name:")
country = input()

percent = (money/100)*30


print("\nDearest", first, "\nIt is with a heavy heart that I inform you of the death of my father,\nGeneral Fayk", last + ", your long lost relative from Mapsfostol. \nMy father left the sum of", str(money) + "USD for us, your distant cousins. \nUnfortunately, we cannot access the money as it is in a bank in", country + ".\nI desperately need your assistance to access this money.\nI will even pay you generously, 30% of the amount -", str(percent) + "USD,\nfor your help.  Please get in touch with me at this email address asap.\nYours sincerely \nFrank", last)