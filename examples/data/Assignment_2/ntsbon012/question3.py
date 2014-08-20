#Ntshangase Bongiwe

import math
a=2**(1/2)
b=2*(2/a)
while(a!=2):
    a=math.sqrt(2+a)
    b=b*(2/a)
    #a=math.sqrt(2+a)
a=round(b,3)
print("Approximation of pi:",a)
rad=eval(input("Enter the radius:\n"))
ro=rad**2
tree=ro*b
why=round(tree,3)
print("Area:",(why))

