#Ikhlaas Pohplonker
#15 April 2014
#calculates change based on the amount paid asks user to enter a cost
cost=eval(input("Enter the cost (in cents):\n"))
deposit=0
#prompts user to add more money until the cost is met/exceeded by the paymen
while deposit<cost:
    p=eval(input("Deposit a coin or note (in cents):\n"))
    deposit=deposit+p
change=deposit-cost
#calculates how many $1, 25c, 10c, 5c, 1c coins the user must get
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
    
    
    
          
    

   