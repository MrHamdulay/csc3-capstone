''' Assignment 6, question 2
Basic vector calculations in 3 dimensions
Tristan Subroyen
21 April 2014 '''

# import math for math functions
import math

# Initializations to be used in program:
vectorA = []
vectorB = []
addition = []
dotProduct = []
normalization = []

def main(): # Does basic vector calculations with arrays
    # Ask user for vector A input, and split
    vector1 = input("Enter vector A:\n")
    vectorA = vector1.split(' ')
    
    # Ask user for vector B input, and split
    vector2 = input("Enter vector B:\n")
    vectorB = vector2.split(' ')
    
    # Addition:
    for i in range (3):
        addNum = eval(vectorA[i]) + eval(vectorB[i])
        addition.append(addNum)
    print("A+B = [" + str(addition[0]) + ", " + str(addition[1]) + ", " + str(addition[2]) + "]")
    
    # dotProduct:
    for i in range (3):
        multNum = eval(vectorA[i]) * eval(vectorB[i])
        dotProduct.append(multNum)
    product = 0
    for i in range (3):
        product += dotProduct[i]
    print("A.B = " + str(product))
    
    # Normalization:
    
    # Vector A dot norm
    aSum = eval(vectorA[0])**2 + eval(vectorA[1])**2 + eval(vectorA[2])**2
    aRoot = ("{0:.2f}".format(math.sqrt(aSum)))
    print("|A| =",aRoot)
    
    # Vector B dot norm
    bSum = eval(vectorB[0])**2 + eval(vectorB[1])**2 + eval(vectorB[2])**2
    bRoot = ("{0:.2f}".format(math.sqrt(bSum)))
    print("|B| =",bRoot)    

if __name__ == '__main__':
    main()
    