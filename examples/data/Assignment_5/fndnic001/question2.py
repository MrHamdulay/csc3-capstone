'''Vending machine change calculator
Nic Findlay April 2014'''
cost = eval(input('Enter the cost (in cents):\n'))
deposit = 0

while cost > deposit:
        change = eval(input('Deposit a coin or note (in cents):\n'))
        deposit += change

change = deposit - cost
changevalues = [100, 25, 10, 5, 1]
endvalues = ['$1', '25c', '10c', '5c', '1c']

if cost == deposit:
        print('')
else:
        print('Your change is:')
        for i in range(5):
                answer = change // changevalues[i]
                change -= answer * changevalues[i]
                if answer == 0:
                        continue
                else:
                        print(answer, 'x', endvalues[i])
         