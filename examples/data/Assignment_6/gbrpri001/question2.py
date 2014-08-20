"""PRIYANKA GOBERDHAN
LIST - MATH FUNCTIONS
25/04/2014"""

import math

x=input("Enter vector A:\n")
y= input("Enter vector B:\n")

a = x.split()

b = y.split()
sum = [ ]
multi = 0
a_abs = 0 
b_abs = 0 

for num in range(len(a)):
    a[num] = eval(a[num])
    b[num] = eval(b[num])
    sum.append(a[num] + b[num])
    multi += (a[num]*b[num])
    a_abs += (a[num])**2
    b_abs += (b[num])**2
    
p = "{:.2f}".format(math.sqrt(a_abs))
q = "{:.2f}".format(math.sqrt(b_abs))
    
print ("A+B =", sum)
print ("A.B =", multi)
print("|A| =", p)
print("|B| =", q)