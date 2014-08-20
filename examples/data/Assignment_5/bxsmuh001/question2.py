#Assignment 5, Question 2
#Author: Sabir Buxsoo
#Class: CSC1015F 2014
#Date Created: 16/04/2014 #Modified: 17/04/2014

#This program is designed to simulate the change output by a vending machine. The change is in various denominations of 1c, 5c, 10c, 25c and $1.

#Defining the function changeDenomination() to simulate the change.
def changeDenomination():
    cost = eval(input("Enter the cost (in cents):\n"))
    if(cost > 0):
        deposit = eval(input("Deposit a coin or note (in cents):\n"))
        
        while((deposit < cost)):
            deposit += eval(input("Deposit a coin or note (in cents):\n"))
        
        change = (deposit - cost)
        
        if (change>0):   
            print("Your change is:")
            if( change != 0):
                if(change//100 !=0):
                    print(change//100, "x $1")     
                    change = change - (change//100) * 100
                    
            if( change != 0):
                if(change//25 !=0):
                    print(change//25, "x 25c")     
                    change = change - (change//25) * 25      
        
            if( change != 0):
                if(change//10 !=0):
                    print(change//10, "x 10c")     
                    change = change - (change//10) * 10
        
            if( change != 0):
                if(change//5 !=0 ):
                    print(change//5, "x 5c")     
                    change = change - (change//5) * 5
                    
            if( change != 0):
                    print(change, "x 1c")     
                    change = change - change
changeDenomination()