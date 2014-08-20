#Asil Motala
#13 April 2014
#Assignment 5
#Question 4

import math
function=input("Enter a function f(x):\n")

for i in range(10,-11,-1):
    g=""
    for j in range(-10,11):
        k="("+str(j)+")"
        new_function=function.replace("x",str(k))
        f=eval(new_function)
        f_round=round(f)
        if f_round==i:
            g+="o"
        elif j==0 and i==0:
            g+="+"
        elif j==0:
            g+="|"
        elif i==0:
            g+="-"
        else:
            g+=" "
    print(g)