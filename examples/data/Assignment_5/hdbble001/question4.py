import math
def function():
    a=input("Enter a function f(x):\n")
    yinc = 0.5
    for y in range(10, -11, -1): 
        got_x = False
        for x in range(-10, 11):
            b=eval(a.replace("x", "("+ str(x) + ")"))
            if y-yinc <= b <= y+yinc:
                print ("o",end="")
                got_x = True
            elif x==0 and y==0:
                print ("+",end="")
            elif x == 0:
                print ("|",end="")
            elif y == 0:
                print ("-",end="")
            else:
                print (" ",end="")   
                got_x = False                 
        print()
        
function()