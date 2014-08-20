firstname=input('Enter first name:\n')
lastname=input('Enter last name:\n')
money=(input('Enter sum of money in USD:\n'))
money2=eval(money)
country=input('Enter country name:\n')
money30=money2*0.3
currency=money+'USD'
money4=str(money30)
currency2=money4+'USD,'
country1=country+'.'

print()
print('Dearest',firstname)
print('It is with a heavy heart that I inform you of the death of my father,')
print('General Fayk',lastname,end='')
print(', your long lost relative from Mapsfostol.')
print('My father left the sum of',currency,end='')
print(' for us, your distant cousins.')
print('Unfortunately, we cannot access the money as it is in a bank in',country1)
print('I desperately need your assistance to access this money.\nI will even pay you generously, 30% of the amount -',currency2)
print('for your help.  Please get in touch with me at this email address asap.')
print('Yours sincerely')
print('Frank',lastname )
