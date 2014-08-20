import math

function=input("Enter a function f(x):\n")
yinc=1/2
for j in range(10,-11,-1):
    
    for i in range(-10,11):
        
        x=i
        y=eval(function)
        
        if(j-yinc<=y<=j+yinc):
            print("o",end="")
        elif(i==0 and j==0):
            print("+",end="")
        elif(i==0):
            print("|",end="")
        elif(j==0):
            print("-",end="")
        else:
            print(" ",end="")
    print()