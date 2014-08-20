#Programming that acts as a vending machine
#Keanon Fell
#15 April 2014

#Only has 1c,5c,10c,25c,$1 = 100c

#Prompting user for inout for the program
cost = eval(input("Enter the cost (in cents):\n"))
deposit = eval(input("Enter a coin or note (in cents):\n"))

while cost != 0 and cost != str:
    if deposit < cost:#if the coins depositted is less than the cost of the product
        newDeposit = eval(input ("Enter a coin or note (in cents):\n"))
    
        #Calculating the amount of change that the user must get
        diff = cost - deposit
        change = newDeposit - diff
    
        if change/100 > 1 :
            newChange = change - (change//100)*100
            print(newChange)
            if newChange%25==0:
                print("Your change is:")
                print(int(change/100),"x $1")
                print(int(newChange/25),"x 25c")
            elif newChange%10 == 0:
                print("Your change is:")
                print(int(change/100),"x $1")
                print(int(newChange/10),"x 10c")            
            elif newChange%5==0:
                print("Your change is:")
                print(int(change/100),"x $1")
                print(int(newChange/5),"x 5c")            
            elif newChange%1==0:
                print("Your change is:")
                print(int(change/100),"x $1")
                print(int(newChange/1),"x 1c")            
        
        elif change/25 > 1: #Making provision if the change is less than a dollar
            newChange = change - (change//100)*100
            if newChange%25==0:
                print("Your change is:")
                print(int(change/100),"x $1")
                print(int(newChange/25),"x 25c")
            elif newChange%10 == 0:
                print("Your change is:")
                print(int(change/100),"x $1")
                print(int(newChange/10),"x 10c")            
            elif newChange%5==0:
                print("Your change is:")
                print(int(change/100),"x $1")
                print(int(newChange/5),"x 5c")            
            elif newChange%1==0:
                print("Your change is:")
                print(int(change/100),"x $1")
                print(int(newChange/1),"x 1c") 
            
        elif change/10 > 1 :#Making provision if the change is less than 25 cents
            newChange = change - (change//100)*100
            if newChange%10 == 0:
                print("Your change is:")
                print(int(change/100),"x $1")
                print(int(newChange/10),"x 10c")            
            elif newChange%5==0:
                print("Your change is:")
                print(int(change/100),"x $1")
                print(int(newChange/5),"x 5c")            
            elif newChange%1==0:
                print("Your change is:")
                print(int(change/100),"x $1")
                print(int(newChange/1),"x 1c") 
                        
        elif change/5 > 1:#Making provision if the change is less than 10 cents
            newChange = change - (change//100)*100
            if newChange%5==0:
                print("Your change is:")
                print(int(change/100),"x $1")
                print(int(newChange/5),"x 5c")            
            elif newChange%1==0:
                print("Your change is:")
                print(int(change/100),"x $1")
                print(int(newChange/1),"x 1c")        
                
        elif change/1 > 1:#Making provision if the change is less than a 5 cents
            newChange = change - (change//100)*100
            if newChange%1==0:
                print("Your change is:")
                print(int(change/100),"x $1")
                print(int(newChange/1),"x 1c")        