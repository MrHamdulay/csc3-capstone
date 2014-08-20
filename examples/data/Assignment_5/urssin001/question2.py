'''Write a program to simulate a vending machine and calculate change based on the amount paid
Sinead Urisohn
15 April 2014'''

#get cost of item and amount deposited input
cost=eval(input("Enter the cost (in cents):\n"))
#set deposit to 0
dep=0
#check if cost entered is bigger than 0
if cost>0:
    #then ask for deposit
    dep=eval(input("Deposit a coin or note (in cents):\n"))
#create a sum to keep track of total amount deposited
sum=dep
#while sum is less than cost and
#check if cost entered is bigger than 0

while sum<cost and cost>0:
    #ask for another deposit
    dep=eval(input("Deposit a coin or note (in cents):\n"))
    #add deposit to sum
    sum+=dep
#get amount of change and temp change variable
change=sum-cost
temp=sum-cost
#Assume that all change is given in coins only and coins come in the following denominations:
# 1c, 5c, 10c, 25c, $1
#create counters to track number of times that a currency values is used
one=0
five=0
ten=0
twentyfive=0
dollar=0
#work out if dollar change 
if change/100>=1:
        dollar=change//100
        #subtract dollar chage from change value to get amount of cents still owed
        change=round((change/100-(dollar))*100)
#loop while change is not zero
while change!=0:
    #while change bigger than coin denominations increase there counters
    #and decrease their value from change
    if change>=25:
        twentyfive+=1
        change=change-25 
    elif change>=10:
        ten+=1
        change=change-10
    elif change >=5:
        five+=1
        change-=5
    else: 
        #work out 1 cent change required based on remaining change value
        one=int(change)
        #set change to 0 to end loop
        change=0
#print change message
if temp>0:
    print("Your change is:")
    #if count values bigger than zero 
    #they must be include in change message
    if dollar>0:
        print(dollar,"x $1")
    if twentyfive>0:
        print(twentyfive,"x 25c")
    if ten>0:
        print(ten,"x 10c")
    if five>0:
        print(five,"x 5c")
    if one>0:
        print(one,"x 1c")