#a program to do vector calculations in 3-D
#F.J.Chigwaza
#24-04-2014


import math
def vectors():
    
    a= input('Enter vector A:\n')
    b= input('Enter vector B:\n')
    
    A = a.split(' ')
    B = b.split(' ')
    
    add_vectors=[int(A[0])+int(B[0]),int(A[1])+int(B[1]),int(A[2])+int(B[2])]
    print('A+B =',add_vectors)
    multiply_vectors=int(A[0])*int(B[0])+int(A[1])*int(B[1])+int(A[2])*int(B[2])
    print('A.B =',multiply_vectors)
    mod_A=math.sqrt(int(A[0])**2 + (int(A[1]))**2 + (int(A[2]))**2)
    mod_A=round((mod_A),2)
    if mod_A ==0:
        print('|A| = 0.00')
    else:
        print('|A| =',mod_A)
    mod_B=math.sqrt(int(B[0])**2 + (int(B[1]))**2 + (int(B[2]))**2)
    mod_B=round((mod_B),2)
    if mod_B==0:
        print('|B| = 0.00')
    else:
        print('|B| =',mod_B)    
    
    
    

vectors()

    

    
    