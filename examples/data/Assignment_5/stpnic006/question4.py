#Nicholas Stephenson
#graph
#16 April 2014

import math



func = eval(input("Enter a function f(x):\n"))
#FUNCtion


for i in range(10,-11,-1):
    for  j in range (-10,11):
        x = j
        y = round(eval(func))  #creating axis
        
        if y == i:
            print("o", end = "") #Prints o
            
        elif(i==0 and j ==0):
            print("+", end ="")
        elif (i==0):
            print("-",end="")
        elif(j==0):
            print("|",end="")
        else:
            print(" ",end="")
    print()        
