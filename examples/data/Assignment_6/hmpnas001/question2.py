"""program that manipulates vectors
nasonkwe hampwaye
21.04.2014"""
import math
def vectors():
    #input vectors
    vector_A=input("Enter vector A:\n")
    vector_B=input("Enter vector B:\n")
    A=vector_A.split(" ")
    B=vector_B.split(" ")
    #evaluating lists
    A_vec=[]
    for n in range(len(A)):
        A[n]=eval(A[n])
        A_vec.append(A[n])
    B_vec=[]    
    for n in range(len(B)):
        B[n]=eval(B[n])
        B_vec.append(B[n])
   
        
     #adding   
    add_new=[A_vec[0]+B_vec[0],A_vec[1]+B_vec[1],A_vec[2]+B_vec[2]]
    print("A+B =",add_new)
    
    #multiplying
    multiply_new=(A_vec[0]*B_vec[0])+(A_vec[1]*B_vec[1])+(A_vec[2]*B_vec[2])
    print("A.B =",multiply_new)
    
    #magnitude of A
    mag_A=math.sqrt(A_vec[0]**2+A_vec[1]**2+A_vec[2]**2)
    print("|A| =",'{0:0.2f}'.format(mag_A))
    
    #magnitude of B
    mag_B=math.sqrt(B_vec[0]**2+B_vec[1]**2+B_vec[2]**2)
    print("|B| =",'{0:0.2f}'.format(mag_B))
    
    
    
    
vectors()    