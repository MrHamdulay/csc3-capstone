# Program to generate a personalised spam message based on the users full name
# Michele Balestra BLSMIC004
# 1st March 2014

first_name = input("Enter first name:\n")
last_name = input("Enter last name:\n")
money = input("Enter sum of money in USD:\n")
money30 = str(0.3*eval(money))
country = input("Enter country name:\n")
    
print("\nDearest " + first_name)
print("It is with a heavy heart that I inform you of the death of my father, \nGeneral Fayk " + last_name +  ", your long lost relative from Mapsfostol. \nMy father left the sum of " + money +"USD for us, your distant cousins. \nUnfortunately, we cannot access the money as it is in a bank in " + country + ". \nI desperately need your assistance to access this money. \nI will even pay you generously, 30% of the amount - " + money30 + "USD, \nfor your help.  Please get in touch with me at this email address asap. \nYours sincerely \nFrank " + last_name)