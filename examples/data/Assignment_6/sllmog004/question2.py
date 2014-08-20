"""Assignment 6 Question 2
Yaseen Sulliman
20 April 2014"""

import math
A=[] # Creating empty array
B=[] # Creating empty array

vector_A=input("Enter vector A:\n").split(" ") # Obtain user input for vector A
# Convert into integers
x=int(vector_A[0])
y=int(vector_A[1])
z=int(vector_A[2])
A.append(x)
A.append(y)
A.append(z)

vector_B=input("Enter vector B:\n").split(" ") # Obtain user input for vector B
# Convert into integers
a=int(vector_B[0])
b=int(vector_B[1])
c=int(vector_B[2])
B.append(a)
B.append(b)
B.append(c)

addition = [x+a, y+b, z+c]
print("A+B =", addition)
AB=(x*a)+(y*b)+(z*c)
print("A.B =", AB)
A=round(math.sqrt((x**2)+(y**2)+(z**2)),2)
print("|A| =", "%2.2f"%A)
B=round(math.sqrt((a**2)+(b**2)+(c**2)),2)
print("|B| =", "%2.2f"%B)