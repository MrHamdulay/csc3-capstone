fname = input("Enter first name: \n")
lname = input("Enter last name: \n")
money = (input("Enter sum of money in USD: \n"))
emoney = eval(money)
country = input("Enter country name: \n")
print()

print("Dearest" , fname , "\n" + "It is with a heavy heart that I inform you of the death of my father,\nGeneral Fayk " +lname + ", your long lost relative from Mapsfostol.\nMy father left the sum of " + money+ "USD for us, your distant cousins.\nUnfortunately, we cannot access the money as it is in a bank in " + country + ".\nI desperately need your assistance to access this money.\nI will even pay you generously, 30% of the amount - " + str((30/100)*emoney) +"USD,\nfor your help.  Please get in touch with me at this email address asap.\nYours sincerely\nFrank " +lname , sep = " ")