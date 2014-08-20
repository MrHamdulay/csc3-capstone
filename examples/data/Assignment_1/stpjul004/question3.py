# Question 3 in Assignment 1
# Author: Julius Stopforth
# Date: 26/02/2014

first_name = input('Enter first name:\n')
last_name = input('Enter last name:\n')
money = input('Enter sum of money in USD:\n')
country = input('Enter country name:\n')
money30 = str(int(money)*0.3)

print('\nDearest %s' % first_name)
print('It is with a heavy heart that I inform you of the death of my father,\nGeneral Fayk %s, your long lost relative from Mapsfostol.' % last_name)
print('My father left the sum of %sUSD for us, your distant cousins.' % money)
print('Unfortunately, we cannot access the money as it is in a bank in %s.' % country)
print('I desperately need your assistance to access this money.')
print('I will even pay you generously, 30% of the amount - '+money30+'USD,')
print('for your help.  Please get in touch with me at this email address asap.')
print('Yours sincerely')
print('Frank', last_name)