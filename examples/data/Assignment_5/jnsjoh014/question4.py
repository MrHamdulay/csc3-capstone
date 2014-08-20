import math

def yValue(function,x):    
    return eval(function)    

def drawGraph():
    function = input("Enter a function f(x):\n")
    for y in range(-10,11):
        for x in range(-10,11):
            yVal = yValue(function,x)
            if y==round(-yVal):
                print("o",end="")
            elif x==0 and y==0:
                print ("+",end="")
            elif x == 0:
                print ("|",end="")
            elif y == 0:
                print ("-",end="")    
            else:
                print(" ",end="")
                
        print()
         
        
if __name__=="__main__":
    drawGraph()
   