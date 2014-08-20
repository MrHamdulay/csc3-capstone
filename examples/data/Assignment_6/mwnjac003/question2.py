# program to do calculations on vectors
# by Jacob Mwanza
# 24/04/2014

import math
# enter vectors
def entry():
    Vector_A = input('Enter vector A:\n')
    A = Vector_A.split(' ')
    Vector_B = input('Enter vector B:\n')
    B = Vector_B.split(' ')
    Ans = [0,0,0]
    
    # add vectors
    for i in range (len(A)):
        Ans[i] = (int(A[i]) + int(B[i]))
    print('A+B =',Ans)
    
    # find dot product
    for i in range(len(A)):
        Ans[i] = (int(A[i]) * int(B[i]))
    print('A.B =',(int(Ans[0]) + int(Ans[1]) +int(Ans[2])))
    
    # find |A| and |B|
    formatted_data = ('{0:3.2f}')
    for i in range(len(A)):
        x = (int(A[0])*int(A[0]) + int(A[1])*int(A[1]) + int(A[2])*int(A[2]))
    print('|A| =',(formatted_data.format(math.sqrt(x))))  
    
    for i in range(len(A)):
        y = (int(B[0])*int(B[0]) + int(B[1])*int(B[1]) + int(B[2])*int(B[2]))
    print('|B| =',(formatted_data.format(math.sqrt(y))))
        
entry()