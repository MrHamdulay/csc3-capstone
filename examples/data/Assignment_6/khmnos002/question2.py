"""program that does basic vector calculations in 3-D
nosipho khumalo
19 April 2014"""

import math
def main():
    #creating vectors
    vectorA = input("Enter vector A: \n")
    vectorB = input("Enter vector B: \n")
    vectorA = vectorA.split(" ")
    vectorB = vectorB.split(" ")
    
    #addition of vectors
    sum = []
    for i in range(3):
        sum.append(int(vectorA[i]) + int(vectorB[i]))

    #dot product of corresponding elements
    dotprod = 0
    for i in range(3):
        dotprod += int(vectorA[i]) * int(vectorB[i])
    
    #norm of vector A
    norm_A = 0
    for i in range(3):
        norm_A += int(vectorA[i]) ** 2
    norm_A = math.sqrt(norm_A)
    
    #norm of vector B
    norm_B = 0
    for i in range(3):
        norm_B += int(vectorB[i]) ** 2
    norm_B = math.sqrt(norm_B)
    
    #printing answers to calculations
    print("A+B =", sum)
    print("A.B =", dotprod)
    print("|A| =", "{0:0.2f}".format(norm_A))
    print("|B| =", "{0:0.2f}".format(norm_B,))
main()     