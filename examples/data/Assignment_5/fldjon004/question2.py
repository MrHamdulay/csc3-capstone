# question2.py
# jono field
# 16 april 2014
# program to calculate change from a vending machine

cost=eval(input("Enter the cost (in cents):\n")) # user enters cost of item
deposit=0
while deposit<cost: # loop for user to enter money to cover cost
    p=eval(input("Deposit a coin or note (in cents):\n")) # prompts user to enter money
    deposit=deposit+p # adding amount entered to total paid
change=deposit-cost # calculates change
# splits change into different money values
z=change//100
u=change%100//25
q=change%100%25//10
r=change%100%25%10//5
s=change%100%25%10%5//1
if change!=0:
    print("Your change is:")
if z!=0:
    print(str(z),"x","$1")
if u!=0:
    print(str(u),"x","25c")
if q!=0:
    print(str(q),"x","10c")
if r!=0:
    print(str(r),"x","5c")
if s!=0:
    print(str(s),"x","1c")
