# A program that can do simple vector calculations
# Wongwa Giqwa
# 23 April 2014

import math


    
vector_A = input('Enter vector A:\n')
a = vector_A.split(' ') # create list for first vector 
vector_B = input('Enter vector B:\n')
b = vector_B.split(' ') # create list for second vector

# create a function for adding vectors
def addition():
    
    # add each component as integers and name them diff. variables
    x = int(a[0]) + int(b[0])
    y = int(a[1]) + int(b[1])
    z = int(a[2]) + int(b[2])
    print('A+B = ['+str(x)+', '+str(y)+', '+str(z)+']') # print the as strings
 
# create a function for multiplying vectors   
def dot_product():
    
    # multiply each component as integers, name them variables
    x = int(a[0])*int(b[0])
    y = int(a[1])*int(b[1])
    z = int(a[2])*int(b[2])
    dot_product = x+y+z
    print('A.B = '+str(dot_product))

# create a function for finding magnitude of each vector
def norm():
    
    # multiply each component of vector by itself
    x = (int(a[0]))**2
    y = (int(a[1]))**2
    z = (int(a[2]))**2
    norm = x+y+z
    norm_1 = (math.sqrt(norm))
    print('|A| = {0:.2f}'.format(norm_1)) # format answer to two decimal places 
    
    xx = (int(b[0]))**2
    yy = (int(b[1]))**2
    zz = (int(b[2]))**2
    mron = (xx)+(yy)+(zz)
    norm_2 = (math.sqrt(mron))
    print('|B| = {0:.2f}'.format(norm_2))

addition()
dot_product()
norm()
    
    

    
    
    

    
    







