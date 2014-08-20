''' This programm do the basic vector calculations in 3 dimensions
Nxumalo Goodman
21 April 2014'''

import math

def vectors():
 
    #prompt user to enter vector a and vector b
    vector_a = input("Enter vector A:\n")
    vector_b = input("Enter vector B:\n")
    
    vector_a = vector_a.split(" ")
    vector_b = vector_b.split(" ")
      

    #sum up each value with it correspondence
    sum_x = eval(vector_a[0]) + eval(vector_b[0])
    sum_y = eval(vector_a[1]) + eval(vector_b[1])
    sum_z = eval(vector_a[2]) + eval(vector_b[2])
    
    #multiply each value with it correspondence
    product_x = eval(vector_a[0]) * eval(vector_b[0])
    product_y = eval(vector_a[1]) * eval(vector_b[1])
    product_z = eval(vector_a[2]) * eval(vector_b[2])
    
    #sum up vector_a and vector_b
    product_all = product_x + product_y + product_z
    
    #calculates magnitude of vector A and vector B
    mag_A = math.sqrt((eval(vector_a[0])**2) + (eval(vector_a[1])**2) + (eval(vector_a[2])**2))
    mag_B = math.sqrt((eval(vector_b[0])**2) + (eval(vector_b[1])**2) + (eval(vector_b[2])**2))
    
    print("A+B = [",sum_x,", ",sum_y,", ",sum_z,"]",sep="")
    print("A.B =",product_all)
    if mag_A == 0 and mag_B == 0 :
        print("|A| = 0.00")
        print("|B| = 0.00")
    else:
        print("|A| =",round((mag_A),2))
        print("|B| =",round((mag_B),2))
    
    
vectors()