# Yentl Naidu (NDXYEN001)
# 17 April 2014
# Assignment 5
# Question 2

# Get the price from a person
cost=eval(input("Enter the cost (in cents):\n"))
# When a valid price is added, program can continue 
if cost>0: 
    paid=eval(input("Deposit a coin or note (in cents):\n"))
    while(paid<cost):
        paid=paid+eval(input("Deposit a coin or note (in cents):\n"))
    change=paid-cost
    # Interger division
    dol=change//100
    # Calculate the remainder
    leftdol=change%100
    tf=leftdol//25
    lefttf=leftdol%25
    t=lefttf//10
    leftt=lefttf%10
    f=leftt//5
    leftf=leftt%5
    
    # Display only if person will get some change 
    if(change>0):
        print("Your change is:")
    if(dol>=1):
        print(str(dol)+" x $1")
    if(tf>=1):
        print(str(tf)+" x 25c")
    if(t>=1):
        print(str(t)+" x 10c")
    if(f>=1):
        print(str(f)+" x 5c")
    if(leftf>=1):
        print(str(leftf)+" x 1c")