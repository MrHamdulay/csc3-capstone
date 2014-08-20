
import math
func = input("Enter a function f(x):\n")

for y in range (-10,11):
    for x in range(-10,11):
        y_value = eval(func)
        if (round(-(y_value),0) == y):
            print("o",end ="")
        elif (x ==0 and y ==0):
            print("+",end="")
        elif (x == 0):
            print("|",end="")          
            
        elif (y ==0):   
            print("-",end="")
            
            
        elif (x ==5 and y==0):
            print("+", end="")
            
        
        else:
            print(" ", end="")
    print()       
        