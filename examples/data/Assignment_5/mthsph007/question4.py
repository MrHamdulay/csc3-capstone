"""Sphiwe Muthembi
MTHSPH007
QUESTION 4 - ASS 5
"""
import math


def graph_func(function):
    
  
    
    
    
    for y in range(-10,11):
        
        for x in range(-10,11,1):
            func= -eval(function)          #change function from str to integer form
            ans = func                      
            
            
            if ans == 0 and x == 0 and y == 0 :         #check if function crosses 0
                print("o",end="")
            elif x == 0 and y == 0:
                print("+",end="")
            elif ans == 0 and y == 0 and x != 0:        #x intercept
                print("o",end="")
                
            elif ans == y and x == 0 :                  # y intercept
                print("o",end="")
                
            elif x== 0 and y != 0 :
                print("|",end="")
                
            elif y == 0 and x != 0:
                print("-",end="")
            elif ans == y and ans != x:
                print("o",end="")
            elif ans == x and ans == y:
                print("o",end="")
            else:
                print(" ",end="")
        print()    
                
            
func= input("Enter a function f(x):\n")            
graph_func(func)            
            
            
            