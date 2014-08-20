firstName = input("Enter first name:\n")
lastName = input("Enter last name:\n")
sumOfMoney = eval(input("Enter sum of money in USD:\n"))
countryName = input("Enter country name:\n")
percentageValue = sumOfMoney*0.3
print("\nDearest "+firstName+"\nIt is with a heavy heart that I inform you of the death of my father,\nGeneral Fayk "+lastName+", your long lost relative from Mapsfostol.\nMy father left the sum of "+str(sumOfMoney)+"USD for us, your distant cousins.\nUnfortunately, we cannot access the money as it is in a bank in "+countryName+".\nI desperately need your assistance to access this money.\nI will even pay you generously, 30% of the amount - "+str(percentageValue)+"USD,\nfor your help.  Please get in touch with me at this email address asap.\nYours sincerely\nFrank "+lastName)