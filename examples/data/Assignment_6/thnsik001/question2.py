"""Sikhulile Thenjwayo
  Assignment 6
  23 April 2014"""

#addition
def addition(a,b):
    vadd = [0,0,0]
    for i in range(3):
        vadd[i] = a[i]+b[i]
    print("A+B =",vadd)

#dot product
def dot(a,b):
    summ=0
    for i in range(3):
        summ += a[i]*b[i]
    print("A.B =",summ)

#normalization
def norm(a):
    
    summ=0
    for i in range(3):
        summ += a[i]**2
    return '{0:1.2f}'.format(summ**.5,2)

vectorA = (input("Enter vector A:\n")).split()
vectorB = (input("Enter vector B:\n")).split()
for i in range(3):
    vectorA[i] =eval(vectorA[i])
    vectorB[i] =eval(vectorB[i])
addition(vectorA,vectorB)
dot(vectorA,vectorB)
print("|A| =",norm(vectorA))
print("|B| =",norm(vectorB))
