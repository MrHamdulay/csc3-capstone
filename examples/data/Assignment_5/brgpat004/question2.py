'''Q2 of Assignment 5: Vending machine change calculator
Patrick Boroughs
16 April 2014'''

cost = eval(input("Enter the cost (in cents):\n"))
payment=0

while cost>payment:
    
    deposit=eval(input("Deposit a coin or note (in cents):\n"))
    payment+=deposit

if payment>cost:
    print("Your change is:")
    change=payment-cost
    
    if change//100>=1:
        print(change//100,"x $1")
        change=change%100
    if change//25>=1:
        print(change//25,"x 25c")
        change=change%25
    if change//10>=1:
        print(change//10,"x 10c")
        change=change%10
    if change//5>=1:
        print(change//5,"x 5c")
        change=change%5
    if change//1>=1:
        print(change,"x 1c")
    