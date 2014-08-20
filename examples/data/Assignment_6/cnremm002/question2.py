"""Vector math
Emmanuel Conradie
25 April 2014"""

import math

#Enter vectors
v1 = input("Enter vector A:\n")
v2 = input("Enter vector B:\n")
vector1 = v1.split()
vector2 = v2.split()

#vector calculations
AB1 = (int(v1[0]) + int(v2[0]))
AB2 = (int(v1[2]) + int(v2[2]))
AB3 = (int(v1[4]) + int(v2[4]))
print ("A+B = [",AB1, ", " ,AB2, ", " ,AB3, "]", sep = "")

AB11 = (int(v1[0])*int(v2[0]))
AB22 = (int(v1[2])*int(v2[2]))
AB33 = (int(v1[4])*int(v2[4]))
AB4 = AB11 + AB22 + AB33
print ("A.B =", AB4)

A1 = (int(v1[0])**2)
A2 = (int(v1[2])**2)
A3 = (int(v1[4])**2)
A4 = math.sqrt(A1 + A2 + A3)
print ("|A| =" , "{0:.2f}".format(A4))

B1 = (int(v2[0])**2)
B2 = (int(v2[2])**2)
B3 = (int(v2[4])**2)
B4 = math.sqrt(B1 + B2 + B3)
print ("|B| =" , "{0:.2f}".format(B4))