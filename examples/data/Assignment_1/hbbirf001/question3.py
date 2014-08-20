# Spam Generator
# Irfan Habib
# 2 March 2014

def spam():
    first_name =input('Enter first name:\n')
    last_name =input('Enter last name:\n')
    sum_money =input('Enter sum of money in USD:\n')
    money30 =eval(sum_money)*0.3
    country_name =input('Enter country name:\n')
    print('\nDearest',first_name)
    print('It is with a heavy heart that I inform you of the death of my father,')
    print('General Fayk ',last_name,', your long lost relative from Mapsfostol.',sep='')
    print('My father left the sum of ',sum_money,'USD for us, your distant cousins.',sep='')
    print('Unfortunately, we cannot access the money as it is in a bank in ', country_name,'.',sep='')
    print('I desperately need your assistance to access this money.')
    print('I will even pay you generously, 30% of the amount - ',money30,'USD,',sep='')
    print('for your help.  Please get in touch with me at this email address asap.',sep='')
    print('Yours sincerely \nFrank ',last_name,sep='')
    
spam()