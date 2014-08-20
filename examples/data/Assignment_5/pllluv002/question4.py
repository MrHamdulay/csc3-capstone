import math
q=input("Enter a function f(x):\n")

for y in range(10,-11,-1):
    for x1 in range(-10,11,1):
        x=x1
        fx=round(eval(q))
        if fx == y:
            print("o",end="")
        
        if y==0 and x==0 and y!= fx:
            print("+",end="")    
        
        if x==0 and y!= fx and y!= 0 :
            print("|",end="")
        
        if y== 0 and x!=0 and y != fx :
            print("-",end="")
            

            
        else:
            if x!=0 and y!=0 and fx!=y :
                        print(" ",end="")
            
    print()
            
        