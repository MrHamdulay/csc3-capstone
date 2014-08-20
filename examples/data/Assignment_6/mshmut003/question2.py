# Program to crunch vectors
# Mutali Mashamba
# 22 April 2014

import math

def vector_thinga():
    # Get sets of vectors from user
    first = input('Enter vector A:\n')
    second = input('Enter vector B:\n')
    
    # Split the string into a list
    a = first.split(' ')
    b = second.split(' ')
    
    # create empty lists
    new_a = []
    new_b = []
    
    # Change strings into integers and add them to respective epmty lists
    for i in a:
        new_a.append(eval(i))
    for j in b:
        new_b.append(eval(j))
    # Addition of vectors
    add = [new_a[0]+new_b[0],new_a[1]+new_b[1],new_a[2]+new_b[2]]
    
    # Multiplication of vectors
    mult = new_a[0]*new_b[0] + new_a[1]*new_b[1] + new_a[2]*new_b[2]
    
    # Absolute Value of  first vector i.t.o second one
    asb = (new_a[0]**2) + (new_a[1]**2) + (new_a[2]**2)
    cor_abs = round(math.sqrt(asb),2)
    if cor_abs == 0.0:
        cor_abs = '0.00'
    # Absolute value of second vector i.t.o first one
    bas = (new_b[0]**2) + (new_b[1]**2) + (new_b[2]**2)
    cor_bas = round(math.sqrt(bas),2)
    if cor_bas == 0.0:
        cor_bas = '0.00'
    
    # Print the Results
    print ('A+B =',add)
    print ("A.B =", mult)
    print ("|A| =",cor_abs)
    print ("|B| =",cor_bas)
    
    # Be Happy
vector_thinga()