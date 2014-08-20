""" A program to simulate a vending machine and calculate change based on the amount paid. 
Author: Afika Nyati
Date: 15th April 2014"""

def main():
    
    
    # Asking for cost
    
    
    cost = eval(input("Enter the cost (in cents):\n")) # Asks for the cost in cents
    
    
    
    
    # Asking for money
    
    amount_deposited = 0 # Initializing the variable for indefinite loop
    
    while amount_deposited < cost :
        
        amount_deposited += eval(input("Deposit a coin or note (in cents):\n")) # As long as the user hasn't given enough to pay for the cost, it will ask for money
        
    
    change = amount_deposited - cost # This is the change the user must get
    
    if change == 0: # If there is no change, don't print anything
        print("", end ="")     
    
    else:
        
        # Calculating the change
    
        dollars = change // 100 # Calculating how many dollars must be paid out
    
        change -= dollars * 100 # Readjusting the amount of change that must be allocated
    
    
        quarters = change // 25 # Calculating how many quarters must be paid out
    
        change -= quarters * 25 # Readjusting the amount of change that must be allocated
    
    
        dimes = change //10 # Calculating how many dimes must be paid out
    
        change -= dimes * 10 # Readjusting the amount of change that must be allocated
    
    
        nickels = change // 5 # Calculating how many nickels must be paid out
    
        change -= nickels * 5 # Readjusting the amount of change that must be allocated. Leftover change is less than 5 and will be 1c coins
    

        # Printing the change
   
   
        print("Your change is:")
    
        if dollars > 0: print(dollars, "x $1") # Only prints if there is change in this form. If lower than zero, it will not print.
    
        if quarters > 0: print(quarters, "x 25c") # Only prints if there is change in this form. If lower than zero, it will not print.
        
        if dimes > 0: print(dimes, "x 10c")  # Only prints if there is change in this form. If lower than zero, it will not print.
        
        if nickels > 0: print(nickels, "x 5c") # Only prints if there is change in this form. If lower than zero, it will not print.
        
        if change > 0: print(change, "x 1c") # Only prints if there is change in this form. If lower than zero, it will not print.
    

main()
    
    
        
        
    
    
    