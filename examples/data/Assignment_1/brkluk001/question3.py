first_name = input('Enter first name:\n')
last_name = input('Enter last name:\n')
money = eval(input('Enter sum of money in USD:\n'))
country = input('Enter country name:\n')

percent = 0.3*money

print('\nDearest ', first_name,'\nIt is with a heavy heart that I inform you of the death of my father,\nGeneral Fayk ', last_name,', your long lost relative from Mapsfostol.\n''My father left the sum of ', money,'USD for us, your distant cousins.\n''Unfortunately, we cannot access the money as it is in a bank in ', country, '.\nI desperately need your assistance to access this money.\nI will even pay you generously, 30% of the amount - ', percent, 'USD,\nfor your help.  Please get in touch with me at this email address asap.\nYours sincerely\nFrank ', last_name, sep='')


