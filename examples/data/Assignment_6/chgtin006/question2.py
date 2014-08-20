"""Program to add, multuiply,find modulus of two vectors
Tinashe Choga
25/04/2014"""
import math #as we shall use it in finding sqrt
A=input("Enter vector A:\n")
B=input("Enter vector B:\n")
a=A.split(" ")             #making list a
b=B.split(" ")  #making list b
sum=[(int(a[0])+int(b[0])),(int(a[1])+int(b[1])),(int(a[2])+int(b[2]))]
multiply=((int(a[0])*int(b[0]))+(int(a[1])*int(b[1]))+(int(a[2])*int(b[2])))
modA=((int(a[0]))**2+(int(a[1]))**2+(int(a[2]))**2)
modA1=math.sqrt(modA)
modB=((int(b[0]))**2+(int(b[1]))**2+(int(b[2]))**2)
modB1=math.sqrt(modB)
if int(a[0])==0 and int(a[1])==0 and int(a[2])==0 and int(b[0])==0 and int(b[1])==0 and int(b[2])==0:
    print("A+B =", sum)
    print("A.B =", multiply)
    print("|A| =","0.00")
    print("|B| =","0.00")
else:
    print("A+B =", sum)
    print("A.B =", multiply)
    print("|A| =", round(modA1,2))
    print("|B| =", round(modB1,2))    
