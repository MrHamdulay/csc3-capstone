"""Program to calculate change from vending machine
Sabelo Xulu
15 April 2014"""

#gather inputs
cost=eval(input("Enter the cost (in cents):\n"))
amount=0
if cost!=0:
    amount=eval(input("Deposit a coin or note (in cents):\n"))
else:
    print()
#function to collect money such that it is greater than the amount needed  

while cost > (amount) :
    new_amount=eval(input("Deposit a coin or note (in cents):\n"))
    amount=amount+new_amount
    


change=amount-cost

num=0
dollars=change/100
strdollars=str(change)
#function to distinguish type of change given

if cost!=0:    
    while change>0:
       
        print("Your change is:\n", end="")
    
        dlramnt=change//100
        if dlramnt>0:
            print(str(dlramnt),"x $1")
            change=change%100
        if len(str(change))>1:
            amnt25=change//25
            if amnt25!=0:
                
                print(str(amnt25),"x 25c")
            change=change%25
        if change>0:
            amnt10=change//10
            if amnt10!=0:
                print(str(amnt10),"x 10c")
            change=change%10
        if change>0:
            amnt5=change//5
            if amnt5 !=0:
                print(str(amnt5),"x 5c")
            change=change%5
        if change>0:
            print(str(change),"x 1c")
            change=0
elif cost==0:
    print()
    


