""" This program will manage vending machine finances
Lubalethu Dube
4/15/2014"""

def Mr_vender():
    
    #enter cost
    cost=eval(input("Enter the cost (in cents):\n"))
    #check if amount is enough
    #ask for more until enough or over    
    #enter amount paid
    amount=(0)
    while amount<cost:
        deposit=eval(input("Deposit a coin or note (in cents):\n"))
        amount+=deposit
        

    #calculate difference
    change=(amount-cost)
    if change>0:
    #convert difference into coins
        print("Your change is:")
    #find the number of dollars
    dollar=(0)
    while change >= 100:
        dollar+=1
        change-=100
    if dollar>=1:
        print(dollar,"x $1",sep=" ")
    
    #find the number of 25 cents
    twenty5=(0)
    while change>=25:
        twenty5+=1
        change-=25
    if twenty5>=1:
        print(twenty5,"x 25c")
    
    #find the number of 10 cents
    ten=(0)
    while change>=10:
        ten+=1
        change-=10
    if ten>=1:
        print(ten,"x 10c")
    #find the numberof 1 cents
    ones=(0)
    while change >=1:
        ones+=1
        change-=1
    if ones>=1:
        print(ones,"x 1c")
    #give them out
Mr_vender()