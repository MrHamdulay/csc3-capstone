""" change calculator
Adam Edelberg
15 April 2014"""

cost = eval(input("Enter the cost (in cents):\n"))

deposit = 0

while (deposit < cost):
    deposit += eval(input("Deposit a coin or note (in cents):\n"))
    
    

change = deposit - cost

dollar = 0
twentyFive = 0
ten = 0
five = 0
one = 0

while (change != 0):

    while (change >= 100):
        dollar = dollar + 1
        change -= 100
        
    while (change >= 25):
        twentyFive = twentyFive + 1
        change -= 25
        
    while (change >= 10):
        ten = ten + 1
        change -= 10  
        
    while (change >= 5):
        five = five + 1
        change -= 5
        
    while (change >= 1):
        one = one + 1
        change -= 1       


    print ("Your change is:\n",end ="")

    if (dollar > 0 ):
        print(dollar, " x $1", sep="")
    
    if (twentyFive > 0 ):
        print(twentyFive, " x 25c", sep="")
    
    if (ten > 0 ):
        print(ten, " x 10c", sep="")
    
    if (five > 0 ):
        print(five, " x 5c", sep="")
    
    if (one > 0 ):
        print(one, " x 1c", sep="")