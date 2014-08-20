#MTHKHI001
#Assignment 6
#Question 2

import math

# user input for vectorA
vectorA = (input("Enter vector A:\n"))
VectorAlpha = vectorA.split(" ")

#User input for VectorB
VectorB = (input("Enter vector B:\n"))
VectorBeta = VectorB.split(" ")

# used to change inputs in lists from strings to numbers
for i in range (3):
    VectorAlpha[i] = eval(VectorAlpha[i])
    VectorBeta[i] = eval(VectorBeta[i])

# used to produce the additions of Vector A and Vector B at their respective position, to form a new list
A_plus_B = []    
for j in range (3):
    addition = VectorAlpha[j] + VectorBeta[j]
    A_plus_B.append(addition)
print("A+B = " + str(A_plus_B))

# used to calculate addition of the two lists of corressponding points in the list and then produce the addition of these collective points
count = 0
for k in range (3):
    count = count + (VectorAlpha[k]*VectorBeta[k])    
print("A.B = " + str(count))

# used to produce a sqrt of lists A & B's, whereby the numbers in the list have been squared and added together, the output is then sqaure rooted to 2 decimal places.
countA = 0
countB = 0
for m in range (3):
    countA = countA + (VectorAlpha[m]**2)
    countB = countB + (VectorBeta[m]**2)
    
    # used to format the outputs to 2 decimal places, aswell as perform the square root
print("|A| = " + str("{0:.2f}".format((math.sqrt(countA)))))
print("|B| = " + str("{0:.2f}".format((math.sqrt(countB)))))
      