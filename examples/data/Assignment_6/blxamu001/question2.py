""" Program to do basic vector calculations
Aubrey Baloi
16 April 2014"""

import math

def add_vectors(a,b):
    X = []
    
    for i in range(3):
        X.append(a[i] + b[i])
    return X
        
def multi_vectors(c,d):
    Y = 0
    
    for i in range(3):
        a = c[i]*d[i]
        Y += a
    return Y

def A_nom(e):
    Z = 0
    
    for i in range(3):
        b = e[i]**2
        Z += b
        
    return math.sqrt(Z)

def B_nom(f):
    D = 0
    
    for i in range(3):
        b = f[i]**2
        D += b
        
    return math.sqrt(D)

def vectors():
    # make an empty list for A and B
    A = []
    valuesA = (input('Enter vector A:\n'))
    A = valuesA.split()
    
    for i in range(3):
        A[i] = eval(A[i])
        
    B = []
    valuesB = (input('Enter vector B:\n'))
    B = valuesB.split()    
    
    for i in range(3):
        B[i] = eval(B[i])
        
    
    
    print('A+B =',add_vectors(A,B))
    print('A.B =',multi_vectors(A,B))
    print('|A| =',"{0:.2f}".format(A_nom(A))) # wow! round off is quite complex
    print('|B| =',"{0:.2f}".format(B_nom(B)))
    
    
vectors()
