#Program to generate personalised spam message
#Jason Findlay
#28/02/2014

Name = input('Enter first name:\n')
Surname = input('Enter last name:\n')
Amount = eval(input('Enter sum of money in USD:\n'))
Country = input('Enter country name:\n')
Payment = Amount/100*30

print()
print('Dearest',Name)
print('It is with a heavy heart that I inform you of the death of my father,')
print('General Fayk ',Surname,', your long lost relative from Mapsfostol.',sep='')
print('My father left the sum of ',Amount,'USD for us, your distant cousins.',sep='')
print('Unfortunately, we cannot access the money as it is in a bank in ',Country,'.',sep='')
print('I desperately need your assistance to access this money.')
print('I will even pay you generously, 30% of the amount - ',Payment,'USD,', sep='')
print('for your help.  Please get in touch with me at this email address asap.')
print('Yours sincerely\nFrank',Surname)
