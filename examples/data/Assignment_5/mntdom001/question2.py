"""question2.py

a program that simulates a vending machine and calculates
change based on the amount paid.

Author: Dominic Manthoko
13 April 2014
"""

def change():
    """ this funtion will determine the total amount of money deposited"""
    
    # prompt the user for the amount owing/cost
    cost = int(input("Enter the cost (in cents): \n"))
    
    # create a variable checkcost, and set it to be True
    checkcost = True
    
    # create a loop that will check the cost, if the cost is less than 
    # or equal to zero, then nothing can be calculated. If
    # the cost is greater than zero, than run the code in the else
    while checkcost:
        if cost <= 0:
            break
        else:
            # the else runs only if the cost is greater than zero
            # prompt the user to deposit some money
            deposit = int(input("Deposit a coin or note (in cents): \n"))
            
            # set up an accumalator variable that will keep track of the amount of
            # money that the user deposits
            total = deposit
            
            # this loop will keep on running until the user has deposited a sum of 
            # money(total) that exceeds the cost 
            while total<cost:
                
                # prompt the user to deposit more money
                deposit = int(input("Deposit a coin or note (in cents): \n"))
                
                # add this money to the amount already deposited
                total+= deposit  
                
            # the change is the total amount deposited minus the cost
            change = total - cost 
            checkchange = True
            
            while checkchange:
                if change==0:
                    break
                else:
                    print("Your change is: ")
                    
                    # determines the number of $1 coins
                    num_1coins = int(change /100)
                    if num_1coins>=1:
                        print(str(num_1coins) + " x $1")
                    change = change %100
                    
                    # determines the number of 25c coins 
                    num_25c = int(change/25)
                    if num_25c>=1:
                        print(str(num_25c) + " x 25c")
                    change = change %25
                    
                    # determines the number of 10c coins
                    num_10c = int(change/10)
                    if num_10c>=1:
                        print(str(num_10c) + " x 10c")
                    change = change %10
                    
                    # determines the number of 5c coins
                    num_5c = int(change/5)
                    if num_5c >=1:
                        print(str(num_5c) + " x 5c")
                    change = change %5
                    
                    # determines the number of 1c coins
                    num_1c= int(change)
                    if num_1c >= 1:
                        print(str(num_1c) + " x 1c")  
                    checkchange= False
                    
            
                
            checkcost = False
         

            
change()
