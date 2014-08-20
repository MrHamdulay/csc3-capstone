"""Question 2 of Assignment 5: Vending Machine Simulator - Change Calculator
Shaheel Kooverjee
17th April 2014"""

cost = eval(input("Enter the cost (in cents):\n")) #input cost

payment = 0
while payment < cost: #prompt until enough deposited
    deposit = eval(input("Deposit a coin or note (in cents):\n"))
    payment += deposit 

fullchange = payment-cost #change (amount unaltered)
change = payment-cost #change

a = change//100
change = change%100
b = change//25
change = change%25
c = change//10
change = change%10
d = change//5
change = change%5

if cost != 0 and fullchange != 0:
    print("Your change is:")
if a != 0: 
    print(a, "x $1")
if b != 0:
    print(b, "x 25c")
if c != 0:
    print(c, "x 10c")
if d != 0:
    print(d, "x 5c")
if change != 0:
    print(change, "x 1c")