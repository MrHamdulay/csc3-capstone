"""Program to add vectoers in lists
   Rivoningo Seweya
   23 April 2014"""
import math
#function to change vector a into a list
def vector_A():
    x=input("Enter vector A:\n")
    b=x.split(" ")
    return b
def vector_B():
    x=input("Enter vector B:\n")
    y=x.split(" ")
    return y
a=vector_A()
b=vector_B()
# function that finds A+B
def dot_product ():
    AB=[]
    for i in range(len(b)):
        d=(a[i])
        c=(b[i])
        f=int(d)+int(c)
        AB.append(f)
    print("A+B =",AB)
#Function that finds A.B
    A=[] 
    f=0
    for i in range(len(b)):
            d=(a[i])
            c=(b[i])
            g=int(d)*int(c)
            f+=g
    z=f
    print("A.B =",z) 
dot_product()
#Function that finds |A|
def norms():
    m=0
    for i in range(len(a)):
        d=int(a[i])
        s=d*d
        m+=s
    c=("{0:.2f}".format(math.sqrt(m)))
    print("|A| =",c)
# reverse that finds |A|
def norm():
    m=0
    for i in range(len(b)):
        c=int(b[i])
        x=c*c
        m+=x
    B=("{0:.2f}".format(math.sqrt(m)))
    print("|B| =",B) 
norms()
norm()