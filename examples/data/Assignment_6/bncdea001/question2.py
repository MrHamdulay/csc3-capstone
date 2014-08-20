#Program to do vector things using arrays
#Dean Bunce
#21 April 2014

import math

def main():
    #Input Arrays
    
    vector_string_A=input("Enter vector A: \n")
    vectors_A=vector_string_A.split(" ")
    a, b, c=vectors_A[0], vectors_A[1], vectors_A[2]
    a, b, c=int(a), int(b), int(c)
    vector_a=[[a],[b],[c]]
    #print(vector_a)
    
    
    vector_string_B=input("Enter vector B: \n")
    vectors_B=vector_string_B.split(" ")
    d, e, f=vectors_B[0], vectors_B[1], vectors_B[2]
    d, e, f=int(d), int(e), int(f)
    vector_b=[[d],[e],[f]]
    #print(vector_b)
    
    #Adding Vectors
    vector_add=[a+d, b+e, c+f]
    print("A+B =", vector_add)
    
    #Dot multiplication
    mult1, mult2, mult3=a*d,b*e,c*f
    sum_mult=mult1+mult2+mult3
    print("A.B =", sum_mult)
    
    # Norm of each vector
    norm_A= math.sqrt(a**2+b**2+c**2)
    print("|A| =", "{0:.2f}".format(norm_A))
    norm_B= math.sqrt(d**2+e**2+f**2)
    print("|B| =", "{0:.2f}".format(norm_B))
    
    
    
    
    
    

main()