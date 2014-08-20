"""Question 2 - vector addition, dot product and norm
Jembe Moran
25 April 2014"""
a=input("Enter vector A:\n")
b=input("Enter vector B:\n")
a=a.split(" ")
b=b.split(" ")

def addition(a,b): #vector addition
    c=[]
    for i in range(len(b)):
        x=eval(a[i])+eval(b[i])
        c.append(x)
    print("A+B =", c)
    
def dot_product(a,b): #dot product
    c=0
    for i in range(len(b)): 
        x=eval(a[i])*eval(b[i]) #multiply corresponding
        c+=x
    print("A.B =", c)


import math    
def norm(a): 
    c=0
    for i in a:
        c+=eval(i)*eval(i)
    c=math.sqrt(c) #squareroot sum of all values, format to 2 decimal places
    c="{0:0.2f}".format(c)
    return c

addition(a,b)
dot_product(a,b)
print("|A| =", norm(a))
print("|B| =", norm(b))