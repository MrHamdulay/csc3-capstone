# Matthew Finlayson - FNLMAT001 
# Assignment 6 question 2
# 22/04/14

import math

# adds each corresponding element and returns a list of the new elements
def addition(vectorA, vectorB):
    output = []
    for i in range(3):
        output.append(int(vectorA[i])+int(vectorB[i]))
    return output

# calculates and returns the sum of the products of corresponding elements
def dotProduct(vectorA, vectorB):
    tot = 0
    for i in range(3):
        tot += int(vectorA[i])*int(vectorB[i])
    return tot    

# calculates and returns the square root of the sum of the squares of the elements
def norm(vector):
    tot = 0
    for i in range(3):
        tot += int(vector[i])*int(vector[i])
    return round(math.sqrt(tot), 2)

def main():
    a = input("Enter vector A:\n")
    vA = a.split(" ")
    b = input("Enter vector B:\n")
    vB = b.split(" ")
    
    addList = addition(vA, vB)
    print("A+B = " + "[" + str(addList[0]) + ", " + str(addList[1]) + ", " + str(addList[2]) + "]" )
    
    print("A.B =", dotProduct(vA, vB))
          
    print("|A| =", "{0:0.2f}".format(norm(vA))) # formats the output so that it always has two decimal places
    print("|B| =", "{0:0.2f}".format(norm(vB)))

if __name__ == "__main__":
    main()

