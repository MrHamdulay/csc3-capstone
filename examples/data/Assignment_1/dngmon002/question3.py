# Program to generate a personalised spam message
# Monwabisi Dingane
# 25 February 2014

first_name = input("Enter first name:\n")

last_name = input("Enter last name:\n")

money_required = eval(input("Enter sum of money in USD:\n"))

country = input("Enter country name:\n")

print("\nDearest",first_name)
print("It is with a heavy heart that I inform you of the death of my father, \nGeneral Fayk",end=' ')
print(last_name,end='')
print(", your long lost relative from Mapsfostol.\nMy father left the sum of", money_required,end='')
print("USD for us, your distant cousins.\nUnfortunately, we cannot access the money as it is in a bank in", country,end='')
print(".\nI desperately need your assistance to access this money.\nI will even pay you generously, 30% of the amount -", (money_required*30/100),end='')
print("USD,\nfor your help.  Please get in touch with me at this email address asap.\nYours sincerely\nFrank", last_name)
