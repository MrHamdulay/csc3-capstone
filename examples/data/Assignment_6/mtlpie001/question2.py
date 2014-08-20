#piet motalaota
import math 


def vectors():
    
    vector_A_request=input('Enter vector A:\n')
    vector_B_request=input('Enter vector B:\n')
    

    vector_A=vector_A_request.split(' ')
    vector_B=vector_B_request.split(' ')
    

    vector_sum=[]
    for i in range(3):
        sum_of_vectors=eval(vector_A[i])+eval(vector_B[i])
        vector_sum.append(sum_of_vectors)
    print('A+B =',vector_sum)
    
    
    A_B=0
    for i in range(3):
        product_of_vectors=eval(vector_A[i])*eval(vector_B[i])
        A_B+=product_of_vectors
    print('A.B =',A_B)
    
    
    norm_A= math.sqrt(eval(vector_A[0])**2+eval(vector_A[1])**2+eval(vector_A[2])**2)
    norm_B=math.sqrt(eval(vector_B[0])**2+eval(vector_B[1])**2+eval(vector_B[2])**2)
    
    print('%s = %.2F'%("|A|",norm_A))
    print('%s = %.2F'%("|B|",norm_B))
vectors()