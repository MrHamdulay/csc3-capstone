# program to generate a personalised spam message
# nomsa gamedze
# 26 february 2014

first_name = input('\n'"Enter first name: ")
last_name = input('\n'"Enter last name: ")
money = input('\n'"Enter sum of money in USD: ")
country = input('\n'"Enter country name: ")

print('\n''\n'"Dearest "+first_name)
print("It is with a heavy heart that I inform you of the death of my father,")
print("General Fayk "+last_name+", your long lost relative from Mapsfostol.")
print("My father left the sum of "+money+"USD for us, your distant cousins.")
print("Unfortunately, we cannot access the money as it is in a bank in "+country+".")
print("I desperately need your assistance to access this money.")
money = eval(money)
money = money*0.3
money = str(money)
print("I will even pay you generously, 30% of the amount - "+money+"USD,")
print("for your help.  Please get in touch with me at this email address asap.")
print("Yours sincerely")
print("Frank "+last_name)