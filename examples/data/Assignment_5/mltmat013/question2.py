''' Assignment 5 Question 2
Matshepo Malatji
15 April 2014'''

#Get cost
cost = eval(input("Enter the cost (in cents):\n"))

#Prompt the user to enter more money until cost is met/exceeded
amount_received = 0
while amount_received < cost:
    deposit = eval(input("Deposit a coin or note (in cents):\n"))
    amount_received += deposit

#Determine value of change

change = amount_received - cost

#Get denominations
if change > 0:
    print("Your change is:")
    
    if change >= 100:
        dollars = change//100
        print(str(dollars) + " x $1")
        change = change - (dollars *100)       

    if (change >= 25) and (change < 100):
        quarters = change//25
        print(str(quarters) + ' x 25c')
        change = change - (quarters*25)
        
    if (change >= 10) and (change < 25):
        tens = change//10
        print(str(tens) + ' x 10c')
        change = change - (tens*10)

    if (change >= 5) and (change < 10):
        fives = change//5
        print(str(fives) + ' x 5c')
        change = change - (fives*5)

    if (change > 0) and (change < 5):
        print(str(change) + ' x 1c')
