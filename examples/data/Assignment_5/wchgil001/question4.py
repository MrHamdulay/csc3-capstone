#Gillian Wachira
#17/04/2014
import math
g=input("Enter a function f(x):\n")

for y in range(10,-11,-1):
        if y!=10:
                print("")
        for x in range(-10,11):
                line=eval(g)
                line=round(line)
                if line==y:
                        print("o",end="")                  
                
                
                elif x==0 and y==0:
                        print("+",end="")                
                        
                elif y==0:
                        print("-",end="")
                elif x==0:
                        print("|",end="")
                else:
                        print(" ",end="")
                  
       

     

