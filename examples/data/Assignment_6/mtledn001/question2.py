'''The vectors thing
19 April 2014
Ednecia Matlapeng'''
import math
#Get the vectors
A = input('Enter vector A:\n').split(' ')
B=(input('Enter vector B:\n')).split(' ')
#convert them into ints
A[0],A[1],A[2]= eval(A[0]),eval(A[1]),eval(A[2])
B[0],B[1],B[2]= eval(B[0]),eval(B[1]),eval(B[2])
#print(A,B)

print('A+B = [',A[0]+B[0],', ',A[1]+B[1],', ',A[2]+B[2],']',sep="")
print('A.B = ',A[0]*B[0]+A[1]*B[1]+A[2]*B[2],sep="")
sqrA =round(math.sqrt(A[0]**2+A[1]**2+A[2]**2),2)
sqrB=round(math.sqrt(B[0]**2+B[1]**2+B[2]**2),2)
if sqrA==0.0 :
    sqrA='0.00'
if sqrB==0.0:
    sqrB='0.00'
print('|A| = ',sqrA,sep="")
print('|B| = ',sqrB,sep="")