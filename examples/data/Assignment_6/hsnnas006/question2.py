'''program to do basic vector calculations in 3 dimensions
nasreen hoosain
27/04/14'''

import math

#functon to add vectors
def add_vectors(vect_a, vect_b):
    add_vect = []
    for i in range(3):
        z = int(vect_a[i]) + int(vect_b[i])
        add_vect.append(z)
    return add_vect

#function to calculate dot product
def dot_product(vect_a, vect_b):
    dot = 0
    for j in range(3):
        prod = int(vect_a[j])*int(vect_b[j])
        dot = dot + prod
    return dot

#function to calculate norm
def norm(vect):
    w = 0
    for k in range(3):
        x = int(vect[k])**2
        w = w + x
        norm = round(math.sqrt(w), 2)
    return norm
    

if __name__=='__main__':
    #get vetors
    vect_a = input('Enter vector A:\n').split(' ')
    vect_b = input('Enter vector B:\n').split(' ')
    #call functions
    add =add_vectors(vect_a, vect_b)
    dot = dot_product(vect_a, vect_b)
    norm_a = norm(vect_a)
    norm_b = norm(vect_b)
    #print results with format
    a = "{0:^3}{1:^3}{2:<}"
    b = "{0:^3}{1:^3}{2:0<4}"
    print(a.format('A+B', '=', add))
    print(a.format('A.B', '=', dot))
    print(b.format('|A|', '=', norm_a))
    print(b.format('|B|', '=', norm_b))