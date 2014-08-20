#Vending Machine
#Sofia Palmer
#15 April 2014


def main():
    cost = eval(input("Enter the cost (in cents):\n"))
    deposit = 0
    # add deposits to one another while it is less than the cost
    while (deposit < cost):     
        addition = eval(input("Deposit a coin or note (in cents):\n"))
        deposit += addition
    change = deposit-cost
    dollars = 0
    quarters = 0 
    dimes = 0
    nickels = 0
    pennys = 0
    # how many denominations of each money are needed for the change
    while (change >= 100):      
        change = change - 100
        dollars += 1
    while (change >= 25):
        change = change - 25
        quarters += 1
    while (change >= 10):
        change = change - 10
        dimes += 1    
    while (change >= 5):
        change = change - 5
        nickels += 1 
    while (change >= 1):
        change = change - 1
        pennys += 1    
    #if the change does not include a certain kind of coin they are not printed    
    if (deposit > cost):
        print("Your change is:")
        if (dollars >= 1):
            print(dollars, "x $1")
        if (quarters >= 1):    
            print(quarters, "x 25c") 
        if (dimes >= 1): 
            print(dimes, "x 10c") 
        if (nickels >= 1):        
            print(nickels, "x 5c")
        if (pennys >= 1):
            print(pennys, "x 1c")
    
main()
    
    
