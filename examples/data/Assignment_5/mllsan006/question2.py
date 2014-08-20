'''Assignment 5 Question 2
Sankara Mallane
14 April 2014'''

cost = eval(input("Enter the cost (in cents):\n"))
userInput = 0
payment = 0

while payment <cost:
    
    userInput = eval(input("Deposit a coin or note (in cents):\n"))
    payment += userInput 

change = payment-cost
dollars = change//100
quarters = (change%100)//25
dimes = ((change%100)%25)//10
nickels = (((change%100)%25)%10)//5
cents = ((((change%100)%25)%10))%5//1

if change>0:
    
    print("Your change is:")
    if dollars>0:
        print(dollars, "x $1")

    if quarters>0:
        print(quarters, "x 25c")
    
    if dimes>0:
        print(dimes, "x 10c")

    if nickels>0:
        print(nickels, "x 5c")

    if cents>0:
        print(cents, "x 1c")
