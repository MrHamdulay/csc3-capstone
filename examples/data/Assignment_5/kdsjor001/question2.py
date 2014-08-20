"""Vending machine program
Jordan Kadish 15 April 2014"""
def VendingMachine():
    y=0
    z=0
    a=0
    b=0
    c=0
    cost=eval(input('Enter the cost (in cents):\n'))
    money=0
#Check to see if enough money has been submitted
    while money<cost:
        x=eval(input('Deposit a coin or note (in cents):\n'))
        money+=x
    change=money-cost
    if change==0:
        print('',end='')
    else:
        while change>0:
            if change>=100:
                y+=1
                change-=100
            elif change>=25:
                z+=1
                change-=25
            elif change>=10:
                a+=1
                change-=10
            elif change>=5:
                b+=1
                change-=5
            elif change>=1:
                c+=1
                change-=1
        print('Your change is:')
        if y!=0:
            print(str(y)+' x $1')
        if z!=0:
            print(str(z)+' x 25c')
        if a!=0:
            print(str(a)+' x 10c')
        if b!=0:
            print(str(b)+' x 5c')
        if c!=0:
            print(str(c)+' x 1c')
if __name__=='__main__':
    VendingMachine()