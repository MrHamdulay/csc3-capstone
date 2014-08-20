import math
f = input("Enter a function f(x):\n")
for  y in range(-10,11):
    som =  0
    for x in range(-10,11):
        if f.find("**2") > 0:
                som +=1
                x = -x
                if som >= 11:
                    x = -x       
        fun = f.replace("x",str(x))
        p1 = eval(fun)
        p2 = -y
        if p2-0.5 <= p1 <= p2+0.5 :
            print("o",end="")        
        elif x == 0 and y == 0:
            print("+",end="")        
        elif x == 0:
            print("|",end="")
        elif y == 0:
            print("-",end="")
        else:
            print(" ",end="")
    
    print()

        

