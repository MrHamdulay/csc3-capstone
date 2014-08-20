import math

function=(input("Enter a function f(x): \n"))
#y=eval(function)

for y_coord in range(10,-11,-1):
    for x in range(-10,11):
        new_x=str(x)
        function.replace("x",new_x)
        y=round(eval(function))
        if y==y_coord:
            print("o",end="")
    
        elif x==0==y_coord:
            print("+",end="")
        elif x==0 and y_coord!=0:
            print("|",end="")
        elif y_coord==0 and x!=0:
            print("-",end="")
        else:
            print(" ",end="")
    print("")
        