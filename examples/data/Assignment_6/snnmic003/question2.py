'''Basic Vector Calculations
Michael Sanne
2014/04/20'''

import math

#Receive input from the user and split it into the three components
vector1_str  = input("Enter vector A:\n")
vector1 = vector1_str.split (" ")
x1 = int (vector1[0])
y1 = int (vector1[1])
z1 = int (vector1[2])
vector2_str  = input("Enter vector B:\n")
vector2 = vector2_str.split (" ")
x2 = int (vector2[0])
y2 = int (vector2[1])
z2 = int (vector2[2])

#Prints A + B
print ("A+B = [" + str(x1+x2) + ", " + str(y1+y2) + ", " + str(z1+z2) + "]")

#Prints A . B
print ("A.B = " + str(x1*x2 + y1*y2 + z1*z2))
a = str(round(math.sqrt(x1**2 + y1**2 + z1**2), 2))
if a== "0.0":
    a+="0"
    
#Prints the absolute values of A and B
print ("|A| = " + (a))

       
b = str(round(math.sqrt(x2**2 + y2**2 + z2**2), 2))
if b == "0.0":
    b+="0"
print ("|B| = " + (b))