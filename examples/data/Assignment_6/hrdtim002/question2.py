"""program to do basic vector calculations in 3 dimension
Tim Hardie
23-4-14"""
import math
if __name__ == '__main__':
    
    #get vectors
    vectorA = input ("Enter vector A:\n").split(' ')
    vectorB = input ("Enter vector B:\n").split(' ')
    
    #convert vector lists to ints
    for i in range (len (vectorA)):
        vectorA[i] = eval (vectorA[i])
    for i in range (len (vectorB)):
        vectorB[i] = eval (vectorB[i])
    
    #addition
    addition_list = []
    for i in range (3):
        addition_list.append(vectorA[i] + vectorB[i])
    
    #dot product
    dot_prod = 0
    for i in range(3):
        dot_prod += vectorA[i] * vectorB[i]
    
    #normalization
    normalisedA = math.sqrt(vectorA[0]**2 + vectorA[1]**2 + vectorA[2]**2)
    normalisedB = math.sqrt(vectorB[0]**2 + vectorB[1]**2 + vectorB[2]**2)
    
    #print
    print ("A+B =",addition_list)
    print ("A.B =", dot_prod)
    print ("|A| =", '{0:.2f}'.format(normalisedA))
    print ("|B| =", '{0:.2f}'.format(normalisedB))