#program that plots graphs
#Anthony Jacob
#16 April 2014

function=(input("Enter a function f(x):\n")) #ask user for the function
import math
for y in range(-10,11):
    yVal=y*-1
    for x in range(-10,11):
        x_real=x
        y_real=round(eval(function.replace("x","("+str(x_real)+")")))
        

        if(y_real/1==yVal):          # 
                    print("o", end ="")    
                    
                    
        elif x_real==0 and yVal==0:     #print + for the origin
            print("+",end="")
            
        
            
        elif(yVal==0):
            print("-",end="")
            x
        elif(x_real==0):               #print | 
            print("|",end="")
            
        else:
            print(" ",end="")          #print nothing when function deosnt intersect any point
    print()
            
        
        
    