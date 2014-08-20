import math
func = input("Enter a function f(x):\n")
for y in range(-10,11):
    for x in range(-10,11):
        if "**" in func:
            if x<0:
                x*=-1        
        val=round(eval(func.replace('x',str(x))),0)
       
        if -y==val:
            print('o',end='')    
        elif x==y and x==0: print("+",end='')
        elif x==0: print("|",end='')
        elif y==0: print("-",end='')    
        else: print(" ",end='')        
    print()