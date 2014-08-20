"""program to generate a text based graph
thushar hariparsad
15 april 2015"""

import math
fx=input("Enter a function f(x):\n")

for i in range(10,-11,-1):
    a=""
    for j in range(-10,11):
        k="("+str(j)+")"
        new_function=fx.replace("x",str(k))
        b=eval(new_function)
        b_round=round(b)
        if b_round==i:
            a+="o"
        elif j==0 and i==0:
            a+="+"
        elif j==0:
            a+="|"
        elif i==0:
            a+="-"
        else:
            a+=" "
    print(a)