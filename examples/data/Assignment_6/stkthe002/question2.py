#STKTHE002, Thea Sitek
#10.05.2014
#Div math applications to vectors

#add A and B
def pluss(A,B):
    #vector = [0,0,0]
    vector = []
    for i in range(len(A)):
        #vector[i] = eval(A[i])+eval(B[i])
        value = (eval(A[i])+eval(B[i]))
        vector.append(value)
    return vector

#dot product of A and B 
def dot(A,B):
    dotprod = 0
    vector = [0,0,0]
    for i in range(len(A)):
        vector[i] = eval(A[i])*eval(B[i])
        dotprod += vector[i]
    return dotprod

import math 

#normalize vector 
def norm(vector):
    value = 0
    for i in range(len(vector)):
        vector[i] = eval(vector[i])
        value += (vector[i])**2
    root = (math.sqrt(value))
    return root

#input
veca = input('Enter vector A: \n')
vecb = input('Enter vector B: \n')

#crate list from input
veca = veca.split(' ')
vecb = vecb.split(' ')

#call functions
print('A+B =', pluss(veca,vecb))
print('A.B =', dot(veca,vecb))
print('|A| =', "%.2f" %norm(veca))
print('|B| =', "%.2f" %norm(vecb))