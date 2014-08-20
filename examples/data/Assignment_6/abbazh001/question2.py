#Azhar Aboobaker
#ABBAZH001
#23/04/2014

import math

def vector(x):
    y=[]
    print("Enter vector ", x, ":", sep="")
    a=input()
    a=a.split(" ")
    for i in a:
        y.append(eval(i))
    return y

def addvector(x, a):
    y=[]
    for i in range(3):
        y.append(x[i]+a[i])
    return y

def dotproduct(x, a):
    y=0
    for i in range(3):
        y+=x[i]*a[i]
    return y

def norm(x):
    y=0.00
    for i in range(3):
        y+=x[i]**2
    if y==0:
        y="0.00"
    elif y!=0:
        y=(round(math.sqrt(y), 2))
    return y

def output():
    c=vector("A")
    d=vector("B")
    print("A+B =", addvector(c, d))
    print("A.B =", dotproduct(c, d))
    print("|A| =", norm(c))
    print("|B| =", norm(d))
    
output()