import math
yinc=0.5
def graph():
    function=input("Enter a function f(x):\n")
    for i in range(10,-11,-1):
        
        
        for a in range(-10,11):
            a=str(a)
            func=function.replace("x","("+a+")")
            y=eval(func)
            a=int(a)        
            if i-yinc<=y<=i+yinc:
                print("o",end="")        
            elif i==0 and a==0:
                print("+",end="") #correct
            elif a==0:
                print("|",end="") #correct
            elif i==0:
                print("-",end="")#correct
            #elif -y==a:
                #print("o",end="")
            else:    
                print(" ",end="")
        print()
graph()        
        