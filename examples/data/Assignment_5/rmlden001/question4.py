#DenishaRamaloo
#question4
#assignment5


import math

graph=input("Enter a function f(x): \n")
 
for y in range (10, -11, -1):
    for x in range (-10, 11, 1):
        coordinate=round(eval(graph))
        if coordinate==y:
            print("o", end="")
        
        else:
            
            if y==0 and x==0: 
                print("+", end="")
            elif x==0: #y-axis
                print("|", end="")
            elif y==0:#x-axis
                print("-", end="")
            else:
                print(" ", end="")
    print()