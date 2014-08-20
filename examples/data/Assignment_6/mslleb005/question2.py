#a program to do basic vector calculations
# Lebogang masila
# 20 April 2014

import math # to use for sqrt
c=[]
A=input("Enter vector A:\n").split()
B=input("Enter vector B:\n").split()
d=A[0] #first index from the 1st list
d=int(d)
e=B[0] #first index from the second list
e=int(e)
f= d + e
c.append(f) #add to list c


second=A[1]
integer=int(second)
second_B=B[1]
Integer=int(second_B)
g=integer+Integer
c.append(g)


third=A[2]
integ=int(third)
third_B=B[2]
Integ=int(third_B)
h=integ+Integ
c.append(h)
print("A+B =",c)

multiple=d*e
multiple2=integer*Integer
multiple3=integ* Integ
product=multiple + multiple2 + multiple3
print("A.B =",product)

expo=d**2
expo2=integer**2
expo3=integ**2
sqrt=expo+expo2+expo3
sqrt=math.sqrt(sqrt)
print("|A| = {0:0.2f}".format(sqrt))

exponent=e**2
exponent2=Integer**2
exponent3=Integ**2
sqrt=exponent+exponent2+exponent3
sqrt=math.sqrt(sqrt)
print("|B| = {0:0.2f}".format(sqrt))


