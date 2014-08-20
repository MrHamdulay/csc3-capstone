#Stephanie latchmanan
#assignment 6(basic vector calculations)
#20 April 2014

import math

#input the two vestors and create a 2d array
a = input("Enter vector A:\n")
vector_a=a.split(" ")
b = input("Enter vector B:\n")
vector_b=b.split(" ")

#work out and print addition of vectors
vector_addition=[]
for i in range(3):
    vector_addition.append(eval(vector_a[i]) + eval(vector_b[i]))
print("A+B =", vector_addition)

#work out and print dot multiplication of vectors
vector_multi=0
for i in range(3):
    x=eval(vector_a[i]) * eval(vector_b[i])
    vector_multi=vector_multi+x
print("A.B =", vector_multi)

#work out and print norm of vectors for A
norm_a=0
for i in range(3):
    x=(eval(vector_a[i]))**2
    norm_a=norm_a+x
print("|A| =", "{0:0<4}".format(round(math.sqrt(norm_a), 2)))

#work out and print norm of vectors for b
norm_b=0
for i in range(3):
    x=eval(vector_b[i])**2
    norm_b=norm_b+x
print("|B| =", "{0:0<4}".format(round(math.sqrt(norm_b), 2)))