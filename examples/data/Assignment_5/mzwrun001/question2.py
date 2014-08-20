"""program to simulate a vending machine
Runako Muzwidzwa
14 April 2014"""
total=0
cost=eval(input("Enter the cost (in cents):\n"))
while total<cost:
    y=eval(input("Deposit a coin or note (in cents):\n"))
    total+=y
    if total==cost: break
    elif total>cost: break

z=total-cost
dollar=z//100#number of $1 bills
d=z%100
quarter=d//25#number of 25c
q=d%25
ten=q//10#number of 10c
t=q%10
five=t//5#number of 5c
f=t%5
one=f//1#number of 1c
if z!=0:
    
    print("Your change is:")
#to have change incuding $
if dollar>0:
    print(dollar,"x $1")
    if quarter>0:
        print(quarter,"x 25c")
        if ten>0:
            print(ten,"x 10c")
            if five>0:
                print(five,"x 5c")
                if one>0:
                    print(one,"x 1c")
#if the dollar change is unavailable
elif quarter>0:
    print(quarter,"x 25c")
    if ten>0:
        print(ten,"x 10c")
        if five>0:
            print(five,"x 5c")
            if one>0:
                print(one,"x 1c")    
        
#if there is no change for a quarter                
elif ten>0:
    print(ten,"x 10c")
    if five>0:
        print(five,"x 5c")
        if one>0:
            print(one,"x 1c")       
#if ther is no change for 10c
elif five>0:
    print(five,"x 5c")
    if one>0:
        print(one,"x 1c")  
#there is only change less than 5c
elif one>0:
    print(one,"x 1c")
