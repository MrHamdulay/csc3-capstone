import math
func = input("Enter a function f(x):\n")

for y in range(-10,11):
    for x in range(-10,11):
        strx = '(' + str(x) + ')'
        function = func.replace("x", strx)
        f = -eval(function)
        f = round(f)
        if y == f:
            print("o",sep="", end="")
        elif y == 0 and x == 0:
            print ("+",sep="", end="")        
        elif y == 0:
            print ("-",sep="", end="")
        elif x == 0:
            print ("|",sep="", end="")

        else:
            print(" ",sep="", end="")
    print()
            
            
        