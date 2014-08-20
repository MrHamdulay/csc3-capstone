#A program that does basic vector caclulations in 3D
#Done by Portia Buthelezi

#Get the values and create a list
x= input('Enter vector A:\n')
A= x.split(' ')
y= input('Enter vector B:\n')
B= y.split(' ')

#The addition part
c= [ int(A[0]) + int(B[0]), int(A[1]) + int(B[1]), int(A[2]) + int(B[2])]
print( 'A+B =',c)

#The dot products part
d= int(A[0])*int(B[0]) + int(A[1])*int(B[1]) + int(A[2])*int(B[2])
print ('A.B =',d)

#The norm part for A
import math
e_a= math.sqrt((int(A[0]))**2 + (int(A[1]))**2 + (int(A[2]))**2)
#print('|A| =',round(e_a,2))
print('|A| =','{0:.2f}'.format(e_a))
#The norm part for B
e_b= math.sqrt((int(B[0]))**2 + (int(B[1]))**2 + (int(B[2]))**2)
#print('|B| =',round(e_b,2))
print('|B| =','{0:.2f}'.format(e_b))
