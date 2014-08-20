import math

a=input("Enter a function f(x):\n")

funct = a

for y in range(-10,11,1):
    
    for i in range(-10,11,1):
        
        string_i="("+str(i)+")"
        
        new_funct=funct.replace('x',string_i)
        x=eval(new_funct)
        x*=-1
        x=round(x)
        if x==y:
            print("o",end=(""))
        elif y==0 and i==0:
            print("+",end=(""))        
        elif y==0:
            print("-",end=(""))
        elif i==0:
            print("|",end=(""))
    
        elif x!=y:
            print(" ",end=(""))
    print()