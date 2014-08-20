#Assignment 5 - Question 2
#Aidan de Nobrega
#13/04/2014

def vending_machine():
    '''Vending machine that calculates change to return'''
    cost = eval(input("Enter the cost (in cents):\n"))
    
    if cost > 0: #Function exits if cost is not greater than 0
        
        total_money_in = 0 #Holder for deposited notes/coins
        
        while total_money_in < cost:
#User prompted to add more money until the cost is met/exceeded by the payment.
            money_in = eval(input("Deposit a coin or note (in cents):\n"))
            total_money_in += money_in 
#Adds note/coin amount to total deposited
            
        total_change = total_money_in - cost #Total change to return
        
        if total_change > 0: #If deposited equals cost, no change
            
            dollars = 0 #holders for number of each denomination to return
            quarters = 0
            dimes = 0
            fives = 0
            pennies = 0
            
#Machine always tries to return as few items as possible
            while total_change > 0: #Returns a dollar
                if total_change >= 100:
                    total_change -= 100
                    dollars += 1 #Increments number of dollar notes returned
                    continue
                if 25 <= total_change < 100: #Returns a quarter
                    total_change -= 25
                    quarters += 1
                    continue
                if 10 <= total_change < 25: #Returns a dime
                    total_change -=10
                    dimes += 1
                    continue
                if 5 <= total_change < 10: #Returns 5c
                    total_change -= 5
                    fives += 1
                    continue
                if 1 <= total_change < 5: #Returns a penny
                    total_change -= 1
                    pennies += 1
                    continue
                
#Prints number of each denomination returned as change
            print("Your change is:")
            if dollars > 0:
                print(dollars, "x $1")
            if quarters > 0:
                print(quarters, "x 25c")
            if dimes > 0:
                print(dimes, "x 10c")
            if fives > 0:
                print(fives, "x 5c")
            if pennies > 0:
                print (pennies, "x 1c")
        
vending_machine()     