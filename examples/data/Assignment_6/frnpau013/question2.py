"""sum, product and respective norms of two 3d vectors"""
import math

# getting vectors and converting list items from str to int
A = list(eval(input("Enter vector A:\n").replace(" ", ", ")))
B = list(eval(input("Enter vector B:\n").replace(" ", ", ")))

# defining functions that do operations on vectors
def sumAB(a, b):
    sumlist = []
    count = 0
    for i in a:
        i = i + b[count]
        count += 1
        sumlist.append(i)
    return sumlist

def productAB(a, b):
    product = 0
    count = 0
    for i in a:
        i = i * b[count]
        product += i
        count += 1
    return product

def normvector(x):
    squaresum = 0
    for i in x:
        i = (i)**2
        squaresum += i
    if squaresum != 0:
        norm = round(math.sqrt(squaresum), 2)
    else:
        norm = '0.00'
    return norm

# printing output
print("A+B =", sumAB(A, B))
print("A.B =", productAB(A, B))
print("|A| =", normvector(A))
print("|B| =", normvector(B))