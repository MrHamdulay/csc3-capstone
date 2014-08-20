"""program that calculates values for vectors"""

from math import sqrt

vA = input("Enter vector A:\n")
a, b, c = vA.split(" ")
a=eval(a)
b=eval(b)
c=eval(c)


vB = input("Enter vector B:\n")
d, e, f = vB.split(" ")

d=eval(d)
e=eval(e)
f=eval(f)


print("A+B = [" , a+d , ", " , b+e , ", " ,  c+f ,"]", sep ="")
print("A.B =", a*d + b*e + c*f)



print("|A| =", "%.2f" % sqrt(((a**2)+(b**2)+(c**2))))
print("|B| =", "%.2f" % sqrt(d**2+e**2+f**2))