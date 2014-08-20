#Vending machine
#Thea Sitek, STKTHE002
#16.04.2014

#variables
deposit = 0
cost = eval(input('Enter the cost (in cents): \n'))

#ask for more input
while deposit < cost:
 payment = eval(input('Deposit a coin or note (in cents): \n'))
 deposit += payment

#calculate change
change = deposit - cost
if change != 0:
 print('Your change is:')

dollar = change//100
change %= 100
if dollar:
 print(dollar, 'x $1')

quarter = change//25
change %= 25
if quarter:
 print(quarter, 'x 25c')

dime = change//10
change %= 10
if dime:
 print(dime, 'x 10c')

nickle = change//5
change %= 5
if nickle:
 print(nickle, 'x 5c')

cent = change
if cent:
 print(cent, 'x 1c')

#for i in[dollar, quarter, dime, nickle, cent]:
# if i:
#  currency = str(i)
#  print(i, 'x', currency)
