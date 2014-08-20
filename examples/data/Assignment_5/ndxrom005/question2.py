cost=eval(input('Enter the cost (in cents):\n'))
deposit=0
tdeposit=0
while tdeposit<cost:
    deposit=eval(input('Deposit a coin or note (in cents):\n'))
    tdeposit+=deposit

change=tdeposit-cost

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