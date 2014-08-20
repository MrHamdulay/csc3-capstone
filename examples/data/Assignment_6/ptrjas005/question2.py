'''Jason Pietersen'''
import math
A= input('Enter vector A:\n').split(' ')

B= input('Enter vector B:\n').split(' ')
form= '{0:0<4}'
additionvector= [0,0,0]
dotproduct= 0
magnitudeA=0
magnitudeB=0
for i in range(3):
   A[i]= eval(A[i])
   B[i]= eval(B[i])
   additionvector[i]=A[i]+B[i]
#dotproduct
   dotproduct +=A[i]*B[i]
#magnitudeA
   magnitudeA+=(A[i]**2)
#magnitudeB
   magnitudeB+=(B[i]**2)
print('A+B =',additionvector)
print('A.B =',dotproduct)
print('|A| =',form.format(round(math.sqrt(magnitudeA),2)))
print('|B| =',form.format(round(math.sqrt(magnitudeB),2)))
