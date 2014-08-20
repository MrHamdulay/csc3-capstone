#Program to do basic vector calculations in 3 dimensions: addition, dot product and normalization.
#21/04/2014
#Gordon Skhosana

import math

def vectors():
    """Function that collects vector inputs from user"""
    global vec_A
    global vec_B
    vector_a=input("Enter vector A:\n")
    vector_b=input("Enter vector B:\n")
    vecA=vector_a.split(" ")
    vecB=vector_b.split(" ")
    #Converting entries to integers
    #Vector A
    vec_A=[]
    for i in vecA:
        j=int(i)
        vec_A.append(j)
    #Vector B
    vec_B=[]
    for i in vecB:
        j=int(i)
        vec_B.append(j)
def addition():
    """Function that adds vectors"""
    global vecA_vecB
    vecA_vecB=[vec_A[0]+vec_B[0],vec_A[1]+vec_B[1],vec_A[2]+vec_B[2]]
    
def dot_product():
    """Function that gets the dot product of two vectors"""
    global vecA_dot_vecB
    vecA_dot_vecB_list=[vec_A[0]*vec_B[0]+vec_A[1]*vec_B[1]+vec_A[2]*vec_B[2]]
    vecA_dot_vecB=vecA_dot_vecB_list[0]

def normalisation():
    """Function that finds the norm of a single vector"""
    global vecA_norm
    global vecB_norm
    vec_A_norm=math.sqrt(vec_A[0]**2+vec_A[1]**2+vec_A[2]**2)
    vec_B_norm=math.sqrt(vec_B[0]**2+vec_B[1]**2+vec_B[2]**2)
    vecA_norm="{0:.2f}".format(vec_A_norm)
    vecB_norm="{0:.2f}".format(vec_B_norm)  
def main():
    """Function that adds, calculates the dot product and norm of two vectors"""
    vectors()
    addition()
    dot_product()
    normalisation()
    print("A+B =",vecA_vecB)
    print("A.B =",vecA_dot_vecB)
    print("|A| =",vecA_norm)
    print("|B| =",vecB_norm)
main()