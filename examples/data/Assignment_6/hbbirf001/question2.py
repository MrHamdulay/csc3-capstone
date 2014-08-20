# Vector Calculations
# Irfan Habib
# 2014/04/23
import math
def main():
    
    v=input('Enter vector A:\n')
    vl= v.split(' ')
    A = [int(vl[0]),int(vl[1]),int(vl[2])]
    v=input('Enter vector B:\n')
    vl= v.split(' ') 
    B = [int(vl[0]),int(vl[1]),int(vl[2])]
    
    sumAB = [A[0] + B[0],A[1] + B[1],A[2] + B[2]]
    prodAB = (A[0] * B[0])+(A[1] * B[1])+(A[2] * B[2])
    normA = '{0:0.2f}'.format((A[0]**2 + A[1]**2 + A[2]**2)**0.5)
    normB = '{0:0.2f}'.format((B[0]**2 + B[1]**2 + B[2]**2)**0.5)
    print('A+B =',sumAB, sep = ' ')
    print('A.B =', prodAB, sep=' ')
    print('|A| = ' + str(normA))
    print('|B| = ' + str(normB))
main()        
        
    