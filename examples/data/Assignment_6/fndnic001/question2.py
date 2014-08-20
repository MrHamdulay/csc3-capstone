'''Vector calculator
nic findlay
21 april 2014'''

from math import *

vector_a = input('Enter vector A:\n') #entering vectors
vector_b = input('Enter vector B:\n')
vector_a = vector_a.split()
vector_b = vector_b.split()

add = []
for i in range(3):      #addition
    component = (eval(vector_a[i]) + eval(vector_b[i]))
    add.append(component)
print("A+B =", add)


dot_sum = 0
for i in range(3):        #dot product
    component = (eval(vector_a[i]) * eval(vector_b[i]))
    dot_sum += component
print("A.B =", dot_sum)

norm_a = sqrt((eval(vector_a[0]) * eval(vector_a[0])) + (eval(vector_a[1]) * eval(vector_a[1])) + (eval(vector_a[2]) * eval(vector_a[2]))) #working out |a|
if round(norm_a,2) == 0.0:
    print("|A| = 0.00")
else:
    print("|A| =", round(norm_a,2))

norm_b = sqrt((eval(vector_b[0]) * eval(vector_b[0])) + (eval(vector_b[1]) * eval(vector_b[1])) + (eval(vector_b[2]) * eval(vector_b[2])))  #working out |b|
if round(norm_b,2) == 0.0:
    print("|B| = 0.00")
else:
    print("|B| =", round(norm_b,2))
