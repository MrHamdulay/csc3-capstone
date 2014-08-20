#program to do basic vector calculations in 3 dimensions
#Ethan Jackson  
#22 April

import math
#create empty list
vecA = []
vector_a = input('Enter vector A:\n').split()# splits list according to spaces in between
a = vecA + vector_a

vecB = []
vector_b = input('Enter vector B:\n').split()
b = vecB + vector_b #combines empty list with entered list

add = [eval(a[0]) + eval(b[0]), eval(a[1]) + eval(b[1]), eval(a[2]) + eval(b[2])]
#adds the vectors in the same position
multiply = (eval(a[0]))*(eval(b[0])) + (eval(a[1]))*(eval(b[1])) + (eval(a[2]))*(eval(b[2]))
#multiplies vectors in the same position
absolute_a = math.sqrt(eval(a[0])**2 + eval(a[1])**2 + eval(a[2])**2 )
#squares each number in the vector and then finds the square root of them when added together
abrnd_a = '{0:.{1}f}'.format(absolute_a, 2) #rounds previous answer to two decimal places
absolute_b = math.sqrt(eval(b[0])**2 + eval(b[1])**2 + eval(b[2])**2 )
abrnd_b = '{0:.{1}f}'.format(absolute_b, 2)

print("A+B =", add)
print("A.B =", multiply)
print("|A| =", abrnd_a)
print("|B| =", abrnd_b)
