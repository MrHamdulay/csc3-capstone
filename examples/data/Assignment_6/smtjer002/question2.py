"""a program to calculate the addition, dot product and normalization of 3 dimensional vectors
by Jeremy Smith
21 April 2014"""

import math

#input series of vectors separated by a space
vector_a = input("Enter vector A:\n")
vector_b = input("Enter vector B:\n")

#split the vectors into a list and convert the strings to integers
a_list = vector_a.split(" ")
for a in range(len(a_list)):
    a_list[a] = eval(a_list[a])

b_list = vector_b.split(" ")
for b in range(len(b_list)):
    b_list[b] = eval(b_list[b])
    
#calculate the addition, dot product and normalization of the vectors
addition = [a_list[0] + b_list[0], a_list[1] + b_list[1], a_list[2] + b_list[2]]
dot_product = a_list[0] * b_list[0] + a_list[1] * b_list[1] +  a_list[2] * b_list[2]
a_normalization = math.sqrt(a_list[0]**2 + a_list[1]**2 + a_list[2]**2)
b_normalization = math.sqrt(b_list[0]**2 + b_list[1]**2 + b_list[2]**2)

#print the answers
print("A+B =", addition)
print("A.B =", dot_product)
print("|A| =", '{0:.2f}'.format(a_normalization))
print("|B| =", '{0:.2f}'.format(b_normalization))