"""ASCII Graph
Yusuf Khan
17 April 2014"""

import math #import necessary packages

function = input("Enter a function f(x):\n")#input

for y in range(-10,11):#loop begins
    for x in range(-10,11):#nested loop
        y1 = -y
        f_of_x = round(eval(function))#convert typed function
        if f_of_x == y1:#              to usable value
            print("o",end="")
        elif y1==0 and x==0:
            print("+",end="")
        elif  x ==0:
            print("|",end="")
        elif y1 == 0:
            print("-",end="")
        else: print (" ",end="")   
    print()