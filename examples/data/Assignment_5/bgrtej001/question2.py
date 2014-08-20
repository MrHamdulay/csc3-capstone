#Assignment 5, Question 2
#Vending Machine Program
#Tejasvin Bagirathi BGRTEJ001
#2014-04-17

#User enters cost
cost = eval(input("Enter the cost (in cents):\n"))
totpaid = 0
#Condidtion to prevent error if 0 is input
if cost > 0:
    deposit = eval(input("Deposit a coin or note (in cents):\n"))
    totpaid = deposit
    
#Declare and initalize variable amount paid
paid = 0

#User continues to deposit money, until item is paid for
while totpaid < cost:
    paid = eval(input("Deposit a coin or note (in cents):\n"))
    totpaid += paid

#If amount paid is greater than cost, calculate change
change = 0
if totpaid > cost:
    change = totpaid-cost
  
#Loop to calculate change
if change > 0:   
    print("Your change is:")
    #Loop to calculate demoninationsof change to be give
    while change != 0:
        #Create loop to calculate amount of coins
        for i in [100, 25, 10, 5, 1]:
            if change == 0: break
            #Calculate dollars
            elif change >= 100:
                dollars = change//i
                print(dollars, "x $1")
                change = change-(dollars*i)
            #Calculate amount of cents coins 
            else:
                dollars = change//i
                if dollars == 0: continue
                print(dollars, " x ", i, 'c', sep = '')
                change = change-(dollars*i) 
else: print()