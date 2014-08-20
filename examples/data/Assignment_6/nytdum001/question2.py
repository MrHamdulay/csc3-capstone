"""Program to do basic vector calculations in 3 dimensions
Dumisani J Nyathi
23-04-2014"""

import math#import the math library
def vectors(a,b):

#funtion to add given input to the list
    get_vec=[]
    for i in range(3):
        get_vec.append(a[i]+b[i])
    return get_vec

#function for dot product   
def product(a,b):
    
    product=0
    for i in range(3):
        product=product+(a[i]*b[i])
    return product

#function to find the length of the vector 
def modulus(x):
    
    mod=math.sqrt(x[0]**2+x[1]**2+x[2]**2)
    return mod

#now outside of functions will use all functions defined 
a=input("Enter vector A:\n")
b=input("Enter vector B:\n")

a=a.split()
b=b.split()
for i in range(3):
    a[i]=eval(a[i])
    b[i]=eval(b[i])

print ("A+B =",vectors(a,b))
print ("A.B =",product(a,b))
print ("|A| =","{:.2f}".format(modulus(a)))
print ("|B| =","{:.2f}".format(modulus(b)))