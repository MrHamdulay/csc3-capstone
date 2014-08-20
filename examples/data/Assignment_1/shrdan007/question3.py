# Danielle Sher
# SHRDAN007
# 06/03/2013
# Assignment 1, Question 3

first_name = input("Enter first name:\n")
last_name = input("Enter last name:\n")
money = eval(input("Enter sum of money in USD:\n"))
country = input("Enter country name:\n")

x = money
answer = 0.3*x

print('')
print('Dearest', first_name)
print('It is with a heavy heart that I inform you of the death of my father,')
print('General Fayk ', end='') 
print(last_name, ', your long lost relative from Mapsfostol.', sep='')
print('My father left the sum of ', end='')
print(money,'USD for us, your distant cousins.', sep='')
print('Unfortunately, we cannot access the money as it is in a bank in ', end='')
print(country, '.', sep='')
print('I desperately need your assistance to access this money.')
print('I will even pay you generously, 30% of the amount - ', answer,'USD,', sep='')
print('for your help.  Please get in touch with me at this email address asap.')
print('Yours sincerely')
print('Frank', last_name)
      
      
