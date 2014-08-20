"""A program to calculate if you have entered enough money on a vending machine and the change thereof
Dudley Mutero
14-04-14"""

def vendor():
    #calculates if user has enter enough money to meet the cost
    deposit=0
    cost=eval(input("Enter the cost (in cents):\n"))
    while deposit<cost:
        deposit+=eval(input("Deposit a coin or note (in cents):\n"))
    # calculates the change the person is to receive
    change=deposit-cost
    changedollars=0
    while change>=100:
        change-=100
        changedollars+=1
    change25cents=0
    while change>=25:
       change-=25
       change25cents+=1
    change10cents=0
    while change>=10:
        change-=10
        change10cents+=1
    change5cents=0
    while change>=5:
        change-=5
        change5cents+=1
       #prints out change in a category in which it exists
    if changedollars>0 or changedollars>0 or  change25cents>0 or change10cents>0 or change5cents>0 :
        print ("Your change is:")
    if (changedollars>0):
        print(changedollars,'x $1')
    if (change25cents>0):
        print(change25cents,'x 25c')
    if (change10cents>0):
        print(change10cents,'x 10c')
    if (change5cents>0):
        print(change5cents,'x 5c')
    if (change>0):
        print(change,'x 1c')
        
vendor()

    