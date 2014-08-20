'''Program to perfom vector calculations
Tinotenda Chevmura (CHMTIN004)
20 April 2014'''

#______________Program Starts Here__________________

import math #to use the sqrt function

#get the 2 vectos from the user
#convert them to lists

vecA = input("Enter vector A:\n")
vecB = input("Enter vector B:\n")
vecA = vecA.split()
vecB = vecB.split()

#add the 2 vectors

def vector_addition():
    i = eval(vecA[0]) + eval(vecB[0])
    j = eval(vecA[1]) + eval(vecB[1])
    k = eval(vecA[2]) + eval(vecB[2])
    vecAB = [i, j, k]
    print("A+B =", vecAB)

#find the dot product

def dot_product():
    i = eval(vecA[0]) * eval(vecB[0])
    j = eval(vecA[1]) * eval(vecB[1])
    k = eval(vecA[2]) * eval(vecB[2])
    vecAB = i+j+k
    print("A.B =", vecAB)    

#find magnitude of the vectors

def mag_A():
    i = eval(vecA[0])
    j = eval(vecA[1])
    k = eval(vecA[2])
    magA = math.sqrt((i**2)+(j**2)+(k**2))
    magA = round(magA,2)
    if i == 0 and  j == 0 and k == 0:
        print("|A| = 0.00")
    else:
        print("|A| =", magA)    
    
def mag_B():
    i = eval(vecB[0])
    j = eval(vecB[1])
    k = eval(vecB[2])
    magB = math.sqrt((i**2)+(j**2)+(k**2))
    magB = round(magB,2)
    if i == 0 and  j == 0 and k == 0:
        print("|B| = 0.00")
    else:
        print("|B| =", magB)    
    
vector_addition()
dot_product()
mag_A()
mag_B()