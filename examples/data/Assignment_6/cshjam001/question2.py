import math
A=input('Enter vector A:\n')
B=input('Enter vector B:\n')
A=A.split(' ')
B=B.split(' ')
A = [int(i) for i in A]
B = [int(i) for i in B]

    
   
print('A+B = [',A[0]+B[0],', ',A[1]+B[1],', ',A[2]+B[2],']',sep='')
print('A.B =',A[0]*B[0]+A[1]*B[1]+A[2]*B[2])
absA=round(math.sqrt((A[0])**2+(A[1])**2+(A[2])**2),2)
absB=round(math.sqrt((B[0])**2+(B[1])**2+(B[2])**2),2)
print('|A| = {0:0.2f}'.format(absA))
print('|B| = {0:0.2f}'.format(absB))


