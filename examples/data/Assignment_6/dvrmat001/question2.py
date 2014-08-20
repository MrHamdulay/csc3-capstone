"""basic vector calculations in 3 dimensions: addition, dot product, and normalization
23 April 2014
yuan-yow wu"""
import math

a=input("Enter vector A: \n")
a=a.split()

b=input("Enter vector B: \n")
b=b.split()
 

print("A+B",end=" ")
numbers=[]
for i in range (3):
    y = eval(a[i]) + eval(b[i])
    numbers.append(y)
print("=",numbers)

print("A.B",end=" ")
product = 0
for i in range (3):
    y = eval(a[i]) * eval(b[i])
    product += y
print("=",product)

print("|A|",end="")
absoluteA=0
for i in range (3):
    squareA = (eval(a[i]))**2
    absoluteA += squareA
print(" =","%.2f" %round(math.sqrt(absoluteA),2))

print("|B|",end="")
absoluteB=0
for i in range (3):
    squareB = (eval(b[i]))**2
    absoluteB += squareB
print(" =","%.2f" %round(math.sqrt(absoluteB),2))

