"""vending machine simulator
Claudia Pastellides
15 April 2014"""

cost=eval(input("Enter the cost (in cents):\n"))
change = 0

while change<cost: #adding together deposit amounts until cost amount is reached
    deposit=eval(input("Deposit a coin or note (in cents):\n"))
    change += deposit 
    
 # working out change
diff = change - cost
dollar=round(diff//100) # calculating the coefficient for each different type of change
twentyfive=round((diff-dollar*100)//25)
ten=round((diff-dollar*100-twentyfive*25)//10)
five=round((diff-dollar*100-twentyfive*25-ten*10)//5)
one=round((diff-dollar*100-twentyfive*25-ten*10-five*5)//1)


if diff>0: # working out what amount of each type of change is needed 
    print("Your change is:")
    if dollar*100+twentyfive*25+ten*10+five*5+one*1==diff:
                if dollar>0:
                    print(dollar,"x $1\n",end="")
                if twentyfive>0:
                    print(twentyfive,"x 25c\n",end="")
                if ten>0:
                    print(ten,"x 10c\n",end="")
                if five>0:
                    print(five,"x 5c\n",end="")
                if one>0:
                    print(one, "x 1c",end="")
    
    

