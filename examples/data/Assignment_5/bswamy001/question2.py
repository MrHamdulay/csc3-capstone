"""Amy Bosworth, question 2, assignent 5, program to simulate a vending machine"""


#ask user for cost
cost=eval(input("Enter the cost (in cents):\n"))

if cost== str:
    print('')
    
#ask user for first deposit
deposit=eval(input("Deposit a coin or note (in cents):\n"))

if deposit==cost:#If first deposit is equal to the cost
    print("")
    
    
#Carry on asking for a deposit until cost is met or exceeded
while deposit<cost:
    adddeposit=eval(input("Deposit a coin or note (in cents):\n"))
    deposit+=adddeposit
    if deposit>cost:
        break
    elif deposit==cost:
        print("")
        break

change=deposit-cost

#If the change is only in dollars
if change!=0 and change%100==0 :
    change=(change//100)
    print("Your change is:\n",change,"x $1",sep='')
  
elif change%100!=0 :
    print("Your change is:")
    if change//100!=0:
        dollar= change//100
        print(dollar," x $1",sep='')
        
    change=change%100
    
    cents=[25, 10, 5]
    for i in range (len(cents)):
        if change%cents[i]!=0:
            cent=change//cents[i]
            change=change%cents[i]
            if cent>0:
                print(cent," x ",cents[i],"c",sep='')
                
        else:
            change=change//cents[i]
            print(change," x ",cents[i],"c",sep='')
    
    
     
            
        
        
            
            
            
            

    

        
