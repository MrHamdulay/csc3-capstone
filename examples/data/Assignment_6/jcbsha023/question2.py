#program to do basic vector calculations
#Anthony Jacob
#24 April 2014

#getting the vector A and B from user
vector_A=input("Enter vector A:\n")
vector_B=input("Enter vector B:\n")
    
#addition of two vectors
def add_vector():
    A=vector_A.split(" ")
    B=vector_B.split(" ")
    
    list_add=[]
    for i in range(len(A)):
        list_add.append (eval(A[i])+eval(B[i]))
    print("A+B =",list_add)    
        
#function for dot product
def dot_product():
    A=vector_A.split(" ")
    B=vector_B.split(" ") 
    
    a=0
    for i in range (len(A)):
        a += eval(A[i])*eval(B[i])
    print("A.B =",a)    

#normalisation of A
def norm_A():
    import math
    A=vector_A.split(" ")
    
    norm = math.sqrt((eval(A[0])**2)+(eval(A[1])**2)+(eval(A[2])**2))
    roundA="%.2f"%norm
    print("|A| =",roundA)
    
#normalisation of B
def norm_B():
    import math
    B=vector_B.split(" ")
        
    norm = math.sqrt((eval(B[0])**2)+(eval(B[1])**2)+(eval(B[2])**2))
    roundB="%.2f"%norm
    print("|B| =",roundB)
       
            
#calling all the fuctions       
def main():
    add_vector()
    dot_product()
    norm_A()
    norm_B()
main()    