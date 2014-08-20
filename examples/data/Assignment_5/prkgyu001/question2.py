import math

#Entering the cost!
cost = eval(input("Enter the cost (in cents): \n"))

#Entering the deposits and calculations!
while cost > 0:
    deposit = eval(input("Deposit a coin or note (in cents): \n"))
    cost = cost - deposit
    
#some tools for the calculator
cost = abs(int(cost))
dollar = cost//100
twenties = (cost - dollar*100)//25
tens = (cost - dollar*100 - twenties*25)//10
fives = (cost - dollar*100 - twenties*25 - tens*10)//5
ones =  (cost - dollar*100 - twenties*25 - tens*10 - fives*5)//1
    
    
#definition of calculator
def calculator():
    if cost == 0:
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
    
    
    