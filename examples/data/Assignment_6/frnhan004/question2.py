"""Question 2-Assignment 6
FRNHAN004
24 April 2014"""

import math
vector_a=input("Enter vector A:\n")
vector_b=input("Enter vector B:\n")

#split input 
split_a=vector_a.split() 
split_b=vector_b.split()

#addition
a=int(split_a[0])+int(split_b[0])
b=int(split_a[1])+int(split_b[1])
c=int(split_a[2])+int(split_b[2])
addition=[a, b, c]
print("A+B = ",addition, sep='')

#dot product
d=int(split_a[0])*int(split_b[0])
e=int(split_a[1])*int(split_b[1])
f=int(split_a[2])*int(split_b[2])
dot_product=d+e+f
print("A.B = ",dot_product, sep='')

#normalization A
g=int(split_a[0])**(2)
h=int(split_a[1])**(2)
i=int(split_a[2])**(2)
normal_a=math.sqrt((g)+(h)+(i))
dec_a=("{:.2f}".format(normal_a))
print("|A| = ",dec_a, sep='')

#normalization B
j=int(split_b[0])**(2)
k=int(split_b[1])**(2)
l=int(split_b[2])**(2)
normal_b=math.sqrt(j+k+l)
dec_b=("{:.2f}".format(normal_b))
print("|B| = ",dec_b, sep='')
