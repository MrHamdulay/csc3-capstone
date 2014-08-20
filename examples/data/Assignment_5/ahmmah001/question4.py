'''Program to draw graphs of functions
Mahnoor Ahmed'''
import math

func=input("Enter a function f(x):\n")

for i in range(10,-11,-1):
    
    for x in range(-10,11):
        function=func.replace("x",str(x))
        y=eval(function)
        
        if i == y and i !=0:
    
            if x > 0:
                print(" "*10,"|"," "*(x-1),"o",sep="")
            elif x < 0:
                print(" "*(10+x),"o"," "*(-x-1),"|",sep="")
            elif x==0:
                print(" "*10,"o"," "*10,sep="")

                
        elif i==0:
            
            if x==0 and y==0:
                print("-"*10,"o","-"*10,sep="")            
                break
            
            elif y==0 and x<0:
                print("-"*(10+x),"o","-"*(-x-1),"+","-"*10,sep="")            
                break
            
            elif y==0 and x>0:
                print("-"*10,"+","-"*x,"o","-"*(10-x),sep="")
            
           