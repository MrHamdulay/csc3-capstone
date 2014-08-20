#Author: NLXALE001
#Date: 15 April 2014
#Assignment 5


#evaluate cost compared to amount paid
cost = eval(input("Enter the cost (in cents):\n"))
paid= 0
while paid<cost:
    deposit = eval(input("Deposit a coin or note (in cents):\n")) 
    paid += deposit
#determine total amount of change
change = paid - cost
#check change is not equal to 0
if(cost!=0 and change!=0):
    print("Your change is:")
    
onehcount = 0
twocount = 0
tencount = 0
fivecount = 0
onecount = 0

#check how many $1 should be given as change
while change>=100:
    change-=100
    onehcount+=1
if onehcount>0:
    print (onehcount, "x $1")

#check how many 25c should be given as change    
while change>=25:
    change-=25
    twocount+=1 
if twocount>0:
    print (twocount, "x 25c") 
    
#check how many 10c should be given as change    
while change>=10:
    change-=10
    tencount+=1 
if tencount>0:
    print (tencount, "x 10c") 
    
#check how many 5c should be given as change    
while change>=5:
    change-=5
    fivecount+=1
if fivecount>0:
    print (fivecount, "x 5c")
        
#check how many 1c should be given as change    
while change>1:
    change-=1
    onecount+=1
if onecount>0:
    print (onecount, "x 1c")
