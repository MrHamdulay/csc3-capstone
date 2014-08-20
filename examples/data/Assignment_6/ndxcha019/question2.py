#luke naude
#program to work with vectors
#14-4-23

#get vectors a and b
GetVector_A = input('Enter vector A:\n')
GetVector_B = input('Enter vector B:\n')

#turn them into strings
Vector_A = GetVector_A.split(' ')
Vector_B = GetVector_B.split(' ')

def Adding_Vectors():
    '''a function to get the sum of two vectors'''
    print('A+B = [',eval(Vector_A[0])+eval(Vector_B[0]),', ',eval(Vector_A[1])+eval(Vector_B[1]),', ',eval(Vector_A[2])+eval(Vector_B[2]),']',sep='')


def Dot_Product():
    '''A function to find the dot product of two vectors'''
    print('A.B = ',eval(Vector_A[0])*eval(Vector_B[0])+eval(Vector_A[1])*eval(Vector_B[1])+eval(Vector_A[2])*eval(Vector_B[2]),sep='')


import math #so that math.sqrt can be used

#variable to store the rounded magnitude A and B
round_A=round((math.sqrt(eval(Vector_A[0])**2+eval(Vector_A[1])**2+eval(Vector_A[2])**2)),2)
round_B=round((math.sqrt(eval(Vector_B[0])**2+eval(Vector_B[1])**2+eval(Vector_B[2])**2)),2)

if round_A==0.0:
    round_A='0.00'
if round_B==0.0:
    round_B='0.00'



def normative_value():
    '''a function to find the normative value of a vector'''
    print('|A| = ',round_A,sep='')
    print('|B| = ',round_B,sep='')
    
Adding_Vectors()
Dot_Product()
normative_value()