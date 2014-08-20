"""Program that simulates a vending machine
04/14/2014
Ricky Conn
CNNRIC004"""



def depositMoney():
    
    costRemaining = eval(input("Enter the cost (in cents):\n"))
    while(costRemaining >0):
        moneyInput = eval(input("Deposit a coin or note (in cents):\n"))
        costRemaining -= moneyInput
        
    if(costRemaining < 0):
        change = costRemaining * -1
        returnChange(change)

def returnChange(change):
    print("Your change is:")
    
    dollars = 0
    twentyFives = 0
    tens = 0
    fives = 0
    ones = 0
    
    while(change > 99):
        change -= 100
        dollars += 1
        
    while((change > 24) and (change < 100)):
        change -= 25
        twentyFives += 1
        
    while((change > 9) and (change < 25)):
        change -= 10
        tens += 1    
    
    while((change > 4) and (change < 10)):
        change -= 5
        fives += 1
        
    while((change > 0) and (change < 5)):
        change -= 1
        ones += 1
        
    if(dollars>0):
        print(dollars,"x $1")
    if(twentyFives>0):
        print(twentyFives,"x 25c")
    if(tens>0):
        print(tens,"x 10c")
    if(fives>0):
        print(fives,"x 5c")
    if(ones>0):
        print(ones,"x 1c")
        
depositMoney()


