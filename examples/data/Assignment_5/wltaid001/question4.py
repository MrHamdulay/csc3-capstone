#ask for function
import math
func=input("Enter a function f(x):\n")
#draw graph
x_inc=1/2
y_inc=1/2
for y in range(-10,11):
    for x in range(-10,11):
        func1=eval(str(func))
        y_real=-y
        x_real=x
        if y_real-y_inc<=func1<=y_real+y_inc:
            print ("o",end="")
        elif x==0 and y==0:
            print("+",end="")
        elif y==0:
            print("-",end="")
        elif x==0:
            print("|",end="")
        else:
            print(" ",end="")        
       
    print()
    
