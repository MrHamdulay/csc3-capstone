import math

fn = input("Enter a function f(x):\n")

for y in range(10,-11,-1):
    for x in range(-10,11):
        function = round(eval(fn))
        #print (y, end="")
        if function == y:
            print("o",end="")
        elif function != y and x != 0 and y!=0:
            print(" ",end="")
        elif function != y and x == 0 and y == 0:
            print("+",end="")
        elif function != y and x == 0:
            print("|",end="")
        elif function != y and y == 0:
            print("-",end="")       
    print()
            
