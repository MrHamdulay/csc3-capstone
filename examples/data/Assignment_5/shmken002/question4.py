"""grapher
ringo shima
17/4/14"""
import math

def graphs():
    func = input("Enter a function f(x):\n")
   
    for y in range(10,-11,-1):
        for x in range(-10,11):
            if y == round(eval(func)):
                print("o",end = "")
            else:
                if y == 0 and x == 0:
                    print(("+"), end = "")
                               
                elif y == 0 and x !=0:
                    print("-", end ="")
                elif x == 0 and y != 0:
                    print("|", end ="")
                else:
                    print(" ", end ="")
        print()
            
        
graphs()