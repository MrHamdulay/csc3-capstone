'''program for basic vector calc in 3dim
nicole henning
due: 24 april 2014'''

import math

vect_A_str = input("Enter vector A:\n")
vect_A = (vect_A_str.split(" ")) #for a list of strings  

vect_B_str = input("Enter vector B:\n")
vect_B = vect_B_str.split(" ") #for a list of strings

#could be made more efficient by combining lists
vect_A_B = [vect_A, vect_B]

#for sum (int each item)
def vect_sum():
    vect_sum = []
    num_A = int(vect_A[0])+int(vect_B[0]) #first in each list - sum
    vect_sum.append(num_A)
    num_B = int(vect_A[1])+int(vect_B[1]) #second position
    vect_sum.append(num_B)        
    num_C = int(vect_A[2])+int(vect_B[2]) #third
    vect_sum.append(num_C)
    print("A+B =", vect_sum)
    
#for dot product
def vect_dot_product():
    num_A = int(vect_A[0])*int(vect_B[0]) #first in each list - product
    num_B = int(vect_A[1])*int(vect_B[1]) #second position
    num_C = int(vect_A[2])*int(vect_B[2]) #third 
    total = num_A + num_B + num_C #sum of products
    print("A.B =", total)

#for normalisation
def vect_norm ():
    #for A
    squares_sum_A = int(vect_A[0])**2+int(vect_A[1])**2+int(vect_A[2])**2 #sum of square of each item
    norm_A = (math.sqrt(squares_sum_A)) #root sum
    print("|A| = {0:0.2f}".format(norm_A))
    
    #for B (same as A)
    squares_sum_B = int(vect_B[0])**2+int(vect_B[1])**2+int(vect_B[2])**2
    norm_B = (math.sqrt(squares_sum_B))
    print("|B| = {0:0.2f}".format(norm_B))

vect_sum()
vect_dot_product()
vect_norm()