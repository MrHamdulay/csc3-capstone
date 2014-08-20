''' Assignment 5, question 2
This program simulates a vending machine and calculates change
Tristan Subroyen
13 April 2014'''

def vendingMachine(): # This function is the program's main process
    deposit = 0 # initializes deposit...
    cost = eval(input("Enter the cost (in cents):\n"))
    while cost > deposit: # while the deposited amt is insufficient, the user continues to deposit deposit
        deposit = deposit + eval(input("Deposit a coin or note (in cents):\n"))
        if deposit > cost: # when deposit exceeds cost..
            
            # The change calculation:
            change = deposit - cost
            cents = change*100
            amtDollars = cents//10000
            cents = cents%10000
            amt25c = (cents//2500)
            cents = cents%2500
            amt10c = cents//1000
            cents = cents%1000
            amt1c = cents//100
            
            # Print results:
            print("Your change is:")
            if amtDollars > 0:
                print(amtDollars,"x $1")
            if amt25c > 0:
                print(amt25c,"x 25c")
            if amt10c > 0:
                print(amt10c,"x 10c")
            if amt1c > 0:
                print(amt1c,"x 1c")
        

if __name__ == '__main__':
    vendingMachine()
    
        
    
        

    
    
        
    
    
    