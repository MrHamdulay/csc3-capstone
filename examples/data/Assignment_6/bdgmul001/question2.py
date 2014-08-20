# program to do basic vector calculations in 3 dimensions: addition, dot product and normalization.
# Mulisa Badugela
# 20 April 2014
import math
def main():
    A = []
    B = []                                  # two empty vectors
    
    vectorA = input('Enter vector A:\n')    # user input for vector A
    vectorB = input('Enter vector B:\n')    # user input for vector B
    
    for i in vectorA.split():
        A.append(eval(i))                   # convert each entered vector into an integer
    for i in vectorB.split():
        B.append(eval(i))                   # convert each entered vector into an integer
     
    w=[A[0]+B[0],A[1]+B[1],A[2]+B[2]]       # adding components from each vector by accessing each component from its vector
    x=A[0]*B[0]+A[1]*B[1]+A[2]*B[2]         # multipying components form each vector and adding them
    y=math.sqrt(A[0]**2+A[1]**2+A[2]**2)    # magnitude of vector A
    z=math.sqrt(B[0]**2+B[1]**2+B[2]**2)    # magnitude of vector B
    
    print('A+B =',w)
    print('A.B =',x)
    print('|A| =',"{:.2f}".format(y))             # round magnitude of vector A to two decimal places
    print('|B| =',"{:.2f}".format(z))             # round magnitude of vector B to two decimal places
    
main()