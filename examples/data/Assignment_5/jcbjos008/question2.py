'''Joshen Credelio Jacob
16/04/14'''

#cost of item
cost=eval(input('Enter the cost (in cents):\n'))
deposit=0
tot_deposit=0
while tot_deposit<cost:
    deposit=eval(input('Deposit a coin or note (in cents):\n'))
    tot_deposit+=deposit

change=tot_deposit-cost

if change > 0:
    print('Your change is:')

for i in (100, 25,10,5,1):
    
    x=change//i
    if(x > 0) :
        if i == 100:
            print(x,'x','$' + str(1))
        else:
            print(x,'x',str(i) + 'c')
        change=change-(x*i)