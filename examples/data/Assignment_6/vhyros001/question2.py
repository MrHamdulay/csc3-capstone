"""Assignment 6 question 2. Do basic vector algebra
Ross van der Heyde VHYROS001
20 April 2014"""

import math

#Add vectors
def add(a,b):
    r = []
    for i in range (3):
        r.append(int(a[i]) + int(b[i]))

    print("A+B = [",r[0], ", " , r[1], ", ", r[2],"]", sep ="")

#calculate dot product
def dot(a,b):
    r = 0
    for i in range (3):
        r += int(a[i]) * int(b[i])

    print("A.B =", r)    

#Normalize a vector
def norm (a):
    r = 0
    for i in range (3):
        r+= int(a[i])**2
        
    r =  math.sqrt(r)
    return round(r,2)
    

#A| = Sqrt(1^2 + 3^2 + 2^2) = Sqrt(1+9+4) = Sqrt(14) = 3.74


#MAIN
#Read in vectors
a = input("Enter vector A:\n").split()
b = input("Enter vector B:\n").split()

#call functions
add(a,b)
dot(a,b)

output = "{:.2f}" # format string
print("|A| =", output.format(norm(a)))
print("|B| =", output.format(norm(b)))

#Enter vector A:
#1 3 2
#Enter vector B:
#2 3 0
#A+B = [3, 6, 2]
#A.B = 11
#|A| = 3.74
#|B| = 3.61