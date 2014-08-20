#CSC1015F - Assignment 1 - Question 3
#Adam Rosendorff
#RSNADA001
fname = input('Enter first name:\n')
sname = input('Enter last name:\n')
money = eval(input('Enter sum of money in USD:\n'))
country = input('Enter country name:\n')
print('''\nDearest {0}
It is with a heavy heart that I inform you of the death of my father,
General Fayk {1}, your long lost relative from Mapsfostol.
My father left the sum of {2}USD for us, your distant cousins.
Unfortunately, we cannot access the money as it is in a bank in {3}.
I desperately need your assistance to access this money.
I will even pay you generously, 30% of the amount - {4}USD,
for your help.  Please get in touch with me at this email address asap.
Yours sincerely
Frank {1}'''.format(fname, sname, money, country,  money*0.3))
