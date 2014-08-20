#Question 2 - Assignment 1
#Spam email generator
#Nikhil Jiten Naik (NKXNIK003)
#3rd of March 2014

firstName = input("Enter first name:\n")
lastName  = input("Enter last name:\n")

moneyText = input("Enter sum of money in USD:\n")
money = eval(moneyText)
percMoney = money * 30/100

country = input("Enter country name:\n")

print("\nDearest "+firstName+" \nIt is with a heavy heart that I inform you of the death of my father,\nGeneral Fayk "+lastName+", your long lost relative from Mapsfostol.\nMy father left the sum of "+moneyText+"USD for us, your distant cousins.\nUnfortunately, we cannot access the money as it is in a bank in "+country+".\nI desperately need your assistance to access this money.\nI will even pay you generously, 30% of the amount - ",percMoney, "USD,\nfor your help.  Please get in touch with me at this email address asap.\nYours sincerely\nFrank "+lastName, sep="")