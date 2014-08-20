#Write a program to simulate a vending machine and calculate change based on the amount paid. Given the cost, the user should first be prompted to add more money until the cost is met/exceeded by the payment.

#Assume that all change is given in coins only and coins come in the following denominations: 1c, 5c, 10c, 25c, $1


import math

#Enter cost
cost = eval(input("Enter the cost (in cents): \n"))

#Entering the payments and calculation thereof
while cost > 0:
    deposit = eval(input("Deposit a coin or note (in cents): \n"))
    cost -= deposit
    
#Change Calculation
change = -cost
cost =  -cost
dollar = cost//100
cost = cost%100
twenties = cost//25
cost = cost%25
tens = cost//10
cost = cost%10
fives = cost//5
cost = cost%5
ones = cost
  
    
#Printing out of change
def calculator():
    if change == 0:
        print("")
    else:
        print("Your change is:")
        if dollar != 0:
            print(dollar,"x","$1")
        if twenties != 0:
            print(twenties,"x","25c")
        if tens != 0:
            print(tens,"x","10c")
        if fives != 0:
            print(fives,"x","5c")
        if ones != 0:
            print(ones,"x","1c")
       

calculator()
    
    
    
