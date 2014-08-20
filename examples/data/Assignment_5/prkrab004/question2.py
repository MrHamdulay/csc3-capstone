#Assignment 5
#Question 2
#Rabia Parker
#Due date:17/04/14

#program to help calculate change in a vending machine.

cost=eval(input("Enter the cost (in cents):\n"))
begin=0


while begin<cost:
    deposit=eval(input("Deposit a coin or note (in cents):\n"))
    begin+=deposit
change=begin-cost
n=change #new_change

change=begin-cost #1c,5c,10c,25c,$1

if change !=0:
    print("Your change is:")
if change>=100:
    print((change//100),'x $1')
    n=change%100         #new change
if (n-25)>=1:
    print((n//25),'x 25c')
    n=n%25                #new change quarters
if (n-10)>=1:
    print((n//10),'x 10c')
    n=n%10                #new change 10c
if (n-5)>=1:
    print((n//5),'x 5c')
    n=n%5
if n !=0:
    print((n//1),'x 1c')

        
    

    

          

        



    

