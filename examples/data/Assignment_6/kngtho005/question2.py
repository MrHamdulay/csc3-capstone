# question2.py
# a program to do basic vector calculations in 3 dimensions:
#   addition, dot product and normalization
# Thomas Konigkramer
# 20 April 2014

import math

a = input("Enter vector A:\n")
b = input("Enter vector B:\n")

total = [a.split(" ")] + [b.split(" ")]

# converting strings in list to numbers
for i in range(3): # since total of 3 numbers in each list inside of total list
    total[0][i] = eval(total[0][i])
    total[1][i] = eval(total[1][i])

# addition
addition = []
for j in range(3):
    addition += [total[0][j] + total[1][j]]

# dot product
dot = 0
for k in range(3):
    dot += total[0][k] * total[1][k]

# normalization
# for A:
a = 0
for l in range(3):
    a += total[0][l]**2
a = math.sqrt(a)
# for B:
b = 0
for m in range(3):
    b += total[1][m]**2
b = math.sqrt(b)

# print output
print("A+B =", addition)
print("A.B =", dot)
print("|A| = %.2f" % a)
print("|B| = %.2f" % b)