#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     addition, dot product and normalization of vectors
#
# Author:      Matthias
#
# Created:     19-04-2014
# Copyright:   (c) Matthias 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import math

vectorA = input("Enter vector A: \n").split()
vectorB = input("Enter vector B: \n").split()

def addition(a,b):
    answer = []
    for i in range(3):
        # add the two values in the vectors and append to answer
        answer.append(eval(a[i]) + eval(b[i]))
    return answer

def dot_product(a,b):
    answer = 0
    for i in range(3):
        # multiply the two values in the vectors and add to answer
        answer += eval(a[i]) * eval(b[i])
    return answer

def normalization(a):
    answer = 0
    for i in range(3):
        # square each value of the vector and add to answer
        answer += eval(a[i])**2
    # take the squareroot of answer and round to two decimal places
    return "{0:0.2f}".format(math.sqrt(answer),2)

def main():
    print("A+B =", addition(vectorA,vectorB))
    print("A.B =", dot_product(vectorA,vectorB))
    print("|A| =", normalization(vectorA))
    print("|B| =", normalization(vectorB))

if __name__ == '__main__':
    main()
