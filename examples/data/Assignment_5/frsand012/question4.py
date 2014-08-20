import math

def grapher():
    function = input("Enter a function f(x):\n")
    
    
    for x in range(10,-11,-1):
        for y in range(-10,11):
           
            if round(eval(function)) == x:
                print("o", end = "")
                
            elif y == 0:
                print("|", end = "")  
                
            elif x == 0 and y == 0:
                print("+", end = "") 
                
            elif x == 0:
                print("-", end = "") 
                
            else:
                print(" ", end = "")
            
        print()
                
