first_name=input('Enter first name: \n')
last_name=input('Enter last name: \n')
money=eval(input('Enter sum of money in USD:\n'))
country=input('Enter country name: \n')
x=(30/100*money)

print('\nDearest' , first_name, end='\n')
print('It is with a heavy heart that I inform you of the death of my father,',end='\n')
print('General Fayk '+last_name+', your long lost relative from Mapsfostol.', end='\n')
print("My father left the sum of", str(money)+'USD for us, your distant cousins.', end='\n')
print('Unfortunately, we cannot access the money as it is in a bank in '+country+'.',end='\n')
print('I desperately need your assistance to access this money.', end='\n')
print('I will even pay you generously, 30% of the amount -',str(x)+'USD,' , end='\n')
print('for your help.  Please get in touch with me at this email address asap.', end='\n')
print('Yours sincerely',end='\n')
print('Frank', last_name)