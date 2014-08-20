"""This program simulates a vending machine and calculates the change
Mtunzi France
15 April 2014"""
def Change_Calculator():
    cost = eval(input("Enter the cost (in cents):\n")) #prompts user type in cost
    if cost == 0:
        return""
    deposit = eval(input("Deposit a coin or note (in cents):\n")) #prompts user to deposit money 
    while cost > deposit: #loop that asks the user to add more money up until the deposited money exceeds the cost
        deposit2 = eval(input("Deposit a coin or note (in cents):\n"))
        deposit = deposit + deposit2
    if deposit > cost:
        change1 = deposit - cost #Change in hundreds of cents
        dollar = change1 // 100 #Converts the change in cents to change in dollars
        remainder1 = change1 % 100 #The change left when the dollar change is taken
        First_Cents = remainder1 // 25 #gives the number of 25 cents in the change left when the dollar is extrapolated
        remainder_2 = remainder1 % 25  #gives the leftover cents after 25 are taken 
        Second_Cents = remainder_2 // 10 #gives the number of 10 cents in change
        remainder_3 = remainder_2 % 10 # gives leftover cents after 10 are taken
        Third_Cents = remainder_3 // 5 #gives the number of 5 cents
        remainder_4 = remainder_3 % 5
        Fourth_Cents = remainder_4 // 1 #number of 1 cents left
        
        #Printing change
        print("Your change is:")
        
        if dollar == 0:
            pass
        else:
            print(dollar,"x $1")
        if First_Cents == 0:
            pass
        else:
            print(First_Cents,"x 25c")
        if Second_Cents == 0:
            pass
        else:
            print(Second_Cents,"x 10c")
        if Third_Cents == 0:
            pass
        else:
            print(Third_Cents,"x 5c")
        if Fourth_Cents == 0:
            pass
        else:
            print(Fourth_Cents,"x 1c") 
            
        
        #print("Your change is:")
        #print(dollar,"x $1")
        #print(First_Cents,"x 25c")
       #print(Second_Cents,"x 10c")
        #print(Third_Cents,"x 5c")
        #print(Fourth_Cents,"x 1c")
    
Change_Calculator()