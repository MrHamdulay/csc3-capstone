#mahdimarcus
import math

def function():
    fx=input("Enter a function f(x):\n")
    x=0
    y=0
    for y2 in range (10,-11,-1):    
        for x2 in range (-10,11,1): #restrict x and y values
            x=x2
            value=round(eval(fx))
            if value == y2:
                print("o", end="")            #indicate points that exist in domain
            if x2==0 and y2==0 and y2!=value:
                print("+", end="")
            if x2==0 and y2!=0 and y2!=value:
                print("|", end="")
            if y2==0 and x2!=0 and y2!=value:
                print("-", end="")              #create axis, however axis is replaced by o when there is an intercept
            else: 
                if y2!=0:
                    if x2!=0 :
                        if y2!=value:
                            print(" ", end="")   #indicate other possibilities                     
        print()
function()        
                
            
        
        