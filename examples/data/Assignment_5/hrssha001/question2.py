#question 2 assignment 5
#Shane Horsley
#14 April 2014

cost = eval(input("Enter the cost (in cents):\n"))
if cost > 0: #if cost has been entered
    x = eval(input("Deposit a coin or note (in cents):\n"))
    while x < cost: # keep asking for more money until x >= cost
        x += eval(input("Deposit a coin or note (in cents):\n"))
    change = x - cost
    if change > 0: 
        print("Your change is:") #if exact amount isnt deposited
    dol = change//100
    if dol > 0: #only print if variable is greater than 0
        print(dol,"x $1") #dollars
    c1 = (change%100)//25
    if c1 > 0:
        print(c1,"x 25c") #25c
    c2 = ((change%100)%25)//10
    if c2 > 0:
        print(c2,"x 10c") #10c
    c3 = (((change%100)%25)%10)//5
    if c3 > 0:
        print(c3,"x 5c") #5c
    c4 = ((((change%100)%25)%10)%5)//1
    if c4 > 0:
        print(c4,"x 1c") #1c