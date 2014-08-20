# This programs computes vector arithmetic
# Given A=(1, 3, 2) and B=(2, 3, 0), then

# A+B = (1+2, 3+3, 2+0) = (3, 6, 2)
# A.B = 1.2 + 3.3 + 2.0 = 2 + 9 = 11
# |A| = Sqrt(1^2 + 3^2 + 2^2) = Sqrt(1+9+4) = Sqrt(14) = 3.74
# |B| = Sqrt(2^2 + 3^2 + 0^2) = Sqrt(4+9+0) = Sqrt(13) = 3.61
# Student Name: Simeon Nandjembo

# Student Number: NNDSIM001

# 22 April 2014

import math

# Create the two vectors A and B
A = input("Enter vector A:\n").split(" ")
B = input("Enter vector B:\n").split(" ")

# This functions does the vector addition
def add(a,b):
    #create local variables
    a,b = a,b
    added = []    
    # for loop does the addition
    for i in range(len(a)):
        added.append(int(a[i]) + int(b[i]))    
    return added

# This functions does the vector dot multiplication
def dot(a,b):
    #create local variables
    a,b = a,b
    multi = 0    
    # for loop does the dot multiplication
    for i in range(len(a)):
        multi += int(a[i]) * int(b[i])    
    return multi

# This functions does the vector normalization
def norm(a):
    #create local variables
    a = a
    squared = 0    
    # for loop add the squares of each element in the vector
    for i in range(len(a)):
        squared += int(a[i])**2
    return math.sqrt(squared)

def main():
    print("A+B = {0}".format(add(A,B)))
    print("A.B = {0}".format(dot(A,B)))
    print("|A| = {0:.2f}".format(norm(A)))
    print("|B| = {0:.2f}".format(norm(B)))

if __name__ == "__main__":
    main()
    
#Sample I/O:

#Enter vector A:
#1 3 2
#Enter vector B:
#2 3 0
#A+B = [3, 6, 2]
#A.B = 11
#|A| = 3.74
#|B| = 3.61