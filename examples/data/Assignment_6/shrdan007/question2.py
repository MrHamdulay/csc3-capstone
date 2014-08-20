# Program to do basic vector calculations in three dimensions
# Danielle Sher

import math

x = input("Enter vector A:\n")
y = x.split()
w = input("Enter vector B:\n")
z = w.split()

add = [int(y[0])+ int(z[0]), int(y[1])+ int(z[1]), int(y[2])+ int(z[2])]
prod = int(y[0])*int(z[0]) + int(y[1])*int(z[1]) + int(y[2])*int(z[2])
normA = math.sqrt((float(y[0]))**2 + (float(y[1]))**2 + (float(y[2]))**2)
normB = math.sqrt((float(z[0]))**2 + (float(z[1]))**2 + (float(z[2]))**2)
if x != '0 0 0' and y  != '0 0 0':
    print("A+B =", add)
    print("A.B =", prod)
    print("|A| =", round(normA, 2))
    print("|B| =", round(normB, 2))


elif x == '0 0 0' and w == '0 0 0':
    print("A+B =", add)
    print("A.B =", prod)
    print("|A| = 0.00")
    print("|B| = 0.00")    







