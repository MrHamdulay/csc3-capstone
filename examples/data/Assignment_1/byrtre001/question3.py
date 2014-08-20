print('')
name=input('Enter first name:''\n')
lastname=input('Enter last name:''\n')
money=eval(input('Enter sum of money in USD:''\n'))
country=input('Enter country name:''\n')
print('')


calculate=(0.3*money)


print('Dearest', name)
print('It is with a heavy heart that I inform you of the death of my father,', '\n',
'General Fayk '+lastname, ', your long lost relative from Mapsfostol.','\n','My father left the sum of '+str(money)+'USD '+'for us, your distant cousins.'
'\n','Unfortunately, we cannot access the money as it is in a bank in ', country+'.', 
'\n','I desperately need your assistance to access this money.','\n','I will even pay you generously, 30% of the amount - ',
str(calculate)+'USD,','\n','for your help.  Please get in touch with me at this email address asap.','\n',
'Yours sincerely','\n','Frank '+lastname, sep='')





