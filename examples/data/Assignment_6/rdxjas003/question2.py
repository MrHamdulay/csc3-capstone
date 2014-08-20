import math
vecA = input('Enter vector A:\n')
A = vecA.split(' ')
vecB = input('Enter vector B:\n')
B = vecB.split(' ')
AplusB = [eval(A[0])+eval(B[0]),eval(A[1])+eval(B[1]),eval(A[2])+eval(B[2])]
print('A+B =',AplusB)
AtimesB =(eval(A[0])*eval(B[0]))+(eval(A[1])*eval(B[1]))+(eval(A[2])*eval(B[2]))
print('A.B = '+str(AtimesB))
rootA = math.sqrt(eval(A[0])**2 + eval(A[1])**2 + eval(A[2])**2)
print('|A| = '+str(format((rootA),'.2f')))
rootB = math.sqrt(eval(B[0])**2 + eval(B[1])**2 + eval(B[2])**2)
print('|B| = '+str(format((rootB),'.2f')))