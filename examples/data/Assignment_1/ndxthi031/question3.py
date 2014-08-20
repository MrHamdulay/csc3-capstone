#NDXTHI031
#Assignment 1
#Question3


print("Enter first name:")
name = input()
print("Enter last name:")
surname = input()
print("Enter sum of money in USD:")
mon = input()
print("Enter country name:")
country = input()
MonPercentage = str(eval(mon) * 0.3)

print('')
print('Dearest', name)
print('It is with a heavy heart that I inform you of the death of my father,')
print('General Fayk ' + surname + ', your long lost relative from Mapsfostol.')
print('My father left the sum of ' + mon + 'USD for us, your distant cousins.')
print('Unfortunately, we cannot access the money as it is in a bank in ' + country + '.')
print('I desperately need your assistance to access this money.')
print('I will even pay you generously, 30% of the amount - ' + MonPercentage + 'USD,')
print('for your help.  Please get in touch with me at this email address asap.')
print('Yours sincerely')
print('Frank ' + surname)


