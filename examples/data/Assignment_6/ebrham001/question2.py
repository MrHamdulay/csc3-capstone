'''Program that does basic vector calculations
HAMZA EBRAHIM
25/04/14'''

# import math function

import math

# Prompt user for vector inputs

A = input("Enter vector A:\n")
B = input("Enter vector B:\n")

vectors = A + " " + B
vectors=vectors.split(' ')

# define vector function

def vector():
    x = 0
    y = 3
    sum = []
    for i in range(3):
        A = int(vectors[x])
        B = int(vectors[y])
        number=((A) + (B))
        sum.append(number)
        x = x + 1
        y = y + 1
    print("A+B =", sum)
    
#define dot product function    
    
def product():
    m = 0
    n = 3
    c = 0
    for i in range(3):
        A = vectors[m]
        B = vectors[n]
        product=int(A)*int(B)
        m = m + 1
        n = n + 1
        c = c + product
    print("A.B =", c)

# define f1 function

def f1():
    begin = 0
    e = 0
    for i in range(3):
        sqr = int(vectors[begin])**(2)
        begin = begin + 1
        e = e + sqr
    s = math.sqrt(e)
    print("|A| =", '{0:.2f}'.format(round(s,2)))

# define f2 function    

def f2():
    begin = 3
    e = 0
    for i in range(3):
        sqr= int(vectors[begin])**(2)
        begin = begin + 1
        e = e + sqr
    s = math.sqrt(e)
    print("|B| =", '{0:.2f}'.format(round(s,2)))
    
vector()
product()
f1()
f2()

# program ends